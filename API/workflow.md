# WORKFLOW — API
1. Get documentation
2. Map endpoints
3. Identify authentication
4. Fuzz parameters
5. Authorization testing
6. Rate limit testing
7. GraphQL testing
8. WebSocket testing

---
Checklist cross-cutting vulnerabilities:
- Mass assignment / over-posting
- AuthZ on GraphQL resolver
- Webhook validation + replay
- Blind SSRF with OAST
- Cache poisoning