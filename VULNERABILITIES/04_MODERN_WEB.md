# 04 — MODERN WEB VULNERABILITIES
Applicable to: Live Domain, API, Mobile (webview)

---

## Types
- XSS
- CSRF
- CORS Misconfigurations
- Prototype Pollution
- Client-Side Template Injection (CSTI)
- GraphQL misconfig (introspection, depth/complexity)

---

## Identification
- Test reflected input
- Manipulate CORS headers
- Modify mutable JavaScript objects
- Enable production introspection
- Unauthorized resolver access

---

## Remediation
- CSP
- SameSite cookies
- Sanitization
- Disable introspection in production
- Limit depth/complexity for GraphQL

---

## 📋 Test Template (expected input/output)

- **Objective:** verify modern web vulnerabilities (XSS/CORS/GraphQL).
- **Controlled input:** reflected field or CORS/GraphQL query header.
- **Test variant:** insert harmless marker or introspection query.
- **Execution steps:** 1) baseline 2) variant 3) compare output.
- **Expected safe output:** sanitized output, restricted CORS, introspection disabled.
- **Indicative vulnerable output:** unsanitized reflection, CORS with credentials, exposed schema.
- **Evidence to save:** response header, HTML, JSON schema.
- **Context notes:** on mobile, focus on webview and related APIs.

### Sample baseline + variant
- **Baseline:** `q=test` → **Variant:** `q=<b>t</b>` (check sanitization)
- **Baseline:** `Origin: https://good.example` → **Variant:** `Origin: https://evil.example`
- **Baseline:** `query={__typename}` → **Variant:** `query={__schema{types{name}}}`