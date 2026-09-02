| Attribute | Value |
| :--- | :--- |
| **Title** | Tactical Mission Intent: Rules of Engagement & Interlocks |
| **Version** | 1.0.0 |
| **Date** | 2026-09-02 |

## 6. Rules of Engagement (ROE) & Weapon/Sensor Interlocks

In accordance with DoD Directive 3000.09 (Autonomy in Weapon Systems), CJCSI 3121.01B, NATO STANAG 4586 (§3.8), and MIL-STD-882E (§4.4), the execution of critical operational actions, sensor designations, and kinetic payload operations is strictly constrained by deterministic logical interlocks and multi-level human authorization architectures.

### 6.1 Doctrinal Interlock Principles
1. **Dual-Consent Authorization:** High-consequence kinetic arming and payload release actions require simultaneous cryptographic key validation from two independent authorized operators (Mission Commander and Range Safety Officer).
2. **Multi-Spectral Positive Identification (PID) Fusion:** Target acquisition and tracking designation require spatial and temporal concurrence across optical and infrared spectra ($C_{\mathrm{PID}} \ge 0.95$).
3. **Human-in-the-Loop (HITL) & Human-on-the-Loop (HOTL) Oversight:** Human operators maintain real-time situational awareness and an un-overridable emergency abort/veto capability at all times.
4. **Fail-Safe Disarmament:** Any loss of primary link telemetry or geofence boundary warning automatically reverts payloads to a safe, un-armed state.

---

### 6.2 Rules of Engagement Roster & Logical Interlock Predicates

- **ROE-01: Minimum Safe Terrain Clearance Interlock**
  - **Rule Statement:** The system shall never execute autonomous descent below the declared minimum safe operating clearance ($30.0\text{ m}$ AGL) without continuous radar altimeter ground clearance confirmation and active obstacle clearance buffer.
  - **Interlock Condition:**
    $$\mathrm{AllowDescent} \iff (h_{\mathrm{RadarAGL}} \ge 30.0) \land (\mathrm{ObstacleClearance} = \mathrm{TRUE}) \land (\mathbf{v}_{\mathrm{sink}} \le 3.0)$$
  - **Public Clause Citation:** NATO STANAG 4586 Annex B §3.2

- **ROE-02: Multi-Spectral Positive Identification (PID) Fusion**
  - **Rule Statement:** Laser designation or tactical strike track locking shall only occur when electro-optical (EO) and infrared (IR) feature correlation exceeds the normative confidence threshold ($C_{\mathrm{PID}} \ge 0.95$).
  - **Interlock Condition:**
    $$\mathrm{AllowDesignation} \iff (\mathrm{Score}_{\mathrm{EO}} \ge 0.90) \land (\mathrm{Score}_{\mathrm{IR}} \ge 0.90) \land (C_{\mathrm{PID}} \ge 0.95)$$
  - **Public Clause Citation:** CJCSI 3121.01B Enclosure A §4.b

- **ROE-03: Dual-Consent Cryptographic Arming Interlock**
  - **Rule Statement:** Payload arming sequence requires simultaneous cryptographic signature submission from Mission Commander (Key A) and Range Safety Officer (Key B) within a rolling validation window $\Delta t_{\mathrm{arm\_window}} \le 10.0\text{ s}$.
  - **Interlock Condition:**
    $$\mathrm{SystemArmed} \iff \mathrm{VerifySig}(\mathrm{Key}_A) \land \mathrm{VerifySig}(\mathrm{Key}_B) \land (|t_A - t_B| \le 10.0) \land (\mathrm{GeofenceStatus} = \mathrm{INSIDE})$$
  - **Public Clause Citation:** DoD Directive 3000.09 §3.1.c

- **ROE-04: Human-on-the-Loop (HOTL) Veto Authority Interlock**
  - **Rule Statement:** The autonomous flight executor shall immediately abort mission tasks and enter safe orbit upon receipt of an authenticated HOTL veto command or upon operator veto timeout expiration ($\tau_{\mathrm{veto\_timeout}} \le 2.0\text{ s}$).
  - **Interlock Condition:**
    $$\mathrm{ContinueMission} \iff (\mathrm{VetoReceived} = \mathrm{FALSE}) \land (\mathrm{Heartbeat}_{\mathrm{Operator}} \le 2.0)$$
  - **Public Clause Citation:** DoD Directive 3000.09 §3.1

- **ROE-05: Non-Combatant & Dynamic Exclusion Interlock (Pop-Up Override)**
  - **Rule Statement:** Automated sensor pointing and strike corridors must enforce a minimum standoff distance ($R_{\mathrm{CDA\_min}} \ge 250.0\text{ m}$) from all designated civilian structures, hospitals, and dynamic pop-up keep-out zones.
  - **Interlock Condition:**
    $$\mathrm{TargetValid} \iff \forall \mathbf{p}_{\mathrm{civilian}} \in \mathcal{Z}_{\mathrm{protected}}, \quad \|\mathbf{p}_{\mathrm{target}} - \mathbf{p}_{\mathrm{civilian}}\|_2 \ge 250.0$$
  - **Public Clause Citation:** CJCSI 3121.01B Enclosure B §3.c

- **ROE-06: 3D Geofence & Lost C2 Weapon/Sensor Safing Interlock**
  - **Rule Statement:** Upon declaration of a lost C2 link condition across all PACE communication tiers or upon reaching a geofence warning boundary, all active designating devices and kinetic payloads shall immediately de-energize and lock into their mechanical stowed position.
  - **Interlock Condition:**
    $$(\mathrm{LinkStatus} = \mathrm{LOST}) \lor (\mathrm{GeofenceStatus} = \mathrm{WARN}) \implies (\mathrm{PayloadState} := \mathrm{SAFE}) \land (\mathrm{EmitterPower} := 0.0) \land (\mathrm{GimbalState} := \mathrm{STOWED})$$
  - **Public Clause Citation:** MIL-STD-882E §4.4
