# WORKFLOW — OPEN SOURCE

> ⚠️ Only usable after requesting and confirming the context: OPEN SOURCE.

1. Obtain the source code
2. Perform initial static analysis
3. Local build of the application
4. Set up the debugger
5. Interactive testing
6. Modify the code to test bypasses
7. Verify exploitability
8. Generate PoC

---

Cross-cutting vulnerability checklist:
- Mass assignment / over-posting
- JWT/session confusion
- Webhook validation
- Business logic race conditions
- File upload parsing and MIME trust