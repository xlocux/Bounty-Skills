# PHASE 0: CONTEXT REQUEST
> **Golden rule:**
> No analysis, no payload, no technical suggestion before defining the **test context**.
>
> ---
>
> ## MANDATORY QUESTION TO ASK THE USER
>
> > “What is the test context we need to perform?”
>
> > 🔍 Select one of the following options:
>
> > ┌─────────────────────────────────────────────────────────┐
> > │  📁 OPEN SOURCE / SOURCE AVAILABLE                      │
> > │     I have the complete application code                 │
> > │     I can build locally and debug                        │
> > │     Example: GitHub repository, downloaded code          │
> > ├─────────────────────────────────────────────────────────┤
> > │  🌐 LIVE DOMAIN / BLACK BOX                              │
> > │     Testing on a production domain (no source code)      │
> > │     I must respect rate limits                           │
> > │     Example: app.target.com, api.example.com             │
> > ├─────────────────────────────────────────────────────────┤
> > │  📱 MOBILE APP                                          │
> > │     I have the APK (Android) or IPA (iOS)                │
> > │     I can decompile and analyze                        │
> > │     Example: app from Play Store/App Store               │
> > ├─────────────────────────────────────────────────────────┤
> > │  🔌 API / SERVICES                                      │
> > │     Testing on APIs with/without documentation           │
> > │     Known or discoverable endpoints                      │
> > │     Example: REST API, GraphQL, WebSocket                │
> > ├─────────────────────────────────────────────────────────┤
> > │  ❓ OTHER                                                │
> > │     Specify the context                                 │
> > └─────────────────────────────────────────────────────────┘
>
> The answer to this question will determine ALL subsequent approach:
> - Analysis methodology
> - Tools to use
> - Testing techniques
> - Limitations and precautions
> - Specific workflow”
>
> ---
>
> ## After the answer: mandatory steps
>
> 1. **Confirm understanding of the context**
>
>    Example:
>
>    - “You indicated a context **OPEN SOURCE**: we will work on the source code and local testing.”
>    - “You indicated a context **LIVE DOMAIN**: we will operate in black‑box mode, respecting rate limits.”
>    - “You indicated a context **MOBILE**: we will use decompilation, emulators, and hooking if necessary.”
>    - “You indicated a context **API**: we will focus on endpoint discovery, authentication, and controlled fuzzing.”
>    - “You indicated **OTHER**: the agent must ask for clarification until the context is clear.”
>
> 2. **Briefly explain the approach that will be followed**
>
>    Example:
>
>    - Open source: “We will start with static analysis, local build, debugging, and targeted testing of the code.”
>    - Live domain: “We will start with reconnaissance, technology fingerprinting, user‑input identification, and structured manual testing.”
>    - Mobile: “We will proceed with decompilation, static analysis, emulator setup, and dynamic analysis.”
>    - API: “We will map endpoints, analyze authentication, and perform controlled fuzzing.”
>
> 3. **Proceed to the appropriate next phase**
>
>    - Always after context, move to: `02_PROGRAM_GUIDELINES.md`
>    - Then, based on the context:
>        - `03_ENVIRONMENT_SETUP.md`
>        - `OPEN_SOURCE/*`
>        - `LIVE_DOMAIN/*`
>        - `MOBILE/*`
>        - `API/*`
>
> ---
>
## Context applicability
>
> - **Open Source:** mandatory question + focus on source code and local testing.
> - **Live Domain:** mandatory question + focus on recon, black‑box, rate limiting.
> - **Mobile:** mandatory question + focus on APK/IPA, emulators, hooking.
> - **API:** mandatory question + focus on endpoints, authentication, fuzzing.
> - **Other:** the agent must request clarification until the context is clear.
>
> Every other skill must assume that this phase has already been completed.