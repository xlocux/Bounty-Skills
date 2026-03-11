# PHASE 2: ENVIRONMENT SETUP PER CONTEXT
> **Prerequisite:** context defined (`01_CONTEXT_REQUEST.md`) and scope analyzed (`02_PROGRAM_GUIDELINES.md`).
>
> Each section applies only to its specific context.
>
> ---
>
> ## TOOL DISCOVERY (KALI)
>
> If the environment is Kali Linux:
>
> - Run tool discovery (`which <tool>`, `<tool> --help`, `<tool> --version`)
> - Use only tools compatible with context and scope
> - For active tools, obtain explicit confirmation
>
> See `KALI_TOOLS.md` for policies and allowlist.
>
> ---

>
> ---
>
## SETUP FOR OPEN SOURCE CONTEXT
>
> **Applicable to:**
> 📁 Open source / source available
> 📱 Mobile (when working on decompiled code or shared source)
>
>- **Application Dockerization**
>  - Create `Dockerfile` and `docker-compose.yml` to reproduce the environment.
>  - Isolate dependencies and services (DB, cache, queue).
>
>- **Build from source**
>  - Install toolchain (language, package manager).
>  - Run build in debug mode if possible.
>
>- **Debugger setup**
>  - Configure breakpoints on critical functions (auth, input parsing, validations).
>  - Use the language's debugger (e.g., `gdb`, `lldb`, IDE).
>
>- **Local database setup**
>  - Import schema and baseline data.
>  - Create test users with different roles.
>
>- **Test data population**
>  - Generate realistic but fictitious data.
>  - Avoid real production data.
>
> ---
>
## SETUP FOR LIVE DOMAIN CONTEXT
>
> **Applicable to:**
> 🌐 Live domain / black box
> 🔌 API (when testing live endpoints)
>
>- **Proxy configuration (Burp, ZAP)**
>  - Set the browser or client to use the proxy.
>  - Configure CA certificates for HTTPS interception.
>
>- **VPN setup if required**
>  - If the program requires specific IPs or a dedicated VPN, note it.
>  - Avoid shared IPs with unrelated activity.
>
>- **Rate limiting configuration**
>  - Set request limits in the proxy or scripts.
>  - Use throttling to avoid spikes.
>
>- **Test accounts**
>  - Create accounts with different roles (user, admin, etc.) if permitted.
>  - Do not use real third‑party accounts.
>
>- **Request monitoring**
>  - Log relevant requests and responses.
>  - Note blocking patterns (WAF, rate limit).
>
> ---
>
## SETUP FOR MOBILE CONTEXT
>
> **Applicable to:**
> 📱 Mobile app (APK/IPA)
>
>- **Emulator configuration**
>  - Android: AVD, Genymotion, etc.
>  - iOS: simulator or physical device (if allowed).
>
>- **APK/IPA installation**
>  - Install the provided or store‑downloaded version (if allowed).
>  - Verify signature and integrity.
>
>- **Proxy setup on device**
>  - Configure Wi‑Fi proxy to point to Burp/ZAP.
>  - Install the CA certificate on the device/simulator.
>
>- **Root/jailbreak detection bypass**
>  - Use tools or patches to bypass root/jailbreak checks.
>  - Apply only if permitted by the program.
>
>- **Hooking tools (Frida, Objection)**
>  - Prepare Frida scripts for sensitive functions (crypto, auth, API).
>  - Use Objection to bypass root detection, SSL pinning, etc.
>
> ---
>
## SETUP FOR API CONTEXT
>
> **Applicable to:**
> 🔌 API / services
> 🌐 Live domain (when focusing on API endpoints)
>
>- **API client (Postman, Insomnia)**
>  - Import any available documentation (OpenAPI/Swagger).
>  - Configure environment (base URL, token, variables).
>
>- **Fuzzer setup**
>  - Integrate fuzzing tools (Burp Intruder, ffuf, custom script).
>  - Define wordlists and payloads consistent with scope.
>
>- **Authentication setup**
>  - Handle tokens (JWT, OAuth, API key).
>  - Automate token refresh if needed.
>
>- **Rate limiting automation**
>  - Implement delays between requests.
>  - Detect rate‑limit response codes (e.g., 429).
>
> ---
>
## Context Linkage
>
> Every setup suggestion must:
>
> - Be consistent with the **declared context**.
> - Avoid tools or techniques prohibited by the program.
> - Prepare the environment for:
>   - Code analysis (`04_SOURCE_CODE_ANALYSIS.md`) for open source/mobile.
>   - Recon and testing (`*`) for live domain/API.