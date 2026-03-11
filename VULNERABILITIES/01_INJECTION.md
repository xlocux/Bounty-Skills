# 01 — INJECTION VULNERABILITIES
Applicable to: Open Source, Live Domain, Mobile (API layer), API

> ⚠️ Before analyzing any potential injection, the agent must have asked and confirmed the test context.

---

## 📌 Description
Injection vulnerabilities occur when unsanitized input is interpreted as commands or queries by an interpreter.

Common types:
- SQL Injection
- Command Injection
- LDAP Injection
- NoSQL Injection
- Template Injection (SSTI)
- CRLF / Response Splitting
- Email Header Injection
- Unicode Normalization Bypass

---

## 🔍 Identification (Open Source)
- Search for string concatenations in queries
- Look for dangerous functions (`exec`, `system`, `eval`)
- Taint tracking from input → sink

---

## 🌐 Identification (Live Domain)
- Test parameters with payloads such as:
  - `' OR 1=1--`
  - `${{7*7}}`
  - `; ls -la`
  - `%0d%0aSet-Cookie: injected=1`

---

## 🧪 Payload base per context

| Context      | Payload |
|--------------|---------|
| Open Source  | Direct code analysis |
| Live Domain  | `' OR '1'='1` |
| Mobile       | API manipulation via proxy |
| API          | JSON injection, header injection |

---

## 🛠️ Exploitation
- SQLi → database dump
- Command Injection → RCE
- SSTI → template breakout
- CRLF → header injection, cache poisoning
- Email Header → spoofing/BCC injection

---

## 🛡️ Remediation
- Prepared statements
- Input validation
- Escaping
- Disable dangerous functions
- Unicode normalization + allowlist
- Header sanitization (CRLF)
- **...*---

## 📋 Test Template (expected input/output)

- **Objective:** verify if user input reaches an interpreter without sanitization.
- **Controlled input:** testable parameter or field with an innocuous baseline value.
- **Test variant:** insert a minimal syntactic token (without destructive effect).
- **Execution steps:** 1) send baseline 2) send variant 3) compare response.
- **Expected safe output:** same status, no parser errors, normalized output.
- **Indicative vulnerable output:** parser errors, consistent timing differences, altered output.
- **Evidence to save:** request/response, timing, parameters, context.
- **Context notes:** live testing only with minimal payloads, no destructive payloads.

### Sample baseline + variant
- **Baseline:** `q=alpha` → **Variant:** `q=alpha'` (check for parsing errors)
- **Baseline:** `q=7` → **Variant:** `q=${7*7}` (check for template expression)
- **Baseline:** `path=report` → **Variant:** `path=report%0d%0aX-Test:1`