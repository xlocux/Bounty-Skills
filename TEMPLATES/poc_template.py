# PoC Template — adapt based on context
#⚠️ The agent must have requested and confirmed the context before generating a PoC.


import requests

TARGET = "https://example.com/api/v1/endpoint"

def exploit():
    payload = {
        "param": "value"
    }

    headers = {
        "User-Agent": "PoC-Agent",
        # Insert token only if allowed by the program
    }

    r = requests.post(TARGET, json=payload, headers=headers)
    print("[STATUS]", r.status_code)
    print("[RESPONSE]", r.text)

if __name__ == "__main__":
    exploit()
    
