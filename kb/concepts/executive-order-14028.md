# Concept: Executive Order 14028 — Improving the Nation's Cybersecurity

**Source:** Wikipedia — Executive Order 14028 (CC BY-SA 4.0)  
**Last reviewed:** 2026-05-09

---

## Overview

Executive Order 14028, signed by President Biden on May 12, 2021, mandates significant cybersecurity improvements across the US federal government and its software supply chain. It is the primary regulatory driver for Zero Trust adoption in US federal agencies.

---

## Key ZT Mandates

- Federal agencies required to develop ZTA implementation plans within 60 days
- OMB M-22-09 (January 2022) followed with specific ZT goals: agencies must meet defined ZT targets by end of FY2024
- CISA Zero Trust Maturity Model developed as the assessment framework for compliance
- NIST SP 800-207 designated as the ZT architecture reference standard

---

## Software Supply Chain Requirements

EO 14028 also mandates supply chain security reforms, introducing the concept of **Software Bills of Materials (SBOMs)**:

- NTIA defines three minimum SBOM elements: Data Fields, Automation Support, Practices & Processes
- SBOMs require organizations to document every software component — origin, version, dependencies
- Enables continuous verification of software components (a ZT principle applied to software)

**Adoption reality (as of 2026):**
- Only ~0.56% of GitHub repositories contain policy-driven SBOMs
- 60–76% of enterprises now require supplier SBOMs
- Fewer than half of software projects include SBOMs in releases

---

## Why SBOMs Are Zero Trust

SBOMs operationalize "never trust, always verify" at the software component level:
- Know exactly what is running and where it came from
- Identify vulnerable dependencies immediately when CVEs are published
- Treat software provenance as an identity claim requiring verification

This directly mirrors how ZT treats user and device identity — no implicit trust in software components either.

---

## Related Directives

| Directive | Scope |
|-----------|-------|
| NSM-8 (Jan 2022) | Extends ZT requirements to National Security Systems |
| OMB M-22-09 | Specific federal ZT goals and FY2024 deadline |
| CISA ZTMM v2 | Maturity model for measuring EO 14028 compliance |
| NSA ZIG Primer (Jan 2026) | 152-activity implementation guide for DoD/NSS |

---

## OZTP Context

- EO 14028 is why US government and defense contractor audiences have urgent ZT mandates
- When users in federal, DoD, or DIB sectors ask about ZT requirements, cite EO 14028 + NSM-8
- SBOM requirements are a future expansion area for OZTP — software supply chain visibility
- The CISA ZTMM v2 (used in OZTP's assessment tool) was developed specifically to support EO 14028 compliance measurement
