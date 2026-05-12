# Canvas LMS — Credential Management and ZT-Aligned Authentication

**Pillar:** Identity  
**CISA ZTMM Target:** Advanced (short-lived, scoped credentials; JIT access)  
**Applies to:** K-12 districts and higher education using Instructure Canvas LMS

---

## The Problem: Long-Lived API Tokens

Canvas allows users and admins to generate **Personal Access Tokens** (Settings → Approved Integrations → New Access Token). By default these never expire. A stolen or leaked token provides persistent read/write access to Canvas data until someone manually revokes it — violating the ZT principle of no standing credentials.

This is the credential risk class exposed in the May 2026 ShinyHunters breach.

---

## The ZT Fix: OAuth 2.0 Developer Keys

Canvas supports **OAuth 2.0** for third-party integrations via Developer Keys (Canvas Admin → Developer Keys). This is the ZT-aligned alternative to personal access tokens.

**How it works:**
1. An admin creates a Developer Key in Canvas Admin (scoped to specific API permissions)
2. Integrations use the OAuth 2.0 Authorization Code flow to request an access token at runtime
3. The token is short-lived and tied to the user session
4. When the session ends or the token expires, access ends automatically

**Key advantages over personal access tokens:**
- Tokens expire automatically (no standing credentials)
- Scoped to only the API endpoints the integration needs (least privilege)
- Can be revoked per-key without rotating all integrations
- Access logs show which key was used and when

---

## Setting Token Expiration

Even for legacy personal access tokens already in use, Canvas allows setting an expiration date at creation time. Enforce an institutional policy:
- Admin tokens: 30-day maximum, rotated on a schedule
- Service account tokens: replace with OAuth 2.0 Developer Keys
- Student/staff tokens: 90-day maximum with calendar reminders

---

## LTI (Learning Tools Interoperability)

For tool integrations (video platforms, proctoring, publishing tools), prefer **LTI 1.3** over API token-based integrations. LTI 1.3 uses signed, per-launch JWTs rather than persistent tokens — aligning with ZT session-scoped access.

Canvas Admin → Settings → Apps → View App Configurations → Add LTI Key

---

## Audit and Rotate — Immediate Actions

- [ ] Canvas Admin → Developer Keys: review all active keys, disable unused ones, check scopes
- [ ] Canvas Admin → People → filter by "Admin" role: verify all admins have MFA enforced
- [ ] Audit personal access tokens: query via Canvas API `GET /api/v1/users/:user_id/tokens` — flag any with no expiration
- [ ] Check SIS integration credentials: most SIS ↔ Canvas connectors use a service account token — replace with an OAuth Developer Key

---

## Framework References

| Control | Reference |
|---------|-----------|
| No standing credentials | NIST SP 800-207 Tenet 3 — per-session access grants |
| JIT access provisioning | CISA ZTMM Identity Pillar — Advanced maturity |
| Least-privilege scoping | CIS Controls v8 #6 — Access Control Management |
| Credential rotation | NIST SP 800-207 §3.3 |
