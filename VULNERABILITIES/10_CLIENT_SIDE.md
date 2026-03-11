# 10 — CLIENT-SIDE VULNERABILITIES
Applicable to: Live Domain, Mobile (webview)

---

## Types
- Advanced XSS
- Prototype Pollution
- CSP Bypass
- DOM-based Vulnerabilities
- Client-side Storage Abuse (localStorage, IndexedDB)

---

## Identification
- DOM analysis
- Manipulate JavaScript objects
- Test CSP
- Verify client storage tokens/scopes

---

## Remediation
- Strict CSP
- Sanitization
- Input validation
- Minimize secrets on client
- *...

---

## 📋 Test Template (expected input/output)

- **Objective:** verify client-side risks (DOM, storage, CSP).
- **Controlled input:** reflected input or baseline storage.
- **Test variant:** insert harmless marker or fake token.
- **Execution steps:** 1) baseline 2) variant 3) observe DOM.
- **Expected safe output:** sanitized DOM, limited storage.
- **Indicative vulnerable output:** unsanitized HTML or persistent token.
- **Evidence to save:** screenshot, storage dump.
- **Context notes:** for mobile, focus on webview.

### Sample baseline + variant
- **Baseline:** `q=test` → **Variant:** `q=<img src=x onerror=1>`
- **Baseline:** empty localStorage → **Variant:** token stored in clear text