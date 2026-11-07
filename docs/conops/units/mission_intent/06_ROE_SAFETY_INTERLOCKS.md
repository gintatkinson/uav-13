| Attribute | Specification Detail |
| :--- | :--- |
| **Title** | Tactical Mission Intent: Safety Constraints & Subsystem Interlocks |
| **Version** | 1.0.0 |
| **Date** | 2026-09-02 |
| **Issue ID** | MI-06 |
| **Type** | Mission Intent |
| **Generation Mode** | Schema-Derived |
| **Specification Source** | `.pipeline/schema.sysml` |

## 6. Safety Constraints & Subsystem Interlocks

In accordance with CI-03 (functional thread isolation), CI-01 (fail-safe interlocks), CI-02 (escalation of force interlocks), CI-04 (functional hazard assessment), CI-05 (software fault detection), and CI-06 (safety net monitors), the mission safety architecture is expressed as deterministic predicates over declared AST ports, AST attributes, and AST parametric assertions. The Electronic Safe and Arm Device is Critical (DAL-A). The Ruddervator is the canonical tail control surface assembly (quantity four). Parachute deployment is a non-mission configuration and receives no safety credit in any interlock predicate. The CI identifiers are expanded in the Public Clause Citation Index in Section 6.8.

### 6.1 Safety Constraint Derivation Basis

The safety constraints in this unit are not free-form prose. They are derived from the following AST declarations:

1. **Parametric assertions**: the AST declares `assert_PL_01_range` through `assert_PL_94_range` at package level (`schema.sysml:506-878`) and re-declares the same 94 assertions inside the `Parametric_Limits_Table_System` part (`schema.sysml:2290-2664`). The numeric values are bound to `schema/extracted/parametric_limits.md`, which carries the OEM file and line evidence.
2. **Discrete interlock ports**: the AST declares `ESAD_Safe_Arm_Interlock : Safe_or_armed_state`, `UAV_Power_Interlock : Power_ON_or_OFF`, and `Warhead_RBF_Interlock : Safe_or_armed`, each with protocol family "Discrete interlock" (`schema.sysml:440-455`, re-declared at `schema.sysml:1656-1671`).
3. **Arming and power parts**: the AST declares `ESAD` as "Electronic Safe and Arm Device, Critical / DAL-A" (`schema.sysml:1133-1143`), `ESAD_RBF_Key` as the "ESAD arming sequence Remove Before Flight key" (`schema.sysml:1172-1183`), `UAV_RBF_Key` as the "UAV power Remove Before Flight key" (`schema.sysml:2888-2898`), `Power_Meter` with a "UAV RBF key" interface (`schema.sysml:2680-2690`), `Safety_RBF_Devices` covering the power RBF and warhead RBF-3 (`schema.sysml:2849-2859`), and `Warhead` with a mass of 5 kg (`schema.sysml:2901-2911`).
4. **Lifecycle state definitions**: the AST declares `Interface_Table_LifecycleState`, `OEM_Bill_of_Materials_LifecycleState`, and `Parametric_Limits_Table_LifecycleState` (`schema.sysml:881-910`). Each state machine enforces `Initial -> System_State -> InitState -> ActiveState -> Terminal` with `Initialize` and `Verify` accept events and no reverse transition from `Terminal`. These state definitions are package lifecycle gates; the AST declares no vehicle-level ESAD state definition. The ESAD safe/arm stage machine in Section 6.2 is therefore an Analytically Derived interlock state machine whose transition guards are bound to the declared discrete interlock ports and parametric assertions.

### 6.2 Safety Constraint Roster

| Constraint ID | Safety Constraint | Enforcement Interlock | Public Clause Citation |
| :--- | :--- | :--- | :--- |
| SC-01 | The ESAD shall default to the SAFE stage while the ESAD RBF key is removed, the warhead RBF-3 is installed, arm enable is low, or any arming precondition is invalid. | INT-02, INT-03, INT-04, INT-05 | CI-01, CI-03 |
| SC-02 | Warhead initiation shall be impossible unless the ESAD is in the ARMED stage. | INT-02, INT-07 | CI-02, CI-01 |
| SC-03 | Transition from ARM_ENABLE to ARMED shall require two independent authenticated human consents. | INT-06 | CI-01, CI-02 |
| SC-04 | Human-in-the-Loop authorization shall temporally precede every initiation command, and no autonomous initiation path shall exist. | INT-07 | CI-01, CI-03 |
| SC-05 | ESAD umbilical continuity shall be valid before and throughout the ARM_ENABLE and ARMED stages. | INT-03 | CI-03, CI-04 |
| SC-06 | ESAD supply potential and arm enable signal shall remain inside the declared electrical envelope; any excursion shall force SAFE. | INT-04, INT-05 | CI-05, CI-06 |
| SC-07 | UAV bus electrical supply and ESAD arming authority shall be controlled by independent Remove Before Flight keys and the electrical meter switch. | INT-01, INT-02 | CI-01, CI-03 |
| SC-08 | Target track and engagement conditions shall remain inside the declared track duration, elevation, and airspeed envelope. | INT-11 | CI-02, CI-01 |
| SC-09 | No mission waypoint shall be accepted below the declared minimum mission waypoint height. | INT-10 | CI-03, CI-08 |
| SC-10 | The Ruddervator control authority shall require the declared control surface count, servo count, and servo rail level. | INT-13 | CI-04, CI-05 |
| SC-11 | Launcher release shall require the declared pneumatic level, launch angle, launched weight, and launch speed limits. | INT-12 | CI-03, CI-09 |
| SC-12 | Parachute deployment is non-mission and shall not be counted as a safety barrier, recovery credit, or interlock in this mission baseline. | None, excluded | CI-10, CI-03 |

### 6.3 ESAD Critical (DAL-A) Arming Interlock

The ESAD is Critical (DAL-A) (`schema.sysml:1135`, `schema/extracted/oem_bom.md at line 52`). Arming is a staged, hardware-gated permission chain. The SAFE stage is the default and the fail-safe destination for every invalid condition. The ARM_ENABLE stage confirms that the ESAD RBF key is inserted, the warhead RBF-3 is removed, umbilical continuity is valid, supply potential is valid, and the arm enable signal is valid. The ARMED stage adds dual human consent and Human-in-the-Loop authorization. The INITIATED stage is reachable only from ARMED and only after the HITL consent token is already present.

| Stage | ESAD RBF Key | Warhead RBF-3 | Umbilical | Supply Potential | Arm Enable | Dual Consent | HITL Consent | Initiation Permitted |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SAFE | Removed or inserted, any | Installed or removed, any | Any | Any | Any | Any | Any | No |
| SAFE (forced) | Inserted | Removed | Invalid | Valid | Valid | Valid | Valid | No |
| ARM_ENABLE | Inserted | Removed | Valid | Valid | Valid | Not yet present | Not yet present | No |
| ARMED | Inserted | Removed | Valid | Valid | Valid | Present and valid | Present and valid | No |
| INITIATED | Inserted | Removed | Valid | Valid | Valid | Present and valid | Present and valid, earlier than initiation | Yes |

The stage transition guard is:

$$
\begin{aligned}
\mathrm{Stage}(t+1) &=
\begin{cases}
\mathrm{SAFE} & \text{if } \neg \mathrm{RBF}_{\mathrm{ESAD}} \lor \mathrm{RBF}_{\mathrm{WH3}} \lor \neg C_{\mathrm{UMB}} \lor \neg V_{\mathrm{ESAD}} \lor \neg S_{\mathrm{ARM}} \\
\mathrm{ARMED} & \text{if } \mathrm{Stage}(t) = \mathrm{ARM\_ENABLE} \land C_{\mathrm{dual}} \land A_{\mathrm{HITL}} \\
\mathrm{ARM\_ENABLE} & \text{if } \mathrm{RBF}_{\mathrm{ESAD}} \land \neg \mathrm{RBF}_{\mathrm{WH3}} \land C_{\mathrm{UMB}} \land V_{\mathrm{ESAD}} \land S_{\mathrm{ARM}} \\
\mathrm{SAFE} & \text{otherwise}
\end{cases}
\end{aligned}
$$

The initiation guard, including absolute HITL temporal precedence, is:

$$
\begin{aligned}
\mathrm{Initiate}(t) &\iff \mathrm{Stage}(t) = \mathrm{ARMED} \land A_{\mathrm{HITL}} \land C_{\mathrm{dual}} \land (t_{\mathrm{consent}} < t_{\mathrm{init}}) \\
\neg \mathrm{Initiate}(t) &\implies \mathrm{Stage}(t+1) = \mathrm{SAFE}
\end{aligned}
$$

#### 6.3.1 Remove Before Flight Key Interlock

The ESAD RBF key is the "ESAD arming sequence Remove Before Flight key" and connects only through the ESAD discrete interlock (`schema.sysml:1172-1183`; `schema/extracted/oem_bom.md at line 60`; `schema/extracted/interface_table.md at line 56`). The warhead RBF-3 is part of the Safety RBF Devices set and drives the separate `Warhead_RBF_Interlock` (`schema.sysml:2849-2859`, `schema.sysml:452-455`; `schema/extracted/interface_table.md at line 58`; OEM `a5-prep-and-safety-rev7.md:321`). The two keys are independent: the UAV power RBF key controls the power meter ON/OFF interlock (`schema.sysml:2888-2898`; OEM `avenger_v2_5_sysml_v2_ingestion.md:48`), while the ESAD RBF key controls the arming sequence and cannot energize the UAV bus. Removing either key shall drive the affected interlock to its safe state.

#### 6.3.2 Safe and Arm Stage Interlock

The safe/arm stage predicate uses the declared discrete state types. `ESAD_Safe_Arm_Interlock` carries `Safe_or_armed_state`, `Warhead_RBF_Interlock` carries `Safe_or_armed`, and `UAV_Power_Interlock` carries `Power_ON_or_OFF` (`schema.sysml:440-455`). The ESAD arm enable port is `ESAD_Arm_Enable_DSC_IN1` with a 1 ms period and 50 percent duty (`schema.sysml:406-409`). The ESAD detonator output is `ESAD_Detonator_High_Voltage`, a firing pulse up to 1800 V (`schema.sysml:434-437`; `schema/extracted/parametric_limits.md at line 66`; OEM `esad-icd-excalibur-ab00-0054.md:613`). The detonator remains isolated until INITIATED.

The electrical guards are:

$$
\begin{aligned}
C_{\mathrm{UMB}} &\iff R_{\mathrm{UMB}} \le 0.5 \quad \land \quad I_{\mathrm{UMB}} = 20 \\
V_{\mathrm{ESAD}} &\iff 14 \le V_{\mathrm{ESAD}} \le 32 \\
S_{\mathrm{ARM}} &\iff (2.5 \le V_{\mathrm{ARM\_HI}} \le 3.3) \land (V_{\mathrm{ARM\_LO}} \le 0.7) \land T_{\mathrm{ARM}} = 1 \land D_{\mathrm{ARM}} = 50
\end{aligned}
$$

The numeric values are bound as follows: umbilical continuity resistance maximum 0.5 Ohm at 20 mA (`schema/extracted/parametric_limits.md at line 55-56`; OEM `esad-icd-excalibur-ab00-0054.md:284`), ESAD power input minimum 14 V and maximum 32 V with nominal 28 V (`schema/extracted/parametric_limits.md at line 52-54`; OEM `esad-icd-excalibur-ab00-0054.md:272`), arm enable low maximum 0.7 V (`schema/extracted/parametric_limits.md at line 57`; OEM `esad-icd-excalibur-ab00-0054.md:285`), arm enable high minimum 2.5 V and maximum 3.3 V (`schema/extracted/parametric_limits.md at line 58-59`; OEM `esad-icd-excalibur-ab00-0054.md:286`), arm enable period 1 ms and duty cycle 50 percent (`schema/extracted/parametric_limits.md at line 60-61`; OEM `esad-icd-excalibur-ab00-0054.md:285`).

#### 6.3.3 Dual Consent Interlock

The ARMED stage requires two independent authenticated consents from two distinct authorized operators. A single consent, a duplicated identity, a replayed consent, or a consent outside the configured consent window shall leave the stage at ARM_ENABLE.

$$
\begin{aligned}
C_{\mathrm{dual}} &\iff S_{A} \land S_{B} \land (O_{A} \neq O_{B}) \land (|t_{A} - t_{B}| \le \Delta t_{\mathrm{arm}})
\end{aligned}
$$

The consent window `Delta t_arm`, the cryptographic algorithm, key length, and key provisioning method are Not stated in OEM sources. `Delta t_arm` is therefore marked OPERATOR_CONFIGURED and shall be bounded and recorded before flight. The anti-tamper and cyber safeguard obligation is cited to CI-01. The dual consent policy is cited to CI-01 and CI-02.

#### 6.3.4 Human-in-the-Loop Precedence Interlock

Human-in-the-Loop (HITL) authority has absolute temporal precedence over ESAD initiation. The HITL consent token must be authenticated, must belong to an operator in the active crew roster, and must be logged with a timestamp earlier than the initiation command. A veto, a stale consent, an absent consent, or a consent from an inactive operator shall force SAFE and shall withdraw the arm enable signal.

$$
\begin{aligned}
A_{\mathrm{HITL}} &\iff \mathrm{ConsentValid} \land \mathrm{CrewActive} \land \neg \mathrm{Veto} \land (t_{\mathrm{now}} - t_{\mathrm{consent}} \le \tau_{\mathrm{HITL}}) \\
\mathrm{Initiate}(t) &\implies \exists t_{\mathrm{consent}} < t : A_{\mathrm{HITL}}(t_{\mathrm{consent}})
\end{aligned}
$$

The HITL consent validity window `tau_HITL` is Not stated in OEM sources and is marked OPERATOR_CONFIGURED. No autonomous initiation path is permitted under any link state, including total C2 loss. This constraint is cited to CI-01, CI-02, and CI-03. Lost-link behavior shall preserve SAFE and shall not promote the stage.

### 6.4 Subsystem Interlock Roster

| Interlock ID | Interlock Name | Interlocked Subsystems | Predicate Summary | Input Anchors | Methodology | Derivation Grade | Caveat |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| INT-01 | UAV Power RBF Interlock | UAV RBF Key, Power Meter, EPS | UAV bus power available only when the UAV power RBF key is inserted and the power meter switch is ON | `schema.sysml:2680-2690`, `schema.sysml:2888-2898`, `schema/extracted/interface_table.md at line 57` | Leveson STPA safety constraint | Directly Evidenced | None |
| INT-02 | ESAD Arming Stage Interlock | ESAD, ESAD RBF Key, Safety RBF Devices, Warhead | ARMED only after RBF key insertion, warhead RBF-3 removal, continuity, power, arm enable, dual consent, and HITL consent | `schema.sysml:1133-1143`, `schema.sysml:440-455`, `schema/extracted/oem_bom.md at line 52`, `schema/extracted/oem_bom.md at line 60`, `schema/extracted/oem_bom.md at line 70` | Leveson STPA; CI-03 | Analytically Derived | No vehicle-level ESAD state definition is declared in the AST |
| INT-03 | ESAD Umbilical Continuity Interlock | ESAD, ESAD Umbilical, ESAD Harness | Continuity valid only when resistance is at or below 0.5 Ohm at 20 mA | `schema.sysml:1198-1208`, `schema.sysml:412-415`, `schema/extracted/parametric_limits.md at line 55-56` | CI-03 | Directly Evidenced | None |
| INT-04 | ESAD Power Input Envelope Interlock | ESAD, EPS | Supply valid only between 14 V and 32 V | `schema.sysml:400-403`, `schema.sysml:1137`, `schema/extracted/parametric_limits.md at line 52-54` | CI-06 | Directly Evidenced | Nominal 28 V is declared; tolerance form is not stated |
| INT-05 | ESAD Arm Enable Signal Interlock | ESAD, RPI | Arm enable valid only with high phase between 2.5 V and 3.3 V, low phase at or below 0.7 V, 1 ms period, and 50 percent duty | `schema.sysml:406-409`, `schema/extracted/interface_table.md at line 50`, `schema/extracted/parametric_limits.md at line 57-61` | CI-06 | Directly Evidenced | Rise and fall time limits are not stated |
| INT-06 | ESAD Dual Consent Interlock | ESAD, Ground Control Station, Human Operators | ARMED requires two distinct authenticated consents inside the configured window | `schema/extracted/oem_bom.md at line 52`, CI-01 | Leveson STPA; CI-02 | Analytically Derived | Consent window and cryptographic method are Not stated in OEM sources |
| INT-07 | ESAD HITL Precedence Interlock | ESAD, Ground Control Station, Human Operators | Initiation only when an earlier authenticated HITL consent exists and no veto is active | `schema.sysml:394-397`, CI-01 | Leveson STPA; CI-03 | Analytically Derived | HITL timeout is Not stated in OEM sources |
| INT-08 | ESAD Command Link Integrity Interlock | ESAD, RPI | Command accepted only for 5 to 14 byte frames, at most 5 ms response turnaround, at most 10 ms incomplete-message wait, 100 Hz command interval, and 115200 bps link data setting | `schema.sysml:376-379`, `schema/extracted/interface_table.md at line 45`, `schema/extracted/parametric_limits.md at line 62-68` | CI-07 | Directly Evidenced | Message authentication method is Not stated in OEM sources |
| INT-09 | Battery Voltage Interlock | Battery, EPS, Power Meter | Pre-flight voltage between 49 V and 50 V; operating voltage between 36 V and 50.4 V | `schema.sysml:990-1000`, `schema/extracted/parametric_limits.md at line 29-30`, `schema/extracted/parametric_limits.md at line 38-39` | CI-04 | Directly Evidenced | Sensor accuracy is not stated |
| INT-10 | Minimum Waypoint Altitude Interlock | Autopilot, Mission Planning, GCS | Waypoint accepted only when altitude is at least 50 m | `schema/extracted/parametric_limits.md at line 42`, `schema/extracted/interface_table.md at line 63` | Leveson STPA | Directly Evidenced | Terrain database resolution is not stated |
| INT-11 | Target Track and Engagement Envelope Interlock | Gimbal, Camera Compute Module, ESAD | Track valid only for 2 s to 5 s duration, elevation at most 15 deg, and airspeed at most 55 m/s | `schema/extracted/parametric_limits.md at line 48-51`, `schema.sysml:1380-1391` | CI-02 | Directly Evidenced | Positive identification confidence threshold is Not stated in OEM sources |
| INT-12 | Launcher Pneumatic Release Interlock | PL-40 Launcher, Carriage Safety Lock Pin, Trigger Handle | Release only at 13 bar to 14 bar, 12 deg launch angle, at most 30 kg launched mass, at most 25 m/s launch velocity, and after safety lock pin removal | `schema/extracted/parametric_limits.md at line 46-47`, `schema/extracted/parametric_limits.md at line 70-72`, `schema/extracted/oem_bom.md at line 88` | CI-03 | Directly Evidenced | Pneumatic leak rate is not stated |
| INT-13 | Ruddervator Control Authority Interlock | Ruddervator, Ruddervator Servos, EPS Servo Power 8 V Rail | Authority requires four Ruddervators, four Ruddervator servos, eight total servos, and an 8 V servo rail | `schema.sysml:2784-2794`, `schema.sysml:1120-1130`, `schema/extracted/parametric_limits.md at line 20-24`, `schema/extracted/parametric_limits.md at line 28` | CI-04 | Directly Evidenced | Servo torque margin is not stated |

#### 6.4.1 INT-01 UAV Power RBF Interlock

UAV bus power is downstream of the power meter, which switches battery power to the ESC and provides the UAV RBF key interface (`schema.sysml:2680-2690`; OEM `avenger_v2_5_sysml_v2_ingestion.md:18`). The UAV RBF key is the "UAV power Remove Before Flight key" (`schema.sysml:2888-2898`; `schema/extracted/oem_bom.md at line 59`).

$$
\begin{aligned}
\mathrm{Power}_{\mathrm{UAV}} &\iff \mathrm{RBF}_{\mathrm{UAV}} \land \mathrm{SW}_{\mathrm{PM}} \\
\neg \mathrm{RBF}_{\mathrm{UAV}} &\implies \mathrm{Power}_{\mathrm{UAV}} = \mathrm{OFF}
\end{aligned}
$$

#### 6.4.2 INT-02 ESAD Arming Stage Interlock

The stage guards are defined in Section 6.3. The ESAD remains SAFE unless every ARM_ENABLE guard and both human consent guards are satisfied. The ESAD is Critical (DAL-A), and no software path may bypass the RBF key, the warhead RBF-3, or the detonator isolation (`schema.sysml:1133-1143`, `schema.sysml:452-455`, `schema/extracted/interface_table.md at line 56`, `schema/extracted/interface_table.md at line 58`). The derivation is Analytically Derived because the AST declares the components and ports but not a vehicle-level ESAD state definition. The caveat requires verification by hardware-in-the-loop safe-switch testing under CI-03.

#### 6.4.3 INT-03 ESAD Umbilical Continuity Interlock

The ESAD umbilical is the J100 UMB and UMB_RTN continuity line (`schema.sysml:1198-1208`; OEM `esad-icd-excalibur-ab00-0054.md:112`). Continuity failure shall force SAFE and shall withdraw arm enable.

$$
\begin{aligned}
C_{\mathrm{UMB}} &\iff (R_{\mathrm{UMB}} \le 0.5) \land (I_{\mathrm{UMB}} = 20) \\
\neg C_{\mathrm{UMB}} &\implies \mathrm{Stage} = \mathrm{SAFE}
\end{aligned}
$$

#### 6.4.4 INT-04 ESAD Power Input Envelope Interlock

The ESAD J100 input accepts 14 V to 32 V DC with a 28 V nominal (`schema.sysml:400-403`; `schema/extracted/parametric_limits.md at line 52-54`; OEM `esad-icd-excalibur-ab00-0054.md:272`).

$$
\begin{aligned}
V_{\mathrm{ESAD}} &\iff 14 \le V_{\mathrm{ESAD}} \le 32 \\
\neg V_{\mathrm{ESAD}} &\implies \mathrm{Stage} = \mathrm{SAFE}
\end{aligned}
$$

#### 6.4.5 INT-05 ESAD Arm Enable Signal Interlock

The ESAD arm enable discrete is DSC_IN1 with a 1 ms period and 50 percent duty (`schema.sysml:406-409`; `schema/extracted/interface_table.md at line 50`). The high phase is 2.5 V to 3.3 V and the low phase is 0 V to 0.7 V (`schema/extracted/parametric_limits.md at line 57-59`; OEM `esad-icd-excalibur-ab00-0054.md:285-286`). A stuck-high, stuck-low, out-of-band, or wrong-period signal shall not satisfy the guard.

$$
\begin{aligned}
S_{\mathrm{ARM}} &\iff (2.5 \le V_{\mathrm{ARM\_HI}} \le 3.3) \land (V_{\mathrm{ARM\_LO}} \le 0.7) \land (T_{\mathrm{ARM}} = 1) \land (D_{\mathrm{ARM}} = 50)
\end{aligned}
$$

#### 6.4.6 INT-06 ESAD Dual Consent Interlock

The dual consent predicate is defined in Section 6.3.3. The two consents must be independently authenticated and must originate from distinct authorized operators. Reuse of one operator identity for both consents shall be rejected. The consent window is Not stated in OEM sources and is OPERATOR_CONFIGURED. The policy basis is CI-01 and CI-02.

#### 6.4.7 INT-07 ESAD HITL Precedence Interlock

The HITL precedence predicate is defined in Section 6.3.4. The temporal ordering is mandatory: the consent token timestamp precedes the initiation timestamp, and a veto at any time before initiation forces SAFE. No lost-link, degraded-link, or autonomous mode may originate an initiation command. The policy basis is CI-01 and CI-03.

#### 6.4.8 INT-08 ESAD Command Link Integrity Interlock

The RPI ESAD RS-485 link runs at 115200 bps with a 100 Hz command interval (`schema/extracted/parametric_limits.md at line 62-63`; OEM `esad-icd-excalibur-ab00-0054.md:306-307`). Response turnaround is at most 5 ms, incomplete-message wait is at most 10 ms, and message length is 5 to 14 bytes (`schema/extracted/parametric_limits.md at line 64-65`, `schema/extracted/parametric_limits.md at line 67-68`; OEM `esad-icd-excalibur-ab00-0054.md:330`, `esad-icd-excalibur-ab00-0054.md:335`, `esad-icd-excalibur-ab00-0054.md:346`).

$$
\begin{aligned}
L_{\mathrm{ESAD}} &\iff (5 \le B_{\mathrm{frame}} \le 14) \land (t_{\mathrm{resp}} \le 5) \land (t_{\mathrm{wait}} \le 10) \land (f_{\mathrm{cmd}} = 100) \land (R_{\mathrm{link}} = 115200)
\end{aligned}
$$

Link integrity failure shall not promote the ESAD stage. Message authentication is Not stated in OEM sources and is marked OPERATOR_CONFIGURED.

#### 6.4.9 INT-09 Battery Voltage Interlock

The UAV battery operating range is 36 V to 50.4 V (`schema/extracted/parametric_limits.md at line 29-30`; OEM `avenger_v2_5_sysml_v2_ingestion.md:16`). The pre-flight range is 49 V to 50 V (`schema/extracted/parametric_limits.md at line 38-39`; OEM `a5-user-manual-2.md:1366`). The battery is removable, 12S2P Li metal with the retaining strap and locking connector (`schema.sysml:990-1000`).

$$
\begin{aligned}
V_{\mathrm{preflight}} &\iff 49 \le V_{\mathrm{bat}} \le 50 \\
V_{\mathrm{operating}} &\iff 36 \le V_{\mathrm{bat}} \le 50.4 \\
\neg V_{\mathrm{preflight}} &\implies \mathrm{LaunchRelease} = \mathrm{INHIBIT}
\end{aligned}
$$

#### 6.4.10 INT-10 Minimum Waypoint Altitude Interlock

The minimum mission waypoint altitude is 50 m (`schema/extracted/parametric_limits.md at line 42`; OEM `a5-user-manual-2.md:1195`). A waypoint below this floor shall be rejected before upload.

$$
\begin{aligned}
W_{\mathrm{valid}} &\iff h_{\mathrm{wp}} \ge 50
\end{aligned}
$$

#### 6.4.11 INT-11 Target Track and Engagement Envelope Interlock

Target track duration is 2 s minimum and 5 s maximum, maximum engagement elevation is 15 deg, and maximum engagement airspeed is 55 m/s (`schema/extracted/parametric_limits.md at line 48-51`; OEM `a5-user-manual-2.md:2055-2061`). The track gate does not replace dual consent or HITL authorization; both remain mandatory for any initiation.

$$
\begin{aligned}
T_{\mathrm{valid}} &\iff (2 \le T_{\mathrm{track}} \le 5) \land (\theta_{\mathrm{eng}} \le 15) \land (V_{\mathrm{eng}} \le 55) \\
\mathrm{Engage} &\iff T_{\mathrm{valid}} \land C_{\mathrm{dual}} \land A_{\mathrm{HITL}}
\end{aligned}
$$

Positive identification confidence, sensor fusion score, and civilian standoff distance are Not stated in OEM sources and are not assigned numeric thresholds in this mission baseline.

#### 6.4.12 INT-12 Launcher Pneumatic Release Interlock

Launcher pressure is 13 bar minimum and 14 bar maximum (`schema/extracted/parametric_limits.md at line 46-47`; OEM `uav_launcher_pl_40_sysml_v2_ingestion_manual.md:1329`). Launch angle is 12 deg, maximum launched plane mass is 30 kg, and maximum launch velocity is 25 m/s (`schema/extracted/parametric_limits.md at line 70-72`; OEM `uav_launcher_pl_40_sysml_v2_ingestion_manual.md:712`, `uav_launcher_pl_40_sysml_v2_ingestion_manual.md:718-719`). The carriage safety lock pin is removed only before launch (`schema/extracted/oem_bom.md at line 88`; OEM `uav_launcher_pl_40_sysml_v2_ingestion_manual.md:16`). Trigger hold time is 2 s (`schema/extracted/parametric_limits.md at line 94`; OEM `uav_launcher_pl_40_sysml_v2_ingestion_manual.md:530`).

$$
\begin{aligned}
L_{\mathrm{release}} &\iff (13 \le P_{\mathrm{launch}} \le 14) \land (\theta_{\mathrm{launch}} = 12) \land (m_{\mathrm{launch}} \le 30) \land (V_{\mathrm{launch}} \le 25) \land \mathrm{PinRemoved}
\end{aligned}
$$

#### 6.4.13 INT-13 Ruddervator Control Authority Interlock

The Ruddervator is the canonical tail control surface assembly with quantity four, four Ruddervator servos, four wing servos, eight total servos, and an 8 V servo rail (`schema.sysml:2784-2794`, `schema.sysml:1120-1130`; `schema/extracted/parametric_limits.md at line 20-24`, `schema/extracted/parametric_limits.md at line 28`; OEM `a5-user-manual-2.md:273`). A missing surface, a missing servo, or a servo rail outside 8 V shall inhibit control authority and shall prevent arming.

$$
\begin{aligned}
A_{\mathrm{ctrl}} &\iff (N_{\mathrm{RUDD}} = 4) \land (N_{\mathrm{RSRV}} = 4) \land (N_{\mathrm{SRV}} = 8) \land (V_{\mathrm{servo}} = 8)
\end{aligned}
$$

### 6.5 Subsystem State Interlock Traceability

The AST state definitions are package lifecycle state machines, not vehicle flight state machines (`schema.sysml:881-910`). Their deterministic transition pattern is reused as the gating model for the ESAD safe/arm stage interlock: a state may be entered only through an explicit accept event, and the terminal state admits no reverse transition.

| AST State Definition | Declared States | Declared Transitions | Interlock Use |
| :--- | :--- | :--- | :--- |
| `Interface_Table_LifecycleState` | System_State, InitState, ActiveState, Terminal | Initial to System_State; System_State to InitState on Initialize; InitState to ActiveState on Verify; ActiveState to Terminal | Supplies the deterministic accept-event transition pattern applied to the ESAD stage machine in INT-02 |
| `OEM_Bill_of_Materials_LifecycleState` | Air_Vehicle_Avenger_V2_5_State, Airframe_Fuselage_State, Airframe_Payload_Bay_State, Terminal | Initial to Air_Vehicle state; Air_Vehicle to Airframe_Fuselage on Initialize; Airframe_Fuselage to Airframe_Payload_Bay on Verify; Airframe_Payload_Bay to Terminal | Binds the warhead bay and warhead configuration to the pre-arm verification gate in INT-02 and INT-12 |
| `Parametric_Limits_Table_LifecycleState` | System_State, InitState, ActiveState, Terminal | Initial to System_State; System_State to InitState on Initialize; InitState to ActiveState on Verify; ActiveState to Terminal | Binds all 94 parametric assertions to the verified active state used by INT-03 through INT-13 |

The subsystem state interlock map is:

| Subsystem | Required State Before Mission | Forbidden State | Enforcing Interlock |
| :--- | :--- | :--- | :--- |
| ESAD | SAFE until ARM_ENABLE guards pass | ARMED while any arming guard is false, or INITIATED from any stage other than ARMED | INT-02, INT-03, INT-04, INT-05, INT-06, INT-07 |
| Power Meter | ON only after UAV RBF key insertion | ON with UAV RBF key removed | INT-01 |
| ESAD Umbilical | Continuity valid | Open or above 0.5 Ohm at 20 mA | INT-03 |
| Battery | Pre-flight 49 V to 50 V; operating 36 V to 50.4 V | Launch release outside the pre-flight range | INT-09 |
| ESAD Command Link | Frames within 5 to 14 bytes and turnaround within 5 ms | Link promotion of the ESAD stage while integrity is invalid | INT-08 |
| Warhead | Mechanically installed in the warhead bay with RBF-3 removed only for authorized flight | Initiation train complete while RBF-3 is installed | INT-02, INT-07 |
| Ruddervator | Four surfaces, four Ruddervator servos, eight total servos, 8 V rail | Arming with missing surface, missing servo, or invalid rail | INT-13 |
| Launcher | 13 bar to 14 bar, 12 deg, at most 30 kg, at most 25 m/s, safety lock pin removed | Release with safety lock pin installed or pressure outside 13 bar to 14 bar | INT-12 |

### 6.6 Consolidated Parameter Definitions

| Parameter | Symbol | Grounded Reference | Value or Constraint | Source Citation |
| :--- | :--- | :--- | :--- | :--- |
| ESAD supply potential minimum | V_ESAD_min | V | 14 V | `schema/extracted/parametric_limits.md at line 52`; OEM `esad-icd-excalibur-ab00-0054.md:272` |
| ESAD supply potential maximum | V_ESAD_max | V | 32 V | `schema/extracted/parametric_limits.md at line 53`; OEM `esad-icd-excalibur-ab00-0054.md:272` |
| ESAD supply potential nominal | V_ESAD_nom | V | 28 V | `schema/extracted/parametric_limits.md at line 54`; OEM `esad-icd-excalibur-ab00-0054.md:272` |
| ESAD umbilical continuity resistance | R_UMB_max | PL-49/PL-50 | 0.5 Ohm | `schema/extracted/parametric_limits.md at line 55`; OEM `esad-icd-excalibur-ab00-0054.md:284` |
| ESAD umbilical continuity current | I_UMB | mA | 20 mA | `schema/extracted/parametric_limits.md at line 56`; OEM `esad-icd-excalibur-ab00-0054.md:284` |
| ESAD arm enable low maximum | V_ARM_LO_max | V | 0.7 V | `schema/extracted/parametric_limits.md at line 57`; OEM `esad-icd-excalibur-ab00-0054.md:285` |
| ESAD arm enable high minimum | V_ARM_HI_min | V | 2.5 V | `schema/extracted/parametric_limits.md at line 58`; OEM `esad-icd-excalibur-ab00-0054.md:286` |
| ESAD arm enable high maximum | V_ARM_HI_max | V | 3.3 V | `schema/extracted/parametric_limits.md at line 59`; OEM `esad-icd-excalibur-ab00-0054.md:286` |
| ESAD arm enable period | T_ARM | ms | 1 ms | `schema/extracted/parametric_limits.md at line 60`; OEM `esad-icd-excalibur-ab00-0054.md:285` |
| ESAD arm enable duty cycle | D_ARM | percent | 50 percent | `schema/extracted/parametric_limits.md at line 61`; OEM `esad-icd-excalibur-ab00-0054.md:285` |
| ESAD RS-485 rate | R_link | bps | 115200 bps | `schema/extracted/parametric_limits.md at line 62`; OEM `esad-icd-excalibur-ab00-0054.md:306` |
| ESAD command interval | f_cmd | Hz | 100 Hz | `schema/extracted/parametric_limits.md at line 63`; OEM `esad-icd-excalibur-ab00-0054.md:307` |
| ESAD response turnaround maximum | t_resp_max | ms | 5 ms | `schema/extracted/parametric_limits.md at line 64`; OEM `esad-icd-excalibur-ab00-0054.md:330` |
| ESAD incomplete message wait maximum | t_wait_max | ms | 10 ms | `schema/extracted/parametric_limits.md at line 65`; OEM `esad-icd-excalibur-ab00-0054.md:335` |
| ESAD detonator high voltage maximum | V_HV_max | V | 1800 V | `schema/extracted/parametric_limits.md at line 66`; OEM `esad-icd-excalibur-ab00-0054.md:613` |
| ESAD message length minimum | B_frame_min | bytes | 5 bytes | `schema/extracted/parametric_limits.md at line 67`; OEM `esad-icd-excalibur-ab00-0054.md:346` |
| ESAD message length maximum | B_frame_max | bytes | 14 bytes | `schema/extracted/parametric_limits.md at line 68`; OEM `esad-icd-excalibur-ab00-0054.md:346` |
| UAV battery operating minimum | V_bat_op_min | V | 36 V | `schema/extracted/parametric_limits.md at line 29`; OEM `avenger_v2_5_sysml_v2_ingestion.md:16` |
| UAV battery operating maximum | V_bat_op_max | V | 50.4 V | `schema/extracted/parametric_limits.md at line 30`; OEM `avenger_v2_5_sysml_v2_ingestion.md:16` |
| UAV battery pre-flight minimum | V_bat_pf_min | V | 49 V | `schema/extracted/parametric_limits.md at line 38`; OEM `a5-user-manual-2.md:1366` |
| UAV battery pre-flight maximum | V_bat_pf_max | V | 50 V | `schema/extracted/parametric_limits.md at line 39`; OEM `a5-user-manual-2.md:1366` |
| Minimum mission waypoint altitude | h_wp_min | m | 50 m | `schema/extracted/parametric_limits.md at line 42`; OEM `a5-user-manual-2.md:1195` |
| Target track duration minimum | T_track_min | s | 2 s | `schema/extracted/parametric_limits.md at line 48`; OEM `a5-user-manual-2.md:2055` |
| Target track duration maximum | T_track_max | s | 5 s | `schema/extracted/parametric_limits.md at line 49`; OEM `a5-user-manual-2.md:2055` |
| Maximum engagement elevation | theta_eng_max | deg | 15 deg | `schema/extracted/parametric_limits.md at line 50`; OEM `a5-user-manual-2.md:2056` |
| Maximum engagement airspeed | V_eng_max | m/s | 55 m/s | `schema/extracted/parametric_limits.md at line 51`; OEM `a5-user-manual-2.md:2061` |
| Launcher pressure minimum | P_launch_min | PL-40/PL-41 | 13 bar | `schema/extracted/parametric_limits.md at line 46`; OEM `uav_launcher_pl_40_sysml_v2_ingestion_manual.md:1329` |
| Launcher pressure maximum | P_launch_max | PL-40/PL-41 | 14 bar | `schema/extracted/parametric_limits.md at line 47`; OEM `uav_launcher_pl_40_sysml_v2_ingestion_manual.md:1329` |
| Maximum launched plane mass | m_launch_max | kg | 30 kg | `schema/extracted/parametric_limits.md at line 70`; OEM `uav_launcher_pl_40_sysml_v2_ingestion_manual.md:718` |
| Maximum launch velocity | V_launch_max | m/s | 25 m/s | `schema/extracted/parametric_limits.md at line 71`; OEM `uav_launcher_pl_40_sysml_v2_ingestion_manual.md:719` |
| Launcher launch angle | theta_launch | deg | 12 deg | `schema/extracted/parametric_limits.md at line 72`; OEM `uav_launcher_pl_40_sysml_v2_ingestion_manual.md:712` |
| Trigger hold time | T_trigger | s | 2 s | `schema/extracted/parametric_limits.md at line 94`; OEM `uav_launcher_pl_40_sysml_v2_ingestion_manual.md:530` |
| Ruddervator quantity | N_RUDD | PL-20/PL-24 | 4 units | `schema/extracted/parametric_limits.md at line 20`; OEM `a5-user-manual-2.md:339` |
| Ruddervator servo quantity | N_RSRV | PL-20/PL-24 | 4 units | `schema/extracted/parametric_limits.md at line 22`; OEM `avenger_v2_5_sysml_v2_ingestion.md:22` |
| Total servo quantity | N_SRV | PL-20/PL-24 | 8 units | `schema/extracted/parametric_limits.md at line 24`; OEM `avenger_v2_5_sysml_v2_ingestion.md:31` |
| Servo power rail voltage | V_servo | V | 8 V | `schema/extracted/parametric_limits.md at line 28`; OEM `avenger_v2_5_sysml_v2_ingestion.md:79` |
| Dual consent window | Delta t_arm | s | Not stated in OEM sources; OPERATOR_CONFIGURED | No OEM line; declared assumption |
| HITL consent validity window | tau_HITL | s | Not stated in OEM sources; OPERATOR_CONFIGURED | No OEM line; declared assumption |
| Positive identification confidence threshold | C_PID | dimensionless | Not stated in OEM sources | No OEM line; declared assumption |
| Parachute deployment | None | Not stated in OEM sources | Non-mission configuration; excluded | `schema/extracted/oem_bom.md at line 47`; `schema.sysml:2061-2071` |

### 6.7 OEM-Silent Fields and Declared Assumptions

The following fields have no OEM numeric declaration and are explicitly carried as declared assumptions or operator-configured values. They are not presented as OEM facts:

1. **Dual consent window `Delta t_arm`**: Not stated in OEM sources. The interlock requires only that both consents fall inside the configured window and that the operator identities differ.
2. **Consent cryptographic method**: Not stated in OEM sources. The anti-tamper obligation is cited to CI-01; the algorithm and key length require a downstream security architecture.
3. **HITL consent validity window `tau_HITL`**: Not stated in OEM sources. The precedence relation is fixed; only the freshness window is configurable.
4. **ESAD safe-to-arm and arm-to-fire dwell times**: Not stated in OEM sources. No dwell-time credit is claimed.
5. **ESAD command authentication**: Not stated in OEM sources. The RS-485 frame timing and length bounds are declared, but message authentication is not declared.
6. **Positive identification confidence**: Not stated in OEM sources. No multi-spectral confidence threshold is asserted in this unit.
7. **Civilian standoff distance**: Not stated in OEM sources. No standoff radius is asserted in this unit.
8. **Servo torque margin and actuator rate limits**: Not stated in OEM sources. The control authority interlock verifies only presence, count, and rail voltage.
9. **Pneumatic leak rate and compressor duty cycle**: Not stated in OEM sources. The launcher interlock verifies only the declared release envelope.
10. **Battery sensor accuracy and state-of-charge model**: Not stated in OEM sources. The voltage interlock uses the declared voltage bounds only.

Parachute deployment is explicitly non-mission (`schema/extracted/oem_bom.md at line 47`; `schema.sysml:2061-2071`). It is excluded from every safety constraint, interlock predicate, and recovery credit in this unit.

### 6.8 Public Clause Citation Index

| Citation ID | Public Clause Citation | Applied To | Verification Mechanism |
| :--- | :--- | :--- | :--- |
| CI-01 | DoD Directive 3000.09 Section 3.1, Section 3.1.a, Section 3.1.b, Section 3.1.c | SC-01, SC-02, SC-03, SC-04, SC-07, INT-02, INT-06, INT-07 | Human judgement policy audit and consent verification |
| CI-02 | CJCSI 3121.01B Enclosure A Section 2.a, Enclosure A Section 4.b, Enclosure B Section 3.c, Enclosure E Section 2.d | SC-02, SC-03, SC-08, INT-06, INT-11 | Escalation of force interlock and identification audit |
| CI-03 | MIL-STD-882E Task 106 Section 4.2, Task 201 Section 4.2, Task 204 Section 4.2, Task 205 Section 4.2, Task 208 Section 4.2 | SC-01, SC-04, SC-05, SC-07, SC-09, SC-11, SC-12, INT-02, INT-03, INT-08, INT-12 | System hazard analysis and functional thread isolation check |
| CI-04 | SAE ARP4761 Section 4.3.1, Section 4.3.3, App. L, App. M | SC-05, SC-10, INT-09, INT-13 | Functional hazard assessment and common cause analysis |
| CI-05 | RTCA DO-178C Section 6.3.1, Section 6.3.2, Section 6.4.3, Section 6.4.4 | SC-06, SC-10, INT-02, INT-05 | Software fault detection and structural coverage review |
| CI-06 | ASTM F3269-17 Section 5.1, Section 5.2, Section 5.3, Section 5.4 | SC-06, INT-04, INT-05 | Run-time assurance monitor and deterministic state switching check |
| CI-07 | MIL-STD-1629A Section 4.3, Section 4.4, Section 4.5, Section 4.6 | INT-08 | Failure detection timing and criticality review |
| CI-08 | FAA 14 CFR Section 107.49(a), Section 107.49(b), Section 107.49(c), Section 107.49(d) | SC-09, INT-10 | Pre-flight inspection and vehicle integrity audit |
| CI-09 | AMC1 UAS.SPEC.050 Section 3.2, Section 3.3, Section 4.1, Section 4.4 | SC-11, INT-12 | Pre-flight checklist and site survey verification |
| CI-10 | JARUS SORA v2.5 Annex E Section E.5, Section E.17, Section E.18 | SC-12 | Single point of failure and payload containment review |

## Source References

This unit is grounded in the SysML interlock port contracts at .pipeline/schema.sysml:440-455, the package lifecycle state definitions at .pipeline/schema.sysml:881-910, the ESAD and RBF key part definitions at .pipeline/schema.sysml:1133-1143 and .pipeline/schema.sysml:1172-1183, the extracted interface table at schema/extracted/interface_table.md at line 45-59, the extracted OEM BOM at schema/extracted/oem_bom.md at line 47-70, the extracted parametric limits at schema/extracted/parametric_limits.md at line 20-94, and the normative baseline at docs/research/RESEARCH_INVENTORY.md at line 18-37.

- [.pipeline/schema.sysml:440-455](../../../../.pipeline/schema.sysml) declares the ESAD safe/arm, UAV power, and warhead RBF discrete interlock ports.
- [.pipeline/schema.sysml:881-910](../../../../.pipeline/schema.sysml) declares the three package lifecycle state definitions.
- [.pipeline/schema.sysml:1133-1143](../../../../.pipeline/schema.sysml) declares the ESAD as Critical (DAL-A).
- [.pipeline/schema.sysml:1172-1183](../../../../.pipeline/schema.sysml) declares the ESAD RBF key.
- [.pipeline/schema.sysml:2061-2071](../../../../.pipeline/schema.sysml) declares parachute deployment as non-mission.
- [.pipeline/schema.sysml:2680-2690](../../../../.pipeline/schema.sysml) declares the power meter and UAV RBF key interface.
- [.pipeline/schema.sysml:2849-2859](../../../../.pipeline/schema.sysml) declares the Safety RBF Devices set including warhead RBF-3.
- [.pipeline/schema.sysml:2888-2898](../../../../.pipeline/schema.sysml) declares the UAV power RBF key.
- [.pipeline/schema.sysml:2901-2911](../../../../.pipeline/schema.sysml) declares the warhead with a 5 kg mass.
- [schema/extracted/interface_table.md at line 45-59](../../../../schema/extracted/interface_table.md) declares the ESAD communication, power, arm enable, umbilical, detonator, and interlock interfaces.
- [schema/extracted/oem_bom.md at line 47-70](../../../../schema/extracted/oem_bom.md) declares the parachute exclusion, ESAD family, warhead, RBF keys, warhead bay, and safety RBF devices.
- [schema/extracted/parametric_limits.md at line 20-94](../../../../schema/extracted/parametric_limits.md) carries the parameter values and their OEM file and line evidence used by every numeric interlock.
- [docs/research/RESEARCH_INVENTORY.md at line 18](../../../../docs/research/RESEARCH_INVENTORY.md) declares DoD Directive 3000.09 clauses Section 3.1, Section 3.1.a, Section 3.1.b, and Section 3.1.c.
- [docs/research/RESEARCH_INVENTORY.md at line 20](../../../../docs/research/RESEARCH_INVENTORY.md) declares CI-02 and Enclosure E Section 2.d.
- [docs/research/RESEARCH_INVENTORY.md at line 36](../../../../docs/research/RESEARCH_INVENTORY.md) declares CI-03.
- [docs/research/RESEARCH_INVENTORY.md at line 34-37](../../../../docs/research/RESEARCH_INVENTORY.md) declares CI-07, CI-04, and CI-05.
- [docs/research/RESEARCH_INVENTORY.md at line 31](../../../../docs/research/RESEARCH_INVENTORY.md) declares CI-06.
