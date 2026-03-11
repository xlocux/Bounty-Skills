# REAL SESSION EXAMPLE
---
## 👤 User:
New target: api.shopwave.com
Context: API

---
## 🤖 Agent:
Perfect. To proceed I need only a few essential pieces of information:

1. Do you have API documentation?
2. Do you have a token or credentials?
3. Do you want to start with fuzzing or auth testing?

---
## 👤 User:
I have a user-level token. No documentation. Let's start with auth testing.

---
## 🤖 Agent:
Perfect. Before proceeding, I verify an important thing:

Does the API behavior have any documentation anywhere?
Do you have an example of the expected behavior for endpoints you've already tried?

---
## 👤 User:
No, there is no documentation. I tried /v1/user/profile and it works.

---
## 🤖 Agent:
Great. I classify this as **feature** (publicly authenticated endpoint).

I'll proceed with a personalized workflow:

### 🔥 API — Auth Testing Workflow
1. Endpoint enumeration via:
   - traffic reverse engineering
   - error analysis
   - undocumented parameters
2. Permission testing:
   - change ID
   - token removal
   - token forging
3. Permission checks:
   - roles
   - scope
   - HTTP methods

Do you want me to start with enumeration or permission testing?

---
## 👤 User:
Start with enumeration.

---
## 🤖 Agent:
Perfect. I save the session:

- target: api.shopwave.com
- context: API
- preference: auth testing
- classification: /v1/user/profile → feature

Proceeding with enumeration.