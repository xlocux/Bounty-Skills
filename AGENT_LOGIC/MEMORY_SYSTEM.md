# MEMORY SYSTEM
How the agent stores and retrieves information.

---

# 🎯 GOAL
Enable the agent to:
- remember already-analyzed targets
- remember user preferences
- avoid repetitive questions
- adapt the workflow
- remember vulnerability/feature classifications

---

# 📁 MEMORY STRUCTURE
- `/memory/`
  - `targets.json`
  - `preferences.json`
  - `history/`
    - `<target>.md`
    - `<target>.json`

---

# 📌 TARGETS.JSON
Contains:
- target name
- context
- last analysis date
- notes
- vulnerability/feature classifications

---

# 📌 PREFERENCES.JSON
Contains:
- workflow preferences
- tool preferences
- analysis preferences
- user style

---

# 📌 HISTORY/<TARGET>.MD
Contains:
- what was done
- found vulnerabilities
- used payloads
- completed steps
- involved vulnerability categories

---

# 🔍 VULNERABILITY/FEATURE CLASSIFICATION MEMORIZATION
The agent must save for each target:
- behaviors classified as feature
- borderline behaviors
- confirmed vulnerabilities
- classification motivations

Example:

```json
"classifications": {
  "/v1/user/profile": "feature",
  "/v1/admin/export": "vulnerability"
}
```

---

# 🔄 MEMORY RETRIEVAL
When the user enters a target:
- the agent checks if it exists in targets.json
- if yes → retrieve preferences and history
- if no → create a new profile

---

# 🧠 LEARNING
The agent updates:
- preferences based on recurring usage
- techniques that succeeded
- frequent vulnerability pattern
