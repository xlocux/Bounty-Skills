# 15 — POSTMESSAGE VULNERABILITIES
Applicable to: Open Source, Live Domain, Mobile (client‑side), API

> ⚠️ **Before analyzing postMessage usage, confirm the test context.**
> If the repository contains source code or decompiled client‑side scripts, this phase applies. For pure live‑domain testing, rely on black‑box assessments.

---

## 📌 Description
`postMessage` enables cross‑origin communication but can become a vector for **data exfiltration** and **command injection** when misused. Vulnerabilities arise from:

- **Wildcard origin targets** (`'*'` or unspecified origin) allowing any party to receive messages.
- **Untrusted message content** passed directly to `postMessage` without sanitization, enabling injection of malicious scripts or Structured PostMessage (e.g., `{source: …, data: …}`) that may be processed by the receiver.
- **Missing origin validation** on the receiving side, permitting malicious origins to bypass security checks.
- **Insecure serialization** of complex objects that may be deserialized unsafely on the receiving end.

---

## 🔍 Identification (Open Source)
- Search for `window.postMessage(`, `addEventListener('message', …)`, `worker.postMessage(`, and `parentPort.postMessage(`.
- Flag any call where the **target origin** argument is:
  - The literal string `'*'` (or a variable evaluating to `'*'`).
  - Omitted when the context requires an explicit origin.
- Flag any **message argument** that originates from:
  - `req.body`, `req.query`, `window.location`, `localStorage`, or any user‑controlled source without validation/sanitization.
- Look for **receivers** that evaluate or `JSON.parse` the received message without strict schema validation.

---

## 🌐 Identification (Live Domain)
| Test Vector | Example Payload | Expected Safe Behavior |
|-------------|----------------|------------------------|
| Wildcard target | `window.postMessage(data, '*')` | **Vulnerable** – any origin can receive data. |
| Untrusted content | `window.postMessage(userInput, 'https://trusted.com')` | **Vulnerable** if `userInput` contains unsanitized data that influences receiver logic. |
| Missing validation on receiver | `window.addEventListener('message', e => { eval(e.data); })` | **Vulnerable** – arbitrary code execution. |
| Complex object serialization | `window.postMessage({cmd: 'exec', args: [userInput]}, 'https://trusted.com')` | **Vulnerable** if the receiver unsafely interprets `cmd`. |

---

## 🧪 Payload Base per Context
| Context      | Payload (Illustrative) | Note |
|--------------|------------------------|------|
| Open Source  | `window.postMessage({source: 'attacker', payload: maliciousCode}, '*')` | Shows data exfiltration + potential code execution. |
| Live Domain  | `POST /target Origin: https://attacker.com Content-Type: application/json {"msg":"<script>malicious</script>"} ` | Attempts to deliver malicious script via postMessage. |
| Mobile (WebView) | `window.postMessage(window.location.href, '*');` | May leak full URL to any listener. |
| API (Node)   | `worker.postMessage({query: userQuery}, '*');` | Risks exposure of internal state to any worker client. |

---

## 🛠️ Exploitation
- **Data Exfiltration** – Sending sensitive data to any listening origin.
- **Code Injection** – If the receiver evaluates the message payload (e.g., `eval`, `Function`, `new Constructor`).
- **Cross‑Site Scripting (XSS)** – Injecting malicious scripts that the receiver renders or executes.
- **Denial‑of‑Service** – Flooding listeners with high‑frequency messages causing performance degradation.

---

## 🛡️ Remediation
- **Validate Origin**: Always specify an explicit, known origin string; never use `'*'` unless the message contains only non‑sensitive, public data.
- **Sanitize Message Content**:
  - For simple data, use primitive types (string, number, boolean).
  - For complex objects, enforce a strict schema (e.g., using JSON Schema) before sending.
- **Receiver Hardening**:
  - Reject messages from unexpected origins.
  - Avoid `eval`, `new Constructor`, or direct `innerHTML` assignment with untrusted data.
  - Prefer structured cloning (`structuredClone`) or typed data interfaces.
- **Least Privilege**: Limit the capabilities of the message receiver (e.g., disable dangerous APIs when handling messages).
- **Audit Third‑Party Scripts**: Ensure external scripts that listen for postMessage are from trusted sources and properly sandboxed.

---

## 📋 Test Template (expected input/output)
1. **Baseline**: Send a harmless message to a known origin and verify the receiver processes it correctly.
2. **Variant**: Send the same message with a wildcard origin or with user‑controlled data to the receiver.
3. **Control**: Observe whether the receiver processes the variant without errors or unintended behavior.
4. **Evidence**: Capture request/response headers, message payloads, and any side effects (e.g., network requests, DOM changes).

### Sample Baseline + Variant
- **Baseline**: `window.postMessage({type: 'ping'}, 'https://trusted.com');` → Receiver logs “ping received”.
- **Variant**: `window.postMessage({type: 'ping', payload: userSupplied}, '*');` → Check if the receiver processes the payload unsafely.

