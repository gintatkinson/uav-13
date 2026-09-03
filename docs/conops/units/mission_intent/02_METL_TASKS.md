| Attribute | Value |
| :--- | :--- |
| **Title** | Tactical Mission Intent: Mission Essential Task List |
| **Version** | 1.0.0 |
| **Date** | 2026-09-02 |

## 2. Mission Essential Task List (METL)

The Mission Essential Task List (METL) establishes the doctrinally grounded, quantitative task inventory required to achieve the Commander's operational intent across all operational lifecycle phases in accordance with CJCSI 3500.02H and NATO STANAG 4586 Annex B.

| Task ID | Task Name | Condition Statement | Standard Metric | Verification Method | Gate 24 Allocation Tag | Public Clause Citation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `MET-01` | PreFlightSystemCheckout | Pre-launch stationary ground state across 10 physical/electronic subsystems with ground support equipment connected | 100% PBIT pass across 10 subsystems (Structures tap/torque/CG, Controls backlash/current, Pitot leak/offset/heater, Propulsion/BMS phase/quiescent/R_i/SoC/delta_V, Avionics IMU/GNSS/PDOP, DAA radar/ADS-B, FTS squib/pin, C2 PER/Remote ID, Payload boresight/cryo lock, 3-tier release ECDSA token 0x5349) | Automated Subsystem PBIT Telemetry & 3-Tier Multi-Disciplinary Digital Logbook Inspection | `/// OperationalAllocation: [MET-01]` | NATO STANAG 4586 Annex B §4.1 |
| `MET-02` | AutonomousIngressTransit | En-route corridor navigation under active flight plan | Lateral cross-track error e_xtrack <= 2.0 m, vertical error e_z <= 1.0 m, motor RPM in [4500, 7200 RPM], ESC temp <= 75.0 C, pitot lag tau <= 50.0 ms, IMU vibration rejection <= 0.01 g^2/Hz | Flight Navigation Log Review & Multi-Subsystem Telemetry Audit | `/// OperationalAllocation: [MET-02]` | RTCA DO-365B §2.2.3 |
| `MET-03` | AreaSurveillanceOrbit | On-station target tracking, search pattern execution (Expanding Square, Creeping Line, Sector Scan), and multi-spectral surveillance within designated geographic boundary | Orbit radius R_orbit = 300.0 m +/- 5.0 m, search coverage rate >= 50.0 km^2/hr, multi-spectral sensor fusion (MWIR 3-5 um, LWIR 8-12 um, SWIR), gimbal servo temp <= 65.0 C, MWIR NUC interval <= 300.0 s, optical boresight jitter <= 0.02 deg RMS under wind shear | Telemetry, Search Coverage Mapping, & Video Frame Analysis | `/// OperationalAllocation: [MET-03]` | NATO STANAG 4586 Annex B §3.2 / NATO STANAG 3733 |
| `MET-04` | DynamicAirspaceDeconfliction | Traffic conflict geometry detected by onboard DAA sensors | Maintain Well-Clear separation (D_horizontal >= 1200.0 m, H_vertical >= 137.0 m), 77 GHz radar rate f >= 20.0 Hz, ADS-B decode latency <= 100.0 ms, vertical rate resolution dz/dt <= 0.2 m/s | DAA Collision Event Log Review & HIL Encounter Audit | `/// OperationalAllocation: [MET-04]` | RTCA DO-365B §2.2.4 |
| `MET-05` | ElectronicCounterCountermeasures | Jamming or intentional RF / navigation spoofing detected | Seamless PACE switch t_switch <= 1.0 s, GNSS J/S anti-jam >= 35.0 dB, CRPA nulling depth >= 25.0 dB, dead-reckoning drift <= 0.5% distance over 60 s GNSS outage | RF Signal Log & Navigation Resiliency Test | `/// OperationalAllocation: [MET-05]` | MIL-STD-461G RS103 §4.3 |
| `MET-06` | PrecisionTargetMensuration | Target acquired across taxonomy classes (Fixed Infrastructure, Moving Vehicle, HVT, Pop-up Threat) within optical/infrared payload field of view | TLE_CEP90 <= 2.5 m at 3.0 km, STANAG 3733 Band I/II laser PRF coding (1111-1788), beam divergence <= 0.3 mrad, boresight alignment <= 0.05 deg, BDA offload <= 30.0 s with structural/thermal kill verification | Optical Mensuration Calibration Log, Laser PRF Telemetry, & BDA Audit | `/// OperationalAllocation: [MET-06]` | NATO STANAG 4586 Annex B §3.5 / NATO STANAG 3733 / CJCSI 3121.01B |
| `MET-07` | AutonomousBingoReturnDivert | Energy monitoring detects current energy E_current <= E_bingo threshold | Autonomous RTB/divert trigger t_resp <= 200.0 ms, dynamic R_i(T) compensation, headwind gradient vector integration, touchdown reserve E_reserve >= 216.0 kJ | BMS Telemetry & Flight Recording Audit | `/// OperationalAllocation: [MET-07]` | JARUS SORA v2.5 Annex E §2.1 |
| `MET-08` | PostMissionDataOffloadShutdown | Post-landing stationary touchdown on recovery pad | Zeroization time <= 10.0 s (NIST SP 800-88r1), DC bus discharge time <= 5.0 s (V_bus < 5.0 V), post-flight motor thermal soak T_motor <= 60.0 C, offload <= 60.0 s | Security Audit Log & Safe Electrical Isolation Verification | `/// OperationalAllocation: [MET-08]` | NIST SP 800-88r1 §2.4 |

---

### 2.1 MET-01: PreFlightSystemCheckout

Formal specification for comprehensive pre-flight built-in test (PBIT), physical structural integrity validation, air data calibration, propulsion and battery impedance verification, sensor bias convergence, detect and avoid self-test, flight termination interlocks, command-and-control link margins, cryogenic payload cooling, and multi-tier cryptographic airworthiness release authorization prior to motor arming.

Pre-flight checkout enforces a strict 3-tier airworthiness release architecture:
1. **Tier 1 (Automated Bus Telemetry & Sensor BITE):** Continuous digital interrogation of all onboard sensors, avionics buses (CAN FD, SPI, ARINC 429, RS-422, Ethernet), and power rails.
2. **Tier 2 (Physical GSE & Mechanical Interlocks):** Calibrated ground support equipment (GSE-01 through GSE-06) verification of structural torques, pitot pneumatic decay, acoustic delamination, servo backlash, and mechanical FTS safety pins.
3. **Tier 3 (Cryptographic Airworthiness Sign-Off):** Digital maintenance manifest verification requiring an authenticated ECDSA electronic signature token (`0x5349`) issued by a Certified O-Level Maintenance Technician.

#### Condition Specification
| Parameter | Condition Value / State | Engineering Unit | Validation Rule |
| :--- | :--- | :--- | :--- |
| Operational State | Stationary Ground Pad | State Enum | Vehicle landed, anchored, and weight-on-wheels interlock active |
| Ambient Ground Temperature | -20.0 to +55.0 | °C | MIL-STD-810H Method 501.7 / 502.7 operational thermal boundary |
| Ambient Barometric Pressure | 700.0 to 1060.0 | hPa | Static airfield pressure within nominal density altitude limits |
| Ground Wind Velocity | <= 8.0 steady, gusts <= 10.0 | m/s | Safe ground checkout and sensor alignment wind envelope |
| Primary DC Power Bus Voltage | 22.2 to 25.2 | V | 6S LiPo operational voltage range across main power distribution bus |
| Regulated Avionics Supply Rails | 5.0 +/- 0.1 and 12.0 +/- 0.2 | V | Secondary power distribution board output rail regulation limits |
| Ground Support Equipment (GSE) | Connected (GSE-01 to GSE-06) | State Enum | Active diagnostic test bench interfaces synchronized |
| Visible GNSS Constellation | >= 12 | Count | Multi-constellation tracking (GPS L1/L2 + Galileo E1/E5b) |
| Position Dilution of Precision | <= 2.0 | Dimensionless | Geodetic PDOP geometry convergence threshold |
| DAA RF Operating Environment | Clear 360-deg FOV | State Enum | Zero near-field RF blockage or multipath reflecting obstacles |
| FTS Mechanical Interlock State | Ground Safety State | State Enum | Mechanical safety pin monitored prior to final launch release |
| C2 Uplink Signal Strength | >= -85.0 | dBm | Primary 5.8 GHz COFDM link established with GCS |
| Maintenance Authorization State | Authenticated Smartcard / PKI | State Enum | Certified Maintenance Technician logged into Ground Control Station |

#### Standard Specification
| Metric ID | Subsystem Domain | Metric Name / Description | Threshold Value | Objective Value | Unit | Bus Protocol / Interface | Timeout Bound |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MET-01-S01 | Structures & Airframe | Composite Skin Delamination Tap Test | 0 delamination | 0 delamination | Count | Acoustic Tap Hammer / NDI Sensor | t_tap <= 120.0 s |
| MET-01-S02 | Structures & Airframe | Primary Joint Fastener Torque | >= 4.5 | >= 5.0 | N*m | Calibrated Digital Torque Driver (GSE-03) | t_torque <= 60.0 s |
| MET-01-S03 | Structures & Airframe | Center of Gravity (CG) Longitudinal Envelope | [x_ref - 5.0, x_ref + 5.0] | x_ref +/- 1.0 | mm | Multi-Point Electronic Scale (GSE-02) | t_wb <= 30.0 s |
| MET-01-S04 | Flight Controls | Control Surface Trailing Edge Backlash | <= 0.20 | <= 0.05 | deg | Digital Inclinometer / Laser Protractor | t_backlash <= 15.0 s |
| MET-01-S05 | Flight Controls | Servo Peak Current Draw Under 1.5 N*m Load | <= 2.20 | <= 1.80 | A | DroneCAN / Actuator Shunt Monitor | t_sweep <= 2.0 s |
| MET-01-S06 | Pitot-Static & Air Data | Static Line Pressure Decay Leak Rate at 100 hPa | <= 0.05 | <= 0.01 | hPa/min | Air Data Calibration Box (GSE-04) | t_leak = 60.0 s |
| MET-01-S07 | Pitot-Static & Air Data | Pitot Dynamic Pressure Offset at Zero Wind | <= 2.0 | <= 0.5 | Pa | CAN 2.0B / Differential Pressure Sensor | Continuous @ 100 Hz |
| MET-01-S08 | Pitot-Static & Air Data | Pitot Anti-Ice Heater Current Draw | [1.80, 2.40] | 2.10 +/- 0.10 | A | Power Distribution Telemetry / Shunt | t_heat <= 3.0 s |
| MET-01-S09 | Propulsion & BMS | BLDC Motor Phase-to-Phase Resistance Balance | <= 2.5 | <= 1.0 | % disparity | ESC Diagnostic Micro-Ohm Injector | t_motor <= 2.0 s |
| MET-01-S10 | Propulsion & BMS | ESC Idling Quiescent Standby Current | <= 0.45 | <= 0.25 | A | Telemetry CAN Bus / Integrated Shunt | Continuous @ 50 Hz |
| MET-01-S11 | Propulsion & BMS | Battery Cell Internal Resistance (R_i) | <= 3.5 | <= 2.0 | mOhm | Smart BMS SMBus / CAN 2.0B | t_bms <= 500.0 ms |
| MET-01-S12 | Propulsion & BMS | Battery Pack State-of-Charge (SoC) | >= 95.0 | >= 99.0 | % | Smart BMS SMBus / CAN 2.0B | Continuous @ 50 Hz |
| MET-01-S13 | Propulsion & BMS | Battery Cell Voltage Delta (V_max - V_min) | <= 20.0 | <= 5.0 | mV | Smart BMS Analog Front-End / CAN 2.0B | Continuous @ 50 Hz |
| MET-01-S14 | Avionics & Navigation | Dual IMU Gyro In-Run Bias Stability | <= 0.05 | <= 0.01 | deg/s | High-Speed SPI / ARINC 429 | t_align <= 8.0 s |
| MET-01-S15 | Avionics & Navigation | GNSS Multi-Constellation C/N_0 (12+ Satellites) | >= 42.0 | >= 48.0 | dB-Hz | Multi-Band GNSS / High-Speed UART | t_gnss <= 15.0 s |
| MET-01-S16 | Avionics & Navigation | Position Dilution of Precision (PDOP) | <= 2.0 | <= 1.2 | Dimensionless | Multi-Band GNSS / High-Speed UART | Continuous @ 10 Hz |
| MET-01-S17 | Detect and Avoid (DAA) | 77 GHz FMCW Radar Loopback Attenuation | >= -12.0 | >= -8.0 | dB | Radar SPI / 100BASE-T1 Ethernet | t_radar <= 1.5 s |
| MET-01-S18 | Detect and Avoid (DAA) | ADS-B In 1090 MHz Receiver Sensitivity Floor | <= -88.0 | <= -92.0 | dBm | 1090 MHz RF Front-End / UART | t_adsb <= 2.0 s |
| MET-01-S19 | Flight Termination (FTS) | Pyrotechnic Squib Bridgewire DC Resistance | [1.05, 1.25] | 1.15 +/- 0.05 | Ohm | FTS Micro-Current Continuity Circuit | t_squib <= 500.0 ms |
| MET-01-S20 | Flight Termination (FTS) | Mechanical Safety Pin Status | 0x01 (REMOVED) | 0x01 (REMOVED) | State Hex | Hardwired Optical / Microswitch GPIO | Continuous Interlock |
| MET-01-S21 | C2 & Communications | Primary 5.8 GHz COFDM Datalink Packet Error Rate | <= 10^-4 | <= 10^-6 | PER | 5.8 GHz COFDM Modem / Ethernet | Continuous @ 20 Hz |
| MET-01-S22 | C2 & Communications | Remote ID Direct Broadcast RF Field Strength at 10 m | >= -75.0 | >= -65.0 | dBm | 2.4 GHz BLE / Wi-Fi Direct Beacon | Continuous @ 1 Hz |
| MET-01-S23 | Payload & Gimbal | Gimbal Optical Boresight Collimation Error | <= 0.05 | <= 0.01 | deg | Optical Collimator (GSE-05) / RS-422 | t_boresight <= 10.0 s |
| MET-01-S24 | Payload & Gimbal | MWIR Detector Cryocooler Lock Temperature (T_cryo) | <= 77.0 | <= 72.0 | K | Cryogenic Controller Serial Link | t_cool <= 180.0 s |
| MET-01-S25 | Airworthiness Release | Certified Maintenance Technician Digital Sign-Off | Valid (0x5349) | Valid (0x5349) | ECDSA Token | TPM 2.0 PKI Verification / GCS Link | t_auth <= 5.0 s |
| MET-01-S26 | Airworthiness Release | 3-Tier Multi-Disciplinary Pre-Flight Gate Pass Rate | 100.0 | 100.0 | % Pass | System Executive State Machine | t_release <= 1.0 s |

#### Verification Specification
| Verification Attribute | Detail Specification |
| :--- | :--- |
| Verification Method | Automated Subsystem PBIT Telemetry Audit, Physical GSE Inspection, and 3-Tier Multi-Disciplinary Digital Logbook Sign-Off Verification |
| Evidence Artifact | `tests/pbit_checkout_test.py` -> `logs/pbit_telemetry_report.json` and `logs/airworthiness_release_manifest.json` |
| Acceptance Criteria | Full conjunction across all 10 physical and electronic subsystems:<br>1. **Structures & Airframe:** 0 composite delamination via acoustic tap; fastener torque >= 4.5 N*m; longitudinal CG within [x_ref - 5.0, x_ref + 5.0] mm.<br>2. **Flight Controls:** Control surface trailing edge backlash <= 0.20 deg; servo peak current <= 2.20 A under 1.5 N*m dynamic load.<br>3. **Pitot-Static & Air Data:** Static line pressure decay <= 0.05 hPa/min at 100 hPa; zero-wind pitot dynamic pressure offset <= 2.0 Pa; pitot anti-ice heater current within [1.80, 2.40] A.<br>4. **Propulsion & BMS:** Motor phase resistance balance <= 2.5% disparity; ESC idling quiescent current <= 0.45 A; cell internal resistance R_i <= 3.5 mOhm; pack SoC >= 95.0%; cell voltage disparity delta_V <= 20.0 mV.<br>5. **Avionics & Navigation:** Dual IMU gyro in-run bias stability <= 0.05 deg/s; GNSS multi-constellation C/N_0 >= 42.0 dB-Hz across 12+ satellites; PDOP <= 2.0.<br>6. **Detect and Avoid:** 77 GHz FMCW radar loopback attenuation >= -12.0 dB; ADS-B In 1090 MHz receiver sensitivity <= -88.0 dBm.<br>7. **Flight Termination:** Pyrotechnic squib bridgewire DC resistance within [1.05, 1.25] Ohm at test current I_test < 5.0 mA; mechanical safety pin in REMOVED state (0x01).<br>8. **C2 & Communications:** Primary 5.8 GHz COFDM datalink PER <= 10^-4; Remote ID broadcast field strength >= -75.0 dBm at 10 m.<br>9. **Payload & Gimbal:** Gimbal optical boresight collimation error <= 0.05 deg; MWIR cryocooler locked at temperature T <= 77 K.<br>10. **Airworthiness Release:** Certified Maintenance Technician digital logbook sign-off verified with valid ECDSA token (0x5349) completing the 3-tier airworthiness release. |
| Pass / Fail Threshold | `PBIT_STATUS == 0x0000_0000` (100% subsystem pass) and `AIRWORTHINESS_TOKEN == 0x5349` with zero active diagnostic fault flags within pre-launch timeout bounds. |
| Traceability | `/// OperationalAllocation: [MET-01]` \| NATO STANAG 4586 Annex B §4.1 \| ISO/IEC/IEEE 29148:2018 §6.4.2 \| CJCSI 3500.02H \| SAE ARP4754A §5.4 |

---

### 2.2 MET-02: AutonomousIngressTransit

Formal specification for autonomous waypoint sequencing, 4D trajectory tracking, wind vector compensation, motor operating RPM bounds containment, ESC thermal regulation, dynamic pitot-static response lag bounding, IMU vibration rejection spectral density gating, and real-time geofence envelope containment during high-speed ingress corridor transit.

#### Condition Specification
| Parameter | Condition Value / State | Engineering Unit | Validation Rule |
| :--- | :--- | :--- | :--- |
| Operational State | En-route Airborne Ingress Transit | State Enum | Flight mode `AUTO_MISSION` |
| Assigned Flight Corridor Width | 50.0 | m | Total lateral clearance boundary |
| Operating Altitude Floor / Ceiling | 30.0 to 120.0 | m AGL | Operational containment envelope |
| Ambient Wind Velocity | <= 12.0 steady, gusts <= 15.0 | m/s | Continuous operating wind envelope |
| Calibrated Airspeed Envelope (CAS) | 18.0 to 28.0 | m/s | Nominal transit airspeed limits |
| Ambient In-Flight Air Temperature | -20.0 to +50.0 | °C | In-flight ambient thermal envelope |
| BLDC Motor Operating RPM Envelope | 4500 to 7200 | RPM | Nominal propulsion drive operating range |
| ESC Inverter Thermal Boundary | <= 75.0 | °C | MOSFET junction thermal limit |
| Pitot Air Data System State | Calibrated / Anti-Ice Active | State Enum | Differential pressure ADU locked |
| IMU Structural Damping State | Isolated Elastomeric Assembly | State Enum | Passive silicone damper array engaged |

#### Standard Specification
| Metric ID | Subsystem Domain | Metric Name / Description | Threshold Value | Objective Value | Unit | Bus Protocol / Interface | Timeout Bound |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MET-02-S01 | Flight Guidance & Trajectory | Lateral Cross-Track Tracking Error (e_xtrack) | <= 2.0 | <= 0.5 | m | High-Speed CAN / Ethernet | Continuous @ 250 Hz |
| MET-02-S02 | Flight Guidance & Trajectory | Vertical Altitude Tracking Error (e_z) | <= 1.0 | <= 0.3 | m | High-Speed CAN / Ethernet | Continuous @ 250 Hz |
| MET-02-S03 | Flight Guidance & Trajectory | Guidance Control Loop Execution Rate | 250 | 500 | Hz | Real-Time OS Task Loop | dt <= 4.0 ms |
| MET-02-S04 | Flight Guidance & Trajectory | Waypoint Transition Latency | <= 50.0 | <= 10.0 | ms | Internal Memory Bus | t_trans <= 50.0 ms |
| MET-02-S05 | Flight Guidance & Trajectory | Geofence Boundary Containment Margin | >= 50.0 | >= 100.0 | m | Simplex RTA Safety Bus | Continuous @ 50 Hz |
| MET-02-S06 | Propulsion & BMS | BLDC Motor Operating Speed Bounds | [4500, 7200] | [5000, 6800] | RPM | DroneCAN / ESC Telemetry | Continuous @ 100 Hz |
| MET-02-S07 | Propulsion & BMS | ESC Inverter MOSFET Temperature (T_esc) | <= 75.0 | <= 60.0 | °C | CAN 2.0B / NTC Thermistor | Continuous @ 50 Hz |
| MET-02-S08 | Propulsion & BMS | Dynamic DC Bus Voltage Under Max Load | >= 21.6 | >= 22.8 | V | Power Distribution Telemetry | Continuous @ 100 Hz |
| MET-02-S09 | Pitot-Static & Air Data | Pitot Airspeed Dynamic Response Lag (tau_lag) | <= 50.0 | <= 20.0 | ms | CAN 2.0B / Differential ADU | Continuous @ 100 Hz |
| MET-02-S10 | Pitot-Static & Air Data | True Airspeed (TAS) Tracking Error (e_v) | <= 1.5 | <= 0.4 | m/s | CAN 2.0B Pitot / ADU | Continuous @ 100 Hz |
| MET-02-S11 | Pitot-Static & Air Data | Dynamic Pressure Sensor Linearity Error | <= 1.0 | <= 0.25 | % Full Scale | Digital SPI / I2C Air Data | Continuous @ 100 Hz |
| MET-02-S12 | Avionics & Navigation | IMU Vibration Rejection Power Spectral Density | <= 0.01 | <= 0.002 | g^2/Hz | High-Speed SPI (10-500 Hz) | Continuous @ 1000 Hz |
| MET-02-S13 | Avionics & Navigation | EKF Attitude Estimation Error (Roll/Pitch) | <= 0.50 | <= 0.15 | deg | ARINC 429 / High-Speed SPI | Continuous @ 250 Hz |
| MET-02-S14 | Flight Controls | Control Surface Actuator Slew Rate | >= 180.0 | >= 240.0 | deg/s | DroneCAN / PWM Actuator Bus | dt <= 4.0 ms |

#### Verification Specification
| Verification Attribute | Detail Specification |
| :--- | :--- |
| Verification Method | Flight Navigation Log Review, High-Frequency Multi-Subsystem Telemetry Audit, and 6-DOF Kinematic Simulation |
| Evidence Artifact | `tests/flight_guidance_sim.py` -> `logs/flight_trajectory_eval.csv` and `logs/ingress_propulsion_telemetry.json` |
| Acceptance Criteria | Conjunction across all monitored transit subsystems:<br>1. **Flight Guidance & Trajectory:** Lateral cross-track error <= 2.0 m and vertical altitude tracking error <= 1.0 m across entire 15.0 km corridor transit; guidance control loop rate >= 250 Hz; waypoint transition latency <= 50.0 ms; geofence containment margin >= 50.0 m.<br>2. **Propulsion & BMS:** Motor speed maintained within [4500, 7200] RPM; ESC inverter MOSFET temperature <= 75.0 °C; dynamic DC bus voltage >= 21.6 V under full throttle.<br>3. **Pitot-Static & Air Data:** Pitot airspeed dynamic response lag tau <= 50.0 ms; TAS tracking error <= 1.5 m/s; dynamic pressure linearity error <= 1.0%.<br>4. **Avionics & Navigation:** IMU vibration rejection spectral density <= 0.01 g^2/Hz over 10-500 Hz vibration spectrum; EKF dynamic roll/pitch attitude error <= 0.50 deg.<br>5. **Flight Controls:** Actuator deflection slew rate >= 180.0 deg/s without command bus saturation. |
| Pass / Fail Threshold | `max(abs(e_xtrack)) <= 2.0 m`, `max(abs(e_z)) <= 1.0 m`, `RPM in [4500, 7200]`, `T_esc <= 75.0 °C`, `tau_lag <= 50.0 ms`, and `PSD_imu <= 0.01 g^2/Hz`. |
| Traceability | `/// OperationalAllocation: [MET-02]` \| RTCA DO-365B §2.2.3 \| NATO STANAG 4586 Annex B §3.2 \| ISO/IEC/IEEE 29148:2018 §6.4.2 |

---

### 2.3 MET-03: AreaSurveillanceOrbit

Formal specification for closed-loop target area loitering, autonomous search pattern execution (Expanding Square, Creeping Line, Sector Scan), multi-spectral sensor collection modes (Wide-FOV Area Search, Narrow-FOV Kinetic Tracking, MWIR 3–5 µm, LWIR 8–12 µm, SWIR fusion), direct-drive gimbal servo thermal regulation, continuous MWIR Non-Uniformity Correction (NUC) recalibration, optical boresight stabilization under dynamic wind shear, high-throughput search coverage rate ($\ge 50.0\text{ km}^2/\text{hr}$), target classification tracking across doctrinal classes (Fixed Hardened Infrastructure, Moving Surface Vehicle, HVT, Pop-up Threat), and post-strike Battle Damage Assessment (BDA) loiter support.

#### Condition Specification
| Parameter | Condition Value / State | Engineering Unit | Validation Rule |
| :--- | :--- | :--- | :--- |
| Operational State | On-Station Loiter / Area Search / BDA Loiter | State Enum | Flight modes `LOITER_ORBIT`, `AREA_SEARCH`, `BDA_LOITER` |
| Target Classification Scope | Taxonomy Classes 1-4 | Taxonomy Enum | Fixed Infrastructure, Moving Vehicle, HVT, Pop-up Threat |
| Search Pattern Algorithms | Expanding Square, Creeping Line, Sector Scan | Algorithm Enum | Autonomous geometric track generator active |
| Minimum Search Area Coverage Rate | >= 50.0 | km^2/hr | Minimum operational search sweep throughput |
| Designated Orbit Centerpoint | Geodetic (Lat, Lon, Alt) | Coordinates | Target Area of Interest (TAI) |
| Nominal Orbit Radius (R_orbit) | 300.0 | m | Commanded circular orbit radius |
| Target Standoff Slant Range | 300.0 to 1500.0 | m | Payload optical/infrared tracking range |
| Sensor Payload Collection State | Active Multi-Spectral Fusion | State Enum | Fused 4K EO + MWIR + LWIR + SWIR |
| Ambient Wind Shear Envelope | Gusts up to 12.0 m/s with 3.0 m/s/s shear | Vector Gradient | Dynamic wind turbulence field |
| Gimbal Actuator Thermal Baseline | <= 65.0 | °C | Direct-drive brushless servo motor limit |
| MWIR Sensor Operating Mode | Cryocooled 640x512 Detector (3.0-5.0 um) | State Enum | Cryocooler locked at T <= 77.0 K |
| LWIR Sensor Operating Mode | Uncooled 640x512 Microbolometer (8.0-12.0 um) | State Enum | Operational 8-12 um thermal channel |
| SWIR Sensor Operating Mode | InGaAs Detector Array (0.9-1.7 um) | State Enum | Multi-spectral laser spot tracking active |

#### Standard Specification
| Metric ID | Subsystem Domain | Metric Name / Description | Threshold Value | Objective Value | Unit | Bus Protocol / Interface | Timeout Bound |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MET-03-S01 | Payload & Gimbal | Optical Boresight Jitter Under Wind Shear (RMS) | <= 0.02 | <= 0.008 | deg RMS | RS-422 / CAN Gimbal Bus | Continuous @ 100 Hz |
| MET-03-S02 | Payload & Gimbal | Gimbal Servo Actuator Temperature (T_servo) | <= 65.0 | <= 50.0 | °C | CAN 2.0B / Digital Thermistor | Continuous @ 20 Hz |
| MET-03-S03 | Payload & Gimbal | MWIR NUC Shutter Calibration Interval | <= 300.0 | <= 180.0 | s | Payload Serial Control Link | t_nuc <= 300.0 s |
| MET-03-S04 | Payload & Gimbal | MWIR Detector Cryocooler Lock Temperature | <= 77.0 | <= 72.0 | K | Cryo Controller Serial Bus | t_cool <= 180.0 s |
| MET-03-S05 | Payload & Gimbal | Gimbal Dynamic Pan/Tilt Slew Rate | >= 60.0 | >= 120.0 | deg/s | RS-422 Serial Driver | t_slew <= 500.0 ms |
| MET-03-S06 | Flight Guidance & Aerodynamics | Loiter Orbit Radius Deviation (abs(R - 300.0)) | <= 5.0 | <= 1.0 | m | Autopilot CAN / Mavlink v2 | Continuous @ 250 Hz |
| MET-03-S07 | Flight Guidance & Aerodynamics | Coordinated Turn Bank Angle Stability | <= 35.0 | <= 25.0 | deg | Autopilot Attitude Loop | Continuous @ 250 Hz |
| MET-03-S08 | Search & Surveillance | Autonomous Search Pattern Area Coverage Rate (A_dot_cov) | >= 50.0 | >= 75.0 | km^2/hr | Flight Mission Computer | Continuous @ 1 Hz |
| MET-03-S09 | Search & Surveillance | Multi-Spectral Sensor Fusion Processing Latency | <= 33.3 | <= 15.0 | ms | Onboard Vision DSP Pipeline | Continuous @ 30 FPS |
| MET-03-S10 | Vision & Mission Computer | Optical Target Centering Error | <= 15.0 | <= 3.0 | pixels | GigE Vision / RTSP | <= 33.3 ms (30 FPS) |
| MET-03-S11 | Vision & Mission Computer | Video Stream H.265 Frame Rate | >= 30 | >= 60 | FPS | 1000BASE-T Ethernet | Frame interval <= 33.3 ms |
| MET-03-S12 | Vision & Mission Computer | Video Telemetry Timestamp Synchronization Skew | <= 10.0 | <= 2.0 | ms | Precision Time Protocol (PTP) | Skew <= 10.0 ms |
| MET-03-S13 | Vision & Mission Computer | Edge Neural Object Detector Inference Latency | <= 33.3 | <= 15.0 | ms | Onboard NPU / Tensor Core | Continuous @ 30 FPS |
| MET-03-S14 | C2 & Datalink | Downlink Video Payload Data Rate | >= 8.0 | >= 15.0 | Mbps | 5.8 GHz COFDM Modem | Continuous @ 30 FPS |

#### Verification Specification
| Verification Attribute | Detail Specification |
| :--- | :--- |
| Verification Method | Telemetry, High-Resolution Video Frame Analysis, Area Search Coverage Mapping, and Gimbal Thermal Telemetry Audit |
| Evidence Artifact | `tests/surveillance_orbit_test.py` -> `logs/gimbal_pointing_metrics.json`, `logs/mwir_calibration_log.json`, and `logs/search_coverage_report.json` |
| Acceptance Criteria | Multi-subsystem conjunction during on-station orbit and area search execution:<br>1. **Payload & Gimbal:** Optical boresight jitter <= 0.02 deg RMS under dynamic wind shear <= 12.0 m/s; gimbal servo actuator temperature <= 65.0 °C; MWIR NUC calibration executed at interval <= 300.0 s without video frame dropping; cryocooler maintained at T <= 77.0 K; dynamic slew rate >= 60.0 deg/s.<br>2. **Search Patterns & Coverage:** Expanding Square, Creeping Line, and Sector Scan patterns achieve cumulative area coverage rate A_dot_cov >= 50.0 km^2/hr with zero unmapped gaps.<br>3. **Multi-Spectral Fusion & Vision:** Multi-spectral fusion (4K EO + MWIR 3-5 um + LWIR 8-12 um + SWIR 0.9-1.7 um) processed with latency <= 33.3 ms at >= 30 FPS; optical target centering error <= 15.0 pixels; video telemetry sync skew <= 10.0 ms; edge NPU inference latency <= 33.3 ms.<br>4. **Flight Guidance & Aerodynamics:** Vehicle maintains circular orbit within 300.0 m +/- 5.0 m with coordinated turn bank angle <= 35.0 deg.<br>5. **C2 & Datalink:** Downlink payload video stream >= 8.0 Mbps with packet error rate <= 10^-4. |
| Pass / Fail Threshold | `abs(R_actual - 300.0) <= 5.0 m`, `A_dot_cov >= 50.0 km^2/hr`, `jitter_RMS <= 0.02 deg`, `T_servo <= 65.0 °C`, and `t_nuc <= 300.0 s`. |
| Traceability | `/// OperationalAllocation: [MET-03]` \| NATO STANAG 4586 Annex B §3.2 \| NATO STANAG 3733 Edition 2 \| INCOSE SEH v5.0 §3.2 \| MIL-STD-810H Method 501.7 |

---

### 2.4 MET-04: DynamicAirspaceDeconfliction

Formal specification for onboard Detect and Avoid (DAA) surveillance, high-rate 77 GHz FMCW radar tracking, low-latency ADS-B message decoding, high-resolution vertical rate estimation per RTCA DO-365B, multi-sensor kinematic track fusion, Well-Clear separation assurance, and autonomous collision avoidance maneuvering.

#### Condition Specification
| Parameter | Condition Value / State | Engineering Unit | Validation Rule |
| :--- | :--- | :--- | :--- |
| Operational State | Active Airspace Monitoring | State Enum | DAA subsystem initialized and tracking |
| Airspace Classification | Class G / Class E (Unsegregated) | Airspace Enum | Mixed cooperative and non-cooperative traffic |
| Cooperative Sensing System | Dual ADS-B In (1090 MHz / 978 UAT) | Hardware State | Operational receiver RF status |
| Non-Cooperative Sensing System | 77 GHz FMCW Radar + EO/IR DAA | Hardware State | Operational multi-mode radar transceiver |
| Multi-Sensor Track Fusion Pipeline | Centralized Extended Kalman Filter | Software State | Real-time state vector fusion active |
| Intruder Closure Velocity | Up to 150.0 | m/s | Maximum relative approach speed |
| Well-Clear Boundary (RTCA DO-365B) | DMOD = 1200.0 m, ZTHR = 137.0 m | Geometrical Vol | Declared Well-Clear separation volume |

#### Standard Specification
| Metric ID | Subsystem Domain | Metric Name / Description | Threshold Value | Objective Value | Unit | Bus Protocol / Interface | Timeout Bound |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MET-04-S01 | DAA Radar Subsystem | 77 GHz FMCW Radar Track State Update Rate (f_radar) | >= 20.0 | >= 50.0 | Hz | 100BASE-T1 / High-Speed SPI | dt <= 50.0 ms |
| MET-04-S02 | DAA Surveillance | ADS-B In Message Processing & Decode Latency | <= 100.0 | <= 30.0 | ms | 1090 MHz RF Front-End / UART | t_adsb <= 100.0 ms |
| MET-04-S03 | DAA Surveillance | DO-365B Intruder Vertical Rate Resolution (dz/dt) | <= 0.20 | <= 0.05 | m/s | DAA Kinematic Tracker Bus | dt <= 50.0 ms |
| MET-04-S04 | DAA Surveillance | Multi-Sensor Track Fusion Kinematic Update Rate | >= 20.0 | >= 50.0 | Hz | Real-Time Fusion Coprocessor | dt <= 50.0 ms |
| MET-04-S05 | Well-Clear Assurance | Horizontal Well-Clear Separation Distance (DMOD) | >= 1200.0 | >= 1500.0 | m | ARINC 429 / Ethernet | Continuous @ 20 Hz |
| MET-04-S06 | Well-Clear Assurance | Vertical Well-Clear Separation Distance (ZTHR) | >= 137.0 (450 ft) | >= 200.0 | m | ARINC 429 / Ethernet | Continuous @ 20 Hz |
| MET-04-S07 | Well-Clear Assurance | Modified Tau Time-to-CPA Threshold (tau_mod) | >= 35.0 | >= 55.0 | s | DAA Kinematics Engine | Continuous @ 20 Hz |
| MET-04-S08 | Collision Avoidance | Intruder Conflict Detection & Correlation Latency | <= 500.0 | <= 100.0 | ms | High-Speed CAN / Ethernet | t_corr <= 500.0 ms |
| MET-04-S09 | Collision Avoidance | Autonomous Escape Maneuver Command Latency | <= 1.0 | <= 0.25 | s | Autopilot Command Bus | t_maneuver <= 1.0 s |
| MET-04-S10 | Collision Avoidance | Well-Clear Recovery Hysteresis Duration | >= 10.0 | >= 15.0 | s | State Machine Timer | tau_hysteresis >= 10.0 s |
| MET-04-S11 | Flight Guidance & Control | Avoidance Maneuver Normal Acceleration Limit | <= 2.50 | <= 1.80 | g | Autopilot Inner Loop | Continuous @ 250 Hz |
| MET-04-S12 | C2 & DAA Telemetry | Conflict Alert & Resolution Advisory Telemetry Broadcast | <= 250.0 | <= 50.0 | ms | PACE C2 Datalink / Mavlink v2 | t_alert <= 250.0 ms |

#### Verification Specification
| Verification Attribute | Detail Specification |
| :--- | :--- |
| Verification Method | DAA Multi-Sensor Hardware-in-the-Loop Simulation & RTCA DO-365B Encounter Review |
| Evidence Artifact | `tests/daa_separation_sim.py` -> `logs/daa_encounter_results.json` and `logs/radar_adsb_telemetry.csv` |
| Acceptance Criteria | Multi-subsystem conjunction for airspace deconfliction:<br>1. **Radar & Surveillance:** 77 GHz radar track update rate f >= 20.0 Hz; ADS-B In message decode latency <= 100.0 ms; DO-365B vertical rate resolution dz/dt <= 0.2 m/s; multi-sensor track fusion rate >= 20.0 Hz.<br>2. **Well-Clear Assurance:** Zero incursions below Well-Clear volume (DMOD >= 1200.0 m, ZTHR >= 137.0 m, tau_mod >= 35.0 s) across all 24 RTCA DO-365B standard encounter stress vectors.<br>3. **Collision Avoidance & Guidance:** Conflict correlation <= 500.0 ms; autonomous escape maneuver command issued in <= 1.0 s with normal acceleration load factor <= 2.5 g; recovery hysteresis >= 10.0 s.<br>4. **C2 & Telemetry:** Conflict alert and advisory telemetry broadcast to GCS in <= 250.0 ms. |
| Pass / Fail Threshold | `min(D_horizontal) >= 1200.0 m` or `min(abs(H_vertical)) >= 137.0 m`, with `f_radar >= 20.0 Hz`, `t_adsb <= 100.0 ms`, and `dz/dt <= 0.2 m/s`. |
| Traceability | `/// OperationalAllocation: [MET-04]` \| RTCA DO-365B §2.2.4 \| NATO STANAG 4586 Annex B §3.3 \| FAA AC 90-114B |

---

### 2.5 MET-05: ElectronicCounterCountermeasures

Formal specification for electronic counter-countermeasures (ECCM), multi-band GNSS anti-jam mitigation, Controlled Radiation Pattern Antenna (CRPA) adaptive nulling, GPS-denied dead-reckoning navigation bounding, automated PACE communication tier failover, and hardware cryptographic session protection under severe electronic warfare threats.

#### Condition Specification
| Parameter | Condition Value / State | Engineering Unit | Validation Rule |
| :--- | :--- | :--- | :--- |
| Operational State | Contested Electromagnetic Spectrum | State Enum | Airborne mission execution |
| RF Electronic Attack Environment | Broadband / Sweep Jamming | EW Vector | Jammer-to-Signal ratio J/S >= 35.0 dB |
| GNSS Deception Environment | Multi-Satellite Pseudorange Spoofing | EW Vector | Innovation gating residual gamma_k > 16.27 |
| CRPA Antenna System | 4-Element Adaptive Array | Hardware State | Digital beamforming receiver online |
| Dead-Reckoning Navigation State | GPS-Denied Degraded Mode | State Enum | EKF INS + Optical Flow / Visual Odometry |
| Primary Communications Link | 5.8 GHz COFDM Datalink | PACE Tier 1 | High-bandwidth payload link |
| Fallback Communications Links | 915 MHz FHSS / Cellular LTE / SATCOM | PACE Tiers 2-4 | Multi-tier failover channels |

#### Standard Specification
| Metric ID | Subsystem Domain | Metric Name / Description | Threshold Value | Objective Value | Unit | Bus Protocol / Interface | Timeout Bound |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MET-05-S01 | EW & Navigation Resiliency | GNSS Jammer-to-Signal (J/S) Anti-Jam Threshold | >= 35.0 | >= 45.0 | dB | Multi-Band RF Front-End | Continuous @ 50 Hz |
| MET-05-S02 | EW & Navigation Resiliency | CRPA Digital Beamforming Spatial Nulling Depth | >= 25.0 | >= 35.0 | dB | 4-Element CRPA Receiver | Continuous @ 100 Hz |
| MET-05-S03 | EW & Navigation Resiliency | Dead-Reckoning Navigation Drift Over 60 s Outage | <= 0.50 | <= 0.15 | % Distance | EKF INS / Optical Flow Bus | t_outage = 60.0 s |
| MET-05-S04 | EW & Navigation Resiliency | GNSS Spoofing Detection & Rejection Latency | <= 100.0 | <= 20.0 | ms | RAIM / Chi-Square Gating | t_reject <= 100.0 ms |
| MET-05-S05 | EW & Navigation Resiliency | Multi-Sensor Dead-Reckoning Loop Rate | >= 250 | >= 500 | Hz | High-Speed SPI / Real-Time OS | dt <= 4.0 ms |
| MET-05-S06 | C2 & Datalink (PACE) | PACE Tier Link Failover Execution Time (t_switch) | <= 1.0 | <= 0.20 | s | Serial SPI / High-Speed UART | t_switch <= 1.0 s |
| MET-05-S07 | C2 & Datalink (PACE) | 915 MHz FHSS Alternate Link Sync Re-Lock Time | <= 500.0 | <= 100.0 | ms | Frequency Hopping Modem | t_sync <= 500.0 ms |
| MET-05-S08 | C2 & Datalink (PACE) | RF Front-End AGC Saturation & Jamming Alarm Latency | <= 50.0 | <= 10.0 | ms | Baseband DSP / CAN 2.0B | t_alarm <= 50.0 ms |
| MET-05-S09 | Security & Cryptography | Cryptographic Session Rekeying Duration | <= 250.0 | <= 50.0 | ms | AES-256-GCM Hardware Core | t_rekey <= 250.0 ms |
| MET-05-S10 | Flight Guidance & Control | Degraded Navigation Geofence Buffer Inflation | >= 100.0 | >= 200.0 | m | Safety Simplex Coprocessor | Continuous @ 50 Hz |

#### Verification Specification
| Verification Attribute | Detail Specification |
| :--- | :--- |
| Verification Method | Anechoic RF Jamming Chamber Injection, GPS Spoofing HIL Emulation, and Optical Flow Odometry Navigation Test |
| Evidence Artifact | `tests/pace_failover_test.py` -> `logs/eccm_mitigation_record.json` and `logs/dead_reckoning_drift_eval.csv` |
| Acceptance Criteria | Multi-subsystem conjunction under EW attack:<br>1. **EW & Navigation Resiliency:** GNSS receiver maintains tracking under J/S >= 35.0 dB; CRPA spatial nulling depth >= 25.0 dB; dead-reckoning drift <= 0.5% total distance traveled during a continuous 60.0 s complete GNSS outage; GNSS spoofing detected and rejected within 100.0 ms.<br>2. **PACE C2 Failover:** Autonomous link failover to Tier 2 FHSS completed within t_switch <= 1.0 s of primary link disruption; 915 MHz link synchronization <= 500.0 ms; AGC jamming alarm raised in <= 50.0 ms.<br>3. **Security & Cryptography:** AES-256-GCM hardware session rekeying executed in <= 250.0 ms.<br>4. **Guidance & Safety:** Safety geofence buffer inflated by >= 100.0 m during GPS-denied operation. |
| Pass / Fail Threshold | `J_S_margin >= 35.0 dB`, `null_depth >= 25.0 dB`, `drift_rate <= 0.005 * distance_traveled` over 60 s outage, and `t_switch <= 1.0 s`. |
| Traceability | `/// OperationalAllocation: [MET-05]` \| MIL-STD-461G RS103 §4.3 \| RTCA DO-362A §3.4 \| NATO STANAG 4586 Annex B §3.4 |

### 2.6 MET-06: PrecisionTargetMensuration

Formal specification for geo-spatial target coordinate mensuration, NATO STANAG 3733 Band I/II laser PRF coding (codes 1111–1788), laser beam divergence ($\le 0.3\text{ mrad}$), boresight collimation alignment ($\le 0.05^\circ$), high-density EO/IR/SWIR focal plane array metrology (12.0 µm pixel pitch), real-time atmospheric extinction compensation, line-of-sight vector kinematics, digital elevation model mapping, Target Location Error (TLE CEP90 $\le 2.5\text{ m}$) bounding across the Target Classification Taxonomy (Fixed Hardened Infrastructure, Moving Surface Vehicle, HVT, Pop-up Threat), and rapid Battle Damage Assessment (BDA) verification with telemetry offload within $\tau_{\mathrm{BDA}} \le 30.0\text{ s}$.

#### Condition Specification
| Parameter | Condition Value / State | Engineering Unit | Validation Rule |
| :--- | :--- | :--- | :--- |
| Operational State | Target Acquisition, Laser Designation & BDA | State Enum | Gimbal in `TRACK_TARGET`, `LASER_DESIGNATE`, `BDA_VERIFY` |
| Target Taxonomy Scope | Classes 1 to 4 | Taxonomy Enum | Fixed Infrastructure, Moving Vehicle, HVT, Pop-up Threat |
| Slant Range to Target (Range_target) | 1000.0 to 3000.0 | m | Laser rangefinder / designator operational envelope |
| Digital Terrain Elevation Data (DTED) | Level 3 (1.0 m grid resolution) | Resolution | Onboard high-resolution DEM loaded |
| Laser Designation & Ranging Subsystem | STANAG 3733 Band I (1064 nm) / Band II Pulsed Diode | Hardware State | Operational firing state |
| NATO Laser PRF Coding Allocation | STANAG 3733 Band I/II Codes (1111 to 1788) | Code Enum | Mission-assigned 3-digit / 4-digit PRF code locked |
| Laser Beam Optical Divergence | <= 0.30 | mrad | Tight spot containment (d_spot <= 0.90 m at 3.0 km) |
| Laser to EO/IR Boresight Collimation | <= 0.05 | deg | Mechanical/optical alignment error bound |
| EO/IR/SWIR Detector Specifications | 12.0 um Pixel Pitch Focal Plane Array | Hardware State | Fused MWIR / LWIR / SWIR sensor suite |
| Atmospheric Visibility Condition | Meteorological Optical Range >= 5.0 km | Visibility | Real-time extinction correction active |
| BDA Assessment Mode | Pre/Post-Strike Mensuration & Radiometric Dissipation | State Enum | Active BDA physical/thermal/functional verification |
| Vehicle Navigation Covariance Norm | <= 0.50 | m | EKF state position uncertainty |

#### Standard Specification
| Metric ID | Subsystem Domain | Metric Name / Description | Threshold Value | Objective Value | Unit | Bus Protocol / Interface | Timeout Bound |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MET-06-S01 | Laser Designation | STANAG 3733 Laser PRF Code Modulation & Timing Jitter | <= 10.0 | <= 2.0 | ns | High-Speed Pulse Driver Bus | Continuous @ PRF |
| MET-06-S02 | Laser Designation | Laser Rangefinder / Designator Pulse Repetition Frequency | 10.0 | 20.0 | Hz | RS-422 / High-Speed Serial | Continuous @ 10 Hz |
| MET-06-S03 | Laser Designation | Laser Optical Beam Divergence (theta_div) | <= 0.30 | <= 0.15 | mrad | Optical Boresight Assembly | Beam quality metric |
| MET-06-S04 | Laser Designation | Laser Transmitter to EO/IR Boresight Collimation Alignment | <= 0.05 | <= 0.01 | deg | Optical Boresight Register | Continuous @ 100 Hz |
| MET-06-S05 | Laser Designation | Laser Range Measurement Accuracy at 3.0 km Slant Range | <= 0.50 | <= 0.15 | m | LRF Serial Interface | Range = 3.0 km |
| MET-06-S06 | EO/IR/SWIR Metrology | EO/IR/SWIR Focal Plane Array Pixel Pitch | 12.0 | 10.0 | um | Sensor Core Specification | Hardware Architecture |
| MET-06-S07 | EO/IR/SWIR Metrology | Atmospheric Extinction Coefficient Correction Rate | >= 10.0 | >= 25.0 | Hz | Radiometric DSP Pipeline | dt <= 100.0 ms |
| MET-06-S08 | Target Mensuration | Target Location Error (TLE CEP90) at 3.0 km Slant Range | <= 2.50 | <= 1.00 | m | STANAG 4586 DLI / RS-422 | Range = 3.0 km |
| MET-06-S09 | Target Mensuration | Line-of-Sight Kinematic Coordinate Transform Rate | >= 50.0 | >= 100.0 | Hz | Real-Time Vector Math Unit | dt <= 20.0 ms |
| MET-06-S10 | Target Mensuration | Mensuration Solution Convergence Time | <= 500.0 | <= 100.0 | ms | Mission Computer Bus | t_mens <= 500.0 ms |
| MET-06-S11 | AI & Computer Vision | Multi-Spectral Target Classification Confidence (C_PID) | >= 0.95 | >= 0.99 | Dimensionless | Edge Neural Classifier | Inference <= 33.3 ms |
| MET-06-S12 | Battle Damage Assessment | BDA Physical Structural Displacement Mensuration Resolution | <= 0.20 | <= 0.05 | m | Stereoscopic 3D Mensuration | Post-strike scan |
| MET-06-S13 | Battle Damage Assessment | BDA Thermal Heat Bloom Dissipation Radiometric Sampling Rate | >= 10.0 | >= 30.0 | Hz | MWIR/LWIR Radiometric Core | Continuous post-strike |
| MET-06-S14 | Battle Damage Assessment | BDA Post-Strike Telemetry & Imagery Offload Time (tau_BDA) | <= 30.0 | <= 10.0 | s | 5.8 GHz / 915 MHz C2 Datalink | tau_BDA <= 30.0 s |

#### Verification Specification
| Verification Attribute | Detail Specification |
| :--- | :--- |
| Verification Method | Surveyed DGPS Ground Target Calibration, STANAG 3733 Laser Receiver Energy / PRF Validation, Atmospheric Extinction Chamber Model, BDA Multi-Spectral Imaging Audit, and Flight Telemetry Review |
| Evidence Artifact | `tests/target_mensuration_test.py` -> `logs/mensuration_accuracy_log.json`, `logs/stanag3733_prf_validation.json`, and `logs/bda_assessment_report.json` |
| Acceptance Criteria | Exhaustive multi-subsystem conjunction for precision target mensuration, laser designation, and BDA verification:<br>1. **Laser Designation & STANAG 3733:** Laser PRF code modulation compliant with NATO STANAG 3733 Band I/II (codes 1111..1788) with pulse timing jitter <= 10.0 ns; beam divergence <= 0.30 mrad; boresight collimation alignment <= 0.05 deg; range measurement accuracy <= 0.50 m at 3.0 km slant range.<br>2. **Target Classification & PID:** Multi-spectral classification confidence C_PID >= 0.95 across Fixed Hardened Infrastructure, Moving Surface Vehicle, High-Value Target (HVT), and Pop-up Threat categories; EO/IR/SWIR pixel pitch <= 12.0 um; atmospheric extinction compensation active at >= 10.0 Hz.<br>3. **Precision Mensuration:** Target Location Error TLE CEP90 <= 2.50 m at 3.0 km standoff range; solution convergence time <= 500.0 ms; LOS kinematic transform rate >= 50.0 Hz.<br>4. **Battle Damage Assessment (BDA):** Structural displacement detection resolution <= 0.20 m (confirming physical displacement Delta_S >= 0.50 m); thermal heat bloom dissipation monitored at >= 10.0 Hz with verified negative temperature gradient; functional kill verification (M-kill, F-kill, K-kill) completed; complete BDA telemetry and imagery report offloaded over C2 link within tau_BDA <= 30.0 s post-strike. |
| Pass / Fail Threshold | `TLE_CEP90 <= 2.5 m` at `Range_target == 3000.0 m`, `theta_div <= 0.3 mrad`, `boresight_alignment <= 0.05 deg`, `STANAG_3733_PRF in [1111, 1788]`, `C_PID >= 0.95`, and `tau_BDA <= 30.0 s`. |
| Traceability | `/// OperationalAllocation: [MET-06]` \| NATO STANAG 3733 Edition 2 \| NATO STANAG 4586 Annex B §3.5 \| CJCSI 3121.01B Enc A §4.b \| MIL-STD-882E §4.3 \| ISO/IEC/IEEE 29148:2018 §6.4.2 |

---

### 2.7 MET-07: AutonomousBingoReturnDivert

Formal specification for real-time onboard energy consumption modeling, dynamic closed-loop battery internal resistance thermal compensation, headwind gradient vector integration, energy-optimal Specific Air Range (SAR) trajectory routing, autonomous return-to-base (RTB) or secondary divert execution, and strict statutory energy reserve preservation (E_reserve >= 216.0 kJ).

#### Condition Specification
| Parameter | Condition Value / State | Engineering Unit | Validation Rule |
| :--- | :--- | :--- | :--- |
| Operational State | In-Flight Energy Management | State Enum | Continuous background monitor |
| Total Nominal Energy Capacity (E_capacity) | 1080000.0 (300.0 Wh) | J | 6S 14Ah nominal energy pack |
| Minimum Statutory Reserve Energy (E_reserve) | 216000.0 (60.0 Wh) | J | Strict 20.0% statutory reserve threshold |
| Battery Cell Operating Temperature | -10.0 to +55.0 | °C | Thermal range for internal resistance model |
| Headwind Gradient Vector Profile | Up to 15.0 m/s with shear dV/dz | Vector Profile | Real-time wind field integration |
| Primary Recovery Site (LZ-PRIMARY) | Geodetic Coordinates | Waypoint ID | Distance d_primary <= 15.0 km |
| Secondary Divert Recovery Site (LZ-DIVERT) | Geodetic Coordinates | Waypoint ID | Distance d_divert <= 5.0 km |

#### Standard Specification
| Metric ID | Subsystem Domain | Metric Name / Description | Threshold Value | Objective Value | Unit | Bus Protocol / Interface | Timeout Bound |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MET-07-S01 | Power & BMS | Dynamic Battery Internal Resistance Thermal Compensation | Active (R_i(T)) | Arrhenius Model | Model State | Smart BMS / CAN 2.0B | Update @ 20 Hz |
| MET-07-S02 | Power & BMS | Statutory Energy Reserve at Recovery Touchdown | >= 216.0 (20%) | >= 270.0 (25%) | kJ | Smart BMS Telemetry | At touchdown |
| MET-07-S03 | Power & BMS | Closed-Loop Energy Coulomb-Counting Accuracy | <= 1.5 | <= 0.5 | % | Current Integrator / Shunt | Continuous @ 50 Hz |
| MET-07-S04 | Power & BMS | Minimum Cell Cutoff Voltage Under Return Load | >= 3.30 | >= 3.45 | V/cell | BMS Analog Front-End | Continuous @ 50 Hz |
| MET-07-S05 | Flight Guidance & Trajectory | Headwind Gradient Vector Integration Update Rate | >= 10.0 | >= 25.0 | Hz | ADU / Path Planner Bus | dt <= 100.0 ms |
| MET-07-S06 | Flight Guidance & Trajectory | Specific Air Range (SAR) Optimal Speed Computation Rate | >= 10.0 | >= 50.0 | Hz | Path Planning Coprocessor | dt <= 100.0 ms |
| MET-07-S07 | Flight Guidance & Trajectory | Autonomous Return / Divert Trigger Latency (t_resp) | <= 200.0 | <= 50.0 | ms | Flight Executive State Machine | t_resp <= 200.0 ms |
| MET-07-S08 | Flight Guidance & Trajectory | Alternate Secondary Divert Path Optimization Time | <= 100.0 | <= 20.0 | ms | Trajectory Planner Memory Bus | t_plan <= 100.0 ms |
| MET-07-S09 | Propulsion & Motor Drive | Return Transit Propulsion Efficiency (eta_prop) | >= 75.0 | >= 82.0 | % | ESC Telemetry / Power Monitor | Continuous @ 50 Hz |
| MET-07-S10 | C2 & Safety Alerting | Bingo Low-Energy Alert GCS Broadcast Latency | <= 500.0 | <= 100.0 | ms | PACE C2 Datalink | t_c2 <= 500.0 ms |

#### Verification Specification
| Verification Attribute | Detail Specification |
| :--- | :--- |
| Verification Method | Battery Management System Telemetry Audit, Dynamic R_i(T) Thermal Chamber Validation, and Autonomous Divert 6-DOF Flight Sim |
| Evidence Artifact | `tests/bingo_energy_math_test.py` -> `logs/bingo_divert_profile.csv` and `logs/bms_thermal_compensation.json` |
| Acceptance Criteria | Multi-subsystem conjunction for autonomous return and divert:<br>1. **Power & BMS:** Dynamic closed-loop battery internal resistance thermal compensation R_i(T) active at >= 20 Hz; touchdown residual reserve energy >= 216.0 kJ (>= 20.0% of nominal 1080.0 kJ pack); Coulomb-counting error <= 1.5%; cell voltage >= 3.30 V/cell under cruise return throttle.<br>2. **Guidance & Trajectory:** Atmospheric headwind gradient vector integrated along trajectory at >= 10.0 Hz; autonomous RTB or secondary divert trigger executed in t_resp <= 200.0 ms when E_current <= E_bingo; divert route optimization <= 100.0 ms.<br>3. **Propulsion:** Return transit propulsion system efficiency eta_prop >= 75.0%.<br>4. **C2 & Safety Alerting:** Low-energy Bingo alert transmitted to GCS within <= 500.0 ms. |
| Pass / Fail Threshold | `E_touchdown >= 216.0 kJ`, `t_response <= 200.0 ms`, with active dynamic R_i(T) compensation and wind gradient vector integration. |
| Traceability | `/// OperationalAllocation: [MET-07]` \| JARUS SORA v2.5 Annex E §2.1 \| EASA GM1 UAS.SPEC.050(1)(g) \| NATO STANAG 4586 Annex B §3.6 |

---

### 2.8 MET-08: PostMissionDataOffloadShutdown

Formal specification for post-touchdown stationary state validation, NIST SP 800-88r1 compliant cryptographic key and volatile data zeroization, active DC power bus capacitor bleed discharge to safe voltage, post-flight motor thermal soak bounding, high-speed flight telemetry offload, and deterministic safe electrical isolation.

#### Condition Specification
| Parameter | Condition Value / State | Engineering Unit | Validation Rule |
| :--- | :--- | :--- | :--- |
| Operational State | Landed & Stationary on Pad | State Enum | Weight-on-wheels interlock confirmed active |
| Propulsion System State | Disarmed / Motor PWM Inhibited | Motor State | ESC gate drive hardware interlock engaged |
| Motor Stator Temperature Envelope | Ambient to 100.0 | °C | Thermal soak monitoring after touchdown |
| DC Power Bus Voltage | Nominal 22.2 to 25.2 down to safe cutoff | V | Active bus discharge circuit engaged |
| Ground Offload Interface | Gigabit Ethernet / USB 3.0 / Optical | Interface | Ground Support Equipment connected |
| Security Key State | Active Session Ephemeral Keys & Logs | Crypto State | Cryptographic volatile storage |

#### Standard Specification
| Metric ID | Subsystem Domain | Metric Name / Description | Threshold Value | Objective Value | Unit | Bus Protocol / Interface | Timeout Bound |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MET-08-S01 | Security & Cryptography | Cryptographic Key & Log Zeroization Time (NIST SP 800-88r1) | <= 10.0 | <= 0.50 | s | Hardware Cryptographic Unit | t_zeroize <= 10.0 s |
| MET-08-S02 | Security & Cryptography | Volatile Memory Overwrite Verification Pass Rate | 100.0 | 100.0 | % | NIST SP 800-88r1 Clear Pattern | Single Pass 0x00/0xFF |
| MET-08-S03 | Security & Cryptography | Security Tamper Log Cryptographic Seal Generation | <= 200.0 | <= 50.0 | ms | TPM 2.0 PCR Signing | t_seal <= 200.0 ms |
| MET-08-S04 | Electrical Power & DC Bus | DC Bus Capacitor Discharge Time to V_bus < 5.0 V | <= 5.0 | <= 2.0 | s | Active Bleed Circuit / Shunt | t_discharge <= 5.0 s |
| MET-08-S05 | Electrical Power & DC Bus | Residual Post-Shutdown DC Bus Voltage (V_bus) | < 5.0 | < 1.0 | V | Power Distribution Telemetry | At t = 5.0 s |
| MET-08-S06 | Electrical Power & DC Bus | Main Power Contactor Isolation Disconnect Time | <= 50.0 | <= 10.0 | ms | Solid-State Power Switch | t_isolate <= 50.0 ms |
| MET-08-S07 | Propulsion & Thermal | Post-Flight Motor Stator Thermal Soak Limit (T_motor) | <= 60.0 | <= 45.0 | °C | CAN 2.0B / Motor Thermistor | Soak window <= 300 s |
| MET-08-S08 | Propulsion & Thermal | ESC Heat Sink Thermal Dissipation Monitor | <= 55.0 | <= 40.0 | °C | CAN 2.0B / ESC NTC Sensor | Soak window <= 300 s |
| MET-08-S09 | Avionics & Ground Offload | Flight Log & Telemetry Offload Duration (64 GB) | <= 60.0 | <= 20.0 | s | Gigabit Ethernet / USB 3.0 | t_offload <= 60.0 s |
| MET-08-S10 | Avionics & Ground Offload | Post-Flight Structural BIT (SBIT) Pass Rate | 100.0 | 100.0 | % Pass | CAN 2.0B Health Bus | t_sbit <= 5.0 s |
| MET-08-S11 | Avionics & Ground Offload | Safe Electrical Isolation Latch Confirmation | <= 10.0 | <= 3.0 | s | Power Distribution Controller | t_shutdown <= 10.0 s |

#### Verification Specification
| Verification Attribute | Detail Specification |
| :--- | :--- |
| Verification Method | Security Audit Log Verification, NIST SP 800-88r1 Memory Forensics, Bus Voltage Oscilloscope Measurement, and Motor Thermal Imaging Audit |
| Evidence Artifact | `tests/crypto_zeroization_test.py` -> `logs/zeroization_audit_log.json` and `logs/post_flight_electrical_thermal.json` |
| Acceptance Criteria | Multi-subsystem conjunction for safe shutdown and offload:<br>1. **Security & Cryptography:** All mission cryptographic keys and ephemeral memory zeroized in t_zeroize <= 10.0 s in accordance with NIST SP 800-88r1; memory overwrite pass rate = 100.0%; TPM 2.0 tamper log seal generated in <= 200.0 ms.<br>2. **Electrical Power & DC Bus:** DC bus capacitor active bleed circuit discharges bus to V_bus < 5.0 V within <= 5.0 s; main power contactor isolation disconnect <= 50.0 ms; complete safe electrical system isolation confirmed in <= 10.0 s.<br>3. **Propulsion & Thermal:** Motor stator core temperature does not exceed thermal soak limit T_motor <= 60.0 °C post touchdown; ESC heat sink temperature <= 55.0 °C.<br>4. **Avionics & Ground Offload:** 64 GB flight log and payload telemetry offloaded via GSE Gigabit Ethernet in <= 60.0 s; post-flight SBIT pass rate = 100.0%. |
| Pass / Fail Threshold | `t_zeroize <= 10.0 s`, `V_bus < 5.0 V` at `t <= 5.0 s`, `T_motor <= 60.0 °C`, and `t_offload <= 60.0 s` with zero uncommitted transactions. |
| Traceability | `/// OperationalAllocation: [MET-08]` \| NIST SP 800-88r1 §2.4 \| DoD Directive 3000.09 §3.1.c \| MIL-STD-882E §4.3 |

---

### 2.9 METL Execution Invariants
1. **Deterministic State Progression:** Progression from `MET-01` through `MET-08` is governed by discrete finite-state transitions in the flight executive.
2. **Allocation Tag Integrity:** Every task defined in the METL table carries an inviolable Gate 24 allocation tag (`/// OperationalAllocation: [MET-XX]`) mapped downstream to SysML v2 architectural activity blocks.
3. **Safety Interlock Coupling:** Non-compliance with standard metrics in tasks `MET-01` through `MET-07` initiates deterministic degraded mode failsafes in accordance with Section 8 (Go/No-Go Decision Matrix).
