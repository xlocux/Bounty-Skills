# PHASE 5: BYPASS TECHNIQUES – COMPLETE MATRIX
> **Each bypass technique must indicate** **in which contexts** it is applicable and provide **concrete examples**.
>
> ---
>
## 1. Applicability Matrix
>
> | Technique          | Open Source | Live Domain | Mobile | API |
> |--------------------|------------|------------|--------|-----|
> | WAF Bypass         | ✅ (local test) | ✅          | ⚠️ (rare) | ✅   |
> | Filter Bypass      | ✅          | ✅          | ⚠️     | ✅   |
> | CSP Bypass         | ✅          | ✅          | ❌     | ⚠️  |
> | Auth Bypass        | ✅          | ✅          | ✅     | ✅   |
> | Rate Limit Bypass  | ⚠️         | ✅          | ⚠️     | ✅   |
>
> Legend:
>
> - ✅: typically applicable
> - ⚠️: special cases / less frequent
> - ❌: generally not applicable
>
> ---
>
## 2. WAF Bypass
>
> **Contexts:**
> - Open source: local testing of custom WAF rules.
> - Live domain: bypass production WAF filters (always within program limits).
> - API: WAF/API gateway.
>
> **Examples:**
>
> - **Payload obfuscation:**
>   - XSS: use mixed encoding, comments, concatenation.
>     - `"<svg/onload=alert(1)>"` → `"<svg/onload=&#97;&#108;&#101;&#114;&#116;(1)>"`
>   - **Case/spacing bypass:**
>     - SQLi: `UNION SELECT` → `UnIoN/**/SeLeCt`
>
> - **Path confusion / encoding:**
>   - `%2e%2e/` instead of `../` (if not properly normalized).
>
> ---
>
## 3. Filter Bypass
>
> **Contexts:**
> - Open source: analysis and modification of code‑level filters.
> - Live domain/API: bypass input/output filters.
> - Mobile: when the app filters input before sending it.
>
> **Examples:**
>
> - **Simple blacklist bypass:**
>   - If `script` is filtered, try:
>     - `scr<script>ipt`
>     - `scr\0ipt`
>     - Alternative HTML events (`onerror`, `onload`, etc.).
>
> - **Incomplete sanitization bypass:**
>   - Double encoding:
>     - `%253Cscript%253Ealert(1)%253C/script%253E`
>
> ---
>
## 4. CSP Bypass
>
> **Contexts:**
> - Open source: analysis of generated CSP headers.
> - Live domain: test XSS in the presence of CSP.
> - API: only when CSP affects HTML responses (⚠️).
> - Mobile: generally not applicable (❌).
>
> **Examples:**
>
> - **Use of allowed endpoints:**
>   - If `script-src` permits a specific domain, look for injection on that domain.
>
> - **JSONP / callback abuse:**
>   - If callbacks from third‑party domains are allowed, they can be controllable.
>
> ---
>
## 5. Auth Bypass
>
> **Contexts:**
> - All (open source, live, mobile, API).
>
> **Examples:**
>
> - **Login bypass:**
>   - Hidden or flag parameters (e.g., `is_admin=true`).
>   - Unprotected endpoints that return sensitive data.
>
> - **JWT manipulation:**
>   - `none` algorithm (if mis‑configured).
>   - Weak or known signing keys.
>
> - **Mobile:**
>   - Hooking to bypass client‑side checks.
>   - Modify API requests before sending.
>
> ---
>
## 6. Rate Limit Bypass
>
> **Contexts:**
> - Live domain, API (primary).
> - Open source/mobile: local testing or simulation (⚠️).
>
> **Examples:**
>
> - **Distribute requests:**
>   - Use different IPs (if allowed).
>   - Use headers like `X-Forwarded-For` (only if not prohibited).
>
> - **Modify request patterns:**
>   - Randomize non‑critical parameters.
>   - Switch between endpoints to avoid triggering limits.
>
> ---
>
## 7. Linkage to BYPASS/* files
>
> Detailed per‑category documentation:
>
> - `BYPASS/01_WAF_BYPASS.md`
> - `BYPASS/02_FILTER_BYPASS.md`
> - `BYPASS/03_CSP_BYPASS.md`
> - `BYPASS/04_AUTH_BYPASS.md`
> - `BYPASS/05_ENCODING_BYPASS.md`
> - `BYPASS/06_RATE_LIMIT_BYPASS.md`
>
> Each file:
>
> - Deepens specific techniques.
> - Provides sample payloads.
> - Clearly indicates **applicable contexts**.