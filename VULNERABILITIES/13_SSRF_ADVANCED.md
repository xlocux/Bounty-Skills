# 13 — ADVANCED SSRF
Applicable to: API, Live Domain

---

## Advanced Techniques
- Redirect chain
- DNS rebinding
- Cloud metadata exploitation
- Gopher/Dict exploitation
- Blind SSRF with OAST/Out-of-band

---

## Identification
- Test internal URLs
- Manipulate redirects
- DNS payloads
- Callback to OAST for blind SSRF
- *...

---

## Remediation
- URL allowlist
- Block dangerous protocols
- *...

---

## 📋 Test Template (expected input/output)

- **Objective:** verify SSRF with advanced and blind techniques.
- **Controlled input:** allowed external URL.
- **Test variant:** internal URL or OAST with DNS lookup.
- **Execution steps:** 1) baseline 2) variant 3) verify callback.
- **Expected safe output:** request blocked or allowlist enforced.
- **Indicative vulnerable output:** OAST callback or metadata access.
- **Evidence to save:** DNS/HTTP logs from OAST.
- **Context notes:** avoid scanning internal IP ranges.

### Sample baseline + variant
- **Baseline:** `url=https://example.com` → **Variant:** `url=http://169.254.169.254/latest/meta-data/`
- **Baseline:** `url=https://example.com` → **Variant:** `url=https://oast.example/trace`