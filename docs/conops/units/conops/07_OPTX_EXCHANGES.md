| Attribute | Specification Detail |
| :--- | :--- |
| **Title** | Operational Information Exchange (Op-Tx) Matrix |
| **Version** | 1.0.0 |
| **Date** | 2026-09-02 |
| **Issue ID** | 7 |
| **Type** | conops |
| **Generation Mode** | subagent |
| **Specification Source** | docs/conops/units/conops/07_OPTX_EXCHANGES.md; .pipeline/schema.sysml; schema/extracted/interface_table.md; schema/extracted/parametric_limits.md; schema/extracted/oem_bom.md; docs/research/RESEARCH_INVENTORY.md |

## 7. Operational Information Exchange (Op-Tx) Matrix

### 7.1 Scope and Operational Exchange Boundary

The Operational Information Exchange (Op-Tx) architecture defines the mission-level, flight-control, telemetry, payload, external-coordination, and safety information exchanges between operational performer nodes. The roster captures high-level operational exchanges only. Component-internal serial opcodes, register bitmasks, pinouts, wire framing, and cyclic-redundancy equations are deferred to the Level 1C Interface Control Documents in accordance with OMG Unified Architecture Framework (UAF) v2.0 Operational Information Views and ISO/IEC/IEEE 29148:2018.

The canonical tail control surface assembly is the Ruddervator. The drawing synonym Fins and the preparation synonym tail stabiliser are retained only parenthetically. The parachute deployment module is a non-mission R&D variant with configuration non-mission and baseline false, so it is excluded from the mission baseline and from mission criticality credit. The ESAD is classified Critical and carries DAL-A integrity.

### 7.2 Operational Information Exchange (Op-Tx) Roster

In accordance with OMG UAF v2.0 Operational Information Views (Op-Tx), RTCA DO-178C design assurance levels, and the extracted Level 0 data contracts, the operational information exchanges are specified in the roster below. Where an OEM source is silent on a rate, throughput, or timing bound, the roster states "Not stated in OEM sources" rather than inventing a value.

| Exchange ID | Information Exchange Name | Source Performer | Destination Performer | Exchange Item and Semantic Content | Trigger Mechanism | Nominal Frequency | Peak Throughput | Max Latency Bound (ms) | Criticality | Security and Integrity Protection | Grounding Citation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **OpTx-01** | PrimarySensorTelemetry | Airframe sensors (IMU, barometer, pitot, magnetometer) | Autopilot Stack ASTK A5 V2.5 | Raw inertial and kinematic measurements, barometric static pressure, magnetometer heading | Periodic sensor sampling | Not stated in OEM sources | Not stated in OEM sources | Not stated in OEM sources | DAL-B (flight-critical) | DroneCAN frame integrity validation | See grounding citation index |
| **OpTx-02** | ActuatorControlDemand | Autopilot Stack ASTK A5 V2.5 | Ruddervator Servos #1 to #4 and Wing Servos #5 to #8 | Dynamic torque demands, control surface deflections, speed controller setpoints | Periodic control-loop execution | Not stated in OEM sources | Not stated in OEM sources | Not stated in OEM sources | DAL-A (flight-critical) | DroneCAN command frames with hardware interlock | See grounding citation index |
| **OpTx-03** | ActuatorStateFeedback | Ruddervator Servos #1 to #4 and Wing Servos #5 to #8 | Autopilot Stack ASTK A5 V2.5 | Measured actuator positions, motor RPM telemetry, phase current draw, thermal diagnostic flags | Periodic feedback sampling | Not stated in OEM sources | Not stated in OEM sources | Not stated in OEM sources | DAL-B | DroneCAN status frames | See grounding citation index |
| **OpTx-04** | PowerResourceTelemetry | EPS Module and Power Meter | Autopilot Stack ASTK A5 V2.5 | Battery pack voltage from 36 V to 50.4 V, cell temperature matrix, state-of-charge, current draw, reserve thresholds | Periodic battery-monitor interval | Not stated in OEM sources | Not stated in OEM sources | Not stated in OEM sources | DAL-B | Isolated bus and range-bound sanitization | See grounding citation index |
| **OpTx-05** | ExternalNavReferenceData | GNSS Module Septentrio Asterx-m3 pro | Autopilot Stack ASTK A5 V2.5 | Multi-constellation position, velocity and time solutions, differential phase residuals, ephemeris data, UTC reference | Periodic epoch arrival | Not stated in OEM sources | Not stated in OEM sources | Not stated in OEM sources | DAL-B | GNSS integrity monitoring and ephemeris sanity verification | See grounding citation index |
| **OpTx-06** | RawPayloadSensorStream | Camera Compute Module Trip6 and Gimbal Nighthawk2UZ | Companion Computer RPI CM5004032 | EO and IR video frames, timestamp metadata, camera orientation, radiometric matrices | Continuous frame-clock synchronized | Not stated in OEM sources | Not stated in OEM sources | Not stated in OEM sources | DAL-D (payload) | Dedicated Ethernet path and isolated network segment | See grounding citation index |
| **OpTx-07** | ProcessedFeatureTelemetry | Companion Computer RPI CM5004032 | Autopilot Stack ASTK A5 V2.5 | Target bounding boxes, optical odometry vectors, obstacle disparities | Periodic inference pipeline execution | Not stated in OEM sources | Not stated in OEM sources | Not stated in OEM sources | DAL-C | Memory partition isolation and ingress range sanitization | See grounding citation index |
| **OpTx-08** | ConsolidatedDownlinkTelemetry | Radio Module DTC | Ground Control System (Panasonic FZ-G2) | Consolidated system state telemetry, 3D kinematics, energy state-of-charge, link signal-to-noise ratio, geofence margin status | Periodic PACE telemetry scheduler | Not stated in OEM sources | Not stated in OEM sources | Not stated in OEM sources | DAL-B | Authenticated encryption and message authentication per the cited OT security standard | See grounding citation index |
| **OpTx-09** | SupervisoryUplinkCommand | Ground Control System (Panasonic FZ-G2, SwarmC2) | Autopilot Stack ASTK A5 V2.5 | Uplink flight directives, 4D waypoint corridors, ROE arming keys, manual override vectors | Aperiodic operator command action | Not stated in OEM sources | Not stated in OEM sources | Not stated in OEM sources | DAL-A | Command authentication and replay protection per the cited OT security standard | See grounding citation index |
| **OpTx-10** | WatchdogHeartbeatStrobe | Autopilot Stack ASTK A5 V2.5 | Safety Watchdog and Interlocks | Controller task-alive token, execution deadline checksum, task schedule monotonic counter | Periodic task deadline checkpoint | Not stated in OEM sources | Not stated in OEM sources | Not stated in OEM sources | DAL-A | Dedicated hardware strobe line and timing-window interlock | See grounding citation index |
| **OpTx-11** | EmergencyFailsafeTrigger | Safety Watchdog and Interlocks | Ruddervator Servos #1 to #4, Wing Servos #5 to #8, EPS Module, ESAD | Hardware safety abort strobe, propulsion isolation command, safe-state clamping signal | Event-driven fault detection | Event-driven | Not stated in OEM sources | Not stated in OEM sources | DAL-A | Hardware interlock and dual-switch isolation | See grounding citation index |
| **OpTx-12** | FailsafeSquibActuationLine (Non-Mission) | Safety Watchdog and Interlocks | Parachute Deployment Non-Mission Igniters #1 and #2 | Dual-channel 50 V fire pulse for the payload bay cover retention wire | Event-driven single pulse | Event-driven | Not stated in OEM sources | Not stated in OEM sources | Non-mission, baseline false, excluded from mission criticality analysis | Isolated high-side and low-side switches with physical key interlock | See grounding citation index |
| **OpTx-13** | BroadcastRemoteIDTelemetry | Radio Module DTC Remote ID function | External airspace authority and receivers | Statutory broadcast identity, session identifier, geodetic position, altitude, ground speed, emergency status | Periodic statutory broadcast | Not stated in OEM sources; statutory interval per the cited Remote ID standard | Not stated in OEM sources | Not stated in OEM sources | DAL-C | Signed public broadcast per the cited Remote ID standard | See grounding citation index |
| **OpTx-14** | AirspaceDeconflictionData | External airspace authority (UTM) | Ground Control System (Panasonic FZ-G2) | Dynamic geo-zone activation and deactivation, 4D corridor clearances, adjacent traffic conformance status | Periodic and event-driven UTM service updates | Not stated in OEM sources | Not stated in OEM sources | Not stated in OEM sources | DAL-C | Mutually authenticated transport per the cited OT security standard | See grounding citation index |
| **OpTx-15** | CompressedPayloadVideoStream | Radio Module DTC | Ground Control System (Panasonic FZ-G2) | Compressed EO and IR video stream with real-time feature overlays | Continuous video frame pipeline | Not stated in OEM sources | Not stated in OEM sources | Not stated in OEM sources | DAL-D | Encrypted video transport per the cited OT security standard | See grounding citation index |
| **OpTx-16** | DiagnosticBlackboxLogStream | Autopilot Stack ASTK A5 V2.5 | Ground Control System and External Interface Board USB ETH | Flight recorder time-series, sensor disparity registers, exception traces, built-in-test failure logs | Periodic buffering and post-operation bulk transfer | Not stated in OEM sources | Not stated in OEM sources | Not stated in OEM sources | DAL-C | Cryptographic hashing and append-only non-volatile storage | See grounding citation index |
| **OpTx-17** | ESADSafetyInterlockAuthorization | Ground Control System and RPI CM5004032 | ESAD | Safe or armed state, arm-enable discrete PWM, umbilical continuity status | Event-driven arm sequence and periodic arm-enable PWM | Arm-enable PWM at 1 kHz | Not stated in OEM sources | 5 ms ESAD response | Critical (DAL-A) | Discrete interlock and hardware key per ESAD Critical classification | See grounding citation index |
| **OpTx-18** | ESADInitiationCommand | Ground Control System and RPI CM5004032 | ESAD and ESAD Detonator | In-line initiation sequence and 1800 V maximum detonator firing pulse after explicit human consent | Event-driven single high-consequence pulse | Event-driven | Not stated in OEM sources | Not stated in OEM sources | Critical (DAL-A) | Isolated firing circuit and hardware interlock | See grounding citation index |

### 7.3 Operational Exchange Grouping

The roster is partitioned across five operational transport groups. Group allocation does not create component-internal interface contracts; those contracts belong to the Level 1C Interface Control Documents.

| Group | Allocated Exchanges | High-Level Transport | Operational Note |
| :--- | :--- | :--- | :--- |
| Deterministic real-time bus | OpTx-01, OpTx-02, OpTx-03, OpTx-04, OpTx-05, OpTx-07, OpTx-10 | DroneCAN over the CAN bus | Flight-control, sensor, power-status, and heartbeat exchanges with fixed-priority arbitration |
| High-speed payload bus | OpTx-06, OpTx-15, OpTx-16 | Ethernet | Payload imagery, compressed video, and diagnostic log transfer isolated from flight-critical traffic |
| Telemetry wireless PACE links | OpTx-08, OpTx-09, OpTx-14, OpTx-15 | Primary RF link in the 4.4 to 5.0 GHz band (interface_table.md line 63); alternate, contingency, and emergency media are Not stated in OEM sources | Primary, Alternate, Contingency, and Emergency tiers preserve command and telemetry continuity |
| Direct broadcast Remote ID | OpTx-13 | ASTM F3411-22a direct broadcast using Bluetooth 5.x or Wi-Fi NAN | Independent broadcast path preserves statutory identification during lost-link states |
| Hardwired failsafe and ESAD safety discretes | OpTx-11, OpTx-12, OpTx-17, OpTx-18 | Discrete interlock, PWM, and pyrotechnic initiation circuits | ESAD is Critical and DAL-A; the parachute squib is a non-mission R&D variant |

### 7.4 Sequence Diagram Parity

The operational interaction sequence diagrams are maintained in the scenarios unit and are partitioned across the canonical four-part interaction architecture. This roster is partitioned across those diagrams as follows, with zero uncovered exchanges.

| Diagram | Realized Exchanges | Operational Thread |
| :--- | :--- | :--- |
| Diagram 10.1 | OpTx-08, OpTx-09, OpTx-14, OpTx-15, OpTx-16 | Supervisory command, telemetry downlink, airspace coordination, video relay, and diagnostic offload |
| Diagram 10.2 | OpTx-01, OpTx-05, OpTx-06, OpTx-07 | Sensor perception, external navigation reference, raw imagery, and processed feature flow |
| Diagram 10.3 | OpTx-02, OpTx-03, OpTx-04 | Actuator demand, actuator feedback, and resource status |
| Diagram 10.4 | OpTx-10, OpTx-11, OpTx-12, OpTx-13, OpTx-17, OpTx-18 | Watchdog heartbeat, emergency containment, non-mission squib, Remote ID broadcast, and ESAD safety interlock and initiation |

### 7.5 Grounding Citation Index

| Exchange ID | Grounding Source and Lines |
| :--- | :--- |
| OpTx-01 | schema/extracted/interface_table.md lines 9-15 and 28-32; .pipeline/schema.sysml lines 192-312 |
| OpTx-02 | schema/extracted/interface_table.md lines 12-15 and 29-31; schema/extracted/oem_bom.md lines 24-27 and 35-38 |
| OpTx-03 | schema/extracted/interface_table.md lines 12-15 and 29-31 |
| OpTx-04 | schema/extracted/parametric_limits.md lines 29-30; schema/extracted/oem_bom.md lines 18 and 20 |
| OpTx-05 | schema/extracted/interface_table.md lines 38-39; schema/extracted/oem_bom.md lines 15-16 |
| OpTx-06 | schema/extracted/interface_table.md lines 33-37; schema/extracted/oem_bom.md lines 42-43 |
| OpTx-07 | schema/extracted/interface_table.md lines 35 and 40; schema/extracted/oem_bom.md lines 14 and 43 |
| OpTx-08 | schema/extracted/interface_table.md line 63; schema/extracted/oem_bom.md lines 44 and 76 |
| OpTx-09 | schema/extracted/interface_table.md line 63; schema/extracted/oem_bom.md line 76; docs/research/RESEARCH_INVENTORY.md line 20 |
| OpTx-10 | schema/extracted/oem_bom.md line 52; .pipeline/schema.sysml lines 440-456 |
| OpTx-11 | schema/extracted/oem_bom.md line 52; .pipeline/schema.sysml lines 440-456 |
| OpTx-12 | schema/extracted/oem_bom.md lines 47-49 |
| OpTx-13 | docs/research/RESEARCH_INVENTORY.md lines 29, 92, and 133; schema/extracted/oem_bom.md line 44 |
| OpTx-14 | docs/research/RESEARCH_INVENTORY.md line 108 |
| OpTx-15 | schema/extracted/interface_table.md lines 42-43 and 63; schema/extracted/oem_bom.md lines 44-46 and 76 |
| OpTx-16 | schema/extracted/interface_table.md lines 36 and 44; schema/extracted/oem_bom.md line 58 |
| OpTx-17 | schema/extracted/parametric_limits.md lines 52-65; schema/extracted/interface_table.md lines 49-51 and 56; schema/extracted/oem_bom.md line 52 |
| OpTx-18 | schema/extracted/parametric_limits.md line 66; schema/extracted/interface_table.md lines 48 and 55; schema/extracted/oem_bom.md lines 52 and 54 |

## Source References
Source: schema/model.sysml
Source: .pipeline/schema.sysml
Source: schema/extracted/interface_table.md
Source: schema/extracted/parametric_limits.md
Source: schema/extracted/oem_bom.md
Source: docs/research/RESEARCH_INVENTORY.md
Clause: ISO/IEC/IEEE 29148:2018 Section 6.4.2
Clause: RTCA DO-178C Section 6.3.1
Clause: RTCA DO-362A Section 3.4
Clause: ASTM F3411-22a Section 6.1
Clause: FAA 14 CFR Section 89.310(b)
Clause: NIST SP 800-82r3 Section 6.2
Viewpoint: OMG UAF v2.0 Operational Information Views
