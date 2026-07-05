# FortiBleed — Mass Credential Exposure on Fortinet Devices (June 2026)

## Summary

FortiBleed is a mass credential exposure affecting roughly 86,644 unique Fortinet devices (FortiGate firewalls and SSL VPN gateways) across 194 countries — close to half of all internet-facing FortiGate firewalls worldwide. It is not a software vulnerability: there is no CVE and no patch. Researcher Volodymyr "Bob" Diachenko discovered the dataset between June 13–17, 2026, after finding a threat actor's own staging server left open on the internet. CISA issued a hardening alert on June 18, 2026.

## Technical Details

Attackers assembled the credential set through multiple parallel techniques:

- **Credential-reuse automation** — an estimated 1.16 billion login attempts against more than 320,000 FortiGate targets using known/leaked credential lists
- **Offline hash-cracking** — SSL VPN authentication hashes intercepted during the login handshake, cracked offline via a 45-GPU cluster orchestrated with Hashtopolis (open-source distributed cracking framework)
- **Multi-source aggregation** — older configuration-file leaks, phishing hauls, credential-stuffing lists, and malware infostealer logs

Roughly 63.3% of exposed accounts were default or built-in Fortinet system accounts (35% generic admin, 28.3% built-in system accounts) never rotated from factory defaults; the remaining 36.7% were organization-specific accounts.

## Affected Systems

- FortiGate firewalls
- Fortinet SSL VPN gateways

Primarily devices with internet-reachable administrative or VPN authentication interfaces.

## CVE and Patch Status (as of July 4, 2026)

- No CVE assigned — this is a credential/exposure issue, not a code vulnerability
- No patch applies; remediation is credential rotation + interface hardening
- CISA alert issued June 18, 2026; confirmed device count updated to ~86,644 by June 19, 2026

## Zero Trust Relevance

- Breaks the ZT principle that perimeter/network devices are exempt from continuous verification — the firewall itself must be treated as an untrusted asset until proven otherwise
- CISA ZTMM Identity Pillar: network-device admin accounts are privileged identities requiring phishing-resistant MFA, not password-only access
- CISA ZTMM Network Pillar: management planes must never be directly internet-routable; require a broker (VPN/bastion/ZTNA) between the internet and any admin interface
- CISA ZTMM Devices Pillar: infrastructure devices belong in the same continuous compliance/drift-detection program as endpoints
- NIST SP 800-207 §3.4: trust is never granted implicitly based on network location — a compromised perimeter device should not grant automatic access to everything behind it (see [Stop the SPOF](https://oztp.org/blog/2026/05/09/stop-the-spof/) anti-single-point-of-failure framing)

## Recommended Mitigations

1. **Terminate all active SSL VPN and admin sessions; reset every Fortinet credential** — assume existing credentials may be compromised
2. **Enable phishing-resistant MFA** on all administrative and VPN accounts
3. **Remove management interfaces from public internet exposure** — restrict to trusted internal networks or a broker (VPN/bastion/ZTNA)
4. **Remove or disable unauthorized/unnecessary accounts** — audit against known provisioning records
5. **Adopt PBKDF2 for stored admin credentials** where firmware supports it
6. **Monitor for compromise indicators** — config exports to external IPs, admin logins from unusual geo/IP ranges, new admin accounts outside normal workflow

## ZT Framework References

- NIST SP 800-207 §2.1, §3.4 — Per-session access with MFA; no implicit trust by network location
- CISA ZTMM Identity Pillar — Phishing-resistant MFA, privileged identity governance
- CISA ZTMM Network Pillar — Macro/micro-segmentation, broker-mediated management access
- CISA ZTMM Devices Pillar — Continuous device health validation extended to network infrastructure

## OZTP Advisory

Full advisory: https://oztp.org/advisories/fortinet-fortibleed-2026-06/

## Related Concepts

- Stop the SPOF — anti-single-point-of-failure framing; a compromised firewall/VPN gateway is a classic SPOF pattern

## Sources

- https://www.cisa.gov/news-events/alerts/2026/06/18/cisa-urges-hardening-fortinet-devices-after-reports-credential-exposure
- https://www.cybersecuritydive.com/news/cisa-device-hardening-thousands-fortinet-credentials-compromised/823397/
- https://www.bleepingcomputer.com/news/security/cisa-warns-fortinet-users-to-secure-devices-after-fortibleed-leak/
- https://www.securityweek.com/fortibleed-86000-fortinet-device-credentials-compromised/
- https://businessinsights.bitdefender.com/technical-advisory-fortibleed-credential-exposure-campaign-targeting-internet-facing-fortinet-devices
- https://labs.cloudsecurityalliance.org/research/csa-research-note-fortibleed-default-credentials-20260620-cs/
- https://securityaffairs.com/193902/hacking/cisa-warns-of-active-exploitation-following-fortibleed-leak.html
