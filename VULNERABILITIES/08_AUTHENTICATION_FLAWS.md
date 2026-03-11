# 08 — AUTHENTICATION FLAWS
Applicable to: All contexts

---

## Types
- Session fixation
- Token prediction
- Weak password reset
- MFA bypass
- Brute force without rate limit
- JWT/Session confusion (alg none, kid injection)
- OAuth/OIDC misbinding and redirect_uri weakness
- Open redirect chaining in auth flows

---

## Identification
- Token manipulation
- Password reset testing
- Session analysis
- MFA testing
- Modify JWT header and `kid`
- Verify `state`/`nonce` in OAuth/OIDC
- Check open redirect chaining in auth flows

---

## Remediation
- Secure tokens
- Robust MFA
- Rate limiting
- Strict JWT/OIDC validation
- Redirect allowlist

---

## 📋 Test Template (expected input/output)

- **Objective:** verify robustness of sessions, tokens, and reset mechanisms.
- **Controlled input:** valid login and baseline token.
- **Test variant:** modify claim or redirect URI.
- **Execution steps:** 1) baseline login 2) variant token/redirect.
- **Expected safe output:** token rejected or redirect blocked.
- **Indicative vulnerable output:** valid session with modified token.
- **Evidence to save:** token, header, response.
- **Context notes:** do not attempt massive brute force.

### Sample baseline + variant
- **Baseline:** valid JWT → **Variant:** `alg=none` or altered `kid`
- **Baseline:** `redirect_uri=https://app.example/cb` → **Variant:** `https://evil.example/cb`