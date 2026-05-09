# Concept: Microsegmentation

**Source:** Wikipedia — Microsegmentation (network security) (CC BY-SA 4.0)  
**Last reviewed:** 2026-05-09

---

## Definition

Microsegmentation establishes security zone boundaries at the level of individual workloads — rather than broad network subnets — within data centers and cloud environments. Each workload is treated as its own security domain requiring explicit authorization to communicate with any other.

It is the primary ZT control for the **Networks pillar**, eliminating lateral movement by removing implicit trust from internal traffic.

---

## How It Works

Traditional segmentation divides a network into large zones (e.g., "internal" vs. "DMZ"). Microsegmentation goes further — each server, VM, container, or application workload has its own policy. East-west traffic (between internal systems) is controlled and monitored, not assumed safe.

The result: a compromised workload can only reach what it is explicitly authorized to reach. Lateral movement requires defeating each workload's individual policy.

---

## Four Implementation Approaches

| Approach | How | Trade-offs |
|----------|-----|-----------|
| **Native OS Firewalls** | Host-based enforcement using OS firewall rules | Simple; limited central management |
| **Host-Agent Model** | Software agent on every host; centralized policy management | Powerful; requires agent on all hosts |
| **Hypervisor-Based** | All traffic flows through hypervisor for inspection | No agent needed; only works in virtualized environments |
| **Network-Based** | ACLs on existing network infrastructure | Leverages existing equipment; less granular |

---

## Zero Trust Relevance

Microsegmentation directly implements NIST SP 800-207 §2.6 — "All communication is secured regardless of network location." It:

- Eliminates implicit trust in internal networks
- Controls lateral communication between devices
- Reduces blast radius when a workload is compromised
- Enforces identity and access verification at the workload level

---

## The Lateral Movement Problem

Most major breaches involve lateral movement — attackers compromise one system, then move through the network to reach high-value targets. Microsegmentation makes this hard:

- Each hop requires explicit authorization
- Unusual east-west traffic patterns are visible and alertable
- A compromised endpoint can't directly reach the database server, domain controller, or backup system

---

## Challenges

- Legacy system support is limited — older systems may not support modern host-agent models
- Policy definition is complex — requires detailed knowledge of every workload's communication patterns
- Initial implementation requires extensive discovery and mapping

---

## OZTP Context

- Microsegmentation is a Networks pillar recommendation Zeta should make for any org with a flat internal network
- The Colonial Pipeline and Target breaches both involved lateral movement through insufficiently segmented networks
- When users ask "how do we stop lateral movement?" — microsegmentation is the primary technical answer
- Pairs with network monitoring/SIEM for visibility into east-west traffic
