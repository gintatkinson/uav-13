| Attribute | Value |
| :--- | :--- |
| **Title** | Current Situation, Deficiency Analysis & Operational Motivation |
| **Version** | 1.0.0 |
| **Date** | 2026-09-02 |

## 2. Current Situation, Deficiency Analysis & Operational Motivation

### 2.1 Current Operational Baseline (Predecessors)
The predecessor operational baseline relies on conventional radio-controlled platforms and legacy point-to-point analog/digital video telemetry systems. These systems were primarily designed for visual line-of-sight (VLOS) remote piloting under benign weather conditions, characterized by:
1. **Single-String Non-Redundant Avionics:** Predecessor platforms utilize flight controllers lacking redundant inertial sensors, isolated power buses, and hardware watchdog circuits. A single sensor anomaly or processor stall leads directly to unrecoverable loss of control.
2. **Manual Point-to-Point Control Links:** Command and control relies on single-frequency analog or low-resilience digital radio links vulnerable to multipath fading, intentional electronic warfare (EW) jamming, and line-of-sight terrain obstruction.
3. **Disjointed Sensor Telemetry Displays:** Payload imagery and flight navigational telemetry are processed on isolated, unintegrated display monitors, forcing human operators to perform manual mental correlation of video feeds with spatial maps.
4. **Ad-Hoc Contingency Management:** Contingency responses lack deterministic timing guarantees, formal SORA containment buffers, and dynamic secondary divert routing.

### 2.2 Operational Capability Gaps
Analysis of historical mission logs, field incident reports, and operator debriefs reveals four critical capability gaps that prevent legacy systems from executing high-tempo autonomous surveillance and tactical engagement:

| Gap ID | Capability Gap Name | Operational Manifestation | Mission Impact & Risk |
| :--- | :--- | :--- | :--- |
| **GAP-01** | Safe BVLOS Autonomous Operation | Inability to maintain statutory airspace separation and geofence containment without constant visual observer line-of-sight. | Restricted operational radius (R_VLOS << 15.0 km), preventing wide-area perimeter monitoring and deep tactical reconnaissance. |
| **GAP-02** | Contested RF / EW Resilience | Loss of vehicle control and video telemetry in the presence of intentional navigation jamming, RF interference, or multipath. | High rate of lost-link aborts, mission abandonment, and uncontained trajectory deviations in hostile RF environments. |
| **GAP-03** | Sub-Second Deterministic Failsafe | Slow anomaly detection (tau_human > 2.0 s) and non-deterministic recovery maneuvers resulting in boundary breaches. | Inability to achieve JARUS SORA Specific Category authorization for populated adjacent areas; catastrophic crash hazard. |
| **GAP-04** | Modular Rapid Field Turnaround | Prolonged ground servicing and complex payload swaps requiring extended turnaround (t_turnaround > 45 min). | Sortie rate limited to low operational tempo, leaving perimeter security coverage gaps and increasing vulnerability. |

### 2.3 Legacy System Deficiencies & Technical Limitations
In accordance with ISO/IEC/IEEE 29148:2018 §5.2.4, system deficiencies are categorized across technical, operational, and human domains:

| Technical Domain | Operational Domain | Human Domain |
| :--- | :--- | :--- |
| Single-string sensor architecture | Lack of dynamic geofencing | High NASA-TLX cognitive load |
| Lack of hard RTOS timing bounds | No automated U-space / UTM link | Disjointed payload displays |
| Unshielded EMI/RF susceptibility | Manual flight log extraction | Pilot fatigue during manual flight |
| Non-hermetic IP enclosures | Extended field turnaround overhead | Complex manual calibration rigs |

1. **Technical Deficiencies:**
   - **Avionics & Compute:** Lack of hard real-time operating system (RTOS) guarantees; flight control loops executed on non-deterministic microcontrollers subject to task starvation and priority inversion.
   - **Environmental Hardening:** Non-sealed enclosures (rated below IP67) vulnerable to wind-driven rain, particulate ingress, and corrosive atmosphere over extreme operational temperature ranges ($-40^\circ\text{C}$ to $+55^\circ\text{C}$).
   - **Power Distribution:** Single power rail architecture without isolation barriers; short-circuit in payload subsystem instantly collapses primary flight avionics bus.

2. **Operational Deficiencies:**
   - **Airspace Integration:** Complete lack of automated communication with U-space / UTM service providers, necessitating manual coordination with local airspace authorities.
   - **Contingency Divert:** Pre-programmed return trajectories follow straight-line paths ignoring active terrain obstacles, dynamic weather cells, and pop-up keep-out zones.

3. **Human Deficiencies:**
   - **Cognitive Overload:** Operators are required to simultaneously supervise flight dynamics, steer optical sensors, monitor energy telemetry, and log airspace coordinates manually, leading to NASA-TLX scores exceeding acceptable limits ($\text{TLX} > 70$).
   - **Operational Error:** Fatigued operators during extended operational shifts exhibit increased reaction times ($\tau_{\mathrm{human}} > 2.0\text{ s}$) to contingency warnings, leading to preventable incidents.

### 2.4 Mission Drivers & User Operational Problems
The primary mission drivers compelling the development of the Tactical UAS include:
- **Statutory Regulatory Mandates:** Civil aviation authorities and defense agencies require formal compliance with JARUS SORA v2.5 Annex B for operations beyond visual line-of-sight. This requires verifiable Ground Risk Buffer calculations ($R_{\mathrm{GRB}} = 200.0\text{ m}$) and DO-178C DAL-A software assurance.
- **Continuous Security Coverage:** Critical perimeter protection requires unbroken surveillance coverage across the operational radius of $15.0\text{ km}$ with autonomous asset handoffs.
- **Adverse Environmental Readiness:** The system must operate reliably across extreme climatic envelopes ($-40^\circ\text{C}$ to $+55^\circ\text{C}$, IP67 sealing, and steady wind limits of $15.0\text{ m/s}$ with gusts up to $20.0\text{ m/s}$ per MIL-STD-810H).
- **Zero-Trust Cybersecurity Baseline:** Modern operational environments demand authenticated C2 command links, hardware security module (HSM) key storage, and automated rejection of spoofed telemetry or malicious command injection.
