| Attribute | Specification Detail |
| :--- | :--- |
| **Title** | Tactical Mission Intent: Gate 24 Operational Allocation Tags |
| **Version** | 1.0.0 |
| **Date** | 2026-09-02 |
| **Issue ID** | MI-10 |
| **Type** | Mission Intent |
| **Generation Mode** | Deterministic |
| **Specification Source** | `.pipeline/schema.sysml` |

## 10. Gate 24 MissionTask Traceability Tags (Operational Allocation Tags)

In accordance with INCOSE Systems Engineering Handbook v5.0 Section 5.4 (System Verification, Validation & Digital Thread Traceability) and the DEAP Gate 24 Architecture Traceability standard, this unit registers the complete set of operational allocation tags that bind every Level 1B Mission Essential Task (`MET-01` through `MET-09`) to its downstream SysML v2 structural block, interface anchor, safety criticality, and verification evidence artifact.

Each register entry carries the machine-readable allocation directive `/// OperationalAllocation: [MET-XX]`. The directive is the operational allocation (OA) link consumed by the Gate 24 traceability scanner; it is reproduced verbatim in the register and in the cross-model allocation matrix so that no tag exists without a mapping row and no mapping row exists without a tag.

### 10.1 Gate 24 Operational Allocation Tag Register

- `/// OperationalAllocation: [MET-01]` -- PreFlightSystemCheckout allocates to the Autopilot Stack Module, Autopilot Computing Board, EPS Module, and GCS equipment; governing endurance ceiling 90 min (PL-06).
- `/// OperationalAllocation: [MET-02]` -- AutonomousIngressTransit allocates to the Autopilot Stack Module, all four Ruddervator servos (PL-16), EPS Servo Power 8V Rail (8 V, PL-22), and Propulsion; governing cruise speed 30 m/s (PL-01) and maximum horizontal speed 38 m/s (PL-02).
- `/// OperationalAllocation: [MET-03]` -- AreaSurveillanceOrbit allocates to the Gimbal Nighthawk2UZ, Camera Compute Module Trip6, RPI CM5004032, and Autopilot Stack Module; governing loiter radius 300 m (PL-37) and minimum waypoint altitude 50 m (PL-36).
- `/// OperationalAllocation: [MET-04]` -- DynamicAirspaceDeconfliction allocates to the GNSS Module and Antenna, Pitot Tube, Magnetometers, Autopilot Stack Module, and Ruddervator; governing RLOS direct range 60 km (PL-07) and RLOS extended range 180 km (PL-08).
- `/// OperationalAllocation: [MET-05]` -- ElectronicCounterCountermeasures allocates to the Radio Module DTC, Radio Antennas MPSL4400, RPI CM5004032, and Autopilot Stack Module; C2 link medium is RF 4.4 to 5.0 GHz (interface_table.md:63-64).
- `/// OperationalAllocation: [MET-06]` -- PrecisionTargetMensuration allocates to the Gimbal Nighthawk2UZ, Camera Compute Module Trip6, and Autopilot Stack Module; governing target track duration 2 s to 5 s (PL-42, PL-43), maximum engagement elevation 15 deg (PL-44), and maximum engagement airspeed 55 m/s (PL-45).
- `/// OperationalAllocation: [MET-07]` -- AutonomousBingoReturnDivert allocates to the Battery 12S2P Li Metal BEI (36 V to 50.4 V, PL-23, PL-24), Power Meter, ESC IBEX160, Motor AXI propulsion motor, Propulsion, and Autopilot Stack Module; governing flight endurance 90 min (PL-06) and maximum dive angle 22 deg (PL-04).
- `/// OperationalAllocation: [MET-08]` -- PostMissionDataOffloadShutdown allocates to the GCS Radio Box, GCS Tablet FZ-G2, External Interface Board USB ETH, RPI CM5004032, and Autopilot Stack Module; GCS ground radio power is 2 W (PL-39).
- `/// OperationalAllocation: [MET-09]` -- DownedVehicleContainmentAntiTamper allocates to the ESAD (Critical, DAL-A), ESAD Sensor Board, ESAD Detonator, Proximity Sensor, Warhead, Lethal Package, ESAD RBF Key, UAV RBF Key, and Safety RBF Devices; ESAD power input is 14 V to 32 V (PL-46, PL-47), RS-485 command interval is 100 Hz (PL-57), and detonator high voltage is up to 1800 V (PL-60). The Parachute Deployment Non-Mission assembly is excluded from the mission baseline (configuration: non-mission; baseline: false) per `schema/extracted/oem_bom.md at line 5,47`.

### 10.2 Cross-Model Architecture Allocation Matrix

| Task ID | MET Task Name | OperationalAllocation OA Link | Allocated System Subsystem | SysML v2 Allocation Block | Governing Level 0 Parameter | Safety Criticality (DAL) | Verification Evidence Artifact |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `MET-01` | PreFlightSystemCheckout | `/// OperationalAllocation: [MET-01]` | Autopilot Stack Module; Autopilot Computing Board; EPS Module; GCS Radio Box; GCS Tablet FZ-G2 | `extracted::Autopilot_Stack_Module_ASTK_A5_V2_5`; `extracted::Autopilot_Computing_Board_Cube_Orange_Plus`; `extracted::EPS_Module`; `extracted::GCS_Radio_Box`; `extracted::GCS_Tablet_FZ_G2` | PL-06 endurance 90 min (`schema/extracted/parametric_limits.md at line 12`) | Not stated in OEM sources | `./target/release/verify-baseline` |
| `MET-02` | AutonomousIngressTransit | `/// OperationalAllocation: [MET-02]` | Autopilot Stack Module; Ruddervator Servos #1 to #4; EPS Servo Power 8V Rail; Propulsion | `extracted::Autopilot_Stack_Module_ASTK_A5_V2_5`; `extracted::Ruddervator_Servo_1`; `extracted::Ruddervator_Servo_2`; `extracted::Ruddervator_Servo_3`; `extracted::Ruddervator_Servo_4`; `extracted::EPS_Servo_Power_8V_Rail`; `extracted::Propulsion` | PL-01 cruise speed 30 m/s (`schema/extracted/parametric_limits.md at line 7`); PL-02 maximum horizontal speed 38 m/s (`schema/extracted/parametric_limits.md at line 8`); PL-22 servo rail 8 V (`schema/extracted/parametric_limits.md at line 28`) | Not stated in OEM sources | `./target/release/compile-sysml` |
| `MET-03` | AreaSurveillanceOrbit | `/// OperationalAllocation: [MET-03]` | Gimbal Nighthawk2UZ; Camera Compute Module Trip6; RPI CM5004032; Autopilot Stack Module | `extracted::Gimbal_Nighthawk2UZ`; `extracted::Camera_Compute_Module_Trip6`; `extracted::RPI_CM5004032`; `extracted::Autopilot_Stack_Module_ASTK_A5_V2_5` | PL-37 loiter radius 300 m (`schema/extracted/parametric_limits.md at line 43`); PL-36 minimum waypoint altitude 50 m (`schema/extracted/parametric_limits.md at line 42`) | Not stated in OEM sources | `./target/release/compile-sysml` |
| `MET-04` | DynamicAirspaceDeconfliction | `/// OperationalAllocation: [MET-04]` | GNSS Module; GNSS Antenna; Pitot Tube; Magnetometers; Autopilot Stack Module; Ruddervator | `extracted::GNSS_Module_Septentrio_Asterx_m3_pro`; `extracted::GNSS_Antenna_Talysman_TW3972EXF`; `extracted::Pitot_Tube_CUAV_SKYE2`; `extracted::Magnetometer_mRo_RM3100_Upper`; `extracted::Magnetometer_mRo_RM3100_Lower`; `extracted::Autopilot_Stack_Module_ASTK_A5_V2_5`; `extracted::Ruddervator` | PL-07 RLOS direct range 60 km (`schema/extracted/parametric_limits.md at line 13`); PL-08 RLOS extended range 180 km (`schema/extracted/parametric_limits.md at line 14`) | Not stated in OEM sources | `./target/release/compile-sysml` |
| `MET-05` | ElectronicCounterCountermeasures | `/// OperationalAllocation: [MET-05]` | Radio Module DTC; Radio Antennas MPSL4400; RPI CM5004032; Autopilot Stack Module | `extracted::Radio_Module_DTC`; `extracted::Radio_Antenna_MPSL4400_Upper`; `extracted::Radio_Antenna_MPSL4400_Lower`; `extracted::RPI_CM5004032`; `extracted::Autopilot_Stack_Module_ASTK_A5_V2_5` | RF 4.4 to 5.0 GHz link medium (`schema/extracted/interface_table.md at line 63-64`) | Not stated in OEM sources | `./target/release/verify-baseline` |
| `MET-06` | PrecisionTargetMensuration | `/// OperationalAllocation: [MET-06]` | Gimbal Nighthawk2UZ; Camera Compute Module Trip6; Autopilot Stack Module | `extracted::Gimbal_Nighthawk2UZ`; `extracted::Camera_Compute_Module_Trip6`; `extracted::Autopilot_Stack_Module_ASTK_A5_V2_5` | PL-42 target track minimum 2 s (`schema/extracted/parametric_limits.md at line 48`); PL-43 target track maximum 5 s (`schema/extracted/parametric_limits.md at line 49`); PL-44 maximum engagement elevation 15 deg (`schema/extracted/parametric_limits.md at line 50`); PL-45 maximum engagement airspeed 55 m/s (`schema/extracted/parametric_limits.md at line 51`) | Not stated in OEM sources | `./target/release/compile-sysml` |
| `MET-07` | AutonomousBingoReturnDivert | `/// OperationalAllocation: [MET-07]` | Battery 12S2P Li Metal BEI; Power Meter; ESC IBEX160; Motor AXI propulsion motor; Propulsion; Autopilot Stack Module | `extracted::Battery_12S2P_Li_Metal_BEI`; `extracted::Power_Meter`; `extracted::ESC_IBEX160`; `extracted::Motor_AXI_5345_16_HD_GOLD_LINE_V3`; `extracted::Propulsion`; `extracted::Autopilot_Stack_Module_ASTK_A5_V2_5` | PL-06 endurance 90 min (`schema/extracted/parametric_limits.md at line 12`); PL-23 battery minimum 36 V (`schema/extracted/parametric_limits.md at line 29`); PL-24 battery maximum 50.4 V (`schema/extracted/parametric_limits.md at line 30`); PL-04 maximum dive angle 22 deg (`schema/extracted/parametric_limits.md at line 10`) | Not stated in OEM sources | `./target/release/verify-baseline` |
| `MET-08` | PostMissionDataOffloadShutdown | `/// OperationalAllocation: [MET-08]` | GCS Radio Box; GCS Tablet FZ-G2; External Interface Board USB ETH; RPI CM5004032; Autopilot Stack Module | `extracted::GCS_Radio_Box`; `extracted::GCS_Tablet_FZ_G2`; `extracted::External_Interface_Board_USB_ETH`; `extracted::RPI_CM5004032`; `extracted::Autopilot_Stack_Module_ASTK_A5_V2_5` | PL-39 ground radio power 2 W (`schema/extracted/parametric_limits.md at line 45`) | Not stated in OEM sources | `./target/release/verify-baseline` |
| `MET-09` | DownedVehicleContainmentAntiTamper | `/// OperationalAllocation: [MET-09]` | ESAD; ESAD Sensor Board; ESAD Detonator; Proximity Sensor; Warhead; Lethal Package; ESAD RBF Key; UAV RBF Key; Safety RBF Devices | `extracted::ESAD`; `extracted::ESAD_Sensor_Board`; `extracted::ESAD_Detonator`; `extracted::Proximity_Sensor`; `extracted::Warhead`; `extracted::Lethal_Package`; `extracted::ESAD_RBF_Key`; `extracted::UAV_RBF_Key`; `extracted::Safety_RBF_Devices` | PL-46 ESAD power input minimum 14 V (`schema/extracted/parametric_limits.md at line 52`); PL-47 ESAD power input maximum 32 V (`schema/extracted/parametric_limits.md at line 53`); PL-57 ESAD command interval 100 Hz (`schema/extracted/parametric_limits.md at line 63`); PL-60 detonator high voltage up to 1800 V (`schema/extracted/parametric_limits.md at line 66`) | DAL-A (Critical) per `schema/extracted/oem_bom.md at line 52` | `./target/release/verify-baseline` |

### 10.3 Allocation Coverage, Canonical Naming & Orphan Audit

| Audit Item | Result | Evidence |
| :--- | :--- | :--- |
| Registered allocation tags | 9 (`MET-01` through `MET-09`) | Section 10.1 register |
| Matrix mapping rows | 9 | Section 10.2 matrix |
| Orphan tags (tag without matrix row) | 0 | One-to-one `MET-XX` parity between Section 10.1 and Section 10.2 |
| Orphan rows (matrix row without tag) | 0 | One-to-one `MET-XX` parity between Section 10.1 and Section 10.2 |
| Canonical tail control surface naming | `Ruddervator` | `schema/extracted/oem_bom.md at line 23` identifies Ruddervator as the canonical assembly name; `Fins` is a drawing synonym and `tail stabiliser` is a preparation synonym, neither of which is used as an allocation target |
| Mission-baseline exclusions | `Parachute_Deployment_Non_Mission`, `Parachute_Igniter_1`, `Parachute_Igniter_2` | `schema/extracted/oem_bom.md at line 5,47-49` declare the parachute assembly configuration: non-mission and baseline: false; these parts are not allocated to any `MET-XX` task |
| Safety-critical allocation | `ESAD` only, Critical / DAL-A | `schema/extracted/oem_bom.md at line 52` |

All allocation targets are declared `part def` nodes in `.pipeline/schema.sysml`; the `extracted::` qualification in Section 10.2 is the AST package path rooted at `package extracted` (`.pipeline/schema.sysml:2`). No allocation target is invented and no declared mission task is left without a structural binding.

### 10.4 OEM-Silent Fields

The following fields are not stated in the six cited OEM sources and are therefore recorded as "Not stated in OEM sources" rather than estimated:

| Field | Status | Evidence |
| :--- | :--- | :--- |
| Component mass for all BOM rows | Not stated in OEM sources | `schema/extracted/oem_bom.md at line 5` and the `Mass (kg)` column of every BOM row |
| Component power draw for all BOM rows | Not stated in OEM sources | `schema/extracted/oem_bom.md at line 5` and the `Power (W)` column of every BOM row |
| Interface refresh rate for CAN bus, UART, and USB links | Not stated in OEM sources | `schema/extracted/interface_table.md at line 9-15,28-32,37-44` |
| DAL for subsystems other than the ESAD | Not stated in OEM sources | `schema/extracted/oem_bom.md at line 9-103` assigns no DAL to non-ESAD rows; DAL-A is stated only for the ESAD at line 52 |
| UAV ambient operating temperature envelope | Not stated in OEM sources | `schema/extracted/parametric_limits.md` states launcher working temperature only (PL-73, PL-74) |
| C2 heartbeat timeout and link re-acquisition hysteresis | Not stated in OEM sources | `schema/extracted/interface_table.md` states no timeout values |
| ESAD-to-warhead in-line initiation latency | Not stated in OEM sources | `schema/extracted/interface_table.md at line 48` lists the initiation sequence as event-driven with no latency value |

## Source References

Authoritative sources: schema/model.sysml and .pipeline/schema.sysml provide the SysML v2 allocation model and declared part def nodes; schema/extracted/oem_bom.md, schema/extracted/interface_table.md, and schema/extracted/parametric_limits.md provide the Level 0 evidence; ISO/IEC/IEEE 29148:2018 Section 6.4.2 and INCOSE SEH v5.0 Section 5.4 provide the normative allocation and traceability clauses.

| Source ID | Source Reference | Citation / Clause | Description |
| :--- | :--- | :--- | :--- |
| SR-01 | schema/model.sysml | schema/model.sysml | Canonical schema path binding the SysML v2 allocation model |
| SR-02 | .pipeline/schema.sysml | .pipeline/schema.sysml | Package extracted AST root for all extracted:: allocation blocks and declared part def nodes used as allocation targets |
| SR-03 | schema/extracted/oem_bom.md | schema/extracted/oem_bom.md at line 5,23,47-49,52 | OEM-silent mass and power convention, parachute non-mission declaration, canonical part naming, and ESAD Critical / DAL-A declaration |
| SR-04 | schema/extracted/interface_table.md | schema/extracted/interface_table.md at line 9-44,63-64 | RF 4.4 to 5.0 GHz C2 link medium and interface refresh-rate silence for CAN, UART, and USB links |
| SR-05 | schema/extracted/parametric_limits.md | schema/extracted/parametric_limits.md at line 7-66 | Governing quantitative limits cited in Sections 10.1 and 10.2 |
| SR-06 | docs/research/RESEARCH_INVENTORY.md | docs/research/RESEARCH_INVENTORY.md at line 19,38 | INCOSE SEH v5.0 Section 5.4 digital thread traceability obligation and NATO STANAG 4586 interoperability framework context for C2 allocation |
| SR-07 | ISO/IEC/IEEE 29148:2018 | ISO/IEC/IEEE 29148:2018 Section 6.4.2 | Concept of Operations operational allocation traceability |
| SR-08 | INCOSE SEH v5.0 | INCOSE SEH v5.0 Section 5.4 | System verification, validation, and digital thread traceability |
