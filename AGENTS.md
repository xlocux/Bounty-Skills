# AGENTS Instructions
>
> This repository contains an operational framework for security researchers (bug bounty and pentest) based on phases and context.
>
> ## Core Principle
>
> Before any technical analysis or payload suggestion, ask and clarify the test context.
>
> Supported contexts: OPEN_SOURCE, LIVE_DOMAIN, MOBILE, API, OTHER.
>
> ## Safety and scope (mandatory)
>
> - Only provide guidance for authorized and in‑scope activities.
> - If no program rules/scope are available, ask for them before proceeding.
> - Avoid destructive techniques (DoS, massive brute force) and respect rate limits.
>
> ## Quick Content Map
>
> - `00_MASTER_SKILL.md`: high‑level view, methodology and phase map.
> - `01_CONTEXT_REQUEST.md`: mandatory context question.
> - `02_PROGRAM_GUIDELINES.md`: scope, limits, out‑of‑scope.
> - `03_ENVIRONMENT_SETUP.md`: tool setup.
> - `04_SOURCE_CODE_ANALYSIS.md`: source code analysis.
> - `05_VULNERABILITY_DATABASE.md`: vulnerability categories database.
> - `06_BYPASS_TECHNIQUES_COMPLETE.md`: bypass and evasion techniques.
> - `07_EXPLOIT_DEVELOPMENT.md`: PoC and impact validation.
> - `08_REPORTING_TEMPLATES.md`: report templates.
> - `09_LEARNING_RESOURCES.md`: resources.
>
> ## Context‑specific maps (folders)
>
> - `OPEN_SOURCE/`
> - `LIVE_DOMAIN/`
> - `MOBILE/`
> - `API/`
>
> ## Agent Logic
>
> See `AGENT_LOGIC/` for behavior, decision tree, memory and vulnerability‑vs‑feature distinction.
>
> ## Expected Output
>
> - Structured, reproducible responses that are consistent with context and scope.
> - Always explain for which context a technique is valid.