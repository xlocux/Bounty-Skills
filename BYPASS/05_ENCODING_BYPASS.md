# 05 — ENCODING BYPASS
Applicable to: All contexts

---

## 📌 Description
Use of alternative encodings to bypass filters or validations.

---

## 🔧 Techniques

### 1. Double encoding
- `%252e%252e%252f`

### 2. Unicode normalization
- `\uFF0E\uFF0E/`

### 3. Mixed encoding
- URL + Base64 + Unicode

### 4. Case folding
- `SeLeCt`, `UNION`

---

## 🛡️ Mitigations
- Input normalization
- Multi-stage decoding on the server

---

## 📋 Test Template (expected input/output)

- **Objective:** verify input normalization with encoding.
- **Controlled input:** baseline innocuous string.
- **Test variant:** URL encoding, double encoding, unicode.
- **Execution steps:** 1) baseline 2) variant 3) compare.
- **Expected safe output:** identical output after normalization.
- **Indicative vulnerable output:** different behavior.
- **Evidence to save:** raw input and decoded versions.
- **Context notes:** use minimal inputs.

### Sample baseline + variant
- **Baseline:** `../` → **Variant:** `%2e%2e%2f` or `%252e%252e%252f`
- **Baseline:** `admin` → **Variant:** `a%64min`