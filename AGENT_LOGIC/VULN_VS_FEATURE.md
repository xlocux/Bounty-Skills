# VULNERABILITY VS FEATURE
How the agent distinguishes a vulnerable behavior from an intended feature.

---
## 🎯 GOAL
Avoid false positives and understand if a behavior:
- is a real vulnerability
- is a intended feature
- is a borderline edge case
- is an undocumented but intended behavior

---
## 🧠 BASE PRINCIPLE
The agent MUST NEVER assume something is a vulnerability without first:
1. asking the user for clarification
2. verifying the context
3. comparing the behavior with the program scope
4. evaluating if there are legitimate alternatives

---
## 🔍 CHECKLIST TO DIFFERENTIATE VULNERABILITIES FROM FEATURES

### 1. **Is the behavior documented?**
- If yes → probably a feature
- If no → could be a vulnerability

### 2. **Does the behavior require elevated permissions?**
- If yes → could be by design
- If no → suspicious

### 3. **Does the behavior break a security model?**
- Access without authorization
- Escalation
- Data manipulation
- Bypass controls
- ...

If yes → vulnerability

### 4. **Is the behavior consistent with other parts of the system?**
- If yes → feature
- If no → vulnerability

### 5. **Can the behavior be exploited to gain an unintended advantage?**
- If yes → vulnerability

---
## ❓ QUESTIONS THE AGENT MUST ASK THE USER

### 1. “Is this behavior documented in the platform or APIs?”
### 2. “Do you have an example of how it should normally work?”
### 3. “Does the bug bounty program consider this behavior in-scope?”
### 4. “Does it require authentication or special permissions to reproduce?”
### 5. “Does the behavior allow obtaining access or actions that were not intended?”

---
## 🧪 PRACTICAL EXAMPLES

### 🔸 Case 1 — Feature
An endpoint `/api/v1/user/profile` returns the user's own profile without token refresh.
→ Feature, not a vulnerability.

### 🔸 Case 2 — Borderline
An endpoint allows viewing public data but with undocumented parameters.
→ Could be an undocumented feature.

### 🔸 Case 3 — Vulnerability
An endpoint allows accessing other users' data by changing the ID.
→ IDOR → vulnerability.

---
## 🛡️ HOW THE AGENT SHOULD ACT

### If it's a feature:
- explain why
- ask if the user wants to explore further anyway

### If it's borderline:
- ask for additional details
- propose additional testing

### If it's a vulnerability:
- proceed with:
    - analysis
    - exploit
    - PoC
    - report

---
## 📌 IMPORTANT NOTE
The agent must ALWAYS:
- ask for context
- ask for clarification
- avoid rushed conclusions
- propose additional verification