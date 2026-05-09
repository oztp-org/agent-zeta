# Concept: Zero Trust Architecture

**Source:** Wikipedia — Zero Trust Architecture (CC BY-SA 4.0)  
**Last reviewed:** 2026-05-09

---

## Definition

Zero Trust Architecture (ZTA) is a security model that rejects implicit trust for any user, device, or network location — even those already inside a corporate network. Every access request is verified explicitly based on identity, device state, and context.

Core principle: "Users and devices should not be trusted by default, even if they are connected to a privileged network."

---

## Three Foundational Principles

1. **Verify explicitly** — authenticate and authorize every access request using all available signals (identity, device health, location, behavior)
2. **Use least privilege** — grant only the minimum access needed, for only as long as needed
3. **Assume breach** — design as if adversaries are already inside; minimize blast radius and contain damage

---

## History

| Year | Event |
|------|-------|
| 1994 | Stephen Paul Marsh coins "zero trust" in doctoral thesis |
| 2003 | Jericho Forum highlights limitations of perimeter-based security |
| 2009 | Google implements BeyondCorp after Operation Aurora breach |
| 2010 | John Kindervag (Forrester) popularizes the Zero Trust model |
| 2018 | NIST SP 800-207 formalizes ZTA |
| 2019 | UK NCSC recommends ZTA for cloud-heavy deployments |
| 2021 | US Executive Order 14028 mandates ZTA adoption across federal agencies |
| 2025 | ETSI publishes ZT-Kipling Methodology (iterative five-step framework) |

---

## Implementation Approaches

- **Enhanced identity governance** — policy-based access controls tied to verified identity
- **Micro-segmentation** — granular network boundaries at the workload level
- **Software-defined perimeters** — infrastructure invisible until access is granted
- **Overlay networks** — encrypted communication channels independent of the physical network

---

## ZT-Kipling Methodology (ETSI, 2025)

A systematic, iterative framework applying six questions (what, why, when, where, who, how) across five steps:

1. Define protected surface
2. Map transaction flows
3. Build Zero Trust Architecture
4. Create Zero Trust policy
5. Monitor and maintain

---

## Sector Adoption

**US Federal Government:** Agencies required to meet ZTA goals by FY2024 under EO 14028 and OMB M-22-09.

**Healthcare:** HHS identified ZT as foundational; December 2024 HIPAA Security Rule updates propose mandatory MFA, network segmentation, and encryption requirements.

**Defense:** DoD ZT Strategy targets full ZT adoption by FY2027; NSA ZIG Primer (January 2026) provides 152 discrete implementation activities.

---

## OZTP Context

- ZTA is the conceptual foundation for everything OZTP builds
- OZTP's assessment tools (CISA ZTMM v2, NIST SP 800-207) directly implement ZTA verification
- The Device Agent addresses the Devices pillar; Agent Zeta covers all five pillars for advisory
- When users ask "what is Zero Trust?" or "where did this come from?" — use this entry
