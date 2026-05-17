# YellowKey — BitLocker Bypass via WinRE (May 2026)

## Summary

YellowKey is an unpatched zero-day disclosed May 12, 2026 by researcher Chaotic Eclipse (also known as Nightmare-Eclipse). It allows an attacker with brief physical access to a Windows device to read all contents of a BitLocker-encrypted drive using only a USB stick. No credentials required.

## Technical Details

WinRE (Windows Recovery Environment) automatically replays Transactional NTFS (TxF) transaction logs found in `\System Volume Information\FsTx` directories on attached drives. An attacker crafts a malicious FsTx folder that, when replayed, deletes `winpeshl.ini` — the file controlling the WinRE recovery shell. With `winpeshl.ini` absent, WinRE defaults to `cmd.exe` with the BitLocker-protected volume already mounted and readable.

TxF was deprecated by Microsoft circa 2012 but never removed. This is an example of a DNR (Deprecated, Never Removed) vulnerability — code officially retired but not actually removed, leaving a persistent and unmonitored attack surface.

## Affected Systems

- Windows 11 (all editions)
- Windows Server 2022
- Windows Server 2025

Older Windows versions not reported as affected.

## Attack Requirements

- Brief physical access to the target device
- USB drive with crafted `FsTx` folder
- Device boots into WinRE (hold Ctrl during boot, or via startup repair trigger)

## Most Exposed Configuration

TPM-only BitLocker — the default for most enterprise deployments. The TPM releases the encryption key during WinRE, making the volume accessible before the attacker's command prompt appears.

## CVE and Patch Status (as of May 17, 2026)

- No CVE assigned
- No patch from Microsoft
- Working PoC publicly released
- Researcher stated a "big surprise" for Microsoft around June 10, 2026 Patch Tuesday
- Monitoring for update

## Researcher Notes

Chaotic Eclipse has stated a TPM+PIN bypass also exists but has not released that PoC. TPM+PIN is still recommended as a mitigation — it significantly raises the bar even if a bypass exists.

## Zero Trust Relevance

- Breaks the ZT principle: physical presence is not trust
- CISA ZTMM Devices Pillar: device trust must be verified continuously, not assumed from encryption state at boot
- NIST SP 800-207 Tenet 7: continuously monitor and measure asset integrity
- Physical access controls are a Devices pillar concern in ZT — not a separate domain

## Recommended Mitigations

1. **BitLocker PIN (TPM+PIN mode)** — requires pre-boot PIN before WinRE mounts the drive. Group Policy: Computer Configuration → Administrative Templates → Windows Components → BitLocker Drive Encryption → Operating System Drives → "Require additional authentication at startup" → Require startup PIN with TPM
2. **UEFI firmware password** — prevents boot order changes and USB boot enablement without authorization
3. **Disable USB boot in UEFI** — directly blocks the USB delivery mechanism; pair with firmware password
4. **Physical access controls** — if attacker cannot reach the device, the attack fails entirely
5. **Monitor WinRE boot events** — alert on unexpected recovery environment entries (Event ID 1796)

## ZT Framework References

- NIST SP 800-207 §3.3 — Trust Algorithm inputs: device state, physical location
- CISA ZTMM Devices Pillar — Continuous device health validation, asset management
- CIS Controls v8 #4 — Secure configuration of enterprise assets

## OZTP Advisory

Full advisory: https://oztp.org/advisories/yellowkey-2026-05/

## Related Concepts

- DNR (Deprecated, Never Removed) vulnerability class — coined by OZTP May 2026
- Blog post defining DNR: https://oztp.org/blog/2026/05/17/dnr-deprecated-never-removed/

## Sources

- https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/
- https://thehackernews.com/2026/05/windows-zero-days-expose-bitlocker.html
- https://www.securityweek.com/researcher-drops-yellowkey-greenplasma-windows-zero-days/
- https://www.privacyguides.org/news/2026/05/15/bitlocker-bypass-found-researcher-warns-of-more-unreleased-vulnerabilities/
- https://www.secureinseconds.com/blog/2026-05-15-patch-tuesday-may-2026-bitlocker-zero-day
