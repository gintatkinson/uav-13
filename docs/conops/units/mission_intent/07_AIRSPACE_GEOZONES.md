| Attribute | Value |
| :--- | :--- |
| **Title** | Tactical Mission Intent: Airspace Deconfliction & Geo-Zones |
| **Version** | 1.0.0 |
| **Date** | 2026-09-02 |

## 7. Airspace Deconfliction & U-space Dynamic Geo-Zones

In accordance with RTCA DO-365B, JARUS SORA v2.5 (Annex C), and EU Regulation 2021/664 (U-space framework), airspace deconfliction is assured through multi-layered 3D spatial containment boundaries, dynamic keep-out zones, and formal Detect and Avoid (DAA) separation minima.

### 7.1 Primary Boundary Perimeter
- **3D Spatial Geometry:** The primary operational airspace is bounded by an authorized 3D containment cylinder with radius $R_{\mathrm{perimeter}} = 15.0\text{ km}$ centered at the GCS launch coordinates.
- **Vertical Altitude Envelope:** Operational floor $0.0\text{ m}$ AGL up to maximum operating ceiling $120.0\text{ m}$ AGL ($h_{\mathrm{operating\_ceiling}} = 120.0\text{ m}$).
- **Containment Buffers:**
  - Lateral Containment Buffer: $50.0\text{ m}$ inward margin along all perimeter boundaries.
  - Vertical Containment Buffer: $20.0\text{ m}$ downward margin below operational ceiling.
  - Trigger Action: Reaching the containment buffer initiates immediate autonomous closed-loop turnaround heading commands (`EMG-05`).
- **Public Clause Citation:** JARUS SORA v2.5 Annex B §2.1

---

### 7.2 Dynamic Exclusion Zones (Pop-Up Geo-Zones)
- **Dynamic U-space Geofences:** U-space tactical updates broadcast via datalink inject dynamic cylindrical or polygonal keep-out volumes into the flight guidance computer.
- **Critical Infrastructure Standoff:** Automated exclusion cylinder of radius $R_{\mathrm{exclusion}} = 500.0\text{ m}$ spanning $[0.0\text{ m}, 120.0\text{ m}]$ around critical infrastructure and populated assemblies.
- **Temporary Flight Restrictions (TFR):** Real-time ingestion of NOTAM/TFR spatial polygons with automated dynamic trajectory re-planning.
- **Public Clause Citation:** EU Regulation 2021/664 Art 4

---

### 7.3 RTCA DO-365B DAA Separation Minima (Well-Clear Envelope)
Deconfliction from cooperative and non-cooperative traffic maintains the RTCA DO-365B Well-Clear boundary at all times:

| DAA Separation Parameter | DO-365B Symbol | Nominal Constraint | Units | Operational Definition |
| :--- | :--- | :--- | :--- | :--- |
| Horizontal Miss Distance | DMOD | DMOD >= 1200.0 | m | Minimum horizontal distance allowed at closest point of approach (0.66 NM) |
| Modified Tau (Time-to-CPA) | tau_mod | tau_mod >= 35.0 | s | Temporal collision hazard threshold triggering evasive maneuvers |
| Vertical Separation Minima | HSEP | HSEP >= 137.0 | m | Minimum vertical boundary separation between aircraft flight levels (450 ft) |
| Collision Alert Warning Time | t_alert | t_alert >= 25.0 | s | Advance warning threshold for automated avoidance trajectory execution |

- **Avoidance Maneuver Rule:** If an intruder breaches the DAA Well-Clear envelope, the flight management system executes an automated coordinated horizontal turn at turn rate $\ge 5.0^\circ/\text{s}$ or vertical climb/dive maneuver prioritizing separation gain.
- **Public Clause Citation:** RTCA DO-365B §2.2.4

---

### 7.4 Terrain Avoidance Envelopes (CFIT Prevention)
- **Digital Elevation Model (DEM) Resolution:** High-resolution digital elevation matrix ($1.0\text{ m}$ grid resolution) loaded into non-volatile avionics memory.
- **Forward Look-Ahead Horizon:** Forward look-ahead time of $t_{\mathrm{lookahead}} \ge 15.0\text{ s}$ at current ground speed ($18.0\text{ m/s}$).
- **Minimum Obstacle Clearance:** Continuous obstacle clearance of $h_{\mathrm{obs\_clear}} \ge 30.0\text{ m}$ along the forward velocity vector.
- **Terrain Avoidance Failsafe:** Detection of terrain penetration along projected trajectory commands immediate maximum-power climb at best climb angle ($\gamma_{\mathrm{climb}} \ge 15.0^\circ$).
- **Public Clause Citation:** ICAO Annex 2 §3.2
