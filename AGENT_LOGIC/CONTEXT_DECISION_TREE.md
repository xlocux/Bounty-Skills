# CONTEXT DECISION TREE
Agent's complete decision tree.

---

# 🔥 STEP 1 — ASK FOR CONTEXT
(open source / live domain / mobile / api)

---

# 🔥 STEP 2 — CONTEXT-SPECIFIC QUESTIONS

## OPEN SOURCE
- repo?
- languages?
- build system?

## LIVE DOMAIN
- domain?
- credentials?
- scope?

## MOBILE
- apk/ipa?
- device?
- proxy?

## API
- documentation?
- token?
- endpoint?

---

# 🔥 STEP 3 — DEFINE THE OBJECTIVE
- recon
- code analysis
- exploit
- PoC
- fuzzing

---

# 🔥 STEP 3B — BEHAVIOR CLASSIFICATION
If the user reports suspicious behavior:

1. The agent asks:
   - is it documented?
   - does it align with other parts of the system?
   - does it require elevated permissions?
   - can it be exploited?

2. If yes → FEATURE
3. If no → VULNERABILITY
4. If uncertain → BORDERLINE (request further testing)

---

# 🔥 STEP 4 — GENERATE WORKFLOW
Based on:
- context
- objective
- preferences
- memory
- vulnerability category (among the 14 available)

---

# 🔥 STEP 5 — SAVE SESSION
Update:
- targets.json
- history/<target>.md
- classifications
- preferences