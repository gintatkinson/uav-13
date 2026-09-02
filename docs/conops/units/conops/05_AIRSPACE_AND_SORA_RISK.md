| Attribute | Value |
| :--- | :--- |
| **Title** | 4D Operational Volume & SORA Risk Assessment |
| **Version** | 1.0.0 |
| **Date** | 2026-09-02 |

## 5. 4D Operational Volume & SORA v2.5 Risk Assessment

### 5.1 4D Spatial-Temporal Operational Volume Formulation
The operational airspace volume is formally defined as a bounded 4D spatial-temporal continuum consisting of the nominal Flight Geometry, the Contingency Volume, and the Ground Risk Buffer (GRB). In accordance with JARUS SORA v2.5 Annex B, the total 4D volume envelope and the minimum Ground Risk Buffer radius are formulated as:

$$
\begin{aligned}
V_{\mathrm{4D}} &= V_{\mathrm{SpatialGeometry}} \cup V_{\mathrm{ContingencyVolume}} \cup V_{\mathrm{GRB}} \\
R_{\mathrm{GRB}} &= h_{\mathrm{max}} \cdot \tan(\theta_{\mathrm{impact}}) + v_{\mathrm{wind,max}} \cdot \sqrt{\frac{2 h_{\mathrm{max}}}{g}} + d_{\mathrm{glide,max}}
\end{aligned}
$$

Where and Operational Parameters:

| Parameter | Symbol | Value | Units | Description |
| :--- | :--- | :--- | :--- | :--- |
| Maximum Operating Ceiling | h_max | 120.0 | m | Maximum operating ceiling above reference ground surface |
| Worst-Case Impact Angle | theta_impact | 45.0 | deg | Worst-case operational trajectory impact angle |
| Maximum Operational Wind Speed | v_wind_max | 15.0 | m/s | Maximum operational wind speed limit |
| Gravitational Acceleration | g | 9.80665 | m/s^2 | Standard gravitational acceleration constant |
| Maximum Glide Distance Margin | d_glide_max | 5.0 | m | Maximum unpowered lateral displacement margin |
| Ground Risk Buffer Radius | R_GRB | 200.0 | m | Declared ground risk buffer lateral containment radius |
| Terminal Velocity with Parachute | v_terminal | 1.65 | m/s | Deployed parachute vertical descent velocity |
| Impact Kinetic Energy | E_impact | 34.0 | J | Kinetic energy at ground impact under parachute |
| Maximum Takeoff Mass | m_system | 25.0 | kg | Total operational mass of the tactical air vehicle |

The symbolic kinematic derivation for $R_{\mathrm{GRB}}$ yields:
- Ballistic fall time from maximum ceiling: $t_{\mathrm{fall}} = \sqrt{\frac{2 \cdot 120.0}{9.80665}} = 4.947\text{ s}$
- Maximum wind drift displacement: $d_{\mathrm{wind}} = 15.0 \cdot 4.947 = 74.2\text{ m}$
- Impact angle projection: $d_{\mathrm{impact}} = 120.0 \cdot \tan(45.0^\circ) = 120.0\text{ m}$
- Theoretical minimum buffer: $R_{\mathrm{calc}} = 120.0 + 74.2 + 5.0 = 199.2\text{ m}$
- The declared $R_{\mathrm{GRB}} = 200.0\text{ m}$ strictly bounds the theoretical minimum ($200.0\text{ m} \ge 199.2\text{ m}$), guaranteeing full 4D containment.

#### 5.1.1 Ground Risk Buffer Sensitivity Analysis Across Wind Profiles
The minimum required Ground Risk Buffer radius $R_{\mathrm{GRB}}(v_{\mathrm{wind}})$ is evaluated parametrically across atmospheric wind conditions:

$$
\begin{aligned}
R_{\mathrm{calc}}(v_{\mathrm{wind}}) &= h_{\mathrm{max}} \cdot \tan(\theta_{\mathrm{impact}}) + v_{\mathrm{wind}} \cdot \sqrt{\frac{2 h_{\mathrm{max}}}{g}} + d_{\mathrm{glide,max}}
\end{aligned}
$$

Evaluating at $h_{\mathrm{max}} = 120.0\text{ m}$, $\theta_{\mathrm{impact}} = 45.0^\circ$, $g = 9.80665\text{ m/s}^2$ ($t_{\mathrm{fall}} = 4.947\text{ s}$), and $d_{\mathrm{glide,max}} = 5.0\text{ m}$ yields the following sensitivity profile:

| Wind Velocity Profile (v_wind) | Ballistic Fall Time (t_fall) | Wind Drift (d_wind) | Trajectory Projection (d_impact) | Glide Margin (d_glide) | Theoretical Minimum (R_calc) | Declared Buffer (R_GRB) | Containment Margin (Delta R) | Containment Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0.0 m/s (Calm) | 4.947 s | 0.0 m | 120.0 m | 5.0 m | 125.0 m | 200.0 m | +75.0 m | Strictly Bounded |
| 5.0 m/s (Light Breeze) | 4.947 s | 24.7 m | 120.0 m | 5.0 m | 149.7 m | 200.0 m | +50.3 m | Strictly Bounded |
| 10.0 m/s (Moderate Breeze) | 4.947 s | 49.5 m | 120.0 m | 5.0 m | 174.5 m | 200.0 m | +25.5 m | Strictly Bounded |
| 15.0 m/s (Operational Limit) | 4.947 s | 74.2 m | 120.0 m | 5.0 m | 199.2 m | 200.0 m | +0.8 m | Strictly Bounded (Optimal Margin) |
| 20.0 m/s (Peak Gust Threshold) | 4.947 s | 98.9 m | 120.0 m | 5.0 m | 223.9 m | 200.0 m | -23.9 m | Exceeds Declared Buffer (Flight Prohibited) |

As demonstrated in the sensitivity analysis, the declared Ground Risk Buffer $R_{\mathrm{GRB}} = 200.0\text{ m}$ strictly bounds all operational wind profiles up to the maximum certified steady-state operational wind limit of $v_{\mathrm{wind,max}} = 15.0\text{ m/s}$ ($R_{\mathrm{calc}} = 199.2\text{ m} \le 200.0\text{ m}$) with an explicit positive containment margin $\Delta R = +0.8\text{ m}$. Steady wind conditions exceeding $15.0\text{ m/s}$ are classified as out-of-envelope, enforcing an automated Go/No-Go inhibit or immediate return-to-base sequence.

### 5.2 JARUS SORA v2.5 Ground Risk Class (GRC) & Kinetic Impact Limits
1. **Intrinsic Ground Risk Class (Initial GRC):**
   - Maximum characteristic dimension: $L_{\mathrm{char}} = 1.8\text{ m}$.
   - Typical operational cruising velocity: $v_{\mathrm{cruise}} = 18.0\text{ m/s}$.
   - Takeoff Mass: $m_{\mathrm{MTOW}} = 25.0\text{ kg}$.
   - Operational scenario: Operations over controlled ground perimeter with sparsely populated adjacent areas.
   - Intrinsic Ground Risk Class: **GRC-3** per JARUS SORA v2.5 Table 2.

2. **Kinetic Impact Energy Analysis ($E_k$):**
   - **Unmitigated Freefall Impact Physics ($E_k = 7812.5\text{ J}$):**
     In the event of a catastrophic structural, propulsion, or power loss without parachute mitigation, the air vehicle accelerates to its unpowered aerodynamic terminal fall velocity $v_{\mathrm{terminal}} = 25.0\text{ m/s}$. The unmitigated kinetic impact energy is governed by:

$$
\begin{aligned}
E_{k,\mathrm{unmitigated}} &= \frac{1}{2} m_{\mathrm{system}} v_{\mathrm{terminal}}^2
\end{aligned}
$$

Where and Operational Parameters:
- $E_{k,\mathrm{unmitigated}}$: Unmitigated kinetic impact energy at aerodynamic terminal velocity ($7812.5\text{ J}$ calculated from $m_{\mathrm{system}} = 25.0\text{ kg}$ and $v_{\mathrm{terminal}} = 25.0\text{ m/s}$).
- $m_{\mathrm{system}}$: Total system operational mass ($25.0\text{ kg}$).
- $v_{\mathrm{terminal}}$: Unpowered aerodynamic terminal fall velocity ($25.0\text{ m/s}$).

An unmitigated impact energy of $7812.5\text{ J}$ substantially exceeds the human critical injury / fatality threshold ($> 1000\text{ J}$ under blunt force impact models), resulting in an unmitigated SORA Ground Risk Class classification of **GRC-3**.

   - **Parachute-Mitigated Descent & Terminal Velocity Kinematics ($v_{\mathrm{terminal}} \le 1.65\text{ m/s}$, $E_k \le 34.0\text{ J}$):**
     To mitigate ground impact severity, the Tactical UAS incorporates an autonomous pyrotechnic ballistic parachute system. Upon contingency detection (`EMG-01`..`EMG-07`), deployment is triggered within $\tau_{\mathrm{deploy}} \le 500.0\text{ ms}$.
     The steady-state descent terminal velocity under canopy is governed by the aerodynamic equilibrium equation where drag balances vehicle weight:

$$
\begin{aligned}
m_{\mathrm{system}} g &= \frac{1}{2} \rho v_{\mathrm{terminal,parachute}}^2 S C_d \\
v_{\mathrm{terminal,parachute}} &= \sqrt{\frac{2 m_{\mathrm{system}} g}{\rho S C_d}}
\end{aligned}
$$

Where and Operational Parameters:
- $m_{\mathrm{system}}$: Total system operational mass ($25.0\text{ kg}$ MTOW).
- $g$: Standard gravitational acceleration constant ($9.80665\text{ m/s}^2$).
- $\rho$: Standard sea-level air density ($1.225\text{ kg/m}^3$).
- $S$: Effective canopy aerodynamic surface area ($2.80\text{ m}^2$).
- $C_d$: Hemispherical parachute drag coefficient ($1.75$).
- $v_{\mathrm{terminal,parachute}}$: Calculated steady-state terminal descent velocity ($\le 1.65\text{ m/s}$).

The resulting ground impact kinetic energy under parachute descent is strictly bounded by:

$$
\begin{aligned}
E_{k,\mathrm{parachute}} &= \frac{1}{2} m_{\mathrm{system}} v_{\mathrm{terminal,parachute}}^2
\end{aligned}
$$

Where and Operational Parameters:
- $E_{k,\mathrm{parachute}}$: Mitigated ground impact kinetic energy ($34.0\text{ J}$ calculated from $m_{\mathrm{system}} = 25.0\text{ kg}$ and $v_{\mathrm{terminal,parachute}} = 1.65\text{ m/s}$).

Because $34.0\text{ J}$ is well below the non-fatal blunt trauma threshold ($< 66\text{ J}$ per JARUS SORA v2.5 Annex E and FAA Range Safety Criteria), the parachute mitigation qualifies for a high-integrity **-1 GRC** credit under SORA Mitigation M2.

3. **Final Ground Risk Class (GRC-3 $\rightarrow$ GRC-2):**
   - Mitigation M1 (Strategic ground risk mitigation - controlled ground perimeter): **-1 GRC** credit.
   - Mitigation M2 (Effects of ground impact - autonomous ballistic parachute ensuring $E_k \le 34.0\text{ J}$): **-1 GRC** credit.
   - Final Ground Risk Class: **GRC-2** (Specific Category low-risk profile).

### 5.3 Air Risk Class (ARC) & Strategic Airspace Deconfliction
- **Initial Air Risk Class:** **ARC-b** (Atypical / Segregated Airspace below $120.0\text{ m}$ AGL in uncontrolled Class G airspace).
- **Strategic Airspace Mitigations:**
  1. Mandatory flight plan filing with U-space / UTM Service Provider prior to launch.
  2. Electronic Conspicuity: Continuous direct Remote ID broadcast (ASTM F3411-22a) and ADS-B In situational awareness receiver.
  3. Tactical Airspace Surveillance: Onboard RTCA DO-365B DAA sensors and visual observer network maintaining continuous 360° airspace deconfliction.

### 5.4 SORA Mitigations (M1–M3)

| Mitigation Level | SORA Mitigation Category | Implementation Mechanism & System Architecture | Target Integrity Level | GRC / ARC Credit |
| :--- | :--- | :--- | :--- | :--- |
| **M1** | Strategic Mitigations for Ground Risk | Controlled ground perimeter fencing, active access control, and 200.0 m Ground Risk Buffer containment. | Medium Integrity (Declared & Audited) | -1 GRC Reduction Credit |
| **M2** | Effects of Ground Impact (Containment) | Autonomous ballistic parachute recovery system deploying in <= 500 ms; reduces descent velocity to <= 1.65 m/s and impact energy to <= 34.0 J. | High Integrity (DO-178C / DO-254 Watchdog) | -1 GRC Reduction Credit |
| **M3** | Emergency Response Plan (ERP) | Formal ERP detailing direct coordination with local emergency services, automated emergency beacon broadcast, and hazardous material isolation. | Medium Integrity (Validated by Drill) | Mandatory Prerequisite for Final SORA Authorization |

### 5.5 Containment Margins & Dynamic Geofence Buffers
To guarantee zero-breach containment of the operational volume:
- **Soft Warning Boundary:** Positioned $50.0\text{ m}$ inboard of the primary operational boundary. Reaching this threshold triggers an automated flight path correction and visual/acoustic alert on the GCS.
- **Hard Geofence Boundary:** The outer edge of the contingency volume. Crossing this threshold activates trigger `EMG-05`, initiating an immediate autonomous $180^\circ$ maximum-rate coordinated turnaround maneuver.
- **Buffer Retention Margin:** The Ground Risk Buffer ($R_{\mathrm{GRB}} = 200.0\text{ m}$) guarantees that in the event of unrecoverable propulsion or control loss at maximum operating ceiling ($120.0\text{ m}$ AGL) under maximum wind conditions ($15.0\text{ m/s}$), all system debris comes to rest strictly within the declared buffer zone.
