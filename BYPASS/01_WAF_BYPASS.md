# 01 — WAF BYPASS
Applicable to: Live Domain, API, Open Source (local test)

> ⚠️ Before applying bypass techniques, the agent must have asked and confirmed the test context.

---

## 📌 Description
Web Application Firewalls (WAFs) filter suspicious requests. Bypass techniques are used to evade overly permissive or misconfigured filters.

---

## 🔧 Common Techniques

### 1. Payload Obfuscation
- **Comment injection:** `UN/**/ION SELECT`
- **Case switching:** `UnIoN SeLeCt`
- **Keyword splitting:** `uni%6fn select`

### 2. Encoding
- **URL double encoding:** `%252e%252e%252f`
- **Unicode encoding:** `\u002e\u002e/`

### 3. Header Manipulation
- `X-Original-URL`
- `X-Rewrite-URL`

### 4. Payload Randomization
- Insert harmless characters
- Multiple variants of the same payload

---

## 🧪 Context Applicability

| Technique            | Open Source | Live Domain | Mobile | API |
|----------------------|------------|------------|--------|-----|
| Obfuscation          | ✅         | ✅         | ⚠️     | ✅   |
| Encoding             | ✅         | ✅         | ⚠️     | ✅   |
| Header manipulation  | ❌         | ✅         | ❌     | ⚠️   |
| Payload randomization| ✅         | ✅         | ⚠️     | ✅   |

---

## 🛡️ Mitigations
- Modern WAFs with ML
- Input normalization
- Server-side validation

---

## 📋 Test Template (expected input/output)

- **Objective:** verify if the WAF properly normalizes input.
- **Controlled input:** baseline payload blocked by WAF.
- **Test variant:** same semantics with obfuscation/encoding.
- **Execution steps:** 1) baseline blocked 2) obfuscated variant.
- **Expected safe output:** consistent blocking across all variants.
- **Indicative vulnerable output:** variant passes and reaches backend.
- **Evidence to save:** response code, WAF header, request details.
- **Context notes:** avoid destructive payloads.

### Sample baseline + variant
- **Baseline:** `q=' OR 1=1--` -> **Variant:** `q=UN/**/ION%20SEL/**/ECT`
- **Baseline:** `../` -> **Variant:** `%252e%252e%252f`