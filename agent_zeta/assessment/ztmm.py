"""
CISA Zero Trust Maturity Model (ZTMM) v2.0 framework data.
Reference: CISA Zero Trust Maturity Model Version 2.0, April 2023.
https://www.cisa.gov/zero-trust-maturity-model
"""
from dataclasses import dataclass
from enum import IntEnum


class MaturityLevel(IntEnum):
    TRADITIONAL = 1
    INITIAL = 2
    ADVANCED = 3
    OPTIMAL = 4

    @property
    def label(self) -> str:
        return {1: "Traditional", 2: "Initial", 3: "Advanced", 4: "Optimal"}[self.value]


@dataclass
class PillarCriteria:
    level: MaturityLevel
    description: str
    indicators: list[str]


@dataclass
class Pillar:
    name: str
    description: str
    questions: list[str]
    criteria: list[PillarCriteria]


PILLARS: list[Pillar] = [
    Pillar(
        name="Identity",
        description=(
            "Managing and continuously authenticating all identities — human users, "
            "service accounts, and machine identities — that access organizational resources."
        ),
        questions=[
            "Do all users authenticate with multi-factor authentication (MFA)?",
            "Do you have a centralized Identity Provider (IdP) for all systems?",
            "Do you use phishing-resistant MFA (e.g., FIDO2, hardware tokens) for privileged accounts?",
            "Are service accounts and machine identities tracked in a separate inventory?",
            "Is access automatically revoked when an employee leaves or changes roles?",
            "Do you enforce least-privilege access and review permissions regularly?",
            "Do you analyze user/identity behavior for anomalies (UEBA)?",
        ],
        criteria=[
            PillarCriteria(
                MaturityLevel.TRADITIONAL,
                "Static, perimeter-based identity with password-only auth for most systems.",
                ["Password-only auth common", "No centralized IdP", "Manual or no access reviews"],
            ),
            PillarCriteria(
                MaturityLevel.INITIAL,
                "MFA deployed for some systems; centralized IdP starting to be used.",
                ["MFA for remote access", "IdP partially adopted", "Basic periodic access reviews"],
            ),
            PillarCriteria(
                MaturityLevel.ADVANCED,
                "MFA broadly enforced; risk-based authentication; automated lifecycle management.",
                [
                    "MFA for most systems",
                    "Centralized IdP with full integration",
                    "Automated provisioning/deprovisioning",
                    "Phishing-resistant MFA for privileged accounts",
                ],
            ),
            PillarCriteria(
                MaturityLevel.OPTIMAL,
                "Fully dynamic, risk-based continuous identity verification with behavioral analytics.",
                [
                    "Phishing-resistant MFA everywhere",
                    "UEBA/behavioral analytics",
                    "Real-time access revocation",
                    "Full machine identity lifecycle management",
                ],
            ),
        ],
    ),
    Pillar(
        name="Devices",
        description=(
            "Ensuring all devices (endpoints) are inventoried, healthy, and compliant "
            "before and during access to organizational resources."
        ),
        questions=[
            "Do you maintain a complete inventory of all devices accessing your network?",
            "Are all devices enrolled in MDM or a device management platform?",
            "Is device health/compliance checked before granting access to resources?",
            "Is endpoint detection and response (EDR) deployed on all endpoints?",
            "Do you enforce application allowlisting on any endpoints?",
            "Is patching performed consistently on a defined schedule (e.g., within 14 days)?",
            "Are non-compliant devices automatically isolated or blocked?",
        ],
        criteria=[
            PillarCriteria(
                MaturityLevel.TRADITIONAL,
                "Partial device inventory; reactive patching; no compliance enforcement at access time.",
                ["Incomplete asset inventory", "Reactive patching", "Basic AV only, no EDR"],
            ),
            PillarCriteria(
                MaturityLevel.INITIAL,
                "Device inventory maturing; MDM deployed for some devices; regular patching cycle.",
                ["Asset inventory improving", "MDM for some devices", "Defined patching schedule"],
            ),
            PillarCriteria(
                MaturityLevel.ADVANCED,
                "Full device inventory; compliance gates enforced; EDR on all devices.",
                [
                    "Complete device inventory",
                    "MDM with compliance enforcement",
                    "EDR fully deployed",
                    "App control on critical systems",
                ],
            ),
            PillarCriteria(
                MaturityLevel.OPTIMAL,
                "Real-time device health signals feed access decisions; fully automated remediation.",
                [
                    "Real-time compliance posture feeds into access decisions",
                    "Automated device remediation",
                    "Full application allowlisting",
                    "Zero-touch device provisioning",
                ],
            ),
        ],
    ),
    Pillar(
        name="Networks",
        description=(
            "Segmenting and monitoring networks to limit lateral movement, "
            "with encrypted traffic and Zero Trust Network Access replacing legacy VPNs."
        ),
        questions=[
            "Is your network segmented (VLANs, micro-segmentation, or software-defined perimeter)?",
            "Is all network traffic encrypted in transit (internal and external)?",
            "Do you have visibility into East-West (internal, server-to-server) traffic?",
            "Are you using Zero Trust Network Access (ZTNA) to replace or supplement VPN?",
            "Do you filter and inspect DNS traffic?",
            "Do you have Network Detection and Response (NDR) capabilities?",
            "Are network access controls enforced based on identity and device posture, not just IP?",
        ],
        criteria=[
            PillarCriteria(
                MaturityLevel.TRADITIONAL,
                "Flat internal network with perimeter firewall only; minimal visibility.",
                ["Flat internal network", "Perimeter-only defense", "Limited internal traffic visibility"],
            ),
            PillarCriteria(
                MaturityLevel.INITIAL,
                "Basic network segmentation; external traffic encrypted; some internal logging.",
                ["VLAN segmentation", "TLS for external traffic", "Firewall and basic log review"],
            ),
            PillarCriteria(
                MaturityLevel.ADVANCED,
                "Micro-segmentation deployed; ZTNA in use; internal traffic encrypted and monitored.",
                [
                    "Micro-segmentation",
                    "Internal TLS / encryption",
                    "ZTNA supplementing or replacing VPN",
                    "NDR or network analytics",
                ],
            ),
            PillarCriteria(
                MaturityLevel.OPTIMAL,
                "Software-defined perimeter; all traffic verified by identity and posture; full East-West visibility.",
                [
                    "Full micro-segmentation",
                    "All traffic encrypted and inspected",
                    "ZTNA everywhere; VPN fully retired",
                    "Real-time anomaly detection across all segments",
                ],
            ),
        ],
    ),
    Pillar(
        name="Applications & Workloads",
        description=(
            "Securing applications, APIs, and cloud workloads through the full lifecycle, "
            "with least-privilege access and integrated security testing."
        ),
        questions=[
            "Do you maintain an inventory of all applications and APIs?",
            "Is security testing (SAST/DAST) integrated into your development pipeline (DevSecOps)?",
            "Do you use a WAF or API gateway with authentication and rate-limiting?",
            "Are secrets and credentials stored in a secrets manager (no hardcoded credentials)?",
            "Do you perform regular vulnerability scanning and remediate findings on a defined SLA?",
            "Do you enforce least-privilege for application service accounts?",
            "Do you monitor application and API behavior for anomalies at runtime?",
        ],
        criteria=[
            PillarCriteria(
                MaturityLevel.TRADITIONAL,
                "Limited app/API inventory; no DevSecOps; minimal API security controls.",
                ["Incomplete app inventory", "No security in CI/CD", "Hardcoded credentials possible"],
            ),
            PillarCriteria(
                MaturityLevel.INITIAL,
                "App inventory growing; some security scanning in pipeline; WAF deployed.",
                ["App/API inventory in progress", "Basic SAST or DAST in pipeline", "WAF deployed"],
            ),
            PillarCriteria(
                MaturityLevel.ADVANCED,
                "DevSecOps integrated; secrets management enforced; API gateway with auth in place.",
                [
                    "Mature DevSecOps pipeline",
                    "Secrets management (vault/HSM)",
                    "API gateway with auth and rate-limiting",
                    "Defined vuln SLAs",
                ],
            ),
            PillarCriteria(
                MaturityLevel.OPTIMAL,
                "Automated security gates block deployments; runtime behavioral monitoring; immutable workloads.",
                [
                    "Automated security gates block risky deployments",
                    "Runtime application self-protection (RASP) or equiv.",
                    "Full API behavioral analytics",
                    "Immutable workload infrastructure",
                ],
            ),
        ],
    ),
    Pillar(
        name="Data",
        description=(
            "Protecting data through classification, access control tied to sensitivity, "
            "encryption at rest and in transit, and Data Loss Prevention."
        ),
        questions=[
            "Do you have an active data classification program (not just a policy)?",
            "Is sensitive and regulated data encrypted at rest?",
            "Do you know where your sensitive data lives (data discovery)?",
            "Is Data Loss Prevention (DLP) deployed and enforced on key channels?",
            "Are access controls tied to data classification labels?",
            "Do you have a data retention and secure disposal policy in active use?",
            "Do you monitor for unusual data access or exfiltration attempts?",
        ],
        criteria=[
            PillarCriteria(
                MaturityLevel.TRADITIONAL,
                "No formal data classification in practice; inconsistent encryption; no DLP.",
                ["No active data classification", "Encryption inconsistent", "No DLP deployed"],
            ),
            PillarCriteria(
                MaturityLevel.INITIAL,
                "Classification policy defined and starting; encryption for regulated data; DLP piloting.",
                ["Classification policy exists", "Encryption for regulated data", "DLP on some channels (e.g., email)"],
            ),
            PillarCriteria(
                MaturityLevel.ADVANCED,
                "Automated data discovery; DLP enforced; access tied to classification.",
                [
                    "Automated data discovery and classification",
                    "Broad DLP enforcement",
                    "Access controls driven by classification labels",
                ],
            ),
            PillarCriteria(
                MaturityLevel.OPTIMAL,
                "Real-time classification; full DLP coverage; behavioral analytics on data access.",
                [
                    "Real-time automated classification",
                    "Full DLP across all channels",
                    "UEBA for data access anomalies",
                    "Automated data lifecycle management",
                ],
            ),
        ],
    ),
]

PILLAR_BY_NAME: dict[str, Pillar] = {p.name: p for p in PILLARS}
