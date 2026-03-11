# PHASE 1: PROGRAM GUIDELINES AND SCOPE
> **Prerequisite:** The test context has already been defined via `01_CONTEXT_REQUEST.md`.
>
> This phase aligns the agent with the **program rules** (bug bounty, pentest, internal audit, etc.).
>
> ---
>
> ## 1. Program Guidelines Analysis
>
> When the user provides a link or text with the program rules, the agent must:
>
> - Extract:
>   - **Scope** (domains, repos, apps, APIs)
>   - **Out-of-scope**
>   - **Accepted vulnerability types**
>   - **Rejected vulnerability types**
>   - **Impact and severity rules**
>   - **Operational limitations** (no DoS, no massive brute force, etc.)
> - Ask for clarification if:
>   - Scope is ambiguous
>   - Unclear whether an asset is in-scope
>   - Traffic limits are not specified
>
> ---
>
> ## 2. Scope Definition
>
> Checklist:
>
> - **In-scope assets**
>   - Domains, subdomains
>   - Repositories, branches
>   - Specific APIs
>   - Mobile app versions
>
> - **Out-of-scope assets**
>   - Third parties
>   - Shared services
>   - Infrastructure not owned by the program
>
> The agent must always remember the context:
>
> - Open source: repo, branch, modules
> - Live domain: domains, subdomains, environments (prod, staging)
> - Mobile: package name, versions, related backend environments
> - API: base URL, versions (v1, v2), environments
>
> ---
>
> ## 3. Testing Rules and Rate Limiting
>
> The agent must identify and respect:
>
> - **Traffic limits** (e.g., max X requests per minute)
> - **Explicit prohibitions**:
>   - No DoS/Stress testing
>   - No massive brute force
>   - No testing on non-consensual user data
> - **Time windows** (if present)
>
> For context:
>
> - **Live domain / API:** extra attention to rate limiting and impact
> - **Open source:** testing primarily on local environment
> - **Mobile:** testing on backend only if in-scope
>
> ---
>
> ## 4. In-scope / Out-of-scope Vulnerabilities
>
> The agent must classify:
>
> - **Typical in-scope:**
>   - Injection (SQLi, XSS, command injection, etc.)
>   - Auth & session issues
>   - Access control (IDOR, privilege escalation)
>   - Server-side issues (SSRF, RCE, file inclusion)
>   - Business logic flaws
>
> - **Typical out-of-scope:**
>   - Minor best practices (e.g., missing low-impact headers)
>   - Version disclosure with no impact
>   - Clickjacking without realistic scenario
>   - “Soft” rate limiting without demonstrable abuse
>
> ---
>
> ## 5. Questions to Ask the Program / User
>
> The agent may ask:
>
> - “Can you share the **official program rules** or a link?”
> - “Which assets are **explicitly in-scope**?”
> - “Are there assets you want to **exclude** from testing?”
> - “Are there **traffic limits** or times to avoid intensive testing?”
> - “Are there vulnerabilities the program considers **irrelevant**?”
>
> ---
>
> ## 6. Compliance Checklist
>
> Before suggesting aggressive testing, the agent should verify:
>
> - [ ] Context is clear (open source, live, mobile, API)
> - [ ] Scope is defined
> - [ ] Traffic limits are known
> - [ ] In-scope vulnerability types are understood
> - [ ] I am not suggesting techniques prohibited by the program
>
> ---
>
> ## 7. Link to Other Phases
>
> - After this phase:
>   - Environment setup: `03_ENVIRONMENT_SETUP.md`
>   - Specific workflow: `*/workflow.md`
>
> All subsequent technical recommendations must be **consistent with context + scope**.