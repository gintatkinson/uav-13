| Attribute | Value |
| :--- | :--- |
| **Title** | Tactical Mission Intent: Airspace Deconfliction & Geo-Zones |
| **Version** | 1.0.0 |
| **Date** | 2026-09-02 |

## 7. Airspace Deconfliction & U-space Dynamic Geo-Zones

In accordance with RTCA DO-365B (MOPS for DAA Systems), JARUS SORA v2.5 (Annex C), and EU Regulation 2021/664 (U-space regulatory framework), airspace safety and deconfliction are guaranteed through multi-layered 3D spatial containment boundaries, dynamic boundary potential fields, real-time Detect and Avoid (DAA) Well-Clear separation minima, and forward-looking terrain avoidance algorithms.

---

### 7.1 Primary Operational 3D Volume Geometry & Dynamic Boundary Gradient

The primary operational airspace volume is bounded by an authorized 3D cylinder of radius $R_{\mathrm{perimeter}} = 15000.0\text{ m}$ centered at the GCS reference origin $(x_0, y_0, 0)$ spanning altitudes from ground level up to the authorized operating ceiling $h_{\mathrm{operating\_ceiling}} = 120.0\text{ m}$ AGL. The vehicle continuously computes the distance function $d(\mathbf{p})$ and the dynamic inward boundary gradient $\nabla d(\mathbf{p})$ to generate proactive containment steering velocities:

$$
\begin{aligned}
r_{xy}(\mathbf{p}) &= \sqrt{(x - x_0)^2 + (y - y_0)^2} \\
d_{\mathrm{lat}}(\mathbf{p}) &= R_{\mathrm{perimeter}} - r_{xy}(\mathbf{p}) \\
d_{\mathrm{vert}}(\mathbf{p}) &= h_{\mathrm{operating\_ceiling}} - z \\
d(\mathbf{p}) &= \min(d_{\mathrm{lat}}(\mathbf{p}), d_{\mathrm{vert}}(\mathbf{p}), z) \\
\nabla d_{\mathrm{lat}}(\mathbf{p}) &= \left( -\frac{x - x_0}{r_{xy}(\mathbf{p})}, -\frac{y - y_0}{r_{xy}(\mathbf{p})}, 0 \right)^T \\
\mathbf{v}_{\mathrm{containment}}(\mathbf{p}) &= \begin{cases}
\mathbf{0} & \text{if } d(\mathbf{p}) \ge d_{\mathrm{buffer}} \\
k_{\mathrm{rep}} \left( \frac{1}{d(\mathbf{p})} - \frac{1}{d_{\mathrm{buffer}}} \right) \nabla d(\mathbf{p}) & \text{if } d(\mathbf{p}) < d_{\mathrm{buffer}}
\end{cases}
\end{aligned}
$$

Where and Operational Parameters:

| Boundary Parameter | Symbol | Nominal Value | Units | Operational Constraint | Public Clause Citation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Operational Perimeter Radius | R_perimeter | 15000.0 | m | Primary 3D cylindrical containment radius | JARUS SORA v2.5 Annex B §2.1 |
| Maximum Operating Ceiling | h_operating_ceiling | 120.0 | m | Statutory maximum altitude above ground level | EU Regulation 2021/664 Art 4 |
| Operational Altitude Floor | h_operating_floor | 0.0 | m | Ground surface reference datum | JARUS SORA v2.5 Annex B §2.1 |
| Lateral Containment Buffer | d_buffer_lat | 50.0 | m | Inward boundary buffer triggering course reversal | JARUS SORA v2.5 Annex B §2.1 |
| Vertical Containment Buffer | d_buffer_vert | 20.0 | m | Downward ceiling buffer triggering altitude hold | JARUS SORA v2.5 Annex B §2.1 |
| Repulsive Potential Gain | k_rep | 5.0 | m^2/s | Proportional gain for containment velocity field | RTCA DO-365B §2.2.3 |
| Containment Turn Authority | psi_dot_contain | >= 5.0 | deg/s | Coordinated yaw rate for boundary turnaround | RTCA DO-365B §2.2.3 |

---

### 7.2 RTCA DO-365B Detect and Avoid (DAA) Well-Clear Volume

Deconfliction from cooperative (ADS-B / transponder equipped) and non-cooperative airborne traffic maintains the RTCA DO-365B Well-Clear boundary at all times. The modified tau ($\tau_{\mathrm{mod}}$) metric defines the temporal hazard horizon, triggering evasive separation maneuvers prior to breach:

$$
\begin{aligned}
\tau_{\mathrm{mod}} &= \begin{cases}
-\frac{r^2 - D_{\mathrm{MOD}}^2}{r \dot{r}} & \text{if } r \dot{r} < 0 \text{ and } r > D_{\mathrm{MOD}} \\
0 & \text{if } r \le D_{\mathrm{MOD}} \\
\infty & \text{if } r \dot{r} \ge 0
\end{cases} \\
\mathrm{WellClearViolation} &\iff (r \le D_{\mathrm{MOD}} \lor \tau_{\mathrm{mod}} \le 35.0) \land (|z_{\mathrm{own}} - z_{\mathrm{intruder}}| \le H_{\mathrm{SEP}})
\end{aligned}
$$

Where and Operational Parameters:

#### RTCA DO-365B DAA Well-Clear Separation Minima Table

| DAA Separation Parameter | DO-365B Symbol | Nominal Constraint | Units | Operational Definition | Public Clause Citation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Horizontal Miss Distance | DMOD | DMOD >= 1200.0 | m | Minimum horizontal distance allowed at closest point of approach (0.66 NM) | RTCA DO-365B §2.2.4 |
| Modified Tau (Time-to-CPA) | tau_mod | tau_mod >= 35.0 | s | Temporal collision hazard threshold triggering evasive maneuvers | RTCA DO-365B §2.2.4 |
| Vertical Separation Minima | HSEP | HSEP >= 137.0 | m | Minimum vertical boundary separation between aircraft flight levels (450 ft) | RTCA DO-365B §2.2.4 |
| Collision Alert Warning Time | t_alert | t_alert >= 25.0 | s | Advance warning threshold for automated avoidance trajectory execution | RTCA DO-365B §2.2.4 |
| Evasive Turn Rate Authority | psi_dot_evasive | psi_dot >= 5.0 | deg/s | Minimum coordinated horizontal turning rate for collision avoidance | RTCA DO-365B §2.2.5 |
| Evasive Vertical Rate Authority | z_dot_evasive | z_dot >= 2.5 | m/s | Minimum climb/dive rate authority for vertical separation | RTCA DO-365B §2.2.5 |

---

### 7.3 Dynamic Exclusion Zones (Pop-Up Geo-Zones) & U-space Integration

Dynamic U-space tactical updates broadcast via the PACE C2 datalink inject real-time keep-out geometries into the guidance computer. The system enforces dynamic trajectory re-planning around critical infrastructure and temporary flight restrictions:

| Zone Type | Geometry | Default Standoff Buffer | Altitude Range | Ingress Policy | Re-Planning Latency | Public Clause Citation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Critical Infrastructure | Cylinder | 500.0 m | 0.0 to 120.0 m AGL | Prohibited (Hardware locked) | t_plan <= 100.0 ms | EU Regulation 2021/664 Art 4 |
| Pop-Up Protected Zone | 2D/3D Polygon | 250.0 m | 0.0 to 120.0 m AGL | Strict Avoidance Corridor | t_plan <= 200.0 ms | CJCSI 3121.01B Enc B §3.c |
| Dynamic NOTAM / TFR | 3D Polyhedron | NOTAM Boundary + 100.0 m | As per NOTAM | Autonomous Perimeter Route | t_plan <= 500.0 ms | ICAO Annex 2 §3.1 |

---

### 7.4 Controlled Flight Into Terrain (CFIT) Prevention Algorithm

The Controlled Flight Into Terrain (CFIT) avoidance executive maintains a high-resolution Digital Elevation Model (DEM) and continuously propagates a forward kinematic trajectory over the lookahead time horizon ($t_{\mathrm{lookahead}} \ge 15.0\text{ s}$):

$$
\begin{aligned}
\mathbf{p}_{\mathrm{pred}}(\tau) &= \mathbf{p}(t) + \mathbf{v}(t) \cdot \tau + \frac{1}{2} \mathbf{a}(t) \cdot \tau^2, \quad \tau \in [0, t_{\mathrm{lookahead}}] \\
h_{\mathrm{clear}}(\tau) &= z_{\mathrm{pred}}(\tau) - z_{\mathrm{DEM}}(x_{\mathrm{pred}}(\tau), y_{\mathrm{pred}}(\tau)) \\
\mathrm{CFIT\_Alert} &\iff \exists \tau \in [0, t_{\mathrm{lookahead}}] : h_{\mathrm{clear}}(\tau) < h_{\mathrm{obs\_clear}} \\
\gamma_{\mathrm{climb}} &= \arctan\left(\frac{\dot{z}_{\mathrm{climb}}}{v_{\mathrm{ground}}}\right) \ge 15.0^\circ
\end{aligned}
$$

Where and Operational Parameters:

| Terrain Parameter | Symbol | Nominal Value | Units | Operational Constraint | Public Clause Citation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| DEM Grid Resolution | res_DEM | 1.0 | m | Level 3 DTED matrix loaded into non-volatile memory | ICAO Annex 2 §3.2 |
| Forward Lookahead Horizon | t_lookahead | >= 15.0 | s | Forward kinematic prediction time horizon | RTCA DO-365B §2.2.3 |
| Lookahead Distance Horizon | d_lookahead | >= 270.0 | m | Lookahead ground track at cruise speed 18.0 m/s | ICAO Annex 2 §3.2 |
| Minimum Obstacle Clearance | h_obs_clear | >= 30.0 | m | Minimum terrain clearance along projected velocity vector | NATO STANAG 4586 Annex B §3.2 |
| Emergency Escape Climb Angle | gamma_climb | >= 15.0 | deg | Commanded climb gradient under maximum continuous power | MIL-STD-882E §4.4 |
| CFIT Reaction Latency | t_cfit_resp | <= 100.0 | ms | Latency from hazard detection to pitch-up command | SAE ARP4761 §4.3 |
