| Attribute | Specification Detail |
| :--- | :--- |
| **Title** | Operational State Space, Boundary Containment & Risk Assessment |
| **Version** | 1.0.0 |
| **Date** | 2026-10-31 |
| **Issue ID** | CONOPS-UNIT-05 |
| **Type** | Concept of Operations Unit |
| **Generation Mode** | Schema-Grounded Deterministic Synthesis |
| **Specification Source** | .pipeline/schema.sysml; schema/extracted/parametric_limits.md; schema/extracted/oem_bom.md; schema/extracted/interface_table.md; docs/research/RESEARCH_INVENTORY.md |

## 5. Operational State Space, Boundary Containment & Risk Assessment

### 5.1 Operational State Space Formulation

The operational state space is a 4D volume spanning horizontal position, vertical position, and mission time. The 4D boundary containment formulation defines the state vector over the declared operational domain, with every numeric boundary anchored to the Level 0 parametric limits or explicitly recorded as silent in the OEM sources.

$$
\begin{aligned}
\mathbf{s}(t) &= \left[x(t), y(t), z(t), t\right]^{\top} \\
\Omega_{\mathrm{state}} &= \left\{ \mathbf{s}(t) \mid x(t)^2 + y(t)^2 \le R_{\mathrm{containment}}^2,\ z_{\mathrm{min}} \le z(t) \le z_{\mathrm{max}},\ 0 \le t \le T_{\mathrm{endurance}} \right\}
\end{aligned}
$$

The horizontal containment radius is the sum of the minimum required operational radius and a declared containment buffer. The buffer is retained as an explicit margin term rather than folded into the operational radius.

$$
\begin{aligned}
R_{\mathrm{containment}} &= R_{\mathrm{min}} + R_{\mathrm{buffer}} \\
R_{\mathrm{containment}} &\ge R_{\mathrm{min}} \\
T_{\mathrm{boundary}} &= \frac{R_{\mathrm{min}}}{v_{\mathrm{max}}} \\
E_{k} &= \frac{1}{2} m v_{\mathrm{dive}}^2
\end{aligned}
$$

- Parameter Definitions & Engineering Units:

| Parameter | Symbol | Nominal Value | Units | Constraint / Derivation Rule | Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Minimum Containment Radius | R_min | 300 m | m | R_min = 300 m (PL-37) | Minimum operational containment radius anchored to the declared loiter radius |
| Containment Buffer | R_buffer | Not stated in OEM sources | m | R_buffer >= 0 m | Additional margin outside the minimum containment radius; OEM sources do not state a numeric buffer |
| Containment Radius | R_containment | R_min + R_buffer | m | R_containment >= R_min | Achieved containment radius evaluated against the minimum required radius |
| Minimum Mission Altitude | z_min | 50 m | m | z_min = 50 m (PL-36) | Lower vertical boundary of the operational state space |
| Maximum Mission Altitude | z_max | Not stated in OEM sources | m | z_max >= z_min | Upper vertical boundary; OEM sources do not state a maximum altitude |
| Flight Endurance | T_endurance | 90 min | min | T_endurance <= 90 min (PL-06) | Temporal extent of the operational state space |
| Maximum Horizontal Speed | v_max | 38 m/s | m/s | v_max = 38 m/s (PL-02) | Maximum horizontal speed used for the time-to-boundary evaluation |
| Minimum Flight Speed | v_min | 26 m/s | m/s | v_min = 26 m/s (PL-05) | Lower airspeed boundary of the operational state space |
| Maximum Dive Speed | v_dive | 55 m/s | m/s | v_dive = 55 m/s (PL-03) | Maximum dive speed used for the kinetic energy evaluation |
| Maximum Dive Angle | theta_dive | 22 deg | deg | theta_dive = 22 deg (PL-04) | Maximum dive angle used for vertical trajectory bounding |
| Maximum Take-Off Mass | m | 17 kg | kg | m <= 17 kg (PL-12) | Maximum take-off mass used for the kinetic energy evaluation |
| Warhead Mass | m_warhead | 5 kg | kg | m_warhead <= 5 kg (PL-13) | Maximum warhead mass carried inside the lethal package |
| Time to Boundary at Maximum Horizontal Speed | T_boundary | 7.89 s | s | Derived from PL-37 and PL-02 via time-to-boundary relation | Time available before the minimum containment radius is reached at maximum horizontal speed |
| Kinetic Energy at Maximum Dive Speed | E_k | 25712.5 J | J | Derived from PL-12 and PL-03 via kinetic energy relation | Worst-case translational kinetic energy at the maximum declared dive speed |

### 5.2 Boundary Containment Margin

The containment margin is the difference between the achieved containment radius and the minimum required radius. A non-negative margin is the mandatory containment condition. The condition is evaluated in the horizontal plane, with the vertical and temporal boundaries enforced independently.

$$
\begin{aligned}
M_{\mathrm{containment}} &= R_{\mathrm{containment}} - R_{\mathrm{min}} = R_{\mathrm{buffer}} \\
M_{\mathrm{containment}} &\ge 0 \\
R_{\mathrm{containment}} &\ge R_{\mathrm{min}}
\end{aligned}
$$

The containment condition is satisfied when the declared buffer is non-negative. The OEM sources do not state a numeric buffer, so the numeric margin remains an operator-declared parameter and is not credited as a fixed OEM value. The minimum containment radius is anchored to the PL-37 loiter radius of 300 m, and the time to boundary at the PL-02 maximum horizontal speed of 38 m/s is 7.89 s. The vertical lower boundary is anchored to the PL-36 minimum mission waypoint altitude of 50 m; the upper vertical boundary is not stated in OEM sources.

### 5.3 Risk Assessment

Risk assessment follows the SORA ground and air risk framework for the ground-risk mitigations, the SAE ARP4761 functional hazard assessment for severity classification, and the MIL-STD-882E risk matrix for probability and severity pairing. The intrinsic Ground Risk Class and Air Risk Class are not stated in OEM sources; no numeric GRC or ARC is claimed here.

| Risk ID | Hazard | Cause | Consequence | Severity | Probability | Mitigation | Citation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| RSK-01 | Loss of horizontal containment | Navigation error, control surface degradation, or C2 link loss | Air vehicle exits the declared containment radius | Catastrophic | Not stated in OEM sources | Minimum containment radius, containment buffer, and R_containment >= R_min condition | SAE ARP4761 Section 4.3.1; JARUS SORA v2.5 Annex E Section E.14 |
| RSK-02 | Loss of vertical containment | Undetected descent below the minimum mission altitude or uncommanded climb | Air vehicle enters an uncontrolled vertical segment | Catastrophic | Not stated in OEM sources | z_min boundary at 50 m (PL-36) and operator altitude monitoring | SAE ARP4761 Section 4.3.1; JARUS SORA v2.5 Annex E Section E.14 |
| RSK-03 | Ground impact at maximum dive speed | Loss of control authority during a dive | Ground impact at the maximum declared dive speed of 55 m/s (PL-03) | Catastrophic | Not stated in OEM sources | Operational speed limiting and containment boundary enforcement | MIL-STD-882E risk matrix; SAE ARP4761 Section 4.3.1 |
| RSK-04 | Uncommanded lethal package initiation | ESAD fault, unauthorized command, or interlock defeat | Warhead initiation outside the authorized engagement condition | Catastrophic | Not stated in OEM sources | ESAD (Critical, DAL-A) safety and arming interlocks | MIL-STD-882E Task 208 Section 4.2; DoD Directive 3000.09 Section 3.1.b |
| RSK-05 | Loss of C2 link during containment | RF link degradation or jamming | Loss of supervisory authority while the air vehicle is inside the containment volume | Catastrophic | Not stated in OEM sources | C2 link loss procedures and deterministic containment behavior | RTCA DO-362A Section 3.4; JARUS SORA v2.5 Annex E Section E.6 |
| RSK-06 | Ruddervator (drawing synonym Fins; preparation synonym tail stabiliser) control degradation | Servo fault or control surface jam | Reduced pitch and yaw authority | Catastrophic | Not stated in OEM sources | Four Ruddervator units (PL-14) and pre-flight control checks | MIL-STD-882E Task 205 Section 4.2; SAE ARP4761 Section 4.3.3 |
| RSK-07 | Parachute deployment unavailable in the mission baseline | Parachute Deployment Non-Mission is configuration: non-mission and baseline: false | No parachute credit is available for ground-risk reduction in the mission baseline | Catastrophic | Not stated in OEM sources | Strategic isolation and emergency response planning; no M2 parachute credit is claimed | JARUS SORA v2.5 Annex B Section B.2; oem_bom.md:47 |

The risk assessment records the following bounded observations:

- The maximum take-off mass is 17 kg (PL-12), and the maximum warhead mass is 5 kg (PL-13). The lethal package therefore remains the dominant consequence driver.
- The worst-case translational kinetic energy at the maximum dive speed is 25712.5 J, derived from the PL-12 mass of 17 kg and the PL-03 dive speed of 55 m/s. This value excludes rotational energy and any warhead energetic contribution; the OEM sources do not state either quantity.
- The ESAD is classified as Critical with DAL-A assurance in the OEM bill of materials. The ESAD remains the primary safety-critical item for the lethal package.
- The Parachute Deployment Non-Mission item is configuration: non-mission and baseline: false. It is therefore excluded from mission-baseline ground-risk mitigation credit.
- The intrinsic Ground Risk Class and Air Risk Class are not stated in OEM sources. The SORA mitigation credit is therefore limited to the mitigations that can be evidenced without a parachute credit.

### 5.4 Containment Controls and OEM Silence Register

The containment controls are expressed as deterministic conditions on the operational state space:

- Horizontal condition: the horizontal position remains inside the R_containment radius, and R_containment >= R_min is maintained.
- Vertical condition: the altitude remains at or above the 50 m minimum mission waypoint altitude (PL-36); the maximum altitude is not stated in OEM sources.
- Temporal condition: the mission time remains within the 90 min flight endurance (PL-06).
- Speed condition: the air vehicle remains within the declared speed envelope bounded by the 26 m/s minimum flight speed (PL-05) and the 38 m/s maximum horizontal speed (PL-02), with the 55 m/s maximum dive speed (PL-03) treated as the worst-case risk input.
- Safety-critical condition: the ESAD (Critical, DAL-A) remains under its safety and arming interlocks, and the lethal package is not initiated without the authorized engagement condition.

OEM-silent fields retained in this unit are:

- Maximum mission altitude: Not stated in OEM sources.
- Containment buffer: Not stated in OEM sources.
- Intrinsic Ground Risk Class: Not stated in OEM sources.
- Intrinsic Air Risk Class: Not stated in OEM sources.
- Risk probability values: Not stated in OEM sources.
- Containment response time: Not stated in OEM sources.
- Deceleration capability: Not stated in OEM sources.

### Source References

[1] schema/extracted/parametric_limits.md
[2] schema/extracted/oem_bom.md
[3] schema/extracted/interface_table.md
[4] .pipeline/schema.sysml
[5] docs/research/RESEARCH_INVENTORY.md
