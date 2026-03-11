# AGENT LOGIC — README
This folder defines the agent behavior, its decision flow, memory handling, and the distinction between vulnerabilities and features.

---

# 📁 CONTENT
- AGENT_BEHAVIOR.md
  → Agent behavior rules
- INTERACTION_FLOW.md
  → Interaction flow and smart questions
- MEMORY_SYSTEM.md
  → How the agent stores and retrieves information
- CONTEXT_DECISION_TREE.md
  → Complete decision tree
- VULN_VS_FEATURE.md
  → How to distinguish vulnerabilities from features
- SESSION_PROFILE_TEMPLATE.md
  → Template for saving target profiles

---

# 🎯 LOGIC GOAL
The agent must:
- always ask for context
- ask only a few essential questions
- distinguish vulnerabilities from features
- remember previous sessions
- adapt to the user's style
- avoid false positives
- propose personalized workflows

---

# 🧠 HOW THE AGENT WORKS

## 1. Ask for context
(open source, live domain, mobile, api)

## 2. Ask only necessary questions
Each context has 3–4 key questions.

## 3. Classify behaviors
(feature / vulnerability / borderline)

## 4. Generate a personalized workflow
Based on:
- context
- objective
- memory
- preferences

## 5. Save the session
To avoid future repetitions.

---

# 🧩 HOW TO USE THIS LOGIC

### To start a session:
“New target: <name>. Context: <type>.”

### To make the agent remember something:
“Save that for this target I prefer to start with recon.”

### To ask for classification:
“Is this behavior a vulnerability or a feature?”

### To retrieve memory:
“What do we already know about this target?”

---

# 🛡️ IMPORTANT NOTES
- The agent must never assume something is a vulnerability without seeking clarification.
- The agent must always respect the program scope.
- The agent must avoid redundant questions.