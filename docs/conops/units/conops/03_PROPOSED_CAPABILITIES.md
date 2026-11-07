| Attribute | Specification Detail |
| :--- | :--- |
| **Title** | Proposed Capabilities & Operational Justification (Trade-Offs) |
| **Document ID** | CONOPS-UNIT-03 |
| **Version** | 1.0.0 |
| **Date** | 2026-10-31 |
| **Status** | Draft |
| **Issue ID** | 276 |
| **Type** | conops |
| **Generation Mode** | subagent |
| **Specification Source** | conops |

## 3. Proposed Capabilities & Operational Justification (Trade-Offs)

### 3.1 Mission Drivers

The proposed architecture is driven by the operational need for a runway-independent, long-endurance, standoff-precision system whose weapon release remains subject to positive human judgment. Each driver below is traced to an OEM row or to the normative baseline. Evidence labels are resolved in the Source References table.

| Driver ID | Mission Driver | Operational Need | Evidence |
| :--- | :--- | :--- | :--- |
| MD-A | Persistent aerial presence | Endurance up to 90 min at 30 m/s cruise speed with a 300 m loiter radius | [A] |
| MD-B | Standoff command and control coverage | Direct radio line-of-sight range up to 60 km, with an extended range band of 60 km to 180 km | [B] |
| MD-C | Runway-independent launch | Pneumatic launch at 13 bar to 14 bar and a 12 deg launch angle, with launcher setup time of 0 min to 5 min | [C] |
| MD-D | Precision terminal effect | Maximum dive speed 55 m/s, maximum dive angle 22 deg, maximum engagement elevation 15 deg, maximum engagement airspeed 55 m/s, target track duration 2 s to 5 s, and warhead mass up to 5 kg | [D] |
| MD-E | Human-authorized weapon release | Positive human judgment and fail-safe interlocks before engagement | [E] |
| MD-F | Containment and recovery assurance | Containment inside the 3D operational volume plus flight termination provisions | [F] |
| MD-G | Expeditionary environmental tolerance | Launcher working thermal window and battery charging thermal window per the cited OEM rows | [G] |
| MD-H | Cyber and electromagnetic resilience | Defense-in-depth for the wireless command link and structured cyber risk assessment | [H] |

### 3.2 Functional Superiority & Operational Value Proposition

The value proposition is stated only against OEM-grounded bounds. Where the OEM sources are silent on a comparison metric, the proposition is marked as unquantified rather than assigned a synthetic value.

| Proposition ID | Value Proposition | Grounded Quantitative Basis | Evidence |
| :--- | :--- | :--- | :--- |
| VP-A | Runway-independent expeditionary launch | 13 bar to 14 bar launch pressure; 12 deg launch angle; 0 min to 5 min setup time; 5 m assembled rail and 1.28 m disassembled rail; 68 kg, 43 kg, and 25 kg set, case, and compressor masses | [I] |
| VP-B | Persistent coverage of the target area | Endurance 0 min to 90 min; cruise speed 30 m/s; loiter radius 300 m; minimum mission waypoint altitude 50 m | [J] |
| VP-C | Standoff command and control | Direct range 0 km to 60 km; extended range 60 km to 180 km; ground radio power 2 W; RF band 4.4 GHz to 5.0 GHz; MARS antenna gain 23 dBi | [K] |
| VP-D | Precision electro-optical and infrared identification | Zoom 1X to 40X; day and thermal resolution 1280x720; seeker pitch -45 deg to 135 deg; seeker yaw and roll -165 deg to 165 deg; target track duration 2 s to 5 s | [L] |
| VP-E | Human-authorized weapon release with a Critical / DAL-A safe-and-arm device | ESAD Critical / DAL-A; acceleration resolution 0.0039 g; arm-enable period 1 ms at 50 percent duty; response latency 0 ms to 5 ms; high-voltage measurement 0 V to 1800 V | [M] |
| VP-F | Separated tail and wing actuation | Four Ruddervator (Fins; tail stabiliser) surfaces and four ruddervator servos; four wing servos; eight servos total; 8 V servo rail; separate CAN 1 and CAN 2 buses | [N] |
| VP-G | Containment and flight termination assurance | Loiter radius 300 m; minimum mission waypoint altitude 50 m; launcher thermal window per the cited OEM rows | [O] |
| VP-H | Environmental and charging discipline | Launcher working thermal window and battery charging thermal window per the cited OEM rows; air vehicle environmental envelope not quantified | [P] |

### 3.3 Engineering Trade-Off Evaluations

The principal quantitative tension in the OEM data is between the launcher maximum launch velocity and the air vehicle minimum flight speed. The following identity makes the deficit explicit and is the basis for the powered climb-out decision.

$$
\begin{aligned}
\Delta V_{\mathrm{launch}} &= V_{\mathrm{min,flight}} - V_{\mathrm{launch,max}} \\
&= 26 - 25 = 1
\end{aligned}
$$

| Symbol | Value | Units | Evidence |
| :--- | :--- | :--- | :--- |
| V_min,flight | 26 | m/s | [Q] |
| V_launch,max | 25 | m/s | [R] |
| Delta V_launch | 1 | m/s | Derived from [Q] and [R] |

The relay option is evaluated as a range multiplier against the direct link bound.

$$
\begin{aligned}
R_{\mathrm{extension}} &= \frac{R_{\mathrm{extended,max}}}{R_{\mathrm{direct,max}}} \\
&= \frac{180}{60} = 3
\end{aligned}
$$

| Symbol | Value | Units | Evidence |
| :--- | :--- | :--- | :--- |
| R_direct,max | 60 | km | [T] |
| R_extended,max | 180 | km | [U] |
| R_extension | 3 | dimensionless | Derived from [T] and [U] |

The actuator count is evaluated as the sum of tail and wing servo populations.

$$
\begin{aligned}
N_{\mathrm{servo}} &= N_{\mathrm{ruddervator}} + N_{\mathrm{wing}} \\
&= 4 + 4 = 8
\end{aligned}
$$

| Symbol | Value | Units | Evidence |
| :--- | :--- | :--- | :--- |
| N_ruddervator | 4 | units | [W] |
| N_wing | 4 | units | [X] |
| N_servo | 8 | units | [Y] |

| Trade-Off ID | Decision | Alternatives Considered | Quantitative Evidence | Evaluation Outcome | Residual Risk / OEM Silence | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TRD-A | Retain the PL-40 pneumatic launcher and rely on powered climb-out after carriage separation | Raise launcher pressure above 14 bar; select a lower-speed airframe | Maximum launch velocity 25 m/s; minimum flight speed 26 m/s; launch pressure 13 bar to 14 bar; compressor working pressure 14 bar | The launch velocity bound is below the minimum flight speed by 1 m/s, and the compressor is already at its stated pressure limit. Pressure alone cannot close the gap, so powered climb-out is required | Separation-to-thrust transition time and thrust margin are Not stated in OEM sources | [Z] |
| TRD-B | Baseline the direct radio line-of-sight link and treat relay extension as optional | Direct-only link bounded at 60 km; beyond-line-of-sight satellite link | Direct range 0 km to 60 km; extended range 60 km to 180 km; RF band 4.4 GHz to 5.0 GHz; ground radio power 2 W | Relay extension raises the maximum range bound by a factor of three, but no relay node, relay data rate, or relay latency is identified in the OEM data | Relay hardware, relay link budget, and relay latency are Not stated in OEM sources | [AA] |
| TRD-C | Retain the removable 12S2P battery and the 17 kg maximum take-off weight class | Larger battery; additional payload | Endurance 0 min to 90 min; maximum take-off weight 17 kg; battery voltage 36 V to 50.4 V; separate launcher battery capacity 6000 mAh | The 90 min endurance bound and the 17 kg maximum take-off weight bound leave no stated mass margin for optional relay or recovery hardware | Component masses are Not stated in OEM sources | [AB] |
| TRD-D | Use four Ruddervator (Fins; tail stabiliser) surfaces on CAN 1 and four wing servos on CAN 2 | Fewer control surfaces; single CAN bus | Four ruddervator surfaces; four ruddervator servos; four wing servos; eight servos; 8 V servo rail; separate CAN 1 and CAN 2 buses | The split bus topology separates tail and wing actuation data paths at the cost of eight servos and two harness families | Common-mode failure of the 8 V servo rail is Not stated in OEM sources | [AC] |
| TRD-E | Use a single ESAD classified Critical / DAL-A with dual-environment arming and human consent | Redundant ESAD channels; mechanical safe-and-arm device | ESAD Critical / DAL-A; acceleration resolution 0.0039 g; arm-enable period 1 ms at 50 percent duty; RS-485 command interval 100 Hz at 115200 bps; response latency 0 ms to 5 ms; high-voltage measurement 0 V to 1800 V; human consent required by the cited normative baseline | The single ESAD is the highest-criticality item. Dual-environment arming and human consent reduce inadvertent initiation risk but do not provide a redundant firing path | ESAD redundancy and quantitative failure probability are Not stated in OEM sources | [AD] |
| TRD-F | Exclude the parachute deployment module from the mission baseline and retain it only for non-mission research and development testbed recovery | Mission parachute recovery; no recovery provision | Parachute configuration non-mission and baseline false, excluded from mission baseline analysis; two 50 V igniter outputs | The OEM configuration does not permit the parachute to be credited as a mission recovery capability | Mission recovery means and flight termination architecture are Not stated in OEM sources | [AE] |
| TRD-G | Use the Nighthawk2UZ gimbal with its stated zoom and pointing envelopes | Fixed electro-optical and infrared sensor; wider gimbal | Pitch envelope -45 deg to 135 deg; yaw and roll envelope -165 deg to 165 deg; zoom 1X to 40X; dive angle 22 deg; engagement elevation 15 deg; day and thermal resolution 1280x720 | The pitch envelope covers the 22 deg dive bound and the 15 deg engagement elevation bound with margin, so a wider gimbal is not required by the stated geometry | Target tracking performance under radio denial or obscuration is Not stated in OEM sources | [AF] |
| TRD-H | Qualify the launcher and charger to their stated thermal windows and leave the air vehicle environmental envelope open | Claim a complete air vehicle environmental envelope | Launcher working thermal window and battery charging thermal window per the cited OEM rows; environmental test basis per the cited normative baseline | Only the launcher and charger thermal windows are stated. The air vehicle thermal, ingress, wind, and icing limits are not quantified by the OEM sources | Air vehicle environmental qualification is Not stated in OEM sources | [AG] |

### 3.4 System Capability Hierarchy

The capability hierarchy below allocates the grounded bounds to operational capabilities. Capability identifiers are ConOps-level labels and are not Level 2 system use cases.

| Capability ID | Capability | Grounded Target Bound | Evidence |
| :--- | :--- | :--- | :--- |
| CAP-A | Expeditionary pneumatic launch and sortie execution | Launch pressure 13 bar to 14 bar; launch angle 12 deg; setup time 0 min to 5 min; rail length 5 m assembled and 1.28 m disassembled | [AH] |
| CAP-B | Navigation and multi-sensor state estimation | Cruise speed 30 m/s; maximum horizontal speed 38 m/s; minimum flight speed 26 m/s; pitot, GNSS, and dual magnetometer sources | [AI] |
| CAP-C | Resilient command and control datalink | Direct range 0 km to 60 km; extended range 60 km to 180 km; ground radio power 2 W; RF band 4.4 GHz to 5.0 GHz | [AJ] |
| CAP-D | Electro-optical and infrared seeker and target acquisition | Zoom 1X to 40X; pitch -45 deg to 135 deg; yaw and roll -165 deg to 165 deg; day and thermal resolution 1280x720; target track duration 2 s to 5 s | [AK] |
| CAP-E | Precision terminal effect and safety interlocks | Dive speed up to 55 m/s; dive angle up to 22 deg; engagement elevation up to 15 deg; engagement airspeed up to 55 m/s; warhead mass up to 5 kg; ESAD Critical / DAL-A | [AL] |

### 3.5 Operational Benefits Summary

1. **Runway-independent launch.** The PL-40 pneumatic launcher operates at 13 bar to 14 bar and a 12 deg launch angle, with a setup time of 0 min to 5 min and a rail that breaks down to 1.28 m [AH].
2. **Persistent coverage.** The air vehicle supports endurance up to 90 min at a 30 m/s cruise speed and a 300 m loiter radius [J].
3. **Standoff command and control.** The direct link is bounded at 60 km and the extended range band at 60 km to 180 km, using a 4.4 GHz to 5.0 GHz radio and a 23 dBi ground antenna [K].
4. **Precision identification.** The seeker provides 1X to 40X zoom, 1280x720 day and thermal imagery, and a 2 s to 5 s target track duration [L].
5. **Human-authorized weapon release.** The ESAD is classified Critical / DAL-A and weapon release remains subject to human judgment and fail-safe interlocks [M].
6. **Separated actuation.** Four Ruddervator (Fins; tail stabiliser) servos on CAN 1 and four wing servos on CAN 2 provide eight total servos on an 8 V rail [N].
7. **Containment assurance.** A 300 m loiter radius, a 50 m minimum mission waypoint altitude, and the cited containment and run-time assurance obligations provide the basis for volume containment [O].
8. **Configuration honesty.** The parachute deployment module is non-mission and excluded from the mission baseline, and the air vehicle environmental envelope is not quantified by the OEM sources [AE].

### 3.6 Source References

This specification is grounded in the schema files `schema/extracted/parametric_limits.md`, `schema/extracted/oem_bom.md`, `schema/extracted/interface_table.md`, and `.pipeline/schema.sysml`, and in the normative clauses ISO/IEC/IEEE 29148:2018 Section 6.4.2 and INCOSE SEH v5.0 Section 4.3.

| Clause | Source |
| :--- | :--- |
| ISO/IEC/IEEE 29148:2018 Section 6.4.2 | [RESEARCH_INVENTORY.md](docs/research/RESEARCH_INVENTORY.md) |
| ISO/IEC/IEEE 15288:2023 Section 6.4.3 | [RESEARCH_INVENTORY.md](docs/research/RESEARCH_INVENTORY.md) |
| INCOSE SEH v5.0 Section 4.3 | [oem_bom.md](schema/extracted/oem_bom.md) |
| ISO/IEC/IEEE 29148:2018 Section 8.4 | [schema.sysml](.pipeline/schema.sysml) |

- ISO/IEC/IEEE 29148:2018 Section 6.4.2 (ConOps): [RESEARCH_INVENTORY.md](docs/research/RESEARCH_INVENTORY.md)
- ISO/IEC/IEEE 15288:2023 Section 6.4.2 and Section 6.4.3 (requirements and architecture definition): [RESEARCH_INVENTORY.md](docs/research/RESEARCH_INVENTORY.md)
- INCOSE SEH v5.0 Section 3.3.1 and Section 4.3 (concept definition and architecture definition): [RESEARCH_INVENTORY.md](docs/research/RESEARCH_INVENTORY.md)
- DoD Directive 3000.09 Section 3.1, Section 3.1.a, Section 3.1.b, Section 3.1.c (human judgment and fail-safe interlocks): [RESEARCH_INVENTORY.md](docs/research/RESEARCH_INVENTORY.md)
- MIL-STD-882E Task 201 Section 4.2, Task 205 Section 4.2, Task 208 Section 4.2 (hazard analysis and thread isolation): [RESEARCH_INVENTORY.md](docs/research/RESEARCH_INVENTORY.md)
- MIL-STD-1629A Section 4.3 (severity classification): [RESEARCH_INVENTORY.md](docs/research/RESEARCH_INVENTORY.md)
- SAE ARP4761 Section 4.3.1 (functional hazard assessment): [RESEARCH_INVENTORY.md](docs/research/RESEARCH_INVENTORY.md)
- RTCA DO-178C Section 6.3.1 (software fault detection): [RESEARCH_INVENTORY.md](docs/research/RESEARCH_INVENTORY.md)
- ASTM F3269-17 Section 5.2 and Section 5.3 (run-time assurance): [RESEARCH_INVENTORY.md](docs/research/RESEARCH_INVENTORY.md)
- RTCA DO-362A Section 2.2, Section 2.2.1, Section 3.4 (C2 link availability and lost-link fallback): [RESEARCH_INVENTORY.md](docs/research/RESEARCH_INVENTORY.md)
- JARUS SORA v2.5 Annex E Section E.11, Section E.14, Section E.18 (ground support, containment, flight termination): [RESEARCH_INVENTORY.md](docs/research/RESEARCH_INVENTORY.md)
- AMC1 UAS.SPEC.050 Section 4.1 (site survey and geofence containment): [RESEARCH_INVENTORY.md](docs/research/RESEARCH_INVENTORY.md)
- MIL-STD-810H Method 501.7 Section 4.2, Method 502.7 Section 4.2, Method 506.6 Section 4.2, Method 521.4 Section 4.2 (environmental test methods): [RESEARCH_INVENTORY.md](docs/research/RESEARCH_INVENTORY.md)
- NIST SP 800-82r3 Section 6.2 (wireless and RF C2 security controls): [RESEARCH_INVENTORY.md](docs/research/RESEARCH_INVENTORY.md)
- ISO/SAE 21434 Section 6.4 (threat analysis and risk assessment): [RESEARCH_INVENTORY.md](docs/research/RESEARCH_INVENTORY.md)
- MIL-STD-461G Section 5.18 (radiated susceptibility): [RESEARCH_INVENTORY.md](docs/research/RESEARCH_INVENTORY.md)
- ISO/IEC/IEEE 29148:2018 Section 6.4.2 (ConOps parameter traceability): [parametric_limits.md](schema/extracted/parametric_limits.md)
- INCOSE SEH v5.0 Section 4.3 (architecture decomposition and component identity): [oem_bom.md](schema/extracted/oem_bom.md)
- ISO/IEC/IEEE 15288:2023 Section 6.4.3 (architecture definition and interface allocation): [interface_table.md](schema/extracted/interface_table.md)
- ISO/IEC/IEEE 29148:2018 Section 8.4 (system requirements traceability): [schema.sysml](.pipeline/schema.sysml)

| Clause | Source Reference |
| :--- | :--- |
| A | parametric_limits.md:12; avenger-5-spec-sheet-rev3.md:53; parametric_limits.md:7; a5-user-manual-2.md:307; parametric_limits.md:43; a5-user-manual-2.md:1497 |
| B | parametric_limits.md:13; a5-user-manual-2.md:315; parametric_limits.md:14; a5-user-manual-2.md:315 |
| C | parametric_limits.md:46-47; a5-user-manual-2.md:1329; parametric_limits.md:72; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:712; parametric_limits.md:78; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:722 |
| D | parametric_limits.md:9-10; a5-user-manual-2.md:309-310; parametric_limits.md:50-51; a5-user-manual-2.md:2056; a5-user-manual-2.md:2061; parametric_limits.md:49; a5-user-manual-2.md:2055; parametric_limits.md:19; avenger-5-spec-sheet-rev3.md:133 |
| E | RESEARCH_INVENTORY.md:18; DoD Directive 3000.09 Section 3.1, Section 3.1.a, Section 3.1.b |
| F | RESEARCH_INVENTORY.md:30; JARUS SORA v2.5 Annex E Section E.14, Section E.18; RESEARCH_INVENTORY.md:26; AMC1 UAS.SPEC.050 Section 4.1 |
| G | parametric_limits.md:79-80; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:723; parametric_limits.md:97-98; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:137 |
| H | RESEARCH_INVENTORY.md:21; NIST SP 800-82r3 Section 6.2; RESEARCH_INVENTORY.md:24; ISO/SAE 21434 Section 6.4; RESEARCH_INVENTORY.md:23; MIL-STD-461G Section 5.18 |
| I | parametric_limits.md:46-47; a5-user-manual-2.md:1329; parametric_limits.md:72; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:712; parametric_limits.md:78; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:722; parametric_limits.md:99-100; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:713-714; parametric_limits.md:75-77; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:715-717 |
| J | parametric_limits.md:12; avenger-5-spec-sheet-rev3.md:53; parametric_limits.md:7; a5-user-manual-2.md:307; parametric_limits.md:43; a5-user-manual-2.md:1497; parametric_limits.md:42; a5-user-manual-2.md:1195 |
| K | parametric_limits.md:13; a5-user-manual-2.md:315; parametric_limits.md:14; a5-user-manual-2.md:315; parametric_limits.md:45; a5-user-manual-2.md:1690; interface_table.md:63; oem_bom.md:75 |
| L | parametric_limits.md:31-37; a5-user-manual-2.md:324-328; parametric_limits.md:49; a5-user-manual-2.md:2055 |
| M | oem_bom.md:52; parametric_limits.md:69; esad-icd-excalibur-ab00-0054.md:438; parametric_limits.md:60-61; esad-icd-excalibur-ab00-0054.md:285; parametric_limits.md:64; esad-icd-excalibur-ab00-0054.md:330; parametric_limits.md:66; esad-icd-excalibur-ab00-0054.md:613 |
| N | parametric_limits.md:20-24; a5-user-manual-2.md:339; avenger_v2_5_sysml_v2_ingestion.md:21-31; parametric_limits.md:28; avenger_v2_5_sysml_v2_ingestion.md:79; interface_table.md:9-32 |
| O | parametric_limits.md:43; a5-user-manual-2.md:1497; parametric_limits.md:42; a5-user-manual-2.md:1195; parametric_limits.md:79-80; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:723; RESEARCH_INVENTORY.md:30; JARUS SORA v2.5 Annex E Section E.14; RESEARCH_INVENTORY.md:31; ASTM F3269-17 Section 5.2; RESEARCH_INVENTORY.md:26; AMC1 UAS.SPEC.050 Section 4.1 |
| P | parametric_limits.md:79-80; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:723; parametric_limits.md:97-98; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:137; RESEARCH_INVENTORY.md:39; MIL-STD-810H Method 501.7 Section 4.2, Method 502.7 Section 4.2, Method 506.6 Section 4.2, Method 521.4 Section 4.2 |
| Q | parametric_limits.md:11; a5-user-manual-2.md:311 |
| R | parametric_limits.md:71; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:719 |
| S | Derived from [Q] and [R] |
| T | parametric_limits.md:13; a5-user-manual-2.md:315 |
| U | parametric_limits.md:14; a5-user-manual-2.md:315 |
| V | Derived from [T] and [U] |
| W | parametric_limits.md:22; avenger_v2_5_sysml_v2_ingestion.md:22 |
| X | parametric_limits.md:23; avenger_v2_5_sysml_v2_ingestion.md:28 |
| Y | parametric_limits.md:24; avenger_v2_5_sysml_v2_ingestion.md:22; avenger_v2_5_sysml_v2_ingestion.md:31 |
| Z | parametric_limits.md:71; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:719; parametric_limits.md:11; a5-user-manual-2.md:311; parametric_limits.md:46-47; a5-user-manual-2.md:1329; parametric_limits.md:73; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:132 |
| AA | parametric_limits.md:13; a5-user-manual-2.md:315; parametric_limits.md:14; a5-user-manual-2.md:315; interface_table.md:63; parametric_limits.md:45; a5-user-manual-2.md:1690 |
| AB | parametric_limits.md:12; avenger-5-spec-sheet-rev3.md:53; parametric_limits.md:18; a5-user-manual-2.md:299; parametric_limits.md:29-30; avenger_v2_5_sysml_v2_ingestion.md:16; parametric_limits.md:82; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:134 |
| AC | parametric_limits.md:20-24; a5-user-manual-2.md:339; avenger_v2_5_sysml_v2_ingestion.md:21-31; parametric_limits.md:28; avenger_v2_5_sysml_v2_ingestion.md:79; interface_table.md:9-32 |
| AD | oem_bom.md:52; parametric_limits.md:69; esad-icd-excalibur-ab00-0054.md:438; parametric_limits.md:60-63; esad-icd-excalibur-ab00-0054.md:285; esad-icd-excalibur-ab00-0054.md:306-307; parametric_limits.md:64; esad-icd-excalibur-ab00-0054.md:330; parametric_limits.md:66; esad-icd-excalibur-ab00-0054.md:613; RESEARCH_INVENTORY.md:18; DoD Directive 3000.09 Section 3.1.b |
| AE | oem_bom.md:47; oem_bom.md:48-49 |
| AF | parametric_limits.md:31-37; a5-user-manual-2.md:324-328; parametric_limits.md:9-10; a5-user-manual-2.md:309-310; parametric_limits.md:50; a5-user-manual-2.md:2056 |
| AG | parametric_limits.md:79-80; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:723; parametric_limits.md:97-98; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:137; RESEARCH_INVENTORY.md:39; MIL-STD-810H Method 501.7 Section 4.2, Method 502.7 Section 4.2, Method 506.6 Section 4.2, Method 521.4 Section 4.2 |
| AH | parametric_limits.md:46-47; a5-user-manual-2.md:1329; parametric_limits.md:72; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:712; parametric_limits.md:78; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:722; parametric_limits.md:99-100; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:713-714 |
| AI | parametric_limits.md:7-8; a5-user-manual-2.md:307-308; parametric_limits.md:11; a5-user-manual-2.md:311; oem_bom.md:15; oem_bom.md:39; oem_bom.md:40-41 |
| AJ | parametric_limits.md:13; a5-user-manual-2.md:315; parametric_limits.md:14; a5-user-manual-2.md:315; parametric_limits.md:45; a5-user-manual-2.md:1690; interface_table.md:63; oem_bom.md:75 |
| AK | parametric_limits.md:31-37; a5-user-manual-2.md:324-328; parametric_limits.md:49; a5-user-manual-2.md:2055 |
| AL | parametric_limits.md:9-10; a5-user-manual-2.md:309-310; parametric_limits.md:19; avenger-5-spec-sheet-rev3.md:133; parametric_limits.md:50-51; a5-user-manual-2.md:2056; a5-user-manual-2.md:2061; oem_bom.md:52 |
