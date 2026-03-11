# 02 — FILTER BYPASS
Applicable to: All contexts

---

## 📌 Description
Bypass of client-side or server-side filters that block certain characters or patterns.

---

## 🔧 Techniques

### 1. HTML entity encoding
- `<script>` → `&lt;script&gt;`

### 2. Polyglot payload
- `"><svg/onload=alert(1)>`

### 3. Input injection via concatenation
- `a"b'c\`

### 4. Bypass weak regex
- Insert unexpected characters
- Break pattern matching

---

## 🛡️ Mitigations
- Robust regexes
- Server-side sanitization
- Whitelist validation

---

## 📋 Test Template (expected input/output)

- **Objective:** verify bypass of custom application filters.
- **Controlled input:** baseline value accepted.
- **Test variant:** insert bypassed characters or mixed case.
- **Execution steps:** 1) baseline 2) variant 3) comparison.
- **Expected safe output:** filter blocks or normalizes the input.
- **Indicative vulnerable output:** variant is accepted with the same effect.
- **Evidence to save:** input, output, errors.
- **Context notes:** use minimal inputs.

### Sample baseline + variant
- **Baseline:** `select` blocked → **Variant:** `SeLeCt` or `sel%65ct`
- **Baseline:** `<script>` blocked → **Variant:** `<scr<script>ipt>`