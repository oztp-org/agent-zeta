# Threat Intel: Instructure Canvas Data Breach (ShinyHunters, May 2026)

**Status:** Active / Ongoing  
**First Observed:** 2026-04-30  
**Ransom Deadline:** 2026-05-12  
**Last Updated:** 2026-05-08  
**Source Type:** Multi-source (news, Wikipedia, Malwarebytes, SOCRadar)

---

## Summary

The hacking group **ShinyHunters** breached **Instructure**, the company behind the **Canvas LMS** — the leading cloud-based learning management system used by K-12 schools, community colleges, and universities worldwide. The group claims to have exfiltrated data on **275 million users** across **~8,809 institutions** and is threatening to publicly release the data unless a ransom is paid by **May 12, 2026**.

This is described as ShinyHunters breaching Instructure **"again"** — suggesting a prior unresolved incident.

---

## Timeline

| Date | Event |
|------|-------|
| 2026-04-30 | Attack begins; Instructure later discloses investigation into breach |
| 2026-05-05 | Instructure confirms incident publicly; data includes names, emails, IDs, messages |
| 2026-05-07 | Canvas login pages replaced with ShinyHunters ransom message; platform placed in maintenance mode (~4 hrs) |
| 2026-05-07 | Platform restored "for most users" by late evening |
| 2026-05-07 | Wake County Public School System (NC) disables Canvas entirely |
| 2026-05-07 | Multiple universities postpone final exams |
| 2026-05-08 | Incident ongoing; ransom deadline still active |
| 2026-05-12 | ShinyHunters deadline to release all data if unpaid |

---

## Threat Actor: ShinyHunters

- **Type:** Criminal extortion / ransomware group
- **Description:** Loose affiliation of teenagers and young adults, primarily based in the U.S. and UK
- **Tactics:** Breach → data exfiltration → public extortion via leak sites → ransom demand with deadline
- **Prior targets (2026):** Infinite Campus (K-12 SIS), McGraw Hill (publisher), Vimeo
- **Escalation pattern:** Posted ransom messages directly on school Canvas login pages — high-visibility, public-facing pressure tactic

---

## Data Compromised

**Confirmed by Instructure:**
- Names
- Email addresses
- Student ID numbers
- Messages between users (private messages within Canvas)

**Instructure states NO evidence of compromise for:**
- Passwords
- Dates of birth
- Social Security numbers / government identifiers
- Financial information

> Note: Instructure's "no evidence" claim should not be treated as definitive — the deadline is still active and the full scope has not been independently verified.

---

## Scale of Impact

| Metric | Value |
|--------|-------|
| Claimed affected users | 275 million |
| Claimed affected institutions | ~8,809 schools, universities, and platforms |
| Canvas global active users | 30+ million |
| Verified impact | Widespread (Cornell, UC Berkeley, Stanford, Duke, U of Minnesota, U of Pennsylvania, OSU, U of Illinois, Sacramento State, SFSU, Peralta CCD, and many others) |
| International | Netherlands (44+ institutions), Australia (multiple universities and vocational providers), plus US nationwide |

---

## Institutional Response

- **Wake County Public Schools (NC):** Disabled Canvas entirely; removed icon from WakeID portal
- **Multiple universities:** Extended deadlines, shuffled or postponed final exams
- **Netherlands:** Universities of the Netherlands umbrella org — no ransom approach received as of May 8
- **Australia:** National Office of Cyber Security coordinating response
- **Instructure:** Stated situation "resolved" on May 7 before ShinyHunters posted ransom note — credibility gap

---

## Zero Trust Relevance

This incident maps directly to CISA ZTMM pillars:

| Pillar | Relevance |
|--------|-----------|
| **Data** | Student PII, private messages, and institutional records exfiltrated from a shared SaaS platform — data classification and DLP controls would reduce exposure scope |
| **Identity** | Ransom messages posted on login pages suggests identity/access control compromise or platform-level credential abuse |
| **Applications & Workloads** | Canvas is a critical SaaS workload — schools lacked controls over what Instructure held on their behalf; third-party SaaS risk not managed |
| **Networks** | Platform-wide outage demonstrates single-point-of-failure risk for SaaS-dependent institutions |

**Key ZT lesson:** Organizations treating a SaaS vendor as a trust boundary instead of applying Zero Trust principles to their SaaS integrations inherited the full blast radius of Instructure's breach.

---

## Recommended Actions for Affected Schools / Districts

Ordered by impact vs. effort:

1. **Communicate to students and staff immediately** — what was taken, what was not, and what they should do (watch for phishing)
2. **Monitor for phishing campaigns** targeting institutional email addresses using Canvas branding or school names — threat actors often weaponize breached data for follow-on attacks
3. **Do NOT pay ransom** — there is no guarantee of data deletion, and payment signals future willingness
4. **Reset any shared or service account credentials** associated with Canvas integrations (SSO connectors, API tokens, LTI integrations)
5. **Audit third-party SaaS integrations** — understand what data each vendor holds and what your incident response options are
6. **Enable MFA** on all accounts linked to Canvas (student, staff, admin) where not already enforced
7. **Review SIS ↔ Canvas data feeds** — if Canvas was syncing from a Student Information System (SIS), assess what data was live in Canvas at time of breach
8. **Document and notify** per applicable state/federal breach notification laws (FERPA, state statutes)

---

## OZTP Context

This breach is a direct, real-world case study for OZTP's mission:

- Demonstrates why **SaaS risk is a Zero Trust problem**, not just a vendor problem
- Reinforces the **Applications & Workloads** and **Data** pillars from CISA ZTMM
- Relevant to **school districts and higher ed** as a target vertical for OZTP outreach
- Could inform an **Agent Zeta advisory thread** for institutions asking "how do we protect against SaaS platform breaches?"
- Potential outreach angle: schools affected by this breach are now actively looking for better ZT posture — OZTP can help with assessment

---

## Sources

- [Canvas hack: What we know (CNN)](https://www.cnn.com/2026/05/07/us/canvas-hack-strands-college-students-finals-week)
- [ShinyHunters Breaches Instructure (SOCRadar)](https://socradar.io/blog/shinyhunters-breach-instructure-students-teachers/)
- [Instructure Confirms Canvas Breach (Bitdefender)](https://www.bitdefender.com/en-us/blog/hotforsecurity/canvas-data-breach-2026)
- [Millions of students' data stolen (Malwarebytes)](https://www.malwarebytes.com/blog/news/2026/05/millions-of-students-personal-data-stolen-in-major-education-cyberattack)
- [TechCrunch: Hackers steal students' data](https://techcrunch.com/2026/05/05/hackers-steal-students-data-during-breach-at-education-tech-giant-instructure/)
- [Inside Higher Ed: PAY OR LEAK](https://www.insidehighered.com/news/tech-innovation/administrative-tech/2026/05/05/pay-or-leak-hackers-target-big-higher-ed-vendor)
- [2026 Canvas security incident (Wikipedia)](https://en.wikipedia.org/wiki/2026_Canvas_security_incident)
- [DataBreaches.net: ShinyHunters Hacks Instructure Again](https://databreaches.net/2026/05/07/developing-shinyhunters-hacks-instructure-again-canvas-down/)
- [HackRead: ShinyHunters Canvas LMS and Vimeo Breaches](https://hackread.com/shinyhunters-instructure-canvas-lms-vimeo-data-breach/)
- [Star Tribune: University of Minnesota affected](https://www.startribune.com/university-of-minnesota-canvas-outage-down-login-cyberattack-breach-shinyhunters-instructure/601838661)
- [KQED: Bay Area Colleges Disrupted](https://www.kqed.org/news/12082828/canvas-hacked-bay-area-colleges-disrupted-by-global-cyberattack-on-learning-platform)
- [Cornell Daily Sun: Canvas Back Online](https://www.cornellsun.com/article/2026/05/canvas-comes-back-online-following-cyberattack-disruption)
- [Space Coast Rocket: Brevard/Florida/EFSC](https://thespacecoastrocket.com/brevard-schools-florida-tech-efsc-canvas-ransomware/)
