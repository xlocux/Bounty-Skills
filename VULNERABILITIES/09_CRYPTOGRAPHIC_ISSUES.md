# 09 — CRYPTOGRAPHIC ISSUES
Applicable to: Open Source, API, Mobile

---

## Types
- Weak hashing (MD5, SHA1)
- Predictable tokens
- Hardcoded keys
- Custom encryption
- Key rotation missing

---

## Identification
- Code analysis
- Key searching
- Token entropy testing
- *...

---

## Remediation
- Modern algorithms
- Key rotation
- Secret management

---

## 📋 Test Template (expected input/output)

- **Objective:** verify correct cryptographic usage.
- **Controlled input:** encrypted/decrypted value with standard parameters.
- **Test variant:** repeat operations to check nonce/IV.
- **Execution steps:** 1) baseline 2) variant 3) compare output.
- **Expected safe output:** unique IV/nonce, no predictable plaintext.
- **Indicative vulnerable output:** identical output or patterns.
- **Evidence to save:** ciphertext, nonce/IV.
- **Context notes:** in open source, check libraries and modes.

### Sample baseline + variant
- **Baseline:** encrypt `data=A` → **Variant:** encrypt `data=A` (different nonce)
- **Baseline:** signed token → **Variant:** signed token with different key