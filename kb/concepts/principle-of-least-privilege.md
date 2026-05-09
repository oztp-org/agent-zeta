# Concept: Principle of Least Privilege

**Source:** Wikipedia — Principle of Least Privilege (CC BY-SA 4.0)  
**Last reviewed:** 2026-05-09

---

## Definition

The Principle of Least Privilege (PoLP) requires that every user, process, or system component be granted only the minimum permissions necessary to perform its defined function — nothing more, for no longer than required.

It is one of the oldest and most fundamental security principles, and a core pillar of Zero Trust Architecture.

---

## Applications

**User accounts:** Accounts should have only the permissions needed for specific job functions. An account used for backups should not have software installation rights.

**Processes and services:** Applications run with minimum required privileges; elevation occurs only when necessary and is revoked immediately after.

**Service accounts:** Non-human identities (APIs, automation, scheduled tasks) should be scoped to the exact resources they need — not domain admin.

**Just-in-time access:** Privileged access is granted only when needed and for a defined time window, then revoked — not held permanently.

---

## Why It Matters: Blast Radius

Least privilege is the primary mechanism for limiting blast radius when a breach occurs:

- A compromised low-privilege account can only damage what that account could access
- Lateral movement requires privilege escalation — which least privilege makes harder
- Insider threats are constrained by the same limits as external attackers

The Snowden and LastPass breaches both demonstrate what happens when this principle is violated: standing access to everything enabled massive exfiltration with no lateral movement required.

---

## Common Violations

| Violation | Risk |
|-----------|------|
| Domain admin used for daily work | Single credential compromise = full domain |
| Service accounts with excessive permissions | Compromised service = full environment access |
| Standing privileged access (no JIT) | Long window for undetected misuse |
| Shared admin credentials | No accountability, no rotation enforcement |
| Personal devices with privileged access | Unmanaged device + standing access = SPOF |

---

## Zero Trust Alignment

| ZT Framework | Least Privilege Reference |
|---|---|
| NIST SP 800-207 | §2.2 — All access granted least privilege; access decisions per-request |
| CISA ZTMM v2 | Identity pillar — privileged access management, JIT access |
| CIS Controls v8 | Control 5 (Account Management), Control 6 (Access Control Management) |

---

## OZTP Context

- Least privilege is the principle behind every "reduce standing access" recommendation Zeta makes
- Reference this when users ask about insider threat, privilege management, or PAM tools
- OZTP's own platform enforces least privilege: per-device scoped API keys, org-level keys separate from admin tokens, no shared credentials
