# 04 — AUTHENTICATION BYPASS
Applicable to: All contexts

---

## 📌 Description
Techniques to bypass weak or improperly implemented authentication.

---

## 🔧 Techniques

### 1. JWT manipulation
- Remove signature (`alg: none`)
- Forge tokens

### 2. Session fixation
- Reuse valid sessions

### 3. Password reset abuse
- Predictable tokens
- Reset without identity verification

### 4. Mobile hooking
- Bypass login by overriding functions

---

## 🛡️ Mitigations
- Signed tokens
- Invalidate sessions
- MFA

---

## 📋 Test Template (expected input/output)

- **Objective:** verify authentication or session bypass.
- **Controlled input:** request without credentials.
- **Test variant:** alternative headers or partial tokens.
- **Execution steps:** 1) baseline unauthenticated 2) variant.
- **Expected safe output:** 401/403 response.
- **Indicative vulnerable output:** access granted.
- **Evidence to save:** headers, response.
- **Context notes:** avoid brute force attempts.

### Sample baseline + variant
- **Baseline:** no auth → **Variant:** `X-Original-URL: /admin`
- **Baseline:** expired token → **Variant:** token with altered `kid`