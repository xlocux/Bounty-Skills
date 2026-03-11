# 14 — LOGIC ABUSE (ADVANCED)
Applicable to: All contexts

---

## Types
- Multi-step workflow bypass
- Sequence manipulation
- Abuse of legitimate functionality
- Business logic chaining

---

## Identification
- Flow analysis
- Test edge cases
- Manipulate steps
- *...

---

## Remediation
- Server-side logical validation
- State checks
- Rate limiting

---

## 📋 Test Template (expected input/output)

- **Objective:** verify chaining of functions and logical abuse.
- **Controlled input:** documented standard flow.
- **Test variant:** combine functions in an unexpected order.
- **Execution steps:** 1) baseline 2) variant 3) observe state.
- **Expected safe output:** block or consistent state.
- **Indicative vulnerable output:** unsanctioned benefit.
- **Evidence to save:** final state, logs.
- **Context notes:** use test environments.

### Sample baseline + variant
- **Baseline:** single purchase → **Variant:** purchase + repeated refund
- **Baseline:** account upgrade → **Variant:** downgrade with elevated permissions retained