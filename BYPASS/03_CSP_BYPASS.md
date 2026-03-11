# 03 — CSP BYPASS
Applicable to: Live Domain, API (webview), Open Source

---

## 📌 Description
The Content Security Policy (CSP) restricts script execution. A weak CSP can be bypassed.

---

## 🔧 Techniques

### 1. JSONP endpoints
- Script loading from trusted endpoints

### 2. Misconfigurations `unsafe-inline`
- Inline JavaScript still allowed

### 3. Bypass via `data:` or `blob:`
- `script src="blob:..."`

### 4. Injection in trusted domains
- Compromised CDN
- Subdomain takeover

---

## 🛡️ Mitigations
- Strict CSP mode
- Remove wildcards
- Do not use `unsafe-inline`

---

## 📋 Test Template (expected input/output)

- **Objective:** verify if CSP prevents execution of unauthorized scripts.
- **Controlled input:** reflected input with harmless marker.
- **Test variant:** attempt execution using an allowed source.
- **Execution steps:** 1) baseline 2) variant 3) check console.
- **Expected safe output:** CSP blocks script in console.
- **Indicative vulnerable output:** script executes despite policy.
- **Evidence to save:** console output, CSP header.
- **Context notes:** test only on authorized environments.

### Sample baseline + variant
- **Baseline:** `<img src=x>` → **Variant:** `<script src=https://trusted.cdn/x.js>`
- **Baseline:** missing `nonce` → **Variant:** `nonce` reused