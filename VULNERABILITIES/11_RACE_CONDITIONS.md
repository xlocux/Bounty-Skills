# 11 — RACE CONDITIONS
Applicable to: API, Live Domain, Open Source

---

## Types
- TOCTOU (Time-of-check to time-of-use)
- Double spending
- Multi-request concurrency
- Rate limit bypass via parallelism
- Token/OTP reuse within valid window

---

## Identification
- Send parallel requests
- Stress test endpoint
- Analyze logical transactions
- Verify statefulness and locking
- Check idempotency

---

## Remediation
- Locking mechanisms
- Atomic transactions
- State checks
- *...

---

## 📋 Test Template (expected input/output)

- **Objective:** verify TOCTOU or state concurrency issues.
- **Controlled input:** single action with expected outcome.
- **Test variant:** send 2+ identical parallel requests.
- **Execution steps:** 1) baseline single request 2) concurrent variant.
- **Expected safe output:** only one valid operation.
- **Indicative vulnerable output:** double effect or inconsistent state.
- **Evidence to save:** timestamps, request ID.
- **Context notes:** do not test on critical production endpoints.

### Sample baseline + variant
- **Baseline:** `POST /coupon/redeem` single request → **Variant:** 2 parallel requests
- **Baseline:** `POST /transfer` → **Variant:** parallelism with same idempotency key