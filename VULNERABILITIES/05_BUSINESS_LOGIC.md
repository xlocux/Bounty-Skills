# 05 — BUSINESS LOGIC
Applicable to: All contexts

---

## Description
Errors in application logic that allow:
- Payment bypass
- Misuse of functionality
- Workflow manipulation
- Tenant/organization isolation violations
- Coupon, bonus, rate, quota abuse

---

## Identification
- Flow analysis
- Test edge cases
- Manipulate sequences
- Verify tenant_id/organization_id separation
- Test idempotency and token reuse

---

## Remediation
- Server-side logical validation
- Rate limiting
- State checks
- Tenant ownership checks

---

## 📋 Test Template (expected input/output)

- **Objective:** verify for inconsistencies or logical abuse.
- **Controlled input:** standard sequence of expected actions.
- **Test variant:** alter order, repeat, or skip a step.
- **Execution steps:** 1) baseline with correct flow 2) variant.
- **Expected safe output:** block or consistent error.
- **Indicative vulnerable output:** valid state with skipped step or unsanctioned advantage.
- **Evidence to save:** final state, logs, API response.
- **Context notes:** use test data, not real users.

### Sample baseline + variant
- **Baseline:** checkout → payment → confirm
- **Variant:** checkout → confirm (skip payment)
- **Baseline:** single coupon → **Variant:** same coupon reused in parallel