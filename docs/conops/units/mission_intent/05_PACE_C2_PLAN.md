| Attribute | Value |
| :--- | :--- |
| **Title** | Tactical Mission Intent: PACE C2 Communications Plan |
| **Version** | 1.0.0 |
| **Date** | 2026-09-02 |

## 5. PACE C2 Link Communications Plan

In accordance with NATO STANAG 4586 (§4.5), RTCA DO-362A, 3GPP Release 15, and NIST SP 800-82r3, Command and Control (C2) link robustness is maintained through a four-tier Primary, Alternate, Contingency, Emergency (PACE) communications architecture with automated failover and hysteresis stabilization.

### 5.1 Master PACE Communications Plan Table

The master communications plan defines the frequency allocations, physical layer transport media, modulation schemes, nominal throughput, and timeout boundaries across all four operational tiers:

| PACE Tier | Link Medium | Frequency Band (f_band) | Modulation / Protocol | Nominal Data Rate (Rate_nom) | Heartbeat Timeout (tau_timeout) | Failover Hysteresis (tau_hysteresis) | Priority / Role | Public Clause Citation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Primary** | 5.8 GHz COFDM Point-to-Point Datalink | 5725 to 5850 MHz | COFDM QPSK/QAM / AES-256-GCM | 12.0 Mbps | 1.0 s | 3.0 s | Full HD Payload Video & High-Rate Telemetry | NATO STANAG 4586 §4.5 |
| **Alternate** | 915 MHz FHSS Encrypted Mesh Datalink | 902 to 928 MHz | 50-Hop FHSS GFSK / AES-256-GCM | 250 kbps | 2.0 s | 5.0 s | Robust Flight Telemetry & Tactical C2 Relay | RTCA DO-362A §2.2 |
| **Contingency** | Encrypted LTE/5G Cellular VPN Tunnel | 700 to 2600 MHz | 3GPP Rel 15 / IPsec AES-256-GCM | 2.0 Mbps | 5.0 s | 10.0 s | Beyond-LOS Backup C2 & Telemetry Bridge | 3GPP Rel 15 / NIST SP 800-82r3 |
| **Emergency** | Autonomous RTH & Satellite Geo-Beacon | 406 MHz / 1616 to 1626 MHz | SBD Burst / COSPAS-SARSAT Beacon | 2.4 kbps | 10.0 s | 15.0 s | Autonomous Lost-Link RTH & Satellite Emergency Beacon | JARUS SORA v2.5 Annex E §E.6 |

---

### 5.2 Complete RF Link Budget & Mathematical Formulation

The RF link budget across all four PACE communication tiers is governed by the Friis transmission formula with atmospheric and miscellaneous line losses evaluated at the maximum operational standoff range ($d = 15.0\text{ km}$):

$$
\begin{aligned}
\mathrm{FSPL} &= 20 \log_{10}(d) + 20 \log_{10}(f) + 20 \log_{10}\left(\frac{4\pi}{c}\right) \\
P_{\mathrm{rx}} &= P_{\mathrm{tx}} + G_{\mathrm{tx}} + G_{\mathrm{rx}} - \mathrm{FSPL} - L_{\mathrm{misc}} \\
\mathrm{Margin}_{\mathrm{fade}} &= P_{\mathrm{rx}} - S_{\mathrm{rx}}
\end{aligned}
$$

Where and Operational Parameters:
- $d$: Line-of-sight propagation distance between ground control station and aircraft ($15000.0\text{ m}$).
- $f$: Carrier center frequency of the active RF communication tier (Hz).
- $c$: Speed of light in vacuum ($2.99792458 \times 10^8\text{ m/s}$).
- $\mathrm{FSPL}$: Free space path loss over the RF transmission channel (dB).
- $P_{\mathrm{tx}}$: RF transmitter output power delivered to the antenna terminal (dBm).
- $G_{\mathrm{tx}}$: Transmit antenna isotropic gain (dBi).
- $G_{\mathrm{rx}}$: Receive antenna isotropic gain (dBi).
- $L_{\mathrm{misc}}$: Miscellaneous RF insertion, polarization mismatch, and atmospheric absorption losses (dB).
- $P_{\mathrm{rx}}$: Received signal power at the receiver input connector (dBm).
- $S_{\mathrm{rx}}$: Effective receiver demodulation sensitivity threshold (dBm).
- $\mathrm{Margin}_{\mathrm{fade}}$: Effective fade margin (dB), with normative requirement $\mathrm{Margin}_{\mathrm{fade}} \ge 12.0\text{ dB}$.

#### Master RF Link Budget Table (15.0 km Operational Range)

| PACE Tier | Link Frequency | Transmit Power (P_tx) | Transmit Gain (G_tx) | Receiver Gain (G_rx) | FSPL @ 15 km | Misc Losses (L_misc) | Received Power (P_rx) | Receiver Sensitivity (S_rx) | Fade Margin | Minimum Margin Required | Public Clause Citation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Primary** | 5.8 GHz | +30.0 dBm | +5.0 dBi | +18.0 dBi (Tracking Mast) | 131.2 dB | 2.0 dB | -80.2 dBm | -95.0 dBm | 14.8 dB | >= 12.0 dB | NATO STANAG 4586 §4.5 |
| **Alternate** | 915 MHz | +27.0 dBm | +3.0 dBi | +6.0 dBi (Ground Omni) | 115.2 dB | 1.5 dB | -80.7 dBm | -108.0 dBm | 27.3 dB | >= 12.0 dB | RTCA DO-362A §2.2 |
| **Contingency** | 800 MHz (Cellular) | +23.0 dBm | +2.0 dBi | +2.0 dBi (Base Station) | 113.8 dB | 1.0 dB | -87.8 dBm | -102.0 dBm | 14.2 dB | >= 12.0 dB | 3GPP Rel 15 / NIST SP 800-82r3 |
| **Emergency** | 1.6 GHz (Satellite) | +33.0 dBm | +3.0 dBi | +0.0 dBi (Space Element) | 120.2 dB | 1.5 dB | -85.7 dBm | -116.0 dBm | 30.3 dB | >= 12.0 dB | JARUS SORA v2.5 Annex E §E.6 |

---

### 5.3 Failover Hysteresis State Machine & Re-acquisition Dynamics

Link degradation triggers deterministic down-tier failover when the active tier's heartbeat packet stream is interrupted beyond its designated timeout threshold $\tau_{\mathrm{timeout},i}$. Promotion back to a higher-priority tier requires continuous, uninterrupted link stability across the re-acquisition hysteresis time window $\tau_{\mathrm{hysteresis},k}$:

$$
\begin{aligned}
\Delta t_{\mathrm{loss},i}(t) &= t - t_{\mathrm{last\_valid\_rx},i} \\
\mathrm{TriggerFailover}(i \to i+1) &\iff \Delta t_{\mathrm{loss},i}(t) \ge \tau_{\mathrm{timeout},i} \\
\Delta t_{\mathrm{stable},k}(t) &= t - t_{\mathrm{reacq\_start},k} \\
\mathrm{PromoteTier}(i \to k) &\iff (k < i) \land (\Delta t_{\mathrm{stable},k}(t) \ge \tau_{\mathrm{hysteresis},k}) \land (\mathrm{Margin}_k(t) \ge 12.0)
\end{aligned}
$$

Where and Operational Parameters:

| Transition Parameter | Symbol | Units | Operational Constraint | Description | Public Clause Citation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Active Link Loss Duration | Delta t_loss | s | Measured Online | Measured elapsed time since last authenticated telemetry frame | NATO STANAG 4586 §4.5 |
| Primary Heartbeat Timeout | tau_timeout_Primary | s | tau_timeout_Primary = 1.0 | Timeout triggering fallback from Primary to Alternate tier | NATO STANAG 4586 §4.5 |
| Alternate Heartbeat Timeout | tau_timeout_Alternate | s | tau_timeout_Alternate = 2.0 | Timeout triggering fallback from Alternate to Contingency tier | RTCA DO-362A §2.2 |
| Contingency Heartbeat Timeout | tau_timeout_Contingency | s | tau_timeout_Contingency = 5.0 | Timeout triggering fallback from Contingency to Emergency tier | 3GPP Rel 15 / NIST SP 800-82r3 |
| Emergency Heartbeat Timeout | tau_timeout_Emergency | s | tau_timeout_Emergency = 10.0 | Timeout initiating definitive autonomous return-to-base | JARUS SORA v2.5 Annex E §E.6 |
| Primary Re-acquisition Window | tau_hysteresis_Primary | s | tau_hysteresis_Primary = 3.0 | Continuous stable link duration required before Primary promotion | RTCA DO-362A §2.2 |
| Alternate Re-acquisition Window | tau_hysteresis_Alternate | s | tau_hysteresis_Alternate = 5.0 | Continuous stable link duration required before Alternate promotion | RTCA DO-362A §2.2 |
| Contingency Re-acquisition Window | tau_hysteresis_Contingency | s | tau_hysteresis_Contingency = 10.0 | Continuous stable link duration required before Contingency promotion | 3GPP Rel 15 / NIST SP 800-82r3 |
| Emergency Re-acquisition Window | tau_hysteresis_Emergency | s | tau_hysteresis_Emergency = 15.0 | Continuous stable link duration required before exiting Emergency RTH | JARUS SORA v2.5 Annex E §E.6 |

---

### 5.4 Cryptographic Security & Link Integrity

All PACE communication tiers employ authenticated AES-256-GCM encryption with monotonic 64-bit sequence counters and Ed25519 digital signature verification to eliminate eavesdropping, packet tampering, and replay injection in compliance with NIST SP 800-82r3 and DoD Directive 3000.09.
