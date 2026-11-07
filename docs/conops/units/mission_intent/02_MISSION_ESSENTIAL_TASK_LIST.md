| Attribute | Specification Detail |
| :--- | :--- |
| **Title** | Tactical Mission Intent: Mission Essential Task List |
| **Issue ID** | MI-02 |
| **Version** | 1.0.0 |
| **Date** | 2026-09-02 |
| **Type** | Mission Intent Specification |
| **Generation Mode** | Schema-Grounded Synthesis |
| **Specification Source** | `.pipeline/schema.sysml`; `schema/extracted/parametric_limits.md`; `schema/extracted/oem_bom.md`; `schema/extracted/interface_table.md`; `docs/research/RESEARCH_INVENTORY.md` |

## 2. Mission Essential Task List (METL)

The Mission Essential Task List (METL) is the doctrinally grounded, quantitative task inventory required to achieve the Commander's operational intent across the launch, transit, on-station, engagement, recovery, and containment phases. Task conditions, standards, and verification methods are bounded by CJCSI 3121.01B, DoD Directive 3000.09, JARUS SORA v2.5 Annex E, MIL-STD-882E, and the public clause baseline cataloged in `docs/research/RESEARCH_INVENTORY.md`.

Numeric standards cite the parametric limit identifier (`PL-xx`) in `schema/extracted/parametric_limits.md`; values absent from the OEM sources are marked "Not stated in OEM sources" and are never synthesized.

| Task ID | Task Name | Condition Statement | Quantitative Standard Metric | Verification Method | Gate 24 Allocation Tag | Public Clause Citation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `MET-01` | PreFlightSystemCheckout | Vehicle stationary on the ground, battery installed, RBF devices removed, ESAD in the safe state | PL-32 = 49 V; PL-33 = 50 V; PL-34 = 0 m/s to 3 m/s; PL-22 = 8 V; PL-49 <= 0.5 Ohm at PL-50 = 20 mA | Ground control station built-in test log and continuity inspection | `/// OperationalAllocation: [MET-01]` | FAA 14 CFR Section 107.49(b), Section 107.49(c) |
| `MET-02` | LaunchAndTransition | Vehicle mounted on the launcher carriage at the 12 deg launch angle (PL-66) with pneumatic supply connected | PL-40 = 13 bar; PL-41 = 14 bar; PL-65 <= 25 m/s; PL-64 <= 30 kg; PL-88 = 2 s; PL-72 <= 5 min | Launcher gauge record and release telemetry review | `/// OperationalAllocation: [MET-02]` | JARUS SORA v2.5 Annex E Section E.11 |
| `MET-03` | FlightControlActuation | Airborne control law active with all control surfaces mechanically connected | PL-14 = 4 units; PL-16 = 4 units; PL-17 = 4 units; PL-18 = 8 units; PL-22 = 8 V; PL-19 = 970 cm; PL-20 = 150 cm; PL-21 = 120 cm | Control surface sweep test and CAN bus message log review | `/// OperationalAllocation: [MET-03]` | SAE ARP4761 Section 4.3.1 |
| `MET-04` | AutonomousIngressTransit | En-route transit under the mission flight plan with the C2 link available | PL-01 = 30 m/s; PL-02 <= 38 m/s; PL-05 >= 26 m/s; PL-36 >= 50 m; PL-06 <= 90 min; PL-07 <= 60 km; PL-08 = 60 km to 180 km | Flight navigation log and link range telemetry review | `/// OperationalAllocation: [MET-04]` | RTCA DO-362A Section 2.2 |
| `MET-05` | AreaSurveillanceOrbit | On-station orbit inside the designated operating area | PL-37 = 300 m; PL-25 = -45 deg to 135 deg; PL-26 = -165 deg to 165 deg; PL-27 = 1 X to 40 X; PL-28 = 1280 pixels; PL-29 = 720 pixels; PL-30 = 1280 pixels; PL-31 = 720 pixels | Gimbal pointing log and video frame metadata review | `/// OperationalAllocation: [MET-05]` | NATO STANAG 4586 Section 4.2 |
| `MET-06` | DynamicAirspaceDeconfliction | Cooperative or non-cooperative traffic detected inside the DAA alert volume | RTCA DO-365B Section 2.2.4 well-clear geometry; DMOD, HMD, and ZTHR Not stated in OEM sources; PL-36 >= 50 m; PL-02 <= 38 m/s | DAA event log and maneuver reconstruction | `/// OperationalAllocation: [MET-06]` | RTCA DO-365B Section 2.2.4, Section 2.2.5 |
| `MET-07` | ElectronicCounterCountermeasures | RF interference or navigation denial detected on the C2 link | C2 link 4.4 GHz to 5.0 GHz (interface_table.md:63); PL-39 = 2 W; PL-05 = 26 m/s to PL-02 = 38 m/s; link-loss expiration Not stated in OEM sources | RF susceptibility test and link log review | `/// OperationalAllocation: [MET-07]` | MIL-STD-461G Section 5.18 |
| `MET-08` | PrecisionTargetMensuration | Target inside the gimbal field of view with designation authority confirmed | PL-42 = 2 s; PL-43 = 5 s; PL-44 <= 15 deg; PL-45 <= 55 m/s; PL-27 = 1 X to 40 X; target location error Not stated in OEM sources | Optical mensuration calibration log and frame review | `/// OperationalAllocation: [MET-08]` | CJCSI 3121.01B Enclosure A Section 4.b |
| `MET-09` | PositiveIdentificationAndAuthorization | Positive identification declared by the authorized operator with ESAD in the armed state | PL-13 <= 5 kg (oem_bom.md:57); PL-46 = 14 V; PL-47 = 32 V; PL-48 = 28 V; PL-54 = 1 ms at PL-55 = 50 percent; PL-60 = 0 V to 1800 V | Hardware-in-the-loop interlock test and ESAD continuity record | `/// OperationalAllocation: [MET-09]` | DoD Directive 3000.09 Section 3.1, Section 3.1.a, Section 3.1.b; CJCSI 3121.01B Enclosure E Section 2.d |
| `MET-10` | BingoReturnDivert | Remaining flight time reaches the computed return-to-base threshold | PL-23 = 36 V; PL-24 = 50.4 V; PL-06 <= 90 min; PL-01 = 30 m/s; reserve threshold and divert response time Not stated in OEM sources | Battery management telemetry replay and divert trajectory reconstruction | `/// OperationalAllocation: [MET-10]` | JARUS SORA v2.5 Annex E Section E.14 |
| `MET-11` | PostMissionDataOffloadShutdown | Vehicle landed and stationary on the recovery area | PL-23 = 36 V; PL-24 = 50.4 V before shutdown; data-offload duration Not stated in OEM sources; cryptographic zeroization duration Not stated in OEM sources | Post-flight inspection and security audit log review | `/// OperationalAllocation: [MET-11]` | AMC1 UAS.SPEC.050 Section 4.4; NIST SP 800-82r3 Section 6.4 |
| `MET-12` | DownedVehicleContainmentAntiTamper | Impact or uncontrolled ground contact detected; the parachute non-mission variant is excluded | PL-63 = 0.0039 g; PL-46 = 14 V; PL-47 = 32 V; PL-60 = 1800 V; parachute configuration non-mission (oem_bom.md:47); containment response times Not stated in OEM sources | Fault-injection test and ESAD safe-state audit | `/// OperationalAllocation: [MET-12]` | DoD Directive 3000.09 Section 3.1.c; MIL-STD-882E Task 208 Section 4.2; JARUS SORA v2.5 Annex E Section E.22 |

### 2.1 METL Execution Invariants

1. **Deterministic State Progression:** Task progression from `MET-01` through `MET-12` is governed by discrete finite-state transitions in the flight executive. Transition trigger times are Not stated in OEM sources and are therefore configuration-defined, never hardcoded.
2. **Allocation Tag Integrity:** Every task carries an inviolable Gate 24 allocation tag (`/// OperationalAllocation: [MET-XX]`) mapped downstream to SysML v2 architectural activity blocks.
3. **Safety Interlock Coupling:** Non-compliance with the standard metrics of `MET-01` through `MET-10` initiates deterministic degraded-mode failsafes in accordance with the Go/No-Go Decision Matrix.
4. **Ruddervator Canonical Naming:** The tail control surface assembly is designated Ruddervator; the drawing synonym Fins and preparation synonym tail stabiliser are not used as task or subsystem identifiers.
5. **ESAD Criticality:** The ESAD is classified Critical at DAL-A ([oem_bom.md](oem_bom.md) line 52). No engagement task may proceed unless the safe and arm interlock chain reports the armed state.
6. **Parachute Non-Mission:** The parachute deployment module is a non-mission configuration (`configuration: non-mission`, `baseline: false`, [oem_bom.md](oem_bom.md) line 47) and is excluded from MET-12 containment credit.
7. **Emergency Downed Vehicle Containment (MET-12):** On catastrophic kinetic impact or uncommanded descent, the system unconditionally triggers cryptographic anti-tamper zeroization, isolates the warhead and battery buses, and activates distress signaling per DoD Directive 3000.09 Section 3.1.c and MIL-STD-882E Task 208 Section 4.2. Numeric response times are Not stated in OEM sources.
8. **OEM Silence Discipline:** Where an OEM source is silent on a numeric threshold, the task records "Not stated in OEM sources" and defers the value to configuration control rather than inventing a bound.

## Source References

This METL is grounded in ISO/IEC/IEEE 29148:2018 Section 6.4.2, ISO/IEC/IEEE 29148:2018 Section 8.4, FAA 14 CFR Section 107.49(b), JARUS SORA v2.5 Annex E Section E.14, RTCA DO-365B Section 2.2.4, MIL-STD-882E Task 208 Section 4.2, and DoD Directive 3000.09 Section 3.1. Source files are schema/extracted/parametric_limits.md, schema/extracted/oem_bom.md, schema/extracted/interface_table.md, docs/research/RESEARCH_INVENTORY.md, and .pipeline/schema.sysml.
