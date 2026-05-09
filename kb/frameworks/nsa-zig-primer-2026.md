# Framework: NSA Zero Trust Implementation Guideline Primer (January 2026)

**Document:** NSA Cybersecurity Technical Report  
**Title:** Zero Trust Implementation Guideline Primer  
**Date:** January 2026  
**Version:** 1.0  
**Classification:** Unclassified  
**Reference:** U/OO/102936-26, PP-25-3613  
**Developed by:** NSA in partnership with DoD CIO

---

## Purpose

A structured, phased approach for implementing Zero Trust across government and critical infrastructure environments. The ZIGs (Zero Trust Implementation Guidelines) provide 152 discrete Activities organized into 5 phases, each tied to 45 Capabilities across 7 ZT pillars.

Not prescriptive or mandatory. Vendor-agnostic. Designed as a modular framework that can be adopted by DoD, the Defense Industrial Base (DIB), NSS networks, and any organization seeking a rigorous ZT implementation path.

---

## Policy Context

| Mandate | Scope |
|---------|-------|
| Executive Order 14028 (May 2021) | Federal civilian agencies — adopt ZT principles |
| NSM-8 (Jan 2022) | NSS (National Security Systems) networks — ZT requirements |
| DoD ZT Strategy (Nov 2022) | DoD-wide ZT adoption target by FY2027 |
| DoD ZT Reference Architecture v2.0 | Technical foundation aligned with ZIGs |

---

## Three Core ZT Principles

1. **Never trust, always verify** — No implicit trust based on network location or asset ownership
2. **Assume breach** — Design as if adversaries already have access; limit blast radius
3. **Verify explicitly** — Continuous authentication and authorization using all available signals

---

## Seven ZT Pillars

| Pillar | Focus |
|--------|-------|
| **Identity** | Users, service accounts, non-person entities; MFA, identity governance |
| **Devices** | Endpoint health, compliance, configuration; managed and unmanaged |
| **Applications & Workloads** | App access control, API security, workload isolation |
| **Data** | Classification, labeling, encryption, DLP, access governance |
| **Networks** | Microsegmentation, encrypted traffic, DNS security, network visibility |
| **Automation & Orchestration** | SOAR, policy automation, orchestrated response |
| **Visibility & Analytics** | SIEM, UEBA, log aggregation, threat detection |

---

## Capability Model

**45 total Capabilities** across three tiers:

| Tier | Count | Meaning |
|------|-------|---------|
| Target | 15 | Baseline ZT posture — foundational controls all organizations should achieve |
| Target + Advanced | 27 | Mature ZT capabilities — continuous verification, automated response |
| Advanced | 3 | Leading-edge capabilities — typically DoD/NSS specific |

---

## Five Implementation Phases

**Total: 152 Activities**

### Phase 0 — Discovery (14 Activities)
- Inventory assets, identities, data flows
- Assess current security posture across all 7 pillars
- Identify gaps vs. ZT target state
- Establish ZT governance structure

### Phase 1 — Foundation (36 Activities)
- Deploy MFA for all privileged users
- Begin device health attestation
- Implement basic network segmentation
- Enable centralized logging and SIEM
- Establish identity governance baseline

### Phase 2 — Advanced Identity & Devices (41 Activities)
- Continuous authentication for all users
- Device compliance enforcement before resource access
- Conditional access policies
- Privileged access workstations (PAWs)
- Begin application microsegmentation

### Phase 3 — Data-Centric Controls (37 Activities)
- Data classification and labeling at scale
- DLP policies enforced at endpoints and cloud
- Attribute-based access control (ABAC)
- Advanced network microsegmentation
- Automated threat detection and response

### Phase 4 — Advanced Automation & Analytics (24 Activities)
- Fully automated policy orchestration
- UEBA with behavioral baselines
- Continuous threat hunting
- Cross-pillar telemetry correlation
- Adaptive access based on real-time risk scoring

---

## Alignment with Other Frameworks

| Framework | Relationship |
|-----------|-------------|
| **NIST SP 800-207** | ZIGs are designed to satisfy all NIST ZT tenets |
| **CISA ZTMM v2** | Phase progression maps to CISA maturity levels (Traditional → Optimal) |
| **DoD ZT Reference Architecture v2.0** | ZIGs implement the DoD ZT RA's technical components |
| **DoD ZT Strategy** | FY2027 "Target" tier goal aligns with ZIG Phase 1-2 completion |

---

## Key Distinctions from CISA ZTMM

| Dimension | CISA ZTMM v2 | NSA ZIGs |
|-----------|-------------|----------|
| Structure | Maturity levels (Traditional/Initial/Advanced/Optimal) | Phased activities (0–4) |
| Use case | Self-assessment, gap scoring | Implementation roadmap |
| Audience | Civilian agencies, broad enterprise | DoD, DIB, NSS; enterprise applicable |
| Prescriptiveness | Descriptive maturity model | Discrete activities with sequencing |
| Activity count | ~98 scored controls | 152 discrete activities |

---

## OZTP Relevance

- The **Devices pillar** directly mirrors OZTP's device agent scope: health attestation, posture checks, enforcement vs. audit mode
- Phase 0 (Discovery) is what OZTP's ZT Maturity Assessment tool supports — inventory gaps before you implement
- Phase 1 activities (device health, centralized logging) are what OZTP's Control Platform delivers for Windows endpoints
- Agent Zeta should reference ZIGs when users ask about:
  - "How do I get started with Zero Trust?" → Phase 0 activities
  - "What should we prioritize?" → Phase 1 foundation activities
  - "How does this compare to CISA ZTMM?" → See comparison table above
  - Any DoD, government, or defense contractor context — ZIGs are directly applicable

---

## Recommended Actions (from ZIG Phase 0)

1. **Inventory all identities** — human, service accounts, non-person entities
2. **Inventory all devices** — managed, BYOD, IoT; assess current health visibility
3. **Map data flows** — where does sensitive data live, how does it move?
4. **Assess current posture** across all 7 pillars (use OZTP ZT Assessment for structured scoring)
5. **Identify quick wins** — Phase 1 activities with highest impact and lowest effort
6. **Establish ZT governance** — assign ZT champion, define success metrics

---

## Sources

- NSA Cybersecurity Technical Report: Zero Trust Implementation Guideline Primer, January 2026 (U/OO/102936-26)
- DoD Zero Trust Reference Architecture v2.0
- CISA Zero Trust Maturity Model v2.0
- NIST SP 800-207: Zero Trust Architecture
- Executive Order 14028 on Improving the Nation's Cybersecurity (May 2021)
