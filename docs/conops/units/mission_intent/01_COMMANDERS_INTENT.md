| Attribute | Specification Detail |
| :--- | :--- |
| **Document ID** | `MI-01` |
| **Issue ID** | `MI-01` |
| **Type** | `Tactical Mission Intent` |
| **Generation Mode** | `Agent-Assisted` |
| **Specification Source** | `docs/research/RESEARCH_INVENTORY.md; schema/extracted/parametric_limits.md` |
| **Version** | `1.0.0` |
| **Date** | `2026-10-31` |

# Tactical Mission Intent & Execution Plan

## 1. Commander's Intent & Operational Objectives

**Operational Purpose.** The Avenger V2.5 air vehicle and PL-40 pneumatic launcher provide expeditionary, runway-independent tactical reconnaissance and precision engagement against designated targets. The commander's purpose is to place a persistent sensor-and-effect capability over the assigned objective within the OEM flight and engagement envelope, while keeping the weapon chain under positive human control, preserving a recoverable energy margin, and containing the air vehicle inside its authorized operating volume. The parachute deployment module is a non-mission R&D variant and is excluded from the mission baseline [schema/extracted/oem_bom.md at line 47].

**Key Mission Tasks.**

1. **Pre-flight verification.** Confirm the UAV battery pre-flight voltage is between 49 V and 50 V [schema/extracted/parametric_limits.md PL-32, PL-33], the pitot static response is between 0 m/s and 3 m/s with a blow-test at or above 10 m/s [schema/extracted/parametric_limits.md PL-34, PL-35], the PL-40 launcher pressure is between 13 bar and 14 bar [schema/extracted/parametric_limits.md PL-40, PL-41], the launcher set-up time is between 0 min and 5 min [schema/extracted/parametric_limits.md PL-72], and the ESAD umbilical continuity is at or below 0.5 Ohm at 20 mA [schema/extracted/parametric_limits.md PL-49, PL-50].
2. **Launch.** Employ the PL-40 launcher at a 12 deg launch angle [schema/extracted/parametric_limits.md PL-66], with launched mass at or below 30 kg [schema/extracted/parametric_limits.md PL-64] and air vehicle maximum take-off weight at or below 17 kg [schema/extracted/parametric_limits.md PL-12]. Respect the launcher maximum launch velocity of 25 m/s [schema/extracted/parametric_limits.md PL-65] and transition to the air vehicle minimum flight speed of 26 m/s [schema/extracted/parametric_limits.md PL-05].
3. **Transit and loiter.** Cruise at 30 m/s [schema/extracted/parametric_limits.md PL-01], and remain within the maximum horizontal speed of 38 m/s [schema/extracted/parametric_limits.md PL-02], maximum dive speed of 55 m/s [schema/extracted/parametric_limits.md PL-03], maximum dive angle of 22 deg [schema/extracted/parametric_limits.md PL-04], minimum mission waypoint altitude of 50 m [schema/extracted/parametric_limits.md PL-36], 300 m loiter radius [schema/extracted/parametric_limits.md PL-37], 90 min flight endurance [schema/extracted/parametric_limits.md PL-06], 60 km direct radio line-of-sight range [schema/extracted/parametric_limits.md PL-07], and 60 km to 180 km extended radio line-of-sight range [schema/extracted/parametric_limits.md PL-08].
4. **Sense, track, and identify.** Use the gimbal seeker across a zoom factor of 1X to 40X [schema/extracted/parametric_limits.md PL-27], seeker pitch of -45 deg to 135 deg [schema/extracted/parametric_limits.md PL-25], seeker yaw and roll of -165 deg to 165 deg [schema/extracted/parametric_limits.md PL-26], and day and thermal imagery at 1280 pixels by 720 pixels [schema/extracted/parametric_limits.md PL-28, PL-29, PL-30, PL-31]. Hold target track duration between 2 s and 5 s [schema/extracted/parametric_limits.md PL-42, PL-43], and remain within the maximum engagement elevation of 15 deg [schema/extracted/parametric_limits.md PL-44] and maximum engagement airspeed of 55 m/s [schema/extracted/parametric_limits.md PL-45].
5. **Command and control.** Maintain the DTC radio link in the 4.4 GHz to 5.0 GHz band [schema/extracted/oem_bom.md at line 44; schema/extracted/interface_table.md at line 63] at the 2 W ground radio setting [schema/extracted/parametric_limits.md PL-39].
   Maintain DroneCAN control of the four ruddervator servos on the first CAN bus [schema/extracted/oem_bom.md at line 23; schema/extracted/interface_table.md at line 12-15] and of the four wing servos on the second CAN bus [schema/extracted/oem_bom.md at line 30-38].
6. **Authorize and engage.** Require positive identification, human authorization, and ESAD safe and arm consent before any warhead initiation. ESAD is Critical / DAL-A [schema/extracted/oem_bom.md at line 52].
   Its arm enable is a 1 ms period at 50 percent duty [schema/extracted/parametric_limits.md PL-54, PL-55], with a high state of 2.5 V DC to 3.3 V DC [schema/extracted/parametric_limits.md PL-52, PL-53] and a low state at or below 0.7 V DC [schema/extracted/parametric_limits.md PL-51].
   ESAD input power is 14 V to 32 V DC, nominal 28 V [schema/extracted/parametric_limits.md PL-46, PL-47, PL-48], with RS-485 at 115200 bps and 100 Hz [schema/extracted/parametric_limits.md PL-56, PL-57], response latency of 0 ms to 5 ms [schema/extracted/parametric_limits.md PL-58], incomplete-message wait of 0 ms to 10 ms [schema/extracted/parametric_limits.md PL-59], high-voltage measurement range of 0 V to 1800 V [schema/extracted/parametric_limits.md PL-60], and message length of 5 bytes to 14 bytes [schema/extracted/parametric_limits.md PL-61, PL-62].
7. **Recover or divert.** Monitor remaining energy against the bingo threshold for the recovery route. Execute return-to-base or secondary divert when bingo is reached, then land, safe the actuators, return ESAD to a safe state, zeroize weapon-chain keys, and offload diagnostic logs.

**Desired End State.**

- All assigned corridor waypoints are traversed and verified within the OEM flight envelope.
- Zero unauthorized four-dimensional boundary excursions and zero unmitigated collision or interference hazards.
- All targets are positively identified and human-authorized before engagement.
- Either a controlled engagement or a safe recovery is complete, with residual energy at or above the bingo threshold computed for the recovery route.
- ESAD is returned to a safe state, weapon-chain keys are zeroized, and diagnostic logs are retained for post-mission review.

**Constraints.**

- ESAD is Critical / DAL-A; autonomous weapon release is prohibited. Human judgment in the use of force and fail-safe interlocks are mandatory [docs/research/RESEARCH_INVENTORY.md; DoD Directive 3000.09 Sec. 3.1, Sec. 3.1.b].
- Positive identification and collateral-damage mitigation are mandatory [docs/research/RESEARCH_INVENTORY.md; CJCSI 3121.01B Enclosure A Sec. 4.b, Enclosure B Sec. 3.c].
- Link-loss fallback, run-time containment, and operational containment follow RTCA DO-362A Sec. 3.4, ASTM F3269-17 Sec. 5.2 and Sec. 5.3, and JARUS SORA v2.5 Annex E Sec. E.14 [docs/research/RESEARCH_INVENTORY.md].
- The launcher works between -20 degC and 50 degC [schema/extracted/parametric_limits.md PL-73, PL-74], and its battery is charged between 10 degC and 40 degC [schema/extracted/parametric_limits.md PL-91, PL-92].
- The air vehicle operating temperature envelope, terminal accuracy, target-confidence threshold, pre-flight built-in-test duration, imagery resolution beyond the stated day and thermal camera limits, and a 90 km relay range are Not stated in OEM sources.
- Parachute deployment is non-mission and excluded from all mission-baseline planning and credit [schema/extracted/oem_bom.md at line 47].

### 1.1 Normative Baseline & Doctrinal Authority

This Tactical Mission Intent is authored under the following cited baselines:

- **ISO/IEC/IEEE 29148:2018** Systems and Software Engineering -- Life Cycle Processes -- Requirements Engineering, Sec. 6.4.2 [docs/research/RESEARCH_INVENTORY.md].
- **INCOSE Systems Engineering Handbook v5.0**, Sec. 3.3.1 and Sec. 5.4 [docs/research/RESEARCH_INVENTORY.md].
- **DoD Directive 3000.09**, Sec. 3.1 and Sec. 3.1.b [docs/research/RESEARCH_INVENTORY.md].
- **CJCSI 3121.01B**, Enclosure A Sec. 4.b and Enclosure B Sec. 3.c [docs/research/RESEARCH_INVENTORY.md].
- **MIL-STD-882E**, Task 205 Sec. 4.2 [docs/research/RESEARCH_INVENTORY.md].
- **RTCA DO-362A**, Sec. 3.4 [docs/research/RESEARCH_INVENTORY.md].
- **ASTM F3269-17**, Sec. 5.2 and Sec. 5.3 [docs/research/RESEARCH_INVENTORY.md].
- **JARUS SORA v2.5**, Annex E Sec. E.14 [docs/research/RESEARCH_INVENTORY.md].
- **NIST SP 800-82r3**, Sec. 6.2 [docs/research/RESEARCH_INVENTORY.md].

## Source References

This specification is grounded in schema/extracted/parametric_limits.md lines 5-100 (parametric limits PL-01 through PL-94), schema/extracted/oem_bom.md lines 7-103 (subsystem, ESAD, ruddervator, parachute, radio, and launcher evidence), schema/extracted/interface_table.md lines 7-67 (CAN, Ethernet, RS-485, RF, ESAD, and launcher interface evidence), .pipeline/schema.sysml lines 1-1123 (consolidated AST part, port, attribute, and constraint definitions), docs/research/RESEARCH_INVENTORY.md lines 15-167 (normative standards, obligations, and public clauses), and ISO/IEC/IEEE 29148:2018 Sec. 6.4.2 (ConOps requirements engineering clause).
