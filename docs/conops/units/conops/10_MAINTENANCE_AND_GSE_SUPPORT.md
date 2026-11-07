| Attribute | Specification Detail |
| :--- | :--- |
| **Title** | Maintenance & Sustainment Concepts (O/I/D Maintenance) |
| **Version** | 1.1.0 |
| **Date** | 2026-10-31 |
| **issue_id** | 124 |
| **type** | conops |
| **generation_mode** | manual |
| **specification_source** | docs/conops/units/conops/10_MAINTENANCE_AND_GSE_SUPPORT.md |
| **Traceability References** | #124, #140, #141 |

## 10. Maintenance & Sustainment Concepts (O/I/D Maintenance)

### 10.1 Three-Tier Maintenance Model (O-Level, I-Level, D-Level)

Sustainment is partitioned into Organizational (O-Level), Intermediate (I-Level), and Depot (D-Level) tiers in accordance with ISO/IEC/IEEE 29148:2018 Section 6.4.2, INCOSE SEH v5.0 Section 3.3.1, JARUS SORA v2.5 Annex E Section E.3, and MIL-STD-882E Task 205 Section 4.2. The Ruddervator is the canonical tail control surface assembly, quantity of 4 units (oem_bom.md:23; schema/extracted/parametric_limits.md PL-14). The ESAD is classified Critical (DAL-A) (oem_bom.md:52). The parachute deployment module is a non-mission configuration with baseline false and is excluded from the sustainment baseline (oem_bom.md:47).

| Tier | Location and Ownership | Authorized Maintenance Scope | Grounding |
| :--- | :--- | :--- | :--- |
| **O-Level (Organizational)** | Operating base or field staging area; certified Maintenance Technician | Pre-operation and post-operation visual inspection; RBF device removal and installation; removable battery exchange; ESD grounding; pre-flight battery voltage and pitot checks | oem_bom.md:18, oem_bom.md:69, oem_bom.md:70; schema/extracted/parametric_limits.md PL-32, PL-33, PL-34, PL-35 |
| **I-Level (Intermediate)** | Regional maintenance shelter or field workshop | Line Replaceable Unit exchange for avionics, radio, camera, gimbal, and servo modules; sensor alignment; firmware and cryptographic key rollover | oem_bom.md:12, oem_bom.md:13, oem_bom.md:14, oem_bom.md:15, oem_bom.md:42, oem_bom.md:43, oem_bom.md:44; NIST SP 800-82r3 Section 6.2 |
| **D-Level (Depot / Factory)** | Centralized factory or certified depot overhaul center | Structural non-destructive inspection; motor and ESC overhaul; ESAD recertification; complete system certification | oem_bom.md:21, oem_bom.md:22, oem_bom.md:52; MIL-STD-1629A Section 4.3 |

#### 10.1.1 Grounded Maintenance Intervals

| Maintenance Item | Interval or Limit | Grounding |
| :--- | :--- | :--- |
| PL-40 pulling rope replacement | At most 100 launches | schema/extracted/parametric_limits.md PL-80; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:138 |
| PL-40 battery charge time, DC18RC charger | 0 min to 55 min | schema/extracted/parametric_limits.md PL-89; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:137 |
| PL-40 battery charge time, DC18SD charger | 0 min to 130 min | schema/extracted/parametric_limits.md PL-90; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:137 |
| PL-40 battery charging temperature | 10 C to 40 C | schema/extracted/parametric_limits.md PL-91 and PL-92; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:137 |
| PL-40 battery over-discharge cutoff | 14.5 V | schema/extracted/parametric_limits.md PL-77; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:135 |
| PL-40 battery over-discharge recovery | 16 V after a 5 s delay | schema/extracted/parametric_limits.md PL-78 and PL-79; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:136 |
| UAV battery pre-flight voltage window | 49 V to 50 V | schema/extracted/parametric_limits.md PL-32 and PL-33; a5-user-manual-2.md:1366 |
| Pitot static airspeed limit | 0 m/s to 3 m/s | schema/extracted/parametric_limits.md PL-34; a5-user-manual-2.md:1368 |
| Pitot blow-test airspeed | At least 10 m/s | schema/extracted/parametric_limits.md PL-35; a5-user-manual-2.md:1369 |
| Air vehicle phase inspection interval | Not stated in OEM sources | oem_bom.md and schema/extracted/parametric_limits.md contain no airframe phase interval |
| Ruddervator servo overhaul interval | Not stated in OEM sources | oem_bom.md and schema/extracted/parametric_limits.md contain no servo overhaul interval |
| ESAD recertification interval | Not stated in OEM sources | oem_bom.md and schema/extracted/parametric_limits.md contain no ESAD recertification interval |
| UAV battery cycle-life replacement interval | Not stated in OEM sources | oem_bom.md and schema/extracted/parametric_limits.md contain no battery cycle-life interval |

#### 10.1.2 Organizational-Level (O-Level) Maintenance Scope

- **Pre-operation and post-operation inspection:** Verify the fuselage assembly with hatches closed and vertical stabilizer attached, the four wing surfaces secured with M6 x 30 mm bolts, the Ruddervator assembly with four tail mounting shafts, and all RBF devices including the pitot cover, sensor cover, gimbal strap, power RBF key, and warhead RBF key (oem_bom.md:31, oem_bom.md:67, oem_bom.md:70).
- **Battery exchange:** Remove and install the removable 12S2P Li metal battery through its retaining strap and locking connector; the battery supplies 36 V to 50.4 V DC main power (oem_bom.md:18; schema/extracted/parametric_limits.md PL-23 and PL-24).
- **ESD control:** Equalize electrostatic charge at the ESD grounding point marked by a yellow label before touching avionics or ESAD connectors (oem_bom.md:69).
- **Pre-flight electrical and pitot checks:** Confirm the UAV battery pre-flight voltage window of 49 V to 50 V, the pitot static airspeed limit of 0 m/s to 3 m/s, and the pitot blow-test airspeed of at least 10 m/s (schema/extracted/parametric_limits.md PL-32, PL-33, PL-34, PL-35; a5-user-manual-2.md:1366, a5-user-manual-2.md:1368, a5-user-manual-2.md:1369).
- **Power-on built-in test duration:** Not stated in OEM sources.

#### 10.1.3 Intermediate-Level (I-Level) Maintenance Scope

- **Line Replaceable Unit exchange:** Replace the autopilot computing board Cube Orange Plus, EPS module, ETH switch, RPI CM5004032, GNSS module Septentrio Asterx-m3 pro, radio module DTC, camera compute module Trip6, and gimbal Nighthawk2UZ (oem_bom.md:12, oem_bom.md:13, oem_bom.md:14, oem_bom.md:15, oem_bom.md:42, oem_bom.md:43, oem_bom.md:44).
- **Servo exchange:** Replace Ruddervator Servos #1 to #4 on the four CAN 1 branches of 120 cm and Wing Servos #5 to #8 on the CAN 2 daisy chain; the air vehicle carries 8 servos in total (schema/extracted/parametric_limits.md PL-16, PL-17, PL-18, PL-21; oem_bom.md:24, oem_bom.md:27, oem_bom.md:35, oem_bom.md:38).
- **Bus restoration checks:** Verify the CAN 1 trunk of 970 cm, the CAN 1 branch of 150 cm, and the four CAN 1 stubs of 120 cm after harness or servo work (schema/extracted/parametric_limits.md PL-19, PL-20, PL-21; schema/extracted/interface_table.md at line 9, schema/extracted/interface_table.md at line 11).
- **Servo power verification:** Confirm the 8 V DC servo power rail after EPS or CAN power distribution board maintenance (schema/extracted/parametric_limits.md PL-22; schema/extracted/interface_table.md at line 16).
- **Firmware and cryptographic key rollover:** Apply configuration-managed firmware updates and cryptographic key rollover in accordance with NIST SP 800-82r3 Section 6.2; the OEM rollover interval is Not stated in OEM sources.
- **Sensor alignment tolerance:** Not stated in OEM sources.

#### 10.1.4 Depot-Level (D-Level) Maintenance Scope

- **Structural non-destructive inspection:** The OEM sources do not state an inspection method, interval, or acceptance threshold; all such values are Not stated in OEM sources.
- **Propulsion overhaul:** The propulsion chain comprises the ESC IBEX160 and the Motor AXI 5345/16 HD GOLD LINE V3; the OEM overhaul interval is Not stated in OEM sources (oem_bom.md:21, oem_bom.md:22).
- **ESAD recertification:** The ESAD is Critical (DAL-A) and all ESAD ICD rows carry prototype-reference and Derived status; depot recertification is mandatory before return to service, and the recertification interval is Not stated in OEM sources (oem_bom.md:52).
- **Parachute deployment module:** The module is a non-mission configuration with baseline false; it is excluded from the depot sustainment baseline (oem_bom.md:47).
- **Battery depot capacity test and cycle replacement:** Not stated in OEM sources.

### 10.2 Ground Support Equipment (GSE) Support

The GSE baseline is bounded by JARUS SORA v2.5 Annex E Section E.11 (Ground Support Equipment and Launch/Recovery Maintenance) and MIL-STD-882E Task 205 Section 4.2. Only GSE items present in the OEM sources are listed; any GSE capability absent from those sources is marked Not stated in OEM sources.

#### 10.2.1 PL-40 Pneumatic Catapult Launcher

| GSE Item | Grounded Specification | Grounding |
| :--- | :--- | :--- |
| PL-40 Rail assembly | Mass 68 kg; rail length 5 m assembled and 1.28 m disassembled | schema/extracted/parametric_limits.md PL-69, PL-93, PL-94; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:715, uav_launcher_pl_40_sysml_v2_ingestion_manual.md:713, uav_launcher_pl_40_sysml_v2_ingestion_manual.md:714 |
| PL-40 Transport Case | Mass 43 kg | schema/extracted/parametric_limits.md PL-70; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:716 |
| PL-40 Compressor Unit | Mass 25 kg | schema/extracted/parametric_limits.md PL-71; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:717 |
| Launched air vehicle envelope | Maximum launched plane mass 30 kg; maximum launch velocity 25 m/s; launch angle 12 deg | schema/extracted/parametric_limits.md PL-64, PL-65, PL-66; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:718, uav_launcher_pl_40_sysml_v2_ingestion_manual.md:719, uav_launcher_pl_40_sysml_v2_ingestion_manual.md:712 |
| Pneumatic pressure envelope | Maximum compressor working pressure 14 bar; auxiliary filling pressure 16 bar | schema/extracted/parametric_limits.md PL-67 and PL-68; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:132, uav_launcher_pl_40_sysml_v2_ingestion_manual.md:133 |
| Launcher operating temperature | -20 C to +50 C | schema/extracted/parametric_limits.md PL-73 and PL-74; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:723 |
| Launcher setup time | 0 min to 5 min | schema/extracted/parametric_limits.md PL-72; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:722 |
| Trigger hold time | At least 2 s | schema/extracted/parametric_limits.md PL-88; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:530 |
| Launcher battery | Makita 18 V Li-Ion 6000 mAh battery, quantity of 2 units | schema/extracted/parametric_limits.md PL-75 and PL-76; oem_bom.md:99; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:39 |
| Pulling rope | High-strength pulling rope from piston to carriage; replacement at most every 100 launches | schema/extracted/parametric_limits.md PL-80; oem_bom.md:86; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:13 |
| Carriage geometry | Overall length 271 mm; lever tip span 206.5 mm; overall height 232.5 mm | schema/extracted/parametric_limits.md PL-81, PL-82, PL-83; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:142 |
| Launcher center-of-mass envelope | 0 mm to 200 mm longitudinal; 0 mm to 100 mm normal | schema/extracted/parametric_limits.md PL-84 and PL-85; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:144 |
| Launcher installed geometry | Overall height 1115 mm; front bipod stance width 602 mm | schema/extracted/parametric_limits.md PL-86 and PL-87; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:143 |
| Launcher maintenance kits | Pulling rope replacement kit and carriage wheel bearing replacement kit | oem_bom.md:103; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:53, uav_launcher_pl_40_sysml_v2_ingestion_manual.md:54 |
| Wheel bearing preheat temperature | Not stated in OEM sources | No value appears in oem_bom.md or schema/extracted/parametric_limits.md |
| Wheel bearing relubrication interval | Not stated in OEM sources | No value appears in oem_bom.md or schema/extracted/parametric_limits.md |

The PL-40 launcher set further comprises the rear, middle, and front rail modules, the carriage with four support levers, the red-handled carriage safety lock pin, the compressor unit, main tank, remote release valve, pressure gauge, power switching circuit, trigger handle, connection hose, three ground anchors, transport case, and hook options A, B, and C (oem_bom.md:82 to oem_bom.md:102). The launcher pneumatic supply is delivered at a maximum of 14 bar and the trigger handle receives 18 V DC (schema/extracted/interface_table.md at line 60, schema/extracted/interface_table.md at line 62; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:132, uav_launcher_pl_40_sysml_v2_ingestion_manual.md:81).

#### 10.2.2 Battery Support Equipment

| Battery | Grounded Specification | Grounding |
| :--- | :--- | :--- |
| UAV Battery 12S2P Li Metal BEI | Removable 12S2P Li metal battery with retaining strap and locking connector; 36 V to 50.4 V DC main power | oem_bom.md:18; schema/extracted/parametric_limits.md PL-23 and PL-24 |
| PL-40 Launcher Battery | Makita BL1860B 18 V Li-Ion 6000 mAh, quantity of two units; over-discharge cutoff 14.5 V; recovery 16 V after a 5 s delay | oem_bom.md:99; schema/extracted/parametric_limits.md PL-75, PL-76, PL-77, PL-78, PL-79 |
| GCS Battery | Ground control station battery, quantity of 2 units | oem_bom.md:77; a5-user-manual-2.md:350 |
| UAV battery charge rate and charge time | Not stated in OEM sources | No value appears in oem_bom.md or schema/extracted/parametric_limits.md |
| UAV battery storage humidity and temperature | Not stated in OEM sources | No value appears in oem_bom.md or schema/extracted/parametric_limits.md |

#### 10.2.3 Tools, Spares, and Maintenance Kits

- **Support Tools:** The OEM support package includes a set of tools and 30 spare attachment bolts (oem_bom.md:81; a5-user-manual-2.md:365, a5-user-manual-2.md:368). The 30 spare attachment bolts cover the M6 x 30 mm wing surface fasteners (oem_bom.md:31).
- **Support Spare Propeller:** The OEM support package includes 2 spare propeller blades and 1 propeller assembly (oem_bom.md:80; a5-user-manual-2.md:366, a5-user-manual-2.md:367).
- **PL-40 Maintenance Kits:** The launcher maintenance kit comprises the pulling rope replacement kit and the carriage wheel bearing replacement kit (oem_bom.md:103; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:53, uav_launcher_pl_40_sysml_v2_ingestion_manual.md:54).
- **Calibrated torque values for airframe fasteners:** Not stated in OEM sources.
- **ESD wrist strap, connector pin extraction tools, lens cleaning kits, and diagnostic bus analyzers:** Not stated in OEM sources; the only grounded ESD item is the yellow-label ESD grounding point (oem_bom.md:69).
- **GSE calibration interval and metrological traceability:** Not stated in OEM sources.

### 10.3 Sustainment Constraints

- **Mass and payload limits:** The maximum take-off weight is 17 kg, the warhead mass is 5 kg, and the maximum launched plane mass is 30 kg (schema/extracted/parametric_limits.md PL-12, PL-13, PL-64; a5-user-manual-2.md:299, avenger-5-spec-sheet-rev3.md:133, uav_launcher_pl_40_sysml_v2_ingestion_manual.md:718).
- **Launch pressure limits:** The catapult launch pressure is 13 bar to 14 bar, the maximum compressor working pressure is 14 bar, and the auxiliary filling pressure is 16 bar (schema/extracted/parametric_limits.md PL-40, PL-41, PL-67, PL-68; a5-user-manual-2.md:1329, uav_launcher_pl_40_sysml_v2_ingestion_manual.md:132, uav_launcher_pl_40_sysml_v2_ingestion_manual.md:133).
- **Thermal limits:** The PL-40 launcher operating temperature is -20 C to +50 C, and the PL-40 battery charging temperature is 10 C to 40 C (schema/extracted/parametric_limits.md PL-73, PL-74, PL-91, PL-92; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:723, uav_launcher_pl_40_sysml_v2_ingestion_manual.md:137). The air vehicle storage and operating temperature limits are Not stated in OEM sources.
- **C2 link constraint:** The GCS-to-UAV telemetry and command link operates in the 4.4 GHz to 5.0 GHz band, and the ground radio output setting is 2 W (schema/extracted/interface_table.md at line 63; schema/extracted/parametric_limits.md PL-39; a5-user-manual-2.md:1273, a5-user-manual-2.md:1690).
- **ESAD handling constraints:** The ESAD is Critical (DAL-A); its umbilical continuity is 0 Ohm to 0.5 Ohm at 20 mA, its arm enable uses a 1 ms period at 50 percent duty, its RS-485 link runs at 115200 bps with a 100 Hz command interval, and its high-voltage measurement range is 0 V to 1800 V (oem_bom.md:52; schema/extracted/parametric_limits.md PL-49, PL-50, PL-54, PL-55, PL-56, PL-57, PL-60); its arm enable levels are specified in VDC as 0 VDC to 0.7 VDC low and 2.5 VDC to 3.3 VDC high (schema/extracted/parametric_limits.md PL-51, PL-52, PL-53).
- **Ruddervator and wing servo constraints:** The Ruddervator uses four servos on the first CAN bus and the wings use four servos on the second CAN bus, for eight servos in total; all servo power is supplied by the 8 V DC rail (schema/extracted/parametric_limits.md PL-14, PL-16, PL-17, PL-18, PL-22; oem_bom.md:23, oem_bom.md:28).
- **Parachute exclusion:** The parachute deployment module is a non-mission configuration with baseline false and imposes no sustainment constraint on the mission baseline (oem_bom.md:47).
- **Spares constraint:** Sustained operations depend on the 30 spare attachment bolts, 2 spare propeller blades, and 1 propeller assembly listed in the OEM support package (oem_bom.md:80, oem_bom.md:81; a5-user-manual-2.md:365, a5-user-manual-2.md:366, a5-user-manual-2.md:367, a5-user-manual-2.md:368).
- **Maintenance interval ceiling:** The only OEM-stated recurring maintenance interval is the PL-40 pulling rope replacement at most every 100 launches; all other recurring intervals are Not stated in OEM sources (schema/extracted/parametric_limits.md PL-80; uav_launcher_pl_40_sysml_v2_ingestion_manual.md:138).

## Source References

Source citations: schema/extracted/oem_bom.md at line 9; schema/extracted/parametric_limits.md at line 7; schema/extracted/interface_table.md at line 9; docs/research/RESEARCH_INVENTORY.md at line 16; .pipeline/schema.sysml; ISO/IEC/IEEE 29148:2018 Section 6.4.2; JARUS SORA v2.5 Annex E Section E.11
