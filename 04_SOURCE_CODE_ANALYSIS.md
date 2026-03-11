# PHASE 3: SOURCE CODE ANALYSIS
> **Applicable only if:**
> - Context is **OPEN SOURCE** (source available)
> - Context is **MOBILE** with decompiled code or provided source
>
> If the context is **only LIVE DOMAIN** or **only API BLACK BOX**, this phase does not apply.
>
> ---
>
## 1. When to Use Source Code Analysis
>
> - When the user has:
>   - Git repository, source archive, or decompiled code.
>   - Ability to build locally or run in a controlled environment.
>
> - Objectives:
>   - Identify vulnerabilities **earlier** or **beyond** black‑box testing.
>   - Understand logic, security checks, and data flows.
>
> ---
>
## 2. Language‑Specific Static Analysis Techniques
>
> The agent must adapt techniques to the language (examples):
>
> - **Java / Kotlin / C#**
>   - Analyze controllers, services, repositories.
>   - Examine security annotations, filters, middleware.
>
> - **JavaScript / TypeScript / Node.js**
>   - Analyze routers, middleware, input validations.
>   - Look for usage of security libraries.
>
> - **PHP / Python / Ruby / Go / etc.**
>   - Search for injection patterns, file handling, deserialization.
>
> ---
>
## 3. Control Flow Analysis
>
> - Map:
>   - Entry point (controller, handler, endpoint).
>   - Execution flow for critical requests (login, payment, upload).
> - Identify:
>   - Unprotected branches.
>   - Alternative paths that bypass checks.
>
> ---
>
## 4. Data Flow Analysis
>
> - Trace data flow:
>   - From user input → functions → sinks (DB, file, OS, HTTP).
> - Goal:
>   - Pinpoint places where data is not validated or sanitized.
>
> ---
>
## 5. Taint Tracking
>
> - Mark as “tainted”:
>   - Input from request, parameters, headers, body, cookies.
> - Verify:
>   - Whether and where they are sanitized.
>   - Whether they reach dangerous sinks (query, exec, file, template).
>
> ---
>
## 6. Sink Detection
>
> Examples of sinks:
>
> - **DB:** concatenated SQL queries, ORM raw queries.
> - **OS:** `exec`, `system`, `Runtime.exec`, `ProcessBuilder`.
> - **File:** read/write with user‑controlled paths.
> - **Template:** rendering with unfiltered user input (XSS).
>
> ---
>
## 7. Input Source Identification
>
> - Identify all input sources:
>   - GET/POST parameters, JSON body, headers, cookies, file uploads.
>   - For mobile: UI input, local storage, backend API input.
>
> ---
>
## 8. Protection Mechanism Analysis
>
> - Analyze:
>   - Authentication (login, token, sessions).
>   - Authorization (role checks, ACLs).
>   - Input validation (server‑side and client‑side).
>   - Anti‑CSRF, rate‑limit, code‑level WAF mechanisms.
>
> ---
>
## Context Linkage
>
> - **Open source:** this phase is central.
> - **Mobile:** useful on decompiled code or provided source.
> - **Live domain / API:** primarily black‑box testing; this phase is not used.
>
> Every suggestion must specify whether it requires **source access** or can also be applied in black‑box scenarios.