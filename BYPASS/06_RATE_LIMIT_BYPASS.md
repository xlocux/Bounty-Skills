# 06 — RATE LIMIT BYPASS
Applicable to: Live Domain, API, Mobile (API layer)

---

## 📌 Description
Techniques to bypass rate limiting restrictions.

---

## 🔧 Techniques

### 1. IP rotation
- Proxy pool
- Tor (if permitted by the program)

### 2. Header spoofing
- `X-Forwarded-For`
- `X-Real-IP`

### 3. Parallelization
- Simultaneous requests

### 4. Distributed testing
- Multiple devices / multiple networks

---

## 🛡️ Mitigations
- Rate limit per account
- Rate limit per token
- Device fingerprinting

---

## 📋 Test Template (expected input/output)

- **Objective:** verify rate limit enforcement.
- **Controlled input:** small number of requests.
- **Test variant:** controlled burst or limited parallelism.
- **Execution steps:** 1) baseline under threshold 2) variant above threshold.
- **Expected safe output:** 429 or backoff response.
- **Indicative vulnerable output:** requests always accepted.
- **Evidence to save:** timestamps, status codes.
- **Context notes:** respect the program's limits.

### Sample baseline + variant
- **Baseline:** 5 req/min → **Variant:** 10 req/min with same parameters
- **Baseline:** single client → **Variant:** IP/header rotation