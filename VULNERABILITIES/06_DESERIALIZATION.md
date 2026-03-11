# 06 — DESERIALIZATION VULNERABILITIES
Applicable to: Open Source, API, Live Domain, Mobile (backend)

---

## 📌 Description
Deserialization vulnerabilities occur when untrusted data is deserialized into complex objects. If the format is dangerous or the library has vulnerabilities, an attacker can:

- Execute arbitrary code (RCE)
- Manipulate internal objects
- Bypass security controls
- Access sensitive data

---

## 🧩 Main Types
### 1. **Insecure Deserialization**
Occurs when user-controlled input is deserialized without validation.

Examples:
- Java `ObjectInputStream`
- PHP `unserialize()`
- Python `pickle.loads()`
- .NET `BinaryFormatter`

---

## 2. **Gadget Chains**
The attacker leverages existing classes in the codebase to chain operations until achieving RCE.

---

## 3. **Logic Manipulation**
Even without RCE, an attacker can:
- Change roles
- Modify permissions
- Alter session objects

---

## 🔍 Identification (Open Source)
Look for:
- Insecure deserialization functions
- Classes with “magic” methods (`__wakeup`, `__destruct`, `readObject`)
- Known libraries with gadget chains

---

## 🌐 Identification (Live Domain / API)
Test endpoints that accept:
- Complex JSON
- Serialized objects
- Poorly signed session cookies
- Custom tokens

Common payloads:
- `O:8:"Exploit":1:{s:4:"pwn";s:3:"yes";}`

---

## 🧪 Payload per Context

| Context      | Payload / Technique |
|--------------|--------------------|
| Open Source  | Gadget chain analysis |
| API          | Manipulated JSON objects |
| Live Domain  | Cookie tampering |
| Mobile       | Backend object manipulation |

---

## 🛠️ Exploitation
- RCE via gadget chain
- Session manipulation
- Privilege escalation
- Access to internal objects

---

## 🛡️ Remediation
- Use safe formats (JSON, protobuf)
- Validate input before deserialization
- Sign and verify objects
- Avoid vulnerable libraries
- Disable unnecessary magic methods
- *****...

## 📋 Test Template (expected input/output)

- **Objective:** verify whether serialized input is deserialized insecurely.
- **Controlled input:** benign serialized payload.
- **Test variant:** structure with unexpected type or extra field.
- **Execution steps:** 1) baseline 2) variant 3) observe errors.
- **Expected safe output:** rejection or schema validation.
- **Indicative vulnerable output:** class errors, stacktrace or side-effects.
- **Evidence to save:** request/response, stacktrace.
- **Context notes:** in open source, inspect gadget chain.

### Sample baseline + variant
- **Baseline:** `data={"type":"Note","id":1}`
- **Variant:** `data={"type":"Admin","id":1}`