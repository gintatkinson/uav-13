| Attribute | Specification Detail |
| :--- | :--- |
| **Title** | Tactical Mission Intent: INCOSE MoE & MoP Metrics |
| **Issue ID** | MI-03 |
| **Type** | Mission Intent |
| **Generation Mode** | Manual |
| **Specification Source** | .pipeline/schema.sysml; schema/extracted/parametric_limits.md; schema/extracted/oem_bom.md; schema/extracted/interface_table.md; docs/research/RESEARCH_INVENTORY.md |
| **Version** | 1.0.0 |
| **Date** | 2026-09-02 |

## 3. Measures of Effectiveness (MoE) & Measures of Performance (MoP) Metrics

In accordance with INCOSE Systems Engineering Handbook v5.0, mission effectiveness is expressed as Measures of Effectiveness (MoE) and technical performance is expressed as Measures of Performance (MoP). Each MoE and MoP in this unit is bounded by a threshold and an objective value.

Grounding discipline for this unit:

- Every numeric threshold, objective, and parameter value cites `schema/extracted/parametric_limits.md` by parameter identifier, or an OEM source line. The parametric table itself records the originating OEM file and line for each parameter.
- Where the OEM sources are silent, the field states "Not stated in OEM sources". No synthetic timeout, protocol, or performance constant is introduced.
- The canonical tail control surface is the Ruddervator, quantity 4 units (oem_bom.md:23; PL-14).
- The ESAD is safety-critical, Critical / DAL-A (oem_bom.md:52; a5-user-manual-2.md:1984), and is measured under the safety assurance criteria of MIL-STD-1629A Section 4.3 and SAE ARP4761 Section 4.3.1.
- The Parachute Deployment Non-Mission module is a non-mission configuration with baseline false (oem_bom.md:47). It is excluded from the mission MoE and MoP baseline and contributes no mission performance value.

OEM-silent fields excluded from numeric MoE and MoP assignment:

- End-to-end C2 latency: Not stated in OEM sources.
- Packet delivery ratio: Not stated in OEM sources.
- C2 link availability: Not stated in OEM sources.
- Maintenance MTBM, MTTR, MLDT, and MADT: Not stated in OEM sources.
- Data throughput capacity: Not stated in OEM sources.
- Target identification probability: Not stated in OEM sources.

### 3.1 Mathematical Formulations

#### 3.1.1 Mission Endurance, Range, and Loiter

Mission endurance is the available endurance time against the required endurance threshold. Direct and extended range coverage are bounded by their OEM range limits. On-station loiter is bounded by the OEM loiter radius.

$$
\begin{aligned}
E_{\mathrm{mission}} &= t_{\mathrm{available}} \ge E_{\mathrm{threshold}} \\
R_{\mathrm{direct}} &\le R_{\mathrm{direct,max}} \\
R_{\mathrm{extended}} &\le R_{\mathrm{extended,max}} \\
R_{\mathrm{loiter}} &\le R_{\mathrm{loiter,max}}
\end{aligned}
$$

- Parameter Definitions & Engineering Units:

| Parameter | Symbol | Units | Threshold | Objective | Source | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Available Endurance Time | t_available | min | 90 min | 90 min | parametric_limits.md PL-06 | Maximum flight endurance |
| Required Mission Endurance | E_threshold | min | 90 min | 90 min | parametric_limits.md PL-06 | Mission endurance threshold |
| Mission Endurance Objective | E_objective | min | 90 min | 90 min | parametric_limits.md PL-06 | Mission endurance objective |
| Direct RLOS Range | R_direct | km | 60 km | 60 km | parametric_limits.md PL-07 | Direct line-of-sight range bound |
| Extended RLOS Range | R_extended | km | 60 km | 180 km | parametric_limits.md PL-08 | Extended line-of-sight range bound |
| On-Station Loiter Radius | R_loiter | m | 300 m | 300 m | parametric_limits.md PL-37 | Loiter radius bound |

#### 3.1.2 Speed and Dive Envelope

The air vehicle speed envelope is bounded below by minimum flight speed and above by maximum horizontal speed. Dive speed and dive angle are separately bounded by their maximum values.

$$
\begin{aligned}
V_{\mathrm{min}} &\le V_{\mathrm{flight}} \le V_{\mathrm{horizontal,max}} \\
V_{\mathrm{dive}} &\le V_{\mathrm{dive,max}} \\
\theta_{\mathrm{dive}} &\le \theta_{\mathrm{dive,max}}
\end{aligned}
$$

- Parameter Definitions & Engineering Units:

| Parameter | Symbol | Units | Threshold | Objective | Source | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Minimum Flight Speed | V_min | m/s | 26 m/s | 26 m/s | parametric_limits.md PL-05 | Lower airspeed bound |
| Maximum Horizontal Speed | V_horizontal_max | m/s | 38 m/s | 38 m/s | parametric_limits.md PL-02 | Upper horizontal airspeed bound |
| Cruise Speed | V_cruise | m/s | 30 m/s | 30 m/s | parametric_limits.md PL-01 | Nominal cruise airspeed |
| Maximum Dive Speed | V_dive_max | m/s | 55 m/s | 55 m/s | parametric_limits.md PL-03 | Upper dive airspeed bound |
| Maximum Dive Angle | theta_dive_max | deg | 22 deg | 22 deg | parametric_limits.md PL-04 | Upper dive angle bound |

#### 3.1.3 Payload Mass Fraction and Launch Kinetic Energy

Payload mass fraction is the ratio of warhead mass to maximum take-off weight. Launch kinetic energy is the kinetic energy implied by the maximum launched plane mass and maximum launch velocity.

$$
\begin{aligned}
f_{\mathrm{payload}} &= \frac{m_{\mathrm{warhead}}}{m_{\mathrm{MTOW}}} \\
E_{\mathrm{launch}} &= \frac{m_{\mathrm{launch}} v_{\mathrm{launch}}^2}{2}
\end{aligned}
$$

- Parameter Definitions & Engineering Units:

| Parameter | Symbol | Units | Threshold | Objective | Source | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Warhead Mass | m_warhead | kg | 5 kg | 5 kg | parametric_limits.md PL-13 | Modular warhead mass |
| Maximum Take-Off Weight | m_MTOW | kg | 17 kg | 17 kg | parametric_limits.md PL-12 | Air vehicle maximum take-off weight |
| Payload Mass Fraction | f_payload | percent | 29.4 percent | 29.4 percent | Derived from PL-13 and PL-12 | Warhead mass fraction of take-off weight |
| Maximum Launched Plane Mass | m_launch | kg | 30 kg | 30 kg | parametric_limits.md PL-64 | Launcher maximum launched mass |
| Maximum Launch Velocity | v_launch | m/s | 25 m/s | 25 m/s | parametric_limits.md PL-65 | Launcher maximum launch velocity |
| Launch Kinetic Energy | E_launch | J | 9375 J | 9375 J | Derived from PL-64 and PL-65 | Kinetic energy at maximum launch condition |

#### 3.1.4 Target Tracking and Engagement Envelope

Target track duration is bounded by a minimum and maximum track window. Engagement elevation and engagement airspeed are bounded by their maximum values.

$$
\begin{aligned}
T_{\mathrm{track,min}} &\le T_{\mathrm{track}} \le T_{\mathrm{track,max}} \\
\theta_{\mathrm{engagement}} &\le \theta_{\mathrm{engagement,max}} \\
V_{\mathrm{engagement}} &\le V_{\mathrm{engagement,max}}
\end{aligned}
$$

- Parameter Definitions & Engineering Units:

| Parameter | Symbol | Units | Threshold | Objective | Source | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Minimum Target Track Duration | T_track_min | s | 2 s | 2 s | parametric_limits.md PL-42 | Lower target track window |
| Maximum Target Track Duration | T_track_max | s | 5 s | 5 s | parametric_limits.md PL-43 | Upper target track window |
| Maximum Engagement Elevation | theta_engagement_max | deg | 15 deg | 15 deg | parametric_limits.md PL-44 | Upper engagement elevation |
| Maximum Engagement Airspeed | V_engagement_max | m/s | 55 m/s | 55 m/s | parametric_limits.md PL-45 | Upper engagement airspeed |

#### 3.1.5 ESAD Safety and Arming Timing

The ESAD is a Critical / DAL-A safety-critical element. Its response latency is bounded, its command rate is fixed, and its arming waveform is defined by period and duty cycle.

$$
\begin{aligned}
\tau_{\mathrm{ESAD}} &\le \tau_{\mathrm{ESAD,max}} \\
f_{\mathrm{ESAD,cmd}} &\ge f_{\mathrm{ESAD,cmd,min}} \\
T_{\mathrm{arm}} &= T_{\mathrm{arm,nominal}} \\
D_{\mathrm{arm}} &= D_{\mathrm{arm,nominal}}
\end{aligned}
$$

- Parameter Definitions & Engineering Units:

| Parameter | Symbol | Units | Threshold | Objective | Source | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ESAD Response Latency | tau_ESAD | ms | 5 ms | 5 ms | parametric_limits.md PL-58 | Maximum ESAD response latency |
| ESAD Command Rate | f_ESAD_cmd | Hz | 100 Hz | 100 Hz | parametric_limits.md PL-57 | ESAD RS-485 command interval |
| ESAD Arm Enable Period | T_arm | ms | 1 ms | 1 ms | parametric_limits.md PL-54 | Arm enable waveform period |
| ESAD Arm Enable Duty Cycle | D_arm | percent | 50 percent | 50 percent | parametric_limits.md PL-55 | Arm enable waveform duty cycle |
| ESAD RS-485 Baud Rate | R_ESAD_baud | bps | 115200 bps | 115200 bps | parametric_limits.md PL-56 | ESAD serial baud rate |
| ESAD Message Length Minimum | L_ESAD_min | bytes | 5 bytes | 5 bytes | parametric_limits.md PL-61 | Minimum ESAD message length |
| ESAD Message Length Maximum | L_ESAD_max | bytes | 14 bytes | 14 bytes | parametric_limits.md PL-62 | Maximum ESAD message length |
| ESAD High Voltage Measurement Range | V_ESAD_HV | V | 1800 V | 1800 V | parametric_limits.md PL-60 | ESAD high voltage measurement bound |
| ESAD Power Input Minimum | V_ESAD_min | V | 14 V | 14 V | parametric_limits.md PL-46 | ESAD power input lower bound |
| ESAD Power Input Maximum | V_ESAD_max | V | 32 V | 32 V | parametric_limits.md PL-47 | ESAD power input upper bound |
| ESAD Power Input Nominal | V_ESAD_nom | V | 28 V | 28 V | parametric_limits.md PL-48 | ESAD nominal power input |
| ESAD Umbilical Continuity Resistance | R_umb | ohm | 0.5 ohm | 0.5 ohm | parametric_limits.md PL-49 | Maximum umbilical continuity resistance |
| ESAD Umbilical Continuity Current | I_umb | mA | 20 mA | 20 mA | parametric_limits.md PL-50 | Umbilical continuity test current |
| ESAD Acceleration Resolution | a_ESAD_res | g | 0.0039 g | 0.0039 g | parametric_limits.md PL-63 | ESAD acceleration measurement resolution |

#### 3.1.6 GCS C2, Power, and Launch Envelope

The GCS C2 link operates in the OEM-declared radio band and at the OEM-declared ground radio power. The air vehicle power and servo rail envelopes are bounded by their OEM values. The launcher envelope is bounded by pressure, velocity, setup time, and temperature.

$$
\begin{aligned}
f_{\mathrm{C2,min}} &\le f_{\mathrm{C2}} \le f_{\mathrm{C2,max}} \\
P_{\mathrm{GCS}} &= P_{\mathrm{GCS,nominal}} \\
V_{\mathrm{battery,min}} &\le V_{\mathrm{battery}} \le V_{\mathrm{battery,max}} \\
P_{\mathrm{launch,min}} &\le P_{\mathrm{launch}} \le P_{\mathrm{launch,max}} \\
T_{\mathrm{launcher,min}} &\le T_{\mathrm{launcher}} \le T_{\mathrm{launcher,max}}
\end{aligned}
$$

- Parameter Definitions & Engineering Units:

| Parameter | Symbol | Units | Threshold | Objective | Source | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| GCS C2 Band Lower Frequency | f_C2_min | GHz | 4.4 GHz | 4.4 GHz | interface_table.md:63 | GCS telemetry link lower band edge |
| GCS C2 Band Upper Frequency | f_C2_max | GHz | 5.0 GHz | 5.0 GHz | interface_table.md:63 | GCS telemetry link upper band edge |
| GCS Ground Radio Power | P_GCS | W | 2 W | 2 W | parametric_limits.md PL-39 | Ground radio output setting |
| UAV Battery Pre-Flight Voltage Minimum | V_preflight_min | V | 49 V | 49 V | parametric_limits.md PL-32 | Pre-flight battery lower bound |
| UAV Battery Pre-Flight Voltage Maximum | V_preflight_max | V | 50 V | 50 V | parametric_limits.md PL-33 | Pre-flight battery upper bound |
| UAV Battery Main Voltage Minimum | V_battery_min | V | 36 V | 36 V | parametric_limits.md PL-23 | Main battery lower bound |
| UAV Battery Main Voltage Maximum | V_battery_max | V | 50.4 V | 50.4 V | parametric_limits.md PL-24 | Main battery upper bound |
| Servo Power Rail Voltage | V_servo | V | 8 V | 8 V | parametric_limits.md PL-22 | Ruddervator and wing servo rail |
| Launcher Pressure Minimum | P_launch_min | MPa | 1.3 MPa | 1.3 MPa | parametric_limits.md PL-40 | Catapult launch pressure lower bound |
| Launcher Pressure Maximum | P_launch_max | MPa | 1.4 MPa | 1.4 MPa | parametric_limits.md PL-41 | Catapult launch pressure upper bound |
| Launcher Setup Time | T_setup | min | 5 min | 5 min | parametric_limits.md PL-72 | Maximum launcher setup time |
| Launcher Working Temperature Minimum | T_launcher_min | deg C | -20 deg C | -20 deg C | parametric_limits.md PL-73 | Launcher lower working temperature |
| Launcher Working Temperature Maximum | T_launcher_max | deg C | 50 deg C | 50 deg C | parametric_limits.md PL-74 | Launcher upper working temperature |
| Launch Angle | theta_launch | deg | 12 deg | 12 deg | parametric_limits.md PL-66 | Launcher rail elevation |
| Assembled Rail Length | L_rail | m | 5 m | 5 m | parametric_limits.md PL-93 | Assembled launcher rail length |

### 3.2 INCOSE SEH v5.0 Metrics Summary Table

| Metric ID | Metric Type | Metric Name | Formulation / Equation | Threshold | Objective | Unit | Public Clause Citation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **MoE-01** | MoE | Mission Endurance | E_mission = t_available | 90 min | 90 min | min | [C1]; parametric_limits.md PL-06 |
| **MoE-02** | MoE | Direct-Range Coverage | R_direct <= R_direct_max | 60 km | 60 km | km | [C1]; parametric_limits.md PL-07 |
| **MoE-03** | MoE | Extended-Range Coverage | R_extended <= R_extended_max | 60 km | 180 km | km | [C1]; parametric_limits.md PL-08 |
| **MoE-04** | MoE | Cruise Speed | V_cruise = 30 m/s | 30 m/s | 30 m/s | m/s | [C1]; parametric_limits.md PL-01 |
| **MoE-05** | MoE | Payload Mass Fraction | f_payload = m_warhead / m_MTOW | 29.4 percent | 29.4 percent | percent | [C2]; parametric_limits.md PL-12, PL-13 |
| **MoE-06** | MoE | On-Station Loiter Containment | R_loiter <= R_loiter_max | 300 m | 300 m | m | [C1]; parametric_limits.md PL-37 |
| **MoP-01** | MoP | Maximum Horizontal Speed | V_horizontal <= V_horizontal_max | 38 m/s | 38 m/s | m/s | [C2]; parametric_limits.md PL-02 |
| **MoP-02** | MoP | Maximum Dive Speed | V_dive <= V_dive_max | 55 m/s | 55 m/s | m/s | [C2]; parametric_limits.md PL-03 |
| **MoP-03** | MoP | Minimum Flight Speed | V_flight >= V_min | 26 m/s | 26 m/s | m/s | [C2]; parametric_limits.md PL-05 |
| **MoP-04** | MoP | Maximum Dive Angle | theta_dive <= theta_dive_max | 22 deg | 22 deg | deg | [C2]; parametric_limits.md PL-04 |
| **MoP-05** | MoP | Target Track Duration | T_track_min <= T_track <= T_track_max | 2 s | 5 s | s | [C2]; parametric_limits.md PL-42, PL-43 |
| **MoP-06** | MoP | Maximum Engagement Elevation | theta_engagement <= theta_engagement_max | 15 deg | 15 deg | deg | [C2]; parametric_limits.md PL-44 |
| **MoP-07** | MoP | Maximum Engagement Airspeed | V_engagement <= V_engagement_max | 55 m/s | 55 m/s | m/s | [C2]; parametric_limits.md PL-45 |
| **MoP-08** | MoP | ESAD Response Latency | tau_ESAD <= tau_ESAD_max | 5 ms | 5 ms | ms | [C3]; parametric_limits.md PL-58 |
| **MoP-09** | MoP | ESAD Command Rate | f_ESAD_cmd >= f_ESAD_cmd_min | 100 Hz | 100 Hz | Hz | [C5]; parametric_limits.md PL-57 |
| **MoP-10** | MoP | ESAD RS-485 Baud Rate | R_ESAD_baud = 115200 bps | 115200 bps | 115200 bps | bps | [C5]; parametric_limits.md PL-56 |
| **MoP-11** | MoP | ESAD Message Length | L_ESAD_min <= L_ESAD <= L_ESAD_max | 5 bytes | 14 bytes | bytes | [C5]; parametric_limits.md PL-61, PL-62 |
| **MoP-12** | MoP | ESAD High Voltage Measurement Range | V_ESAD_HV <= 1800 V | 1800 V | 1800 V | V | [C3]; parametric_limits.md PL-60 |
| **MoP-13** | MoP | ESAD Arm Enable Duty Cycle | D_arm = 50 percent | 50 percent | 50 percent | percent | [C3]; parametric_limits.md PL-55 |
| **MoP-14** | MoP | ESAD Arm Enable Period | T_arm = 1 ms | 1 ms | 1 ms | ms | [C3]; parametric_limits.md PL-54 |
| **MoP-15** | MoP | ESAD Power Input Nominal | V_ESAD_nom = 28 V | 14 V | 28 V | V | [C3]; parametric_limits.md PL-46, PL-47, PL-48 |
| **MoP-16** | MoP | ESAD Acceleration Resolution | a_ESAD_res = 0.0039 g | 0.0039 g | 0.0039 g | g | [C3]; parametric_limits.md PL-63 |
| **MoP-17** | MoP | Maximum Launch Velocity | v_launch <= 25 m/s | 25 m/s | 25 m/s | m/s | [C2]; parametric_limits.md PL-65 |
| **MoP-18** | MoP | Launch Kinetic Energy | E_launch = m_launch * v_launch^2 / two | 9375 J | 9375 J | J | [C2]; parametric_limits.md PL-64, PL-65 |
| **MoP-19** | MoP | Launcher Setup Time | T_setup <= 5 min | 5 min | 5 min | min | [C2]; parametric_limits.md PL-72 |
| **MoP-20** | MoP | GCS Ground Radio Power | P_GCS = 2 W | 2 W | 2 W | W | [C2]; parametric_limits.md PL-39 |
| **MoP-21** | MoP | GCS C2 Band | 4.4 GHz <= f_C2 <= 5.0 GHz | 4.4 GHz | 5.0 GHz | GHz | [C6]; interface_table.md:63 |
| **MoP-22** | MoP | UAV Battery Pre-Flight Voltage | 49 V <= V_preflight <= 50 V | 49 V | 50 V | V | [C2]; parametric_limits.md PL-32, PL-33 |
| **MoP-23** | MoP | UAV Battery Main Voltage | 36 V <= V_battery <= 50.4 V | 36 V | 50.4 V | V | [C2]; parametric_limits.md PL-23, PL-24 |
| **MoP-24** | MoP | Servo Power Rail Voltage | V_servo = 8 V | 8 V | 8 V | V | [C2]; parametric_limits.md PL-22 |
| **MoP-25** | MoP | Minimum Waypoint Altitude | h_waypoint >= 50 m | 50 m | 50 m | m | [C2]; parametric_limits.md PL-36 |
| **MoP-26** | MoP | Pitot Static Airspeed Limit | 0 m/s <= V_pitot <= 3 m/s | 0 m/s | 3 m/s | m/s | [C2]; parametric_limits.md PL-34 |
| **MoP-27** | MoP | Seeker Pitch Envelope | -45 deg <= theta_pitch <= 135 deg | -45 deg | 135 deg | deg | [C2]; parametric_limits.md PL-25 |
| **MoP-28** | MoP | Seeker Yaw and Roll Envelope | -165 deg <= psi_yaw_roll <= 165 deg | -165 deg | 165 deg | deg | [C2]; parametric_limits.md PL-26 |
| **MoP-29** | MoP | Launch Angle | theta_launch = 12 deg | 12 deg | 12 deg | deg | [C2]; parametric_limits.md PL-66 |
| **MoP-30** | MoP | Assembled Rail Length | L_rail = 5 m | 5 m | 5 m | m | [C2]; parametric_limits.md PL-93 |
| **MoP-31** | MoP | Maximum Launched Plane Mass | m_launch <= 30 kg | 30 kg | 30 kg | kg | [C2]; parametric_limits.md PL-64 |

### 3.3 Public Clause Citation Legend

| Citation Key | Public Clause Citation |
| :--- | :--- |
| C1 | INCOSE SEH v5.0 Section 3.3.1 |
| C2 | INCOSE SEH v5.0 Section 5.4 |
| C3 | MIL-STD-1629A Section 4.3 |
| C4 | SAE ARP4761 Section 4.3.1 |
| C5 | RTCA DO-178C Section 6.3.1 |
| C6 | RTCA DO-362A Section 2.2 |
| C7 | MIL-STD-810H Method 501.7 Section 4.2 |
| C8 | MIL-STD-810H Method 502.7 Section 4.2 |

## Source References

Authoritative schema paths and normative clauses for this unit are `.pipeline/schema.sysml`, `schema/extracted/parametric_limits.md`, `schema/extracted/oem_bom.md`, `schema/extracted/interface_table.md`, and `docs/research/RESEARCH_INVENTORY.md`; the applicable public clauses are INCOSE SEH v5.0 Section 3.3.1, INCOSE SEH v5.0 Section 5.4, MIL-STD-1629A Section 4.3, SAE ARP4761 Section 4.3.1, RTCA DO-178C Section 6.3.1, RTCA DO-362A Section 2.2, and MIL-STD-810H Method 501.7 Section 4.2.

- Source: `.pipeline/schema.sysml`; INCOSE SEH v5.0 Section 3.3.1.
- Source: `schema/extracted/parametric_limits.md`; INCOSE SEH v5.0 Section 5.4.
- Source: `schema/extracted/oem_bom.md`; MIL-STD-1629A Section 4.3.
- Source: `schema/extracted/interface_table.md`; RTCA DO-362A Section 2.2.
- Source: `docs/research/RESEARCH_INVENTORY.md`; MIL-STD-810H Method 501.7 Section 4.2.
