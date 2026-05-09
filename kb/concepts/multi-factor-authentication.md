# Concept: Multi-Factor Authentication (MFA)

**Source:** Wikipedia — Multi-factor authentication (CC BY-SA 4.0)  
**Last reviewed:** 2026-05-09

---

## Definition

Multi-factor authentication (MFA) requires users to present two or more distinct types of evidence before gaining access. It significantly reduces compromise risk because an attacker must obtain multiple independent credentials rather than just a password.

MFA is the single highest-impact ZT control for the Identity pillar — and the most commonly missing control in breach post-mortems.

---

## Authentication Factors

| Factor | Type | Examples |
|--------|------|---------|
| **Knowledge** | What you know | Password, PIN, passphrase, security question |
| **Possession** | What you have | Hardware token, FIDO2 key, authenticator app, smart card |
| **Inherence** | What you are | Fingerprint, facial recognition, iris scan, voice, keystroke dynamics |
| **Location** | Where you are | Network context, geolocation — adapts rigor based on risk |

True MFA requires factors from at least two different categories.

---

## Common Implementations — Strengths and Weaknesses

| Method | Strength | Weakness |
|--------|----------|----------|
| SMS one-time password | Accessible, no extra hardware | Vulnerable to SIM swapping, SS7 attacks, phishing interception |
| Authenticator app (TOTP) | Strong, offline, no carrier dependency | Device loss = lockout risk |
| Push notification | Convenient | Vulnerable to MFA fatigue attacks |
| FIDO2 / hardware security key | Phishing-resistant, strongest available | Cost, logistics, loss management |
| Biometrics | Convenient, hard to steal | Privacy concerns, spoofing, no revocation |

---

## Critical Vulnerabilities

**MFA fatigue attacks:** Attackers send repeated push notification requests until the user accepts out of frustration. Used in the 2022 Uber breach — one contractor accepted a push after being bombarded. Mitigation: require number matching or explicit context confirmation rather than a simple tap-to-approve.

**Phishing / AiTM (Adversary-in-the-Middle):** Attackers intercept the authentication flow in real time, capturing session tokens after MFA is satisfied. FIDO2 hardware keys are the primary defense — they are domain-bound and phishing-resistant.

**Recovery bypass:** Poorly implemented account recovery (SMS reset, security questions) can bypass MFA entirely. Account recovery is an attack surface as dangerous as the login itself.

---

## ZT Recommendations (Priority Order)

1. **Enforce MFA on all privileged accounts** — no exceptions, including service accounts where possible
2. **Enforce MFA on VPN and remote access** — the Colonial Pipeline breach was one VPN account with no MFA
3. **Prefer authenticator apps over SMS** — SMS is the weakest form of MFA still widely deployed
4. **Evaluate FIDO2 for high-risk accounts** — executives, admins, finance, HR
5. **Harden recovery procedures** — MFA is only as strong as its weakest bypass path
6. **Enable number matching on push notifications** — defeats most MFA fatigue attacks

---

## Framework Alignment

| Framework | MFA Requirement |
|-----------|----------------|
| NIST SP 800-207 | §2.1 — All access requests authenticated; phishing-resistant MFA for privileged access |
| CISA ZTMM v2 | Identity pillar — MFA required at Initial maturity level |
| CIS Controls v8 | Control 6.3 — Require MFA for externally-exposed applications |
| HIPAA (proposed 2024) | Mandatory MFA for covered entities |

---

## OZTP Context

- MFA is the first recommendation Zeta should make for any org that doesn't have it universally deployed
- Colonial Pipeline (no MFA on VPN), Twitter 2020 (no secondary verification on admin tools), and Uber 2022 (MFA fatigue) are all directly relevant incident references
- OZTP's own platform enforces MFA at sign-in
