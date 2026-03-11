# KALI TOOLS – SAFE USE POLICY
>
> This file defines how the agent can use tools available on Kali Linux in a safe and context‑consistent manner.
>
> ## Security Principles
>
> - Do not use active tools without clear context and scope.
> - Prefer passive and non‑destructive tools.
> - Respect rate limits and program prohibitions.
> - Always log the command, parameters, and relevant output.
>
> ## Discovery tool (mandatory)
>
> Before using a tool, verify:
>
> - `which <tool>`
> - `<tool> --help` or `<tool> --version`
>
> Do not assume a tool is installed just because it appears on the official Kali list.
>
> ## Allowlist per context (examples)
>
> Note: the list is indicative and must be adapted to the scope.
>
> ### OPEN SOURCE
>
> - Static analysis, linters, dependency scanners
> - Grep/RG, ripper, parser
>
> ### LIVE DOMAIN
>
> - Light passive reconnaissance
> - Proxy for traffic inspection
> - Scanner only if permitted
>
> ### MOBILE
>
> - Decompiler, emulator tools, proxy, hooking
>
> ### API
>
> - API client, controlled fuzzing, auth testing
>
> ## Controlled execution
>
> - If the tool is potentially active (scanner, brute force, stress), obtain explicit confirmation.
> - If the risk is unclear, ask for clarification before executing.
>
> ## Expected Output
>
> - Brief report containing: tool, command, why it was chosen, relevant results, next step.