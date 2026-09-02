| Attribute | Value |
| :--- | :--- |
| **Title** | Tactical Mission Intent: Mission Essential Task List |
| **Version** | 1.0.0 |
| **Date** | 2026-09-02 |

## 2. Mission Essential Task List (METL)

The Mission Essential Task List (METL) establishes the doctrinally grounded, quantitative task inventory required to achieve the Commander's operational intent across all operational lifecycle phases in accordance with CJCSI 3500.02H and NATO STANAG 4586 Annex B.

| Task ID | Task Name | Condition Statement | Standard Metric | Verification Method | Gate 24 Allocation Tag | Public Clause Citation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `MET-01` | PreFlightSystemCheckout | Pre-launch stationary ground state with active energy and avionics power | 100% PBIT pass, IMU bias convergence t_PBIT <= 10.0 s, battery SoC >= 95.0% | Automated BIT Log Inspection | `/// OperationalAllocation: [MET-01]` | NATO STANAG 4586 Annex B §4.1 |
| `MET-02` | AutonomousIngressTransit | En-route corridor navigation under active flight plan | Lateral cross-track error e_xtrack <= 2.0 m, vertical error e_z <= 1.0 m | Flight Navigation Log Review | `/// OperationalAllocation: [MET-02]` | RTCA DO-365B §2.2.3 |
| `MET-03` | AreaSurveillanceOrbit | On-station target tracking within designated geographic boundary | Orbit radius R_orbit = 300.0 m +/- 5.0 m, payload pointing jitter <= 0.05 deg | Telemetry & Video Frame Analysis | `/// OperationalAllocation: [MET-03]` | NATO STANAG 4586 Annex B §3.2 |
| `MET-04` | DynamicAirspaceDeconfliction | Traffic conflict geometry detected by onboard DAA sensors | Maintain Well-Clear separation (D_horizontal >= 1200.0 m, H_vertical >= 137.0 m) | DAA Collision Event Log Review | `/// OperationalAllocation: [MET-04]` | RTCA DO-365B §2.2.4 |
| `MET-05` | ElectronicCounterCountermeasures | Jamming or intentional RF / navigation spoofing detected | Seamless PACE tier switch t_switch <= 1.0 s, dead-reckoning drift <= 1.0% distance | RF Signal Log & Navigation Test | `/// OperationalAllocation: [MET-05]` | MIL-STD-461G RS103 §4.3 |
| `MET-06` | PrecisionTargetMensuration | Target identified within optical/infrared payload field of view | Target Location Error TLE_CEP90 <= 2.5 m at slant range Range_target = 3.0 km | Optical Mensuration Calibration Log | `/// OperationalAllocation: [MET-06]` | NATO STANAG 4586 Annex B §3.5 |
| `MET-07` | AutonomousBingoReturnDivert | Energy monitoring detects current energy E_current <= E_bingo threshold | Autonomous RTB or divert trigger t_resp <= 200.0 ms, touchdown with E_reserve >= 216.0 kJ | BMS Telemetry & Flight Recording | `/// OperationalAllocation: [MET-07]` | JARUS SORA v2.5 Annex E §2.1 |
| `MET-08` | PostMissionDataOffloadShutdown | Post-landing stationary touchdown on recovery pad | Cryptographic key zeroization and data offload in t_offload <= 60.0 s, safe shutdown | Security Audit Log Verification | `/// OperationalAllocation: [MET-08]` | NIST SP 800-88r1 §2.4 |

### 2.1 METL Execution Invariants
1. **Deterministic State Progression:** Progression from `MET-01` through `MET-08` is governed by discrete finite-state transitions in the flight executive.
2. **Allocation Tag Integrity:** Every task defined in the METL table carries an inviolable Gate 24 allocation tag (`/// OperationalAllocation: [MET-XX]`) mapped downstream to SysML v2 architectural activity blocks.
3. **Safety Interlock Coupling:** Non-compliance with standard metrics in tasks `MET-01` through `MET-07` initiates deterministic degraded mode failsafes in accordance with Section 8 (Go/No-Go Decision Matrix).
