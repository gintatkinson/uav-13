| Attribute | Value |
| :--- | :--- |
| **Title** | Tactical Mission Intent: Airspace Deconfliction & Geo-Zones |
| **Version** | 1.0.0 |
| **Date** | 2026-09-02 |

## 7. Airspace Deconfliction & U-space Dynamic Geo-Zones

In accordance with RTCA DO-365B, JARUS SORA v2.5 (Annex C), and EU Regulation 2021/664 (U-space framework), airspace deconfliction is assured through multi-layered 3D spatial containment boundaries, dynamic keep-out zones, formal Detect and Avoid (DAA) separation minima, and multi-asset swarm coordination protocols.

### 7.1 Primary Boundary Perimeter
- **3D Spatial Geometry:** The primary operational airspace is bounded by an authorized convex polygon defined by parameterized geodetic vertices $\{\mathbf{p}_{\mathrm{vertex},1}, \dots, \mathbf{p}_{\mathrm{vertex},N}\}$.
- **Vertical Altitude Envelope:** Altitude floor $h_{\mathrm{floor}}$ up to operating ceiling $h_{\mathrm{ceiling}}$ (bounded by $h_{\mathrm{MSL}}$).
- **Containment Buffers:**
  - Lateral Containment Buffer: $d_{\mathrm{lateral}}$ inward margin along all perimeter boundaries.
  - Vertical Containment Buffer: $d_{\mathrm{vertical}}$ downward margin below operational ceiling.
  - Trigger Action: Reaching the containment buffer initiates immediate autonomous closed-loop turnaround heading commands.
- **Public Clause Citation:** JARUS SORA v2.5 Annex B §2.1

---

### 7.2 Dynamic Exclusion Zones (Pop-Up Geo-Zones)
- **Dynamic U-space Geofences:** U-space tactical updates broadcast via datalink inject dynamic cylindrical or polygonal keep-out volumes into the flight guidance computer.
- **Critical Infrastructure Standoff:** Automated exclusion cylinder of radius $R_{\mathrm{exclusion}}$ spanning $[h_{\mathrm{floor}}, h_{\mathrm{ceiling}}]$ around critical infrastructure and populated assemblies.
- **Temporary Flight Restrictions (TFR):** Real-time ingestion of NOTAM/TFR spatial polygons with automated dynamic trajectory re-planning.
- **Public Clause Citation:** EU Regulation 2021/664 Art 4

---

### 7.3 RTCA DO-365B DAA Separation Minima (Well-Clear Envelope)
Deconfliction from cooperative and non-cooperative traffic maintains the RTCA DO-365B Well-Clear boundary at all times:

| DAA Separation Parameter | DO-365B Symbol | Nominal Constraint | Units | Operational Definition |
| :--- | :--- | :--- | :--- | :--- |
| Horizontal Miss Distance | DMOD | DMOD >= DMOD_min | m | Minimum horizontal distance allowed at closest point of approach |
| Modified Tau (Time-to-CPA) | tau_mod | tau_mod >= tau_mod_min | s | Temporal collision hazard threshold triggering evasive maneuvers |
| Vertical Separation Minima | HSEP | HSEP >= HSEP_min | m | Minimum vertical boundary separation between aircraft flight levels |
| Collision Alert Warning Time | t_alert | t_alert >= tau_alert_min | s | Advance warning threshold for automated avoidance trajectory execution |

- **Avoidance Maneuver Rule:** If an intruder breaches the DAA Well-Clear envelope, the flight management system executes a coordinated horizontal turn at turn rate $\omega_{\mathrm{turn}}$ or vertical climb/dive maneuver prioritizing separation gain.
- **Public Clause Citation:** RTCA DO-365B §2.2.4

---

### 7.4 Terrain Avoidance Envelopes (CFIT Prevention)
- **Digital Elevation Model (DEM) Resolution:** High-resolution digital elevation matrix loaded into non-volatile avionics memory.
- **Forward Look-Ahead Horizon:** Forward look-ahead time ($t_{\mathrm{lookahead}} \ge \tau_{\mathrm{lookahead}}$) at current ground speed ($v_{\mathrm{ground}}$).
- **Minimum Obstacle Clearance:** Continuous obstacle clearance of $h_{\mathrm{clearance}} \ge h_{\mathrm{min}}$ along the forward velocity vector.
- **Terrain Avoidance Failsafe:** Detection of terrain penetration along projected trajectory commands immediate maximum-power climb at best climb angle ($\gamma_{\mathrm{climb}} \ge \gamma_{\mathrm{min}}$).
- **Public Clause Citation:** ICAO Annex 2 §3.2

---

### 7.5 Multi-Asset Coordination & Swarm Deconfliction Protocols

In accordance with STANAG 4586 Annex B and multi-agent cooperative flight standards, multi-asset swarm operations maintain deterministic separation minima and dynamic inter-vehicle trajectory deconfliction:

| Asset ID | Role / Echelon | Relative Nav Accuracy | Separation Minima (H / V) | Deconfliction Protocol | Inter-Vehicle Link |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `UAS-SWARM-01` | Lead Scout | +/- 0.5 m | 15.0 m / 10.0 m | Distributed Dynamic Potential Field | 5.8 GHz Mesh Ad-Hoc |
| `UAS-SWARM-02` | Wing Asset | +/- 0.5 m | 15.0 m / 10.0 m | Distributed Dynamic Potential Field | 5.8 GHz Mesh Ad-Hoc |

- **Swarm Separation Enforcement:** Autonomous peer-to-peer relative navigation continuously broadcasts position/velocity state vectors over the inter-vehicle ad-hoc mesh, executing dynamic artificial potential field avoidance whenever inter-vehicle separation breaches 15.0 m horizontal or 10.0 m vertical minima.
- **Public Clause Citation:** NATO STANAG 4586 Annex B §3.4

---

### 7.6 GCS-to-GCS Control Authority Handover & STANAG 4586 LOI Matrix

Control authority transfers between primary and secondary Ground Control Stations adhere to formal STANAG 4586 Levels of Interoperability (LOI 1 through 5) handshakes:

| Handover Phase | Controlling Entity | Receiving Entity | STANAG 4586 LOI | Handshake Verification | Timeout Failsafe |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `HO-REQ-01` | Primary GCS (GCS-A) | Secondary GCS (GCS-B) | LOI 4 (Vehicle Control) | Token Transfer + Nonce Exchange | Revert to GCS-A on 3000 ms loss |
| `HO-GRANT-01` | Secondary GCS (GCS-B) | Primary GCS (GCS-A) | LOI 4 (Vehicle Control) | Telemetry Lock + Uplink Ack | Abort handover if unacknowledged |

- **Handover Protocol Guarantees:** Prevents concurrent dual-master command conflicts through atomic token exchange. If the receiving GCS fails to acknowledge within 3000 ms, control automatically reverts to the transferring GCS.
- **Public Clause Citation:** NATO STANAG 4586 §3.8

---

### 7.7 Manned-Unmanned Teaming (MUM-T) Operational Modes
- **MUMT-01 (Direct Sensor Receipt & Payload Tasking):** Airborne operator LOI 2/3 direct sensor receipt and payload tasking override under airborne tactical control.
- **MUMT-02 (Collaborative Route Modification):** Autonomous flight route updates subject to airborne mission commander cryptographic consent.
- **Public Clause Citation:** NATO STANAG 4586 §3.8 / DoD Directive 3000.09 §4.1
