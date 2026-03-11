# 08 — REPORTING TEMPLATES
**Applicable to all contexts (after the initial context has been asked and confirmed)**
>
> ⚠️ Remember: every report must be built **only after** asking and confirming the test context.
> The report format can vary slightly depending on the context (Open Source, Live Domain, Mobile, API).
>
> ---
>
## 📌 VULNERABILITY REPORT TEMPLATE
>
### **1. Vulnerability Title**
- Short and descriptive
- Example: `IDOR on endpoint /api/v1/user/profile`
>
### **2. Test Context**
- Test type (Open Source, Live Domain, Mobile, API)
- Defined scope
- Operational limitations
>
### **3. Description**
- Clear explanation of the vulnerability
- Where it was found
- Why it is significant
>
### **4. Impact**
- Technical impact
- Business impact
- Possible escalation
>
### **5. Proof of Concept**
- Reproducible steps
- Used payloads
- Screenshots/evidence
>
### **6. Steps to Reproduce**
1. Step 1
2. Step 2
3. Step 3
>
### **7. Recommendations**
- Technical fixes
- Structural improvements
- Best practices
>
> ---
>
## 📌 EXECUTIVE SUMMARY TEMPLATE
>
### **Test Objective**
- General purpose
- Operational context
>
### **Key Findings**
- Critical vulnerabilities
- Risk areas
- Priority recommendations
>
### **Conclusions**
- Overall risk level
- Recommended next steps
>
> ---
>
## 📌 PoC (Proof of Concept) TEMPLATE
>
```python
# PoC Template — adapt according to context
# Remember: the PoC must be generated only after confirming the context

import requests

TARGET = "https://example.com/api/v1/endpoint"

def exploit():
    payload = {
        "param": "value"
    }
    r = requests.post(TARGET, json=payload)
    print(r.status_code, r.text)

if __name__ == "__main__":
    exploit()
```