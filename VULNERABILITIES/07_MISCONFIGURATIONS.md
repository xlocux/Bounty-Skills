# 07 — MISCONFIGURATIONS
Applicable to: Live Domain, API, Open Source, Cloud

---

## 📌 Description
Misconfigurations are errors in server, service, cloud, or application configurations that expose unintended functionality.

---

## Common Types
- Permissive CORS
- Directory listing
- Debug mode enabled
- Cloud misconfig (public S3 bucket)
- Missing security headers
- Accessible backups
- Cache poisoning / cache key injection
- HTTP request smuggling / desync
- Exposed secrets (logs, CI, config)

---

## Identification
- Header inspection
- CORS testing
- Cloud permission verification
- Sensitive file search
- Cache keying tests (Vary, Host, X-Forwarded-*)
- Proxy/front-end vs back-end parsing analysis

---

## Remediation
- Secure configurations
- Server hardening
- Remove debug mode
- Keep secrets out of repo and rotate keys

---

## 📋 Test Template (expected input/output)

- **Objective:** verify weak configurations (CORS, cache, debug, cloud).
- **Controlled input:** standard request with normal headers.
- **Test variant:** cache keying header, host, origin, etc.
- **Execution steps:** 1) baseline 2) variant 3) check differences.
- **Expected safe output:** secure headers, no debug, isolated cache.
- **Indicative vulnerable output:** permissive CORS with credentials, poisoned cache.
- **Evidence to save:** response header, cache hit/miss.
- **Context notes:** avoid impactful testing on production.

### Sample baseline + variant
- **Baseline:** `Origin: https://app.example` → **Variant:** `Origin: https://evil.example`
- **Baseline:** `Host: app.example` → **Variant:** `Host: attacker.example`