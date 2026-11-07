| Attribute | Specification Detail |
| :--- | :--- |
| **Issue ID** | #Not assigned |
| **Title** | Master Signal Flow Dictionary and Safety Invariants |
| **Type** | icd |
| **Interface Level** | Level 1C Logical Interface |
| **Generation Mode** | subagent |
| **Specification Source** | [.pipeline/schema.sysml](../../.pipeline/schema.sysml) |

# Level 1C: Master Signal Registry and Safety Invariants

## 1. Executive Summary and Signal Flow Overview

This Master Signal Dictionary defines 28 logical signals conveyed across the 17 connections registered in `ICD_01_SYSTEM_INTERFACE_MATRIX.md`. Each signal is bound to a declared source port and destination port, a logical data type, normalized SI units, a valid range, an update rate, a deterministic safe default, and an exact Level 0 schema citation. Signals are logical data entities only; no physical connector, pinout, wire gauge, or transport byte framing is specified.

Values that are absent from the OEM sources are explicitly marked "Not stated in OEM sources". Safe defaults are the deterministic values applied during cold initialization, link loss, sensor fault, or emergency failsafe. The safety-critical subset is mapped to the STPA hazards in `docs/safety/STPA_MATRIX.md`.

## 2. Master Signal Flow Dictionary Table

| Signal ID | Signal Name | Source Port | Dest Port | Data Type | SI Units | Valid Range | Update Rate | Safe Default Value | Schema Citation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SIG-SPACE-AV-001 | GnssPositionFix | PORT-SPACE-GNSS | PORT-AV-GNSS | Record | m | Not stated in OEM sources | Not stated in OEM sources | 0.0 | `schema/extracted/interface_table.md#L38` |
| SIG-SPACE-AV-002 | GnssVelocityFix | PORT-SPACE-GNSS | PORT-AV-GNSS | Vector3D | m/s | Not stated in OEM sources | Not stated in OEM sources | 0.0 | `schema/extracted/interface_table.md#L38` |
| SIG-RELAY-AV-001 | RelayCommandFrame | PORT-SPACE-RELAY | PORT-AV-C2 | Record | dimensionless | Not stated in OEM sources | Not stated in OEM sources | 0.0 | `docs/conops/CONOPS.md#L306` |
| SIG-AV-GCS-001 | SupervisoryCommandFrame | PORT-AV-C2 | PORT-GCS-RF | Record | dimensionless | Not stated in OEM sources | Continuous | DISARMED | `schema/extracted/interface_table.md#L63` |
| SIG-AV-GCS-002 | TelemetryDownlinkFrame | PORT-AV-C2 | PORT-GCS-RF | Record | dimensionless | Not stated in OEM sources | Continuous | 0.0 | `schema/extracted/interface_table.md#L63` |
| SIG-AV-GCS-003 | VideoDownlinkFrame | PORT-AV-C2 | PORT-GCS-RF | Record | count | Not stated in OEM sources | Continuous | 0.0 | `schema/extracted/interface_table.md#L64` |
| SIG-AV-AV-001 | Can1VehicleStateFrame | PORT-AV-SENS | PORT-AV-SENS | Record | dimensionless | Not stated in OEM sources | Not stated in OEM sources | 0.0 | `schema/extracted/interface_table.md#L9` |
| SIG-AV-AV-002 | Can2ActuatorStatusFrame | PORT-AV-SENS | PORT-AV-SENS | Record | dimensionless | Not stated in OEM sources | Not stated in OEM sources | 0.0 | `schema/extracted/interface_table.md#L28` |
| SIG-AV-AV-003 | ServoPositionDemand | PORT-AV-CMD | PORT-AV-CMD | Float32 | percent | [-100.0, 100.0] | Not stated in OEM sources | 0.0 | `schema/extracted/interface_table.md#L9` |
| SIG-AV-AV-004 | ServoPowerEnable | PORT-AV-CMD | PORT-AV-CMD | Bool | dimensionless | [false, true] | Not stated in OEM sources | false | `.pipeline/schema.sysml#L220` |
| SIG-AV-AV-005 | TargetTrackFrame | PORT-AV-PAYLOAD | PORT-AV-VIDEO | Record | count | Not stated in OEM sources | Continuous | 0.0 | `schema/extracted/interface_table.md#L34` |
| SIG-AV-AV-006 | GimbalAttitudeFrame | PORT-AV-PAYLOAD | PORT-AV-VIDEO | Vector3D | deg | [-165.0, 165.0] | Continuous | 0.0 | `schema/extracted/parametric_limits.md#L32` |
| SIG-MSO-AV-001 | WeaponReleaseConsent | PORT-HUM-MSO | PORT-AV-ESAD | Bool | dimensionless | [false, true] | Not stated in OEM sources | false | `schema/extracted/oem_bom.md#L52` |
| SIG-MSO-AV-002 | ReleaseConsentToken | PORT-HUM-MSO | PORT-AV-ESAD | UInt32 | dimensionless | Not stated in OEM sources | Not stated in OEM sources | 0 | `schema/extracted/oem_bom.md#L52` |
| SIG-AV-AV-007 | SafetyVeto | PORT-AV-SAFE | PORT-AV-VETO | Bool | dimensionless | [false, true] | Continuous | true | `schema/extracted/oem_bom.md#L52` |
| SIG-GCS-GCS-001 | DownlinkTelemetryFrame | PORT-GCS-RF | PORT-GCS-HMI | Record | dimensionless | Not stated in OEM sources | Continuous | 0.0 | `schema/extracted/interface_table.md#L63` |
| SIG-GCS-GCS-002 | DownlinkVideoFrame | PORT-GCS-RF | PORT-GCS-HMI | Record | count | Not stated in OEM sources | Continuous | 0.0 | `schema/extracted/interface_table.md#L64` |
| SIG-GCS-GCS-003 | MissionArchivePacket | PORT-GCS-LAN | PORT-GCS-LAN | Record | bytes | Not stated in OEM sources | Not stated in OEM sources | 0 | `schema/extracted/interface_table.md#L66` |
| SIG-HUM-GCS-001 | TrajectoryCommandFrame | PORT-HUM-SO | PORT-GCS-HMI | Record | dimensionless | Not stated in OEM sources | Not stated in OEM sources | HOLD | `docs/conops/CONOPS.md#L315` |
| SIG-HUM-GCS-002 | GimbalPointingCommand | PORT-HUM-PS | PORT-GCS-HMI | Float32 | deg | [-165.0, 165.0] | Not stated in OEM sources | 0.0 | `schema/extracted/parametric_limits.md#L32` |
| SIG-HUM-GCS-003 | TargetLockCommand | PORT-HUM-PS | PORT-GCS-HMI | Bool | dimensionless | [false, true] | Not stated in OEM sources | false | `docs/conops/CONOPS.md#L316` |
| SIG-HUM-GSE-001 | DiagnosticCommandFrame | PORT-HUM-MT | PORT-GSE-DIAG | Record | dimensionless | Not stated in OEM sources | Not stated in OEM sources | IDLE | `docs/conops/CONOPS.md#L317` |
| SIG-HUM-GSE-002 | DiagnosticResponseFrame | PORT-HUM-MT | PORT-GSE-DIAG | Record | dimensionless | Not stated in OEM sources | Not stated in OEM sources | 0.0 | `docs/conops/CONOPS.md#L317` |
| SIG-LCH-AV-001 | LaunchReleaseDiscrete | PORT-LCH-MECH | PORT-AV-LAUNCH | Bool | dimensionless | [false, true] | Not stated in OEM sources | false | `schema/extracted/interface_table.md#L61` |
| SIG-LCH-LCH-001 | PneumaticSupplyPressure | PORT-LCH-PNEU | PORT-LCH-PNEU | Float32 | dimensionless | [0.0, 14.0] | Continuous | 0.0 | `schema/extracted/parametric_limits.md#L73` |
| SIG-LCH-LCH-002 | LauncherTriggerPower | PORT-LCH-PNEU | PORT-LCH-PNEU | Float32 | V | [18.0, 18.0] | Continuous | 0.0 | `schema/extracted/parametric_limits.md#L81` |
| SIG-GCS-EXT-001 | AirspaceClearanceState | PORT-GCS-HMI | PORT-EXT-AIR | Enum | dimensionless | [DENIED, CLEARED] | Not stated in OEM sources | DENIED | `docs/conops/CONOPS.md#L320` |
| SIG-EXT-GCS-001 | FieldWeatherObservation | PORT-EXT-WX | PORT-GCS-HMI | Record | dimensionless | Not stated in OEM sources | Not stated in OEM sources | 0.0 | `docs/conops/CONOPS.md#L321` |

## 3. Mathematical Formulations and Safety Invariants

$$
\begin{aligned}
\tau_{\mathrm{transport}} &\le \tau_{\mathrm{latency,max}} \\
\mathrm{VETO} &= \mathrm{true} \Rightarrow a_{\mathrm{cmd}} = 0
\end{aligned}
$$

- Parameter Definitions and Engineering Units:
- tau_transport: End-to-end logical signal transport latency from source port to destination port, in ms.
- tau_latency,max: Maximum allowable transport latency threshold, in ms. Not stated in OEM sources.
- VETO: Hardware safety veto assertion state, dimensionless boolean.
- a_cmd: Actuation demand accepted by the actuator core, in percent of commanded range.

## 4. Safety-Critical Signal Allocation and STPA Hazard Mapping

| Signal ID | Safety Criticality | Hazard Ref | Safety Constraint | Failsafe Action |
| :--- | :--- | :--- | :--- | :--- |
| SIG-MSO-AV-001 | Critical (DAL-A) | **H-1** | ESAD arming and initiation requires valid dual authorization and independent interlock consent | Assert false on link loss or invalid consent |
| SIG-MSO-AV-002 | Critical (DAL-A) | **H-1** | Release consent token must be time-ordered and unique for each engagement | Reject stale or duplicate token |
| SIG-AV-AV-007 | Critical (DAL-A) | **H-1**, **H-2** | Hardware safety veto must dominate actuation demand during an unsafe state | Assert true and force actuation demand to zero |
| SIG-AV-AV-003 | High | **H-3** | Servo commands must remain within the control-surface travel envelope | Revert to neutral demand 0.0 percent |
| SIG-AV-AV-004 | High | **H-3** | Servo power enable must not be asserted during an invalid actuator state | Assert false and remove servo power |
| SIG-AV-GCS-001 | Critical | **H-5** | C2 commands must not be applied when the link is lost or stale | Revert to DISARMED and preserve the last safe mission state |
| SIG-LCH-AV-001 | Critical | **H-7** | Launch release must occur only after pressure, mass, velocity, and angle checks pass | Assert false and inhibit carriage release |
| SIG-LCH-LCH-001 | Critical | **H-7** | Pneumatic supply must remain within the declared 13 bar to 14 bar launch pressure window | Vent to 0.0 bar and inhibit launch |
| SIG-AV-AV-005 | High | **H-11** | Target track data must be rejected when its validity or age bound is violated | Revert to zero track and hold the current flight path |

## 5. Source References

- Structural Schema: [.pipeline/schema.sysml](../../.pipeline/schema.sysml)
- Interface Extraction: [schema/extracted/interface_table.md](../../schema/extracted/interface_table.md)
- OEM Bill of Materials: [schema/extracted/oem_bom.md](../../schema/extracted/oem_bom.md)
- Parametric Limits: [schema/extracted/parametric_limits.md](../../schema/extracted/parametric_limits.md)
- STPA Safety Matrix: [docs/safety/STPA_MATRIX.md](../safety/STPA_MATRIX.md)
- Normative ConOps: [docs/conops/CONOPS.md](../conops/CONOPS.md)
