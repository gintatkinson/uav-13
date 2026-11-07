| Attribute | Specification Detail |
| :--- | :--- |
| **Title** | 7-Row Emergency Decision & Contingency Matrix |
| **Version** | 1.1.0 |
| **Date** | 2026-10-31 |
| **Issue ID** | CONOPS-12 |
| **Type** | ConOps Specification Unit |
| **Generation Mode** | Manual |
| **Specification Source** | docs/conops/units/conops/12_EMERGENCY_DECISION_MATRIX.md |

## 12. 7-Row Emergency Decision & Contingency Matrix

In accordance with MIL-STD-882E Task 205 and SAE ARP4761 Section 4.3.1, the system implements a seven-row Emergency Decision and Contingency Matrix. The matrix is executed by a deterministic safety monitor that is independent of the primary mission controller (ASTM F3269-17 Section 5.1). The canonical triggers EMG-01 through EMG-07 are the complete set of emergency triggers for this ConOps.

Table 12.1 defines the detection mechanism, containment action, failsafe recovery state, maximum response time, and HITL authority for each trigger. Where the OEM sources are silent on a numeric threshold or response deadline, the matrix states "Not stated in OEM sources" and does not invent a value.

| Trigger ID | Contingency Trigger Event | Anomaly Detection Mechanism | Automated Containment Action | Failsafe Recovery State | Maximum Response Time | HITL Authority Role |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **EMG-01** | Communications Timeout (Lost C2 Link) | Loss of the authenticated heartbeat on the GCS UAV telemetry link, RF 4.4 GHz to 5.0 GHz (a5-user-manual-2.md:1273; interface_table.md); the loss interval is measured from the last valid frame. Timeout threshold: Not stated in OEM sources. | Enter the autonomous lost-link hold; if the link is not reacquired within the operator-configured hold window, execute a deterministic return-to-base. | `Contingency_LostLinkFallback` | Not stated in OEM sources | The supervisory operator may command hold, return, or divert when the link is available; the autonomous lost-link logic retains authority during link loss (RTCA DO-362A Section 3.4). |
| **EMG-02** | Sensor Integrity Fault (Navigation Degradation) | Cross-channel disparity between the GNSS Septentrio Asterx-m3 pro, the two mRo RM3100 magnetometers, the CUAV SKYE2 pitot, and the inertial state estimate (oem_bom.md:15, oem_bom.md:39-41); disparity threshold: Not stated in OEM sources. | Isolate the disagreeing channel; transition to dead-reckoning and optical-flow fallback; bound speed between the 26 m/s minimum flight speed (PL-05) and the 30 m/s cruise speed (PL-01). | `Contingency_SensorFallback` | Not stated in OEM sources | The supervisory operator may command hold or divert and may veto the fallback when a validated alternate navigation source is available. |
| **EMG-03** | Critical Resource Depletion | Power meter voltage and current telemetry (oem_bom.md:20) reports pack voltage at or below the 36 V minimum (PL-23), or mission elapsed time reaches the 90 min endurance limit (PL-06). Bingo reserve ratio: Not stated in OEM sources. | Shed non-essential payload loads; select the nearest pre-surveyed divert site that preserves the operator-configured energy reserve; execute a resource-conserving transit. | `Contingency_ResourceDivert` | Not stated in OEM sources | Informed advisory to the supervisory operator; the operator confirms the divert site when the link is available, and autonomous divert applies when the link is lost. |
| **EMG-04** | Controller Processing Fault | Autopilot Cube Orange Plus watchdog expiry, control-loop task deadline breach, or partition fault (oem_bom.md:12); timing threshold: Not stated in OEM sources. The OEM BOM declares no redundant flight controller. | Isolate the faulted partition (RTCA DO-178C Section 6.3.2); hold the last validated actuator setpoint; execute a watchdog reset; if the fault persists, remain in a deterministic safe hold until a supervisory recovery order. | `Degraded_ControllerFailsafe` | Not stated in OEM sources | Supervisory precautionary recovery order; a physical ground maintenance reset is required before the failsafe lock is cleared. |
| **EMG-05** | Operational Boundary Excursion | The state estimate places the vehicle outside the pre-loaded containment volume; the nominal containment geometry uses the 300 m loiter radius (PL-37) and the 50 m minimum mission waypoint altitude (PL-36); proximity margin: Not stated in OEM sources (ASTM F3269-17 Section 5.2). | Command a deterministic turn-back toward the containment volume and reduce speed toward the 26 m/s minimum flight speed (PL-05); inhibit commands that increase boundary penetration. | `Contingency_BoundaryContainment` | Not stated in OEM sources | Supervisory manual override; the containment interlock rejects any operator command that increases boundary penetration (ASTM F3269-17 Section 5.3). |
| **EMG-06** | Collision or Interference Hazard | The proximity sensor discrete active-low trigger (interface_table.md) and the Camera Compute Module Trip6 optical track (oem_bom.md:36, oem_bom.md:43) indicate an external entity inside the separation envelope; separation threshold: Not stated in OEM sources. | Execute a deterministic multi-axis escape vector away from the hazard while maintaining the pre-loaded separation margin; if an escape corridor is unavailable, transition to EMG-05 containment or EMG-07 safe state. | `Contingency_EvasiveManeuver` | Not stated in OEM sources | Supervisory override to divert; the operator may command an alternative escape route. |
| **EMG-07** | Structural or Actuator Failure | Ruddervator servo status frames on CAN 1 and wing servo status frames on CAN 2 report stall, loss of feedback, or position disagreement across the four Ruddervators (PL-14) and the eight total servos (PL-18); airframe vibration threshold: Not stated in OEM sources. A dual-consent authenticated abort discrete is also a valid trigger (interface_table.md). | De-energize the 8 V servo rail (PL-22) and the motor drive; hold the ESAD in the safe state; the ESAD is Critical / DAL-A (oem_bom.md:52). Parachute deployment is non-mission and excluded from the mission baseline (oem_bom.md:47); the research and development testbed may use the two 50 V igniter outputs (oem_bom.md:48-49). | `Emergency_SafeStateTermination` | Not stated in OEM sources | Dual-consent authenticated command is required for any ESAD arm or initiation action (DoD Directive 3000.09 Section 3.1.b; CJCSI 3121.01B Enclosure E Section 2.d). De-energization is a fail-safe action and does not require consent. |

### 12.1 Failsafe State Transition Semantics and Timing Guarantees

The emergency decision logic executes in a dedicated safety monitor on an isolated hardware partition, separate from the mission controller (ASTM F3269-17 Section 5.1; RTCA DO-178C Section 6.3.2). The state machine applies the following deterministic invariants:

1. **Priority Arbitration:** When multiple triggers are active, a higher-priority row suppresses lower-priority transitions. The strict priority order, highest first, is EMG-07, EMG-03, EMG-05, EMG-06, EMG-04, EMG-02, EMG-01. EMG-07 latches until a physical ground reset.
2. **Deterministic Response Timing:** The maximum response time for each trigger is listed in Table 12.1. Where the OEM sources are silent, no numeric deadline is asserted; the value shall be allocated during detailed design and verified by test (MIL-STD-882E Task 205).
3. **Fail-Safe Retention:** `Emergency_SafeStateTermination` and `Contingency_ResourceDivert` are non-reentrant and remain latched until a physical post-operation ground reset and an authorized maintenance clearance are complete.

### 12.2 Deterministic Emergency Transition Logic

Table 12.2 defines the deterministic predicate and transition for each trigger. The predicates are evaluated every control cycle; the first true row in the priority order of Section 12.1 is executed.

| Trigger ID | Decision Predicate | Deterministic Transition |
| :--- | :--- | :--- |
| **EMG-01** | `heartbeat_lost` is true AND `Delta_t_loss >= tau_loss_configured` | Transition to `Contingency_LostLinkFallback`; when `Delta_t_hold >= tau_hold_configured`, execute the return-to-base trajectory. |
| **EMG-02** | `cross_channel_disparity > disparity_threshold_configured` AND persists for the configured confirmation window | Transition to `Contingency_SensorFallback`; isolate the disagreeing channel; bound speed to the 26 m/s to 30 m/s range (PL-05, PL-01). |
| **EMG-03** | `pack_voltage <= 36 V` (PL-23) OR `elapsed_mission_time >= 90 min` (PL-06) OR `predicted_energy_to_divert >= remaining_usable_energy` | Transition to `Contingency_ResourceDivert`; shed non-essential loads; select the nearest divert site that satisfies the operator-configured reserve. |
| **EMG-04** | `watchdog_expired` OR `task_deadline_missed` OR `partition_fault` | Transition to `Degraded_ControllerFailsafe`; isolate the partition; hold the last validated setpoint; reset; if the fault persists, latch the safe hold. |
| **EMG-05** | `containment_margin <= 0` OR `predicted_trajectory_exits_containment_volume` | Transition to `Contingency_BoundaryContainment`; command the turn-back; reject commands that increase boundary penetration. |
| **EMG-06** | `separation_envelope_breached` | Transition to `Contingency_EvasiveManeuver`; execute the escape vector; if the escape corridor is unavailable, evaluate EMG-05 then EMG-07. |
| **EMG-07** | `structural_or_actuator_fault` OR (`abort_discrete` AND `dual_consent_valid`) | Transition to `Emergency_SafeStateTermination`; de-energize the 8 V servo rail (PL-22) and the motor drive; hold the ESAD safe (Critical / DAL-A). The ESAD RS-485 command-path response latency is 5 ms maximum (PL-58) and bounds only the command path, not the end-to-end emergency response. |

Where a predicate uses a configured threshold, the numeric value is Not stated in OEM sources and shall be an operator-configurable parameter verified at commissioning.

### 12.3 Degraded Modes and Fallback Hierarchy

- **Tier One (Nominal Execution):** Full multi-sensor fusion, RF 4.4 GHz to 5.0 GHz C2 link with the upper and lower MPSL4400 antennas (oem_bom.md:45-46; a5-user-manual-2.md:1273), and nominal envelope margins.
- **Tier Two (Degraded Sensor Mode):** A single-sensor failure activates the secondary observer and dead reckoning; speed is bounded between 26 m/s (PL-05) and 30 m/s (PL-01).
- **Tier Three (Contingency Link Mode):** Loss of the primary C2 link triggers the lost-link hold and return-to-base sequence; the 60 km direct RLOS range (PL-07) bounds the nominal link geometry.
- **Tier Four (Emergency Containment Mode):** An unrecoverable fault triggers de-energization of the 8 V servo rail (PL-22) and motor drive; the ESAD remains safe (Critical / DAL-A, oem_bom.md:52). The parachute deployment module is non-mission and excluded from the mission baseline (oem_bom.md:47); the research and development testbed may use the two 50 V igniter outputs (oem_bom.md:48-49).

### 12.4 Human-in-the-Loop (HITL) Authority and Override Protocols

- **Supervisory Authority:** The operator retains supervisory override over the GCS UAV telemetry link when the link is available (a5-user-manual-2.md:1273).
- **Dual-Consent Authentication:** Any ESAD arm or initiation action in EMG-07 requires two-operator verified consent (DoD Directive 3000.09 Section 3.1.b; CJCSI 3121.01B Enclosure E Section 2.d).
- **Autonomous Fail-Safe Boundary:** Autonomous de-energization of the 8 V servo rail (PL-22) and motor drive is permitted as a fail-safe action; autonomous ESAD initiation is prohibited without dual consent.
- **Interlock Inhibit:** The flight computer rejects operator commands that violate the containment limits in EMG-05 (ASTM F3269-17 Section 5.3).

### 12.5 Autonomous Divert and Secondary Recovery Protocols

- **Primary Recovery:** The designated nominal landing site or recovery zone.
- **Secondary Divert Sites:** Pre-surveyed alternate recovery coordinates evaluated against the operator-configured energy reserve; the OEM sources do not state a numeric reserve ratio.
- **Terrain Clearance:** All emergency divert trajectories maintain the 50 m minimum mission waypoint altitude (PL-36) as the planning floor; the OEM sources do not state a separate terrain clearance value.
- **Divert Authority:** The operator confirms the divert site when the link is available; the autonomous logic selects the nearest site that satisfies the reserve when the link is lost.

### 12.6 Post-Emergency Containment, Latching, and Reset Procedures

- **Safety Lockout:** Emergency shutdown latches all actuators and high-voltage buses in de-energized safe states; the ESAD remains safe and the ESAD RBF key is reinstalled before ground handling (interface_table.md; oem_bom.md:60).
- **Non-Volatile Blackbox Offload:** Diagnostic fault logs, sensor telemetry, and watchdog stack traces are written to non-volatile flash.
- **Authorized Ground Clearance:** Physical inspection and signed maintenance clearance are required before the failsafe lock is cleared; the UAV RBF key and the ESAD RBF key are restored to the safe configuration before power is reapplied (interface_table.md).

## Source References

The emergency matrix is grounded in schema/extracted/parametric_limits.md for PL-01, PL-05, PL-06, PL-07, PL-14, PL-18, PL-22, PL-23, PL-36, PL-37, and PL-58, and in schema/extracted/interface_table.md for the GCS UAV telemetry link, CAN 1 and CAN 2 servo frames, proximity sensor trigger, and ESAD interlocks. The OEM evidence is schema/extracted/oem_bom.md and .pipeline/schema.sysml. Normative clauses are ISO/IEC/IEEE 29148:2018 Section 6.4.2, MIL-STD-882E Section 4.3, SAE ARP4761 Section 4.3.1, ASTM F3269-17 Section 5.1, RTCA DO-362A Section 3.4, RTCA DO-178C Section 6.3.1, MIL-STD-1629A Section 4.3, DoD Directive 3000.09 Section 3.1, and CJCSI 3121.01B Enclosure E Section 2.d.
