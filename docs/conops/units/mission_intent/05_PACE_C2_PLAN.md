| Attribute | Specification Detail |
| :--- | :--- |
| **Title** | Tactical Mission Intent: PACE C2 Communications Plan |
| **Version** | 1.0.0 |
| **Date** | 2026-09-02 |
| **Issue ID** | MI-05 |
| **Type** | Mission Intent |
| **Generation Mode** | Schema-Derived |
| **Specification Source** | `.pipeline/schema.sysml` |

## 5. PACE C2 Link Communications Plan

In accordance with RTCA DO-362A Section 2.2 and Section 3.4, Command and Control (C2) communications robustness is maintained through a four-tier Primary, Alternate, Contingency, Emergency (PACE) architecture with deterministic down-tier failover and re-acquisition hysteresis. The only C2 medium declared by the OEM sources is the DTC radio transceiver operating in the 4.4 GHz to 5.0 GHz band. Alternate, Contingency, and Emergency media are not declared in the OEM sources and are carried as operator-configured parameters pending OEM data.

| PACE Tier | Link Medium | Frequency Band (f_band) | Bandwidth (Rate_nom) | Heartbeat Timeout (tau_timeout) | Failover Hysteresis (tau_hysteresis) | Priority / Role | Grounding Citation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Primary** | DTC C2 radio transceiver with dual MPSL4400 antennas | 4.4 GHz to 5.0 GHz | Not stated in OEM sources | Not stated in OEM sources (OPERATOR_CONFIGURED tau_timeout_Primary) | Not stated in OEM sources (OPERATOR_CONFIGURED tau_hysteresis_Primary) | Primary C2 and telemetry path; ground radio output power 2 W | RTCA DO-362A Section 2.2.1; FAA pre-flight C2 link verification clause; schema/extracted/interface_table.md at line 63-64; schema/extracted/oem_bom.md at line 44-46; schema/extracted/parametric_limits.md at line 45 |
| **Alternate** | Not stated in OEM sources | Not stated in OEM sources | Not stated in OEM sources | Not stated in OEM sources (OPERATOR_CONFIGURED tau_timeout_Alternate) | Not stated in OEM sources (OPERATOR_CONFIGURED tau_hysteresis_Alternate) | Degraded C2 and telemetry continuity; no OEM-declared alternate medium | RTCA DO-362A Section 3.4; NATO STANAG 4586 Section 5.1; AMC1 UAS.SPEC.050 Section 3.3 |
| **Contingency** | Not stated in OEM sources | Not stated in OEM sources | Not stated in OEM sources | Not stated in OEM sources (OPERATOR_CONFIGURED tau_timeout_Contingency) | Not stated in OEM sources (OPERATOR_CONFIGURED tau_hysteresis_Contingency) | Essential flight-control command and abort path; no OEM-declared contingency medium | RTCA DO-362A Section 3.4; NATO STANAG 4586 Section 5.1; MIL-STD-882E Task 208 Section 4.2 |
| **Emergency** | Not stated in OEM sources | Not stated in OEM sources | Not stated in OEM sources | Not stated in OEM sources (OPERATOR_CONFIGURED tau_timeout_Emergency) | Not stated in OEM sources (OPERATOR_CONFIGURED tau_hysteresis_Emergency) | Autonomous lost-link navigation and flight termination; no OEM-declared emergency medium; parachute deployment is non-mission and excluded | RTCA DO-362A Section 3.4; DoD Directive 3000.09 Section 3.1.b; JARUS SORA v2.5 Annex E Section E.6 |

### 5.1 Failover State Transition Dynamics

Link state degradation triggers deterministic down-tier failover when the active tier heartbeat stream is interrupted beyond its designated timeout threshold tau_timeout,i. Re-acquisition up-tier promotion is gated by the hysteresis window tau_hysteresis,i+1 to prevent oscillatory tier chattering.

$$
\begin{aligned}
\Delta t_{\mathrm{loss}}(t) &= t - t_{\text{last\_valid\_rx}} \\
\mathrm{State}(t) &= \begin{cases}
\mathrm{Tier}_i & \text{if } \Delta t_{\mathrm{loss}} < \tau_{\mathrm{timeout},i} \\
\mathrm{Tier}_{i+1} & \text{if } \Delta t_{\mathrm{loss}} \ge \tau_{\mathrm{timeout},i} \quad \text{for } t \ge t_{\mathrm{fail}} + \tau_{\mathrm{hysteresis},i+1}
\end{cases}
\end{aligned}
$$

- Parameter Definitions & Engineering Units:

| Parameter | Symbol | Units | Constraint / Rule | Description |
| :--- | :--- | :--- | :--- | :--- |
| Active Link Loss Duration | Delta t_loss | s | Measured online | Measured elapsed duration since the last authenticated frame |
| Last Valid Receive Epoch | t_last_valid_rx | s | Measured online | Time epoch of the last authenticated frame on the active tier |
| Failover Epoch | t_fail | s | Measured online | Time epoch at which the active tier timeout threshold was exceeded |
| Primary Heartbeat Timeout | tau_timeout_Primary | s | tau_timeout_Primary > 0 s | Timeout triggering fallback to Alternate tier; Not stated in OEM sources, OPERATOR_CONFIGURED |
| Alternate Heartbeat Timeout | tau_timeout_Alternate | s | tau_timeout_Alternate > tau_timeout_Primary | Timeout triggering fallback to Contingency tier; Not stated in OEM sources, OPERATOR_CONFIGURED |
| Contingency Heartbeat Timeout | tau_timeout_Contingency | s | tau_timeout_Contingency > tau_timeout_Alternate | Timeout triggering fallback to Emergency tier; Not stated in OEM sources, OPERATOR_CONFIGURED |
| Emergency Heartbeat Timeout | tau_timeout_Emergency | s | tau_timeout_Emergency > tau_timeout_Contingency | Timeout initiating the definitive lost-link failsafe sequence; Not stated in OEM sources, OPERATOR_CONFIGURED |
| Re-acquisition Hysteresis Window | tau_hysteresis,i | s | tau_hysteresis,i > 0 s | Continuous stable link duration required before up-tier promotion; Not stated in OEM sources, OPERATOR_CONFIGURED |

### 5.2 Link Integrity and Safety Interlocks

All PACE tiers require authenticated and replay-resistant frames per NIST SP 800-82r3 Section 6.2, with RF susceptibility bounded per MIL-STD-461G Section 5.18. The internal CAN 1 Ruddervator bus and CAN 2 wing servo bus are onboard control buses and are not PACE communication tiers. The ESAD is Critical (DAL-A); no PACE tier may initiate, arm, or command the ESAD, whose initiation remains gated by hardware interlocks and human authorization per DoD Directive 3000.09 Section 3.1.b and MIL-STD-882E Task 208 Section 4.2. Parachute deployment is a non-mission configuration and is excluded from all PACE recovery credit.

## Source References

The PACE plan is grounded in the SysML port contracts at .pipeline/schema.sysml:482-487 and the extracted schema table at schema/extracted/interface_table.md, with OEM source lines a5-user-manual-2.md:1273 and a5-user-manual-2.md:1687, together with the public clauses RTCA DO-362A Section 2.2.1 and Section 3.4, MIL-STD-461G Section 5.18, NATO STANAG 4586 Section 5.1, and NIST SP 800-82r3 Section 6.2.

- [.pipeline/schema.sysml:482-487](../../../../.pipeline/schema.sysml) declares GCS_UAV_Telemetry_Link and GCS_Antenna_RF with protocol family "RF 4.4 to 5.0 GHz".
- [schema/extracted/interface_table.md at line 42-43](../../../../schema/extracted/interface_table.md) declares Radio RF Feed Upper and Radio RF Feed Lower.
- [schema/extracted/interface_table.md at line 63-64](../../../../schema/extracted/interface_table.md) declares GCS UAV Telemetry Link and GCS Antenna RF at RF 4.4 to 5.0 GHz, citing OEM [a5-user-manual-2.md:1273](../../../../schema/a5-user-manual-2.md) and [a5-user-manual-2.md:1687](../../../../schema/a5-user-manual-2.md).
- [schema/extracted/oem_bom.md at line 44-46](../../../../schema/extracted/oem_bom.md) declares Radio Module DTC, Radio Antenna MPSL4400 Upper, and Radio Antenna MPSL4400 Lower.
- [schema/extracted/oem_bom.md at line 47](../../../../schema/extracted/oem_bom.md) declares Parachute Deployment Non-Mission with configuration non-mission and baseline false.
- [schema/extracted/parametric_limits.md at line 45](../../../../schema/extracted/parametric_limits.md) declares PL-39 Ground radio power 2 W.
- [docs/research/RESEARCH_INVENTORY.md at line 18](../../../../docs/research/RESEARCH_INVENTORY.md) declares DoD Directive 3000.09 Section 3.1.b.
- [docs/research/RESEARCH_INVENTORY.md at line 19](../../../../docs/research/RESEARCH_INVENTORY.md) declares NATO STANAG 4586 Section 5.1.
- [docs/research/RESEARCH_INVENTORY.md at line 21](../../../../docs/research/RESEARCH_INVENTORY.md) declares NIST SP 800-82r3 Section 6.2.
- [docs/research/RESEARCH_INVENTORY.md at line 23](../../../../docs/research/RESEARCH_INVENTORY.md) declares MIL-STD-461G Section 5.18.
- [docs/research/RESEARCH_INVENTORY.md at line 25](../../../../docs/research/RESEARCH_INVENTORY.md) declares FAA 14 CFR Section 107.49(b).
- [docs/research/RESEARCH_INVENTORY.md at line 26](../../../../docs/research/RESEARCH_INVENTORY.md) declares AMC1 UAS.SPEC.050 Section 3.3.
- [docs/research/RESEARCH_INVENTORY.md at line 28](../../../../docs/research/RESEARCH_INVENTORY.md) declares RTCA DO-362A Section 2.2, Section 2.2.1, Section 2.2.4, and Section 3.4.
- [docs/research/RESEARCH_INVENTORY.md at line 30](../../../../docs/research/RESEARCH_INVENTORY.md) declares JARUS SORA v2.5 Annex E Section E.6.
- [docs/research/RESEARCH_INVENTORY.md at line 36](../../../../docs/research/RESEARCH_INVENTORY.md) declares MIL-STD-882E Task 208 Section 4.2.
