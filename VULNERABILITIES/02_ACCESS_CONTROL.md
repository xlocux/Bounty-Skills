# 02 — ACCESS CONTROL
Applicable to: All contexts

---

## 📌 Description
Authorization check errors allow unauthorized access to resources or functionality.

Types:
- IDOR
- Broken Access Control
- Privilege Escalation
- Horizontal/Vertical bypass
- Mass Assignment / Over-posting
- Multi-tenant Isolation Failures
- Authorization bypass via Object-level Caching

---

## 🔍 Identification
- ID manipulation (`/user/123 → /user/124`)
- Remove auth header
- Change role in JWT
- Update unforeseen fields (e.g., `role`, `isAdmin`, `ownerId`)
- Shared cache between users/tenants
- Authorization bypass via object-level caching

---

## 🧪 Test per context

| Context      | Technique |
|--------------|-----------|
| Open Source  | Analyze middleware and ACLs |
| Live Domain  | Parameter manipulation |
| Mobile       | Hook auth functions |
| API          | Test RBAC/ABAC |
| All          | Verify tenant isolation and cache keying |

---

## 🛡️ Remediation
- Server-side authorization checks
- Centralized authorization policies

---

## 📋 Test Template (expected input/output)

- **Objective:** verify enforcement of authorization for resources and actions.
- **Controlled input:** resource ID or owner value that is legitimate.
- **Test variant:** replace ID with another user's/tenant's resource.
- **Execution steps:** 1) baseline on own resource 2) variant on another's resource.
- **Expected safe output:** 403/404 or consistent empty response.
- **Indicative vulnerable output:** access to another's data or unauthorized modification.
- **Evidence to save:** resource ID, account, request/response.
- **Context notes:** in open source, check centralized policies and cache keying.

### Sample baseline + variant
- **Baseline:** `GET /profile/100` (mine) → **Variant:** `GET /profile/101`
- **Baseline:** `PATCH /user/100 {name:"A"}` → **Variant:** `PATCH /user/101 {name:"B"}`
- **Baseline:** `POST /team/1/invite {role:"member"}` → **Variant:** `{role:"admin"}`