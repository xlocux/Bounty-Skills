# INTERACTION FLOW
Agent's decision flow to guide the user without asking too many questions.

---

# 🔥 PHASE 0 — CONTEXT REQUEST (MANDATORY)
"Whats the test context?"

---

# 🔥 PHASE 1 — MINIMAL QUESTIONS TO DEFINE THE TARGET

## If LIVE DOMAIN
- What is the target domain?
- Do you have credentials?
- Are there any known program limitations?
- Do you want to start with recon or manual testing?

## If OPEN SOURCE
- Do you already have the repository?
- Is the project buildable?
- What languages/frameworks does it use?
- Do you want static or dynamic analysis?

## If MOBILE
- Do you have an APK/IPA?
- Do you want to decompile or perform dynamic analysis?
- Is the traffic interceptable?

## If API
- Do you have documentation?
- Do you have a token?
- Do you want fuzzing or auth testing?
- Is the API REST, GraphQL, or WebSocket?

---

# 🔥 PHASE 2 — DEFINE THE OBJECTIVE
The agent asks:
- Do you want to find vulnerabilities?
- Do you want to create a PoC?
- Do you want to do recon?
- Do you want to analyze code?

---

# 🔥 PHASE 2.5 — VERIFY "VULNERABILITY OR FEATURE?"
Before proceeding with analysis or exploit, the agent must ask:

- “Is this behavior documented?”
- “Do you have an example of the expected behavior?”
- “Does it require authentication or special permissions?”
- “Does it provide an unintended advantage?”
- “Does the program consider this behavior in-scope?”

If the behavior is:
- documented → FEATURE
- undocumented but harmless → BORDERLINE
- exploitable → VULNERABILITY

---

# 🔥 PHASE 3 — PERSONALIZED WORKFLOW
The agent generates workflows based on:
- context
- objective
- memory
- preferences
- relevant vulnerability category

---

# 🔥 PHASE 4 — SESSION MEMORY
The agent saves:
- target
- context
- preferences
- classifications
- progress
