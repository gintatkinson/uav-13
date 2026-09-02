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
| `MET-02` | AutonomousIngressTransit | En-route corridor navigation under active flight plan | Lateral cross-track error e_xtrack <= 2.0 m, vertical error e_z <= 1.0 m | Flight Navigation Log Review | `/// OperationalAllocation: [MET-02]` | RTCA DO-365B §2.2.3 |
| `MET-03` | AreaSurveillanceOrbit | On-station target tracking within designated geographic boundary | Orbit radius R_orbit = 300.0 m +/- 5.0 m, payload pointing jitter <= 0.05 deg | Telemetry & Video Frame Analysis | `/// OperationalAllocation: [MET-03]` | NATO STANAG 4586 Annex B §3.2 |
| `MET-04` | DynamicAirspaceDeconfliction | Traffic conflict geometry detected by onboard DAA sensors | Maintain Well-Clear separation (D_horizontal >= 1200.0 m, H_vertical >= 137.0 m) | DAA Collision Event Log Review | `/// OperationalAllocation: [MET-04]` | RTCA DO-365B §2.2.4 |
| `MET-05` | ElectronicCounterCountermeasures | Jamming or intentional RF / navigation spoofing detected | Seamless PACE tier switch t_switch <= 1.0 s, dead-reckoning drift <= 1.0% distance | RF Signal Log & Navigation Test | `/// OperationalAllocation: [MET-05]` | MIL-STD-461G RS103 §4.3 |
| `MET-06` | PrecisionTargetMensuration | Target identified within optical/infrared payload field of view | Target Location Error TLE_CEP90 <= 2.5 m at slant range Range_target = 3.0 km | Optical Mensuration Calibration Log | `/// OperationalAllocation: [MET-06]` | NATO STANAG 4586 Annex B §3.5 |
| `MET-07` | AutonomousBingoReturnDivert | Energy monitoring detects current energy E_current <= E_bingo threshold | Autonomous RTB or divert trigger t_resp <= 200.0 ms, touchdown with E_reserve >= 216.0 kJ | BMS Telemetry & Flight Recording | `/// OperationalAllocation: [MET-07]` | JARUS SORA v2.5 Annex E §2.1 |
| `MET-08` | PostMissionDataOffloadShutdown | Post-landing stationary touchdown on recovery pad | Cryptographic key zeroization and data offload in t_offload <= 60.0 s, safe shutdown | Security Audit Log Verification | `/// OperationalAllocation: [MET-08]` | NIST SP 800-88r1 §2.4 |

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

Formal specification for autonomous waypoint following, 4D trajectory generation, wind vector compensation, and flight envelope containment during ingress transit.

#### Condition Specification
| Parameter | Condition Value / State | Engineering Unit | Validation Rule |
| :--- | :--- | :--- | :--- |
| Operational State | En-route Airborne Transit | State Enum | Flight mode `AUTO_MISSION` |
| Assigned Flight Corridor Width | 50.0 | m | Total lateral clearance boundary |
| Operating Altitude Floor / Ceiling | 30.0 to 120.0 | m AGL | Operational containment envelope |
| Ambient Wind Speed Limit | <= 12.0 | m/s | Maximum continuous operating wind |
| Wind Gust Limit | <= 15.0 | m/s | Maximum 3-second wind gust |

#### Standard Specification
| Metric Name | Threshold Value | Objective Value | Unit | Bus Protocol / Interface | Timeout Bound |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Lateral Cross-Track Error (e_xtrack) | <= 2.0 | <= 0.5 | m | High-speed CAN / Ethernet | Continuous @ 250 Hz |
| Vertical Altitude Tracking Error (e_z) | <= 1.0 | <= 0.3 | m | High-speed CAN / Ethernet | Continuous @ 250 Hz |
| True Airspeed Tracking Error (e_v) | <= 1.5 | <= 0.4 | m/s | CAN 2.0B Pitot / ADU | Continuous @ 100 Hz |
| Guidance Control Loop Rate | 250 | 500 | Hz | Real-Time OS Task Loop | dt <= 4.0 ms |
| Waypoint Transition Latency | <= 50.0 | <= 10.0 | ms | Internal Memory Bus | t_trans <= 50.0 ms |
| Geofence Boundary Containment Margin | >= 50.0 | >= 100.0 | m | Simplex RTA Safety Bus | Continuous @ 50 Hz |

#### Verification Specification
| Verification Attribute | Detail Specification |
| :--- | :--- |
| Verification Method | Flight Navigation Log Review & 6-DOF Kinematic Simulation Audit |
| Evidence Artifact | `tests/flight_guidance_sim.py` -> `logs/flight_trajectory_eval.csv` |
| Acceptance Criteria | Maximum lateral deviation <= 2.0 m over entire 15.0 km corridor transit; zero geofence boundary infringements; zero aerodynamic stall warnings. |
| Pass / Fail Threshold | `max(abs(e_xtrack)) <= 2.0 m` and `max(abs(e_z)) <= 1.0 m` across all ingress waypoints. |
| Traceability | `/// OperationalAllocation: [MET-02]` \| RTCA DO-365B §2.2.3 \| NATO STANAG 4586 Annex B §3.2 |

---

### 2.3 MET-03: AreaSurveillanceOrbit

Formal specification for closed-loop target area loitering, continuous payload pointing stabilization, multi-spectral sensor streaming, and orbit radius precision.

#### Condition Specification
| Parameter | Condition Value / State | Engineering Unit | Validation Rule |
| :--- | :--- | :--- | :--- |
| Operational State | On-Station Loiter / Orbit | State Enum | Flight mode `LOITER_ORBIT` |
| Designated Orbit Centerpoint | Geodetic (Lat, Lon, Alt) | Coordinates | Target Area of Interest (TAI) |
| Nominal Orbit Radius (R_orbit) | 300.0 | m | Nominal orbit radius |
| Target Standoff Slant Range | 300.0 to 1500.0 | m | Payload optical tracking range |
| Sensor Payload State | Active EO/IR Multi-Spectral | State Enum | MWIR + 4K Electro-Optical Gimbal |

#### Standard Specification
| Metric Name | Threshold Value | Objective Value | Unit | Bus Protocol / Interface | Timeout Bound |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Orbit Radius Deviation | <= 5.0 | <= 1.0 | m | Autopilot CAN / Mavlink v2 | Continuous @ 250 Hz |
| Payload Pointing Jitter (RMS) | <= 0.05 | <= 0.01 | deg | RS-422 / CAN Gimbal Bus | Continuous @ 100 Hz |
| Optical Target Centering Error | <= 15.0 | <= 3.0 | pixels | GigE Vision / RTSP | <= 33.3 ms (30 FPS) |
| Video Stream H.265 Frame Rate | >= 30 | >= 60 | FPS | 1000BASE-T Ethernet | Frame interval <= 33.3 ms |
| Sensor Gimbal Dynamic Slew Rate | >= 60.0 | >= 120.0 | deg/s | RS-422 Serial Driver | t_slew <= 500 ms |
| Video Telemetry Timestamp Skew | <= 10.0 | <= 2.0 | ms | Precision Time Protocol (PTP) | Skew <= 10.0 ms |

#### Verification Specification
| Verification Attribute | Detail Specification |
| :--- | :--- |
| Verification Method | Telemetry & High-Resolution Video Frame Analysis |
| Evidence Artifact | `tests/surveillance_orbit_test.py` -> `logs/gimbal_pointing_metrics.json` |
| Acceptance Criteria | Vehicle maintains circular orbit within 300.0 m +/- 5.0 m; gimbal pointing jitter <= 0.05 deg RMS under 12 m/s winds; uninterrupted video encoding. |
| Pass / Fail Threshold | `abs(R_actual - 300.0) <= 5.0 m` and `RMS(pointing_error) <= 0.05 deg`. |
| Traceability | `/// OperationalAllocation: [MET-03]` \| NATO STANAG 4586 Annex B §3.2 \| INCOSE SEH v5.0 §3.2 |

---

### 2.4 MET-04: DynamicAirspaceDeconfliction

Formal specification for onboard Detect and Avoid (DAA) surveillance, intruder track correlation, Well-Clear separation assurance, and autonomous collision avoidance maneuvering.

#### Condition Specification
| Parameter | Condition Value / State | Engineering Unit | Validation Rule |
| :--- | :--- | :--- | :--- |
| Operational State | Active Airspace Monitoring | State Enum | DAA subsystem initialized |
| Airspace Class | Class G / Class E (Unsegregated) | Airspace Enum | Mixed traffic environment |
| Cooperative Sensing | Dual ADS-B In (1090 MHz / 978 UAT) | Hardware | Operational receiver status |
| Non-Cooperative Sensing | 77 GHz FMCW Radar + EO/IR DAA | Hardware | Operational sensor track fusion |
| Track Fusion Rate | >= 10.0 | Hz | Multi-sensor track state update |

#### Standard Specification
| Metric Name | Threshold Value | Objective Value | Unit | Bus Protocol / Interface | Timeout Bound |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Horizontal Well-Clear Distance (DMOD) | >= 1200.0 | >= 1500.0 | m | ARINC 429 / Ethernet | Continuous @ 10 Hz |
| Vertical Well-Clear Separation (ZTHR) | >= 137.0 (450 ft) | >= 200.0 | m | ARINC 429 / Ethernet | Continuous @ 10 Hz |
| Modified Tau Horizon (tau_mod) | >= 35.0 | >= 55.0 | s | DAA Kinematics Engine | Continuous @ 10 Hz |
| Intruder Threat Correlation Latency | <= 1.0 | <= 0.2 | s | High-Speed CAN / Ethernet | t_corr <= 1.0 s |
| Autonomous Escape Maneuver Trigger | <= 2.0 | <= 0.5 | s | Autopilot Command Bus | t_maneuver <= 2.0 s |
| Well-Clear Recovery Hysteresis Duration | >= 10.0 | >= 15.0 | s | State Machine Timer | tau_hysteresis >= 10.0 s |

#### Verification Specification
| Verification Attribute | Detail Specification |
| :--- | :--- |
| Verification Method | DAA Collision Encounter Simulation & Hardware-in-the-Loop Event Review |
| Evidence Artifact | `tests/daa_separation_sim.py` -> `logs/daa_encounter_results.json` |
| Acceptance Criteria | Zero incursions below Well-Clear volume (1200 m horizontal, 137 m vertical) against standard RTCA DO-365B 24-encounter stress suite. |
| Pass / Fail Threshold | `min(D_horizontal) >= 1200.0 m` or `min(abs(H_vertical)) >= 137.0 m` across all simulated intruder trajectories. |
| Traceability | `/// OperationalAllocation: [MET-04]` \| RTCA DO-365B §2.2.4 \| NATO STANAG 4586 Annex B §3.3 |

---

### 2.5 MET-05: ElectronicCounterCountermeasures

Formal specification for electronic counter-countermeasures (ECCM), RF jamming detection, PACE communication tier failover, and GPS-denied dead-reckoning navigation.

#### Condition Specification
| Parameter | Condition Value / State | Engineering Unit | Validation Rule |
| :--- | :--- | :--- | :--- |
| Operational State | Contested Electronic Spectrum | State Enum | In-flight operations |
| RF Threat Environment | Narrowband / Broadband Noise Jamming | EW Vector | Jammer-to-Signal ratio J/S > 15 dB |
| Navigation Environment | GNSS Spoofing / Pseudorange Denial | EW Vector | Chi-Square residual gamma_k > 16.27 |
| Primary Communications Link | 5.8 GHz COFDM Datalink | PACE Tier 1 | Nominal primary link |
| Fallback Communications Links | 915 MHz FHSS / Cellular LTE / SATCOM | PACE Tiers 2-4 | Pre-configured backup channels |

#### Standard Specification
| Metric Name | Threshold Value | Objective Value | Unit | Bus Protocol / Interface | Timeout Bound |
| :--- | :--- | :--- | :--- | :--- | :--- |
| PACE Link Failover Execution Time | <= 1.0 | <= 0.2 | s | Serial SPI / High-Speed UART | t_switch <= 1.0 s |
| GPS-Denied Navigation Drift Rate | <= 1.0 | <= 0.2 | % Distance | EKF INS / Optical Flow | Continuous @ 250 Hz |
| Jamming Detection & Isolation Latency | <= 200.0 | <= 50.0 | ms | RF Frontend AGC Monitor | t_detect <= 200.0 ms |
| Spoofed GNSS Satellite Rejection Latency | <= 100.0 | <= 20.0 | ms | RAIM / Innovation Gating | t_reject <= 100.0 ms |
| Alternate Link Re-Sync Lock Time | <= 500.0 | <= 100.0 | ms | 915 MHz FHSS Modem | t_sync <= 500.0 ms |
| Cryptographic Session Rekeying Time | <= 250.0 | <= 50.0 | ms | AES-256-GCM Hardware Core | t_rekey <= 250.0 ms |

#### Verification Specification
| Verification Attribute | Detail Specification |
| :--- | :--- |
| Verification Method | RF Jamming Chamber Injection & GPS Spoofing HIL Navigation Test |
| Evidence Artifact | `tests/pace_failover_test.py` -> `logs/eccm_mitigation_record.json` |
| Acceptance Criteria | Autonomous failover to Tier 2 FHSS within 1.0 s of primary link loss; seamless switchover to optical flow odometry maintaining navigation error < 1.0% distance. |
| Pass / Fail Threshold | `t_switch <= 1.0 s` and `drift_rate <= 0.01 * distance_traveled`. |
| Traceability | `/// OperationalAllocation: [MET-05]` \| MIL-STD-461G RS103 §4.3 \| RTCA DO-362A §3.4 |

---

### 2.6 MET-06: PrecisionTargetMensuration

Formal specification for geo-spatial target coordinate extraction, multi-sensor line-of-sight intersection, terrain elevation model mapping, and Target Location Error (TLE) bounding.

#### Condition Specification
| Parameter | Condition Value / State | Engineering Unit | Validation Rule |
| :--- | :--- | :--- | :--- |
| Operational State | Target Acquisition & Mensuration | State Enum | Gimbal locked in `TRACK_TARGET` |
| Slant Range to Target (Range_target) | 1000.0 to 3000.0 | m | Laser rangefinder operating window |
| Digital Terrain Elevation Data (DTED) | Level 3 (1.0 m resolution) | Resolution | Local onboard elevation map loaded |
| Vehicle Navigation Covariance Norm | <= 1.5 | m | EKF state position uncertainty |
| Laser Rangefinder Accuracy | <= 0.5 | m | Time-of-flight optical pulse |

#### Standard Specification
| Metric Name | Threshold Value | Objective Value | Unit | Bus Protocol / Interface | Timeout Bound |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Target Location Error (TLE CEP90) | <= 2.5 | <= 1.0 | m | STANAG 4586 DLI / RS-422 | Range = 3.0 km |
| Target Range Estimation Error | <= 1.0 | <= 0.2 | m | LRF Serial Interface | Continuous @ 20 Hz |
| Line-of-Sight Kinematic Transform Rate | >= 50 | >= 100 | Hz | Real-Time Vector Math Unit | dt <= 20.0 ms |
| Mensuration Solution Convergence Time | <= 500.0 | <= 100.0 | ms | Mission Computer Bus | t_mens <= 500.0 ms |
| Target Coordinate Telemetry Latency | <= 50.0 | <= 10.0 | ms | Ethernet / STANAG DLI | t_tx <= 50.0 ms |
| Multi-Spectral Positive ID Confidence | >= 0.95 | >= 0.99 | Dimensionless | Edge Neural Classifier | Inference <= 33.3 ms |

#### Verification Specification
| Verification Attribute | Detail Specification |
| :--- | :--- |
| Verification Method | Surveyed Ground Target Mensuration Calibration & Flight Telemetry Audit |
| Evidence Artifact | `tests/target_mensuration_test.py` -> `logs/mensuration_accuracy_log.json` |
| Acceptance Criteria | Computed target geodetic coordinate error relative to DGPS surveyed ground truth <= 2.5 m CEP90 at 3.0 km standoff range under dynamic vehicle maneuvering. |
| Pass / Fail Threshold | `TLE_CEP90 <= 2.5 m` at `Range_target == 3000.0 m`. |
| Traceability | `/// OperationalAllocation: [MET-06]` \| NATO STANAG 4586 Annex B §3.5 \| INCOSE SEH v5.0 §3.2 |

---

### 2.7 MET-07: AutonomousBingoReturnDivert

Formal specification for real-time onboard energy consumption modeling, dynamic Bingo energy threshold evaluation, automated return-to-base (RTB) routing, and statutory reserve preservation.

#### Condition Specification
| Parameter | Condition Value / State | Engineering Unit | Validation Rule |
| :--- | :--- | :--- | :--- |
| Operational State | In-Flight Energy Management | State Enum | Continuous background monitor |
| Total Nominal Energy Capacity | 1080000.0 (300.0 Wh) | J | 6S 14Ah nominal energy pack |
| Minimum Statutory Reserve Energy | 216000.0 (60.0 Wh) | J | Strict 20.0% statutory reserve |
| Primary Recovery Site | Base Landing Pad (LZ-PRIMARY) | Waypoint ID | Distance d_primary <= 15.0 km |
| Secondary Divert Recovery Site | Alternate Field (LZ-DIVERT-ALPHA)| Waypoint ID | Distance d_divert <= 5.0 km |

#### Standard Specification
| Metric Name | Threshold Value | Objective Value | Unit | Bus Protocol / Interface | Timeout Bound |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Autonomous Return / Divert Trigger Latency | <= 200.0 | <= 50.0 | ms | Flight Executive State Machine | t_resp <= 200.0 ms |
| Touchdown Residual Energy Reserve | >= 216.0 (20%) | >= 270.0 (25%) | kJ | Smart BMS Telemetry | At touchdown |
| Closed-Loop Energy Consumption Accuracy | <= 2.0 | <= 0.5 | % | Current Integrator / Coulomb Count | Continuous @ 50 Hz |
| Real-Time Specific Air Range (SAR) Update | >= 10 | >= 50 | Hz | Path Planning Coprocessor | dt <= 100.0 ms |
| Alternate Divert Path Optimization Time | <= 100.0 | <= 20.0 | ms | Trajectory Planner Memory Bus | t_plan <= 100.0 ms |
| Low-Energy Alert GCS Broadcast Latency | <= 500.0 | <= 100.0 | ms | PACE C2 Datalink | t_c2 <= 500.0 ms |

#### Verification Specification
| Verification Attribute | Detail Specification |
| :--- | :--- |
| Verification Method | Battery Management System Telemetry & Autonomous Divert Flight Sim |
| Evidence Artifact | `tests/bingo_energy_math_test.py` -> `logs/bingo_divert_profile.csv` |
| Acceptance Criteria | Autonomous RTB triggers within 200 ms when E_current <= E_bingo; vehicle completes landing at primary or secondary divert site with reserve energy >= 216.0 kJ. |
| Pass / Fail Threshold | `E_touchdown >= 216.0 kJ` and `t_response <= 200.0 ms`. |
| Traceability | `/// OperationalAllocation: [MET-07]` \| JARUS SORA v2.5 Annex E §2.1 \| EASA GM1 UAS.SPEC.050(1)(g) |

---

### 2.8 MET-08: PostMissionDataOffloadShutdown

Formal specification for post-flight stationary confirmation, automated cryptographic payload zeroization, mission flight log offload, and deterministic safe electrical isolation.

#### Condition Specification
| Parameter | Condition Value / State | Engineering Unit | Validation Rule |
| :--- | :--- | :--- | :--- |
| Operational State | Landed & Stationary on Pad | State Enum | Weight-on-wheels active |
| Propulsion System State | Disarmed / Motor RPM == 0 | Motor State | ESC pulse output inhibited |
| Ground Support Interface | Optical / Direct Ethernet Offload | Interface | Physical GSE connected |
| Security Key State | Active Session Encryption Keys | Crypto State | Cryptographic volatile storage |

#### Standard Specification
| Metric Name | Threshold Value | Objective Value | Unit | Bus Protocol / Interface | Timeout Bound |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Cryptographic Key Zeroization Duration | <= 500.0 | <= 50.0 | ms | Hardware Cryptographic Unit | t_zeroize <= 500.0 ms |
| Flight Log & Telemetry Offload Duration | <= 60.0 | <= 20.0 | s | Gigabit Ethernet / USB 3.0 | t_offload <= 60.0 s |
| Complete Safe Electrical System Shutdown | <= 10.0 | <= 3.0 | s | Power Distribution Controller | t_shutdown <= 10.0 s |
| Memory Overwrite Verification Pass Rate | 100.0 | 100.0 | % | NIST SP 800-88r1 Clear Pattern | Single Pass 0x00/0xFF |
| Post-Flight Structural BIT Validation | 100.0 | 100.0 | % Pass | CAN 2.0B Health Bus | t_sbit <= 5.0 s |
| Security Tamper Log Seal Generation | <= 200.0 | <= 50.0 | ms | TPM 2.0 PCR Signing | t_seal <= 200.0 ms |

#### Verification Specification
| Verification Attribute | Detail Specification |
| :--- | :--- |
| Verification Method | Security Audit Log Verification & Memory Forensics Inspection |
| Evidence Artifact | `tests/crypto_zeroization_test.py` -> `logs/zeroization_audit_log.json` |
| Acceptance Criteria | All mission cryptographic keys erased and overwritten within 500 ms; full flight telemetry dump transferred in <= 60 s; clean power bus cutoff. |
| Pass / Fail Threshold | `KEY_ZEROIZED == TRUE` and `OFFLOAD_STATUS == SUCCESS` with zero uncommitted transactions. |
| Traceability | `/// OperationalAllocation: [MET-08]` \| NIST SP 800-88r1 §2.4 \| DoD Directive 3000.09 §3.1.c |

---

### 2.9 METL Execution Invariants
1. **Deterministic State Progression:** Progression from `MET-01` through `MET-08` is governed by discrete finite-state transitions in the flight executive.
2. **Allocation Tag Integrity:** Every task defined in the METL table carries an inviolable Gate 24 allocation tag (`/// OperationalAllocation: [MET-XX]`) mapped downstream to SysML v2 architectural activity blocks.
3. **Safety Interlock Coupling:** Non-compliance with standard metrics in tasks `MET-01` through `MET-07` initiates deterministic degraded mode failsafes in accordance with Section 8 (Go/No-Go Decision Matrix).
