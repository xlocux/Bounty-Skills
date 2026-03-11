# 12 — FILE UPLOAD VULNERABILITIES
Applicable to: Live Domain, API

---

## Types
- Content-type bypass
- Polyglot file
- Path traversal upload
- RCE via file
- Excessive trust in MIME/client-side validation

---

## Identification
- Upload malicious files
- Manipulate extensions
- Test MIME types
- Verify server-side parsing (image/audio/video)

---

## Remediation
- Allowlist extensions
- Sanitization
- Antivirus scanning

---

## 📋 Test Template (expected input/output)

- **Objective:** verify controls on uploads and server parsing.
- **Controlled input:** benign file with allowed extension.
- **Test variant:** file with double extension or altered MIME.
- **Execution steps:** 1) upload baseline 2) upload variant.
- **Expected safe output:** rejection or normalization.
- **Indicative vulnerable output:** file accepted and served for execution.
- **Evidence to save:** file hash, response, access URL.
- **Context notes:** do not host executable payloads in production.

### Sample baseline + variant
- **Baseline:** `image.jpg` → **Variant:** `image.jpg.php`
- **Baseline:** `Content-Type: image/jpeg` → **Variant:** `Content-Type: text/html`