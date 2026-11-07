| Attribute | Specification Detail |
| :--- | :--- |
| **Title** | Tactical Mission Intent: Critical Energy Threshold Mathematics and Secondary Divert Protocols |
| **Document ID** | MI-09 |
| **Version** | 1.0.0 |
| **Date** | 2026-10-31 |
| **Issue ID** | MI-09 |
| **Type** | Tactical Mission Intent Unit |
| **Generation Mode** | Schema-grounded single-unit elaboration |
| **Specification Source** | skills/spec-conops-engineering/SKILL.md |

## 9. Critical Energy Threshold Mathematics & Secondary Divert Protocols

In accordance with the spec-conops-engineering skill Section 2.2 and INCOSE SEH v5.0 Section 4.6, mission endurance is bounded by a continuously evaluated critical energy threshold. The statutory reserve ratio of at least 20 percent is a declared mission constraint, not an OEM-measured value. The OEM sources do not publish a usable battery energy capacity, so the threshold is defined symbolically and evaluated from measured battery voltage and current telemetry.

### 9.1 Critical Energy Dynamics Formulation

The critical energy state is the sum of the return transit energy, the secondary divert energy, and the mandatory reserve. The reserve ratio is bounded below by the declared mission constraint.

$$
\begin{aligned}
E_{\mathrm{critical}}(t) &= E_{\mathrm{bingo}}(t) \\
E_{\mathrm{bingo}}(t) &= E_{\mathrm{return}}(t) + E_{\mathrm{divert}} + E_{\mathrm{reserve}} \\
E_{\mathrm{return}}(t) &= \int_{t}^{t_{\mathrm{recovery}}} P_{\mathrm{total}}(\tau) \, d\tau \\
E_{\mathrm{divert}} &= \frac{d_{\mathrm{alt}}}{v_{\mathrm{nominal}}} \cdot P_{\mathrm{cruise}} \\
E_{\mathrm{reserve}} &\ge \mathrm{Ratio}_{\mathrm{reserve\_min}} \cdot E_{\mathrm{capacity}} \\
\frac{E_{\mathrm{reserve}}}{E_{\mathrm{capacity}}} &\ge 0.20
\end{aligned}
$$

The divert predicate and the maximum feasible divert distance are evaluated at each control cycle:

$$
\begin{aligned}
D_{\mathrm{divert}}(t) &= \begin{cases} \text{true} & \text{if } E_{\mathrm{current}}(t) \le E_{\mathrm{bingo}}(t) \\ \text{false} & \text{otherwise} \end{cases} \\
d_{\mathrm{divert,max}}(t) &= \frac{\left( E_{\mathrm{current}}(t) - E_{\mathrm{return}}(t) - E_{\mathrm{reserve}} \right) v_{\mathrm{nominal}}}{P_{\mathrm{cruise}}}
\end{aligned}
$$

- Parameter Definitions & Engineering Units:

| Parameter | Symbol | Value | Units | Constraint Rule | Grounding Citation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Total storage capacity | E_capacity | Not stated in OEM sources | J | Positive capacity required; battery terminal envelope is 36 V to 50.4 V | oem_bom.md:18; parametric_limits.md:29; parametric_limits.md:30 |
| Battery minimum voltage | V_batt_min | 36 V | V | Equal to PL-23 | parametric_limits.md:29 |
| Battery maximum voltage | V_batt_max | 50.4 V | V | Equal to PL-24 | parametric_limits.md:30 |
| Pre-flight battery voltage minimum | V_preflight_min | 49 V | V | Equal to PL-32 | parametric_limits.md:38 |
| Pre-flight battery voltage maximum | V_preflight_max | 50 V | V | Equal to PL-33 | parametric_limits.md:39 |
| Nominal cruise speed | v_nominal | 30 m/s | m/s | Equal to PL-01 | parametric_limits.md:7 |
| Maximum horizontal speed | v_horizontal_max | 38 m/s | m/s | Equal to PL-02 | parametric_limits.md:8 |
| Maximum dive speed | v_dive_max | 55 m/s | m/s | Equal to PL-03 | parametric_limits.md:9 |
| Maximum flight endurance | t_endurance_max | 90 min | min | Equal to PL-06 | parametric_limits.md:12 |
| Direct RLOS range | d_rlos_direct | 60 km | km | Equal to PL-07 | parametric_limits.md:13 |
| Extended RLOS range | d_rlos_extended | 180 km | km | Equal to PL-08 | parametric_limits.md:14 |
| Minimum mission waypoint altitude | h_waypoint_min | 50 m | m | Equal to PL-36 | parametric_limits.md:42 |
| Loiter radius | r_loiter | 300 m | m | Equal to PL-37 | parametric_limits.md:43 |
| Mandatory reserve ratio | Ratio_reserve_min | 0.20 | dimensionless | Declared mission constraint; E_reserve at least 0.20 times E_capacity; not OEM-measured | skills/spec-conops-engineering/SKILL.md:115 |
| Mandatory reserve energy | E_reserve | Not stated in OEM sources | J | At least Ratio_reserve_min times E_capacity | skills/spec-conops-engineering/SKILL.md:115 |
| Current energy state | E_current | Measured online | J | Computed from Power Meter voltage and current telemetry | oem_bom.md:20 |
| Return transit energy | E_return | Computed online | J | Integral of P_total over the return transit | Critical energy dynamics equation |
| Secondary divert energy | E_divert | Computed online | J | d_alt divided by v_nominal times P_cruise | Critical energy dynamics equation |
| Total cruise power | P_total | Not stated in OEM sources | W | Sum of propulsion, control, and avionics loads | oem_bom.md:18; oem_bom.md:19; oem_bom.md:20; oem_bom.md:21; oem_bom.md:22 |
| Cruise power | P_cruise | Not stated in OEM sources | W | Propulsion power at v_nominal | oem_bom.md:21; oem_bom.md:22 |
| Alternate site distance | d_alt | Not stated in OEM sources | m | Distance from primary to alternate recovery location; OEM sources contain no site coordinates | OEM sources silent |
| Bingo threshold | E_bingo | Computed online | J | Sum of E_return, E_divert, and E_reserve | Critical energy dynamics equation |
| Critical energy threshold | E_critical | Computed online | J | Equal to E_bingo | Critical energy dynamics equation |
| Divert predicate | D_divert | Computed online | boolean | Asserted when E_current is at or below E_bingo | Critical energy dynamics equation |
| Maximum divert distance | d_divert_max | Computed online | m | Feasibility limit for secondary divert | Critical energy dynamics equation |

### 9.2 Secondary and Tertiary Divert Recovery Protocol

The secondary divert protocol is a deterministic contingency sequence, not an autonomous engagement. It is grounded in AMC1 UAS.SPEC.050 Section 3.3 (in-flight contingency management) and JARUS SORA v2.5 Annex E Section E.14 (operational containment).

1. **State estimation.** The current energy state E_current(t) is computed from Battery 12S2P Li Metal BEI terminal voltage and Power Meter current telemetry (oem_bom.md:18, oem_bom.md:20). The OEM sources do not publish a state-of-charge curve, so the voltage-to-energy mapping is computed online and is not stated in OEM sources.
2. **Threshold assertion.** The divert predicate D_divert(t) is asserted when E_current(t) is at or below the bingo threshold E_bingo(t).
3. **Recovery site priority.** The executive controller evaluates the primary recovery location first, the secondary recovery location second, and the tertiary recovery location third. Site coordinates, elevations, and dimensions are not stated in OEM sources.
4. **Feasibility gate.** Divert to the secondary location is commanded only when the alternate site distance d_alt is at or below the maximum divert distance d_divert_max(t). If the secondary location is not feasible, the controller retains the reserve and executes the containment action defined by JARUS SORA v2.5 Annex E Section E.14.
5. **Reserve preservation.** The mandatory reserve E_reserve is never allocated to transit or divert. The reserve ratio remains at or above 0.20 of E_capacity as a declared mission constraint (skills/spec-conops-engineering/SKILL.md Section 2.2).
6. **Deterministic switching.** The transition from mission transit to divert follows the deterministic state-switching discipline of ASTM F3269-17 Section 5.3, as listed in docs/research/RESEARCH_INVENTORY.md.

### 9.3 Resource Boundary Conditions

- The energy budget covers the mission-baseline propulsion and avionics loads supplied by the Battery 12S2P Li Metal BEI (oem_bom.md:18) through the 200 A automotive fuse (oem_bom.md:19), Power Meter (oem_bom.md:20), ESC IBEX160 (oem_bom.md:21), and Motor AXI HD GOLD LINE V3 (oem_bom.md:22).
- Control loads include four Ruddervator servos (parametric_limits.md:22) and four wing servos (parametric_limits.md:23). Ruddervator is the canonical tail control surface assembly, quantity 4 (oem_bom.md:23; parametric_limits.md:20).
- ESAD is Critical / DAL-A (oem_bom.md:52). The bingo computation does not command, inhibit, or reallocate ESAD energy. ESAD power input is 14 V to 32 V DC, nominal 28 V (parametric_limits.md:52; parametric_limits.md:53; parametric_limits.md:54).
- Parachute Deployment Non-Mission is excluded from the mission energy baseline because its configuration is non-mission and its baseline flag is false (oem_bom.md:47).
- OEM sources are silent on battery energy capacity, state-of-charge curve, propulsion power, control power, avionics power, recovery site coordinates, and divert response time. These fields are marked Not stated in OEM sources.

## Source References

The formulation is grounded in [parametric_limits.md](schema/extracted/parametric_limits.md) at PL-01 (parametric_limits.md:7), PL-02 (parametric_limits.md:8), PL-03 (parametric_limits.md:9), PL-06 (parametric_limits.md:12), PL-07 (parametric_limits.md:13), PL-08 (parametric_limits.md:14), PL-14 (parametric_limits.md:20), PL-16 (parametric_limits.md:22), PL-17 (parametric_limits.md:23), PL-23 (parametric_limits.md:29), PL-24 (parametric_limits.md:30), PL-32 (parametric_limits.md:38), PL-33 (parametric_limits.md:39), PL-36 (parametric_limits.md:42), PL-37 (parametric_limits.md:43), PL-46 (parametric_limits.md:52), PL-47 (parametric_limits.md:53), and PL-48 (parametric_limits.md:54); in [oem_bom.md](schema/extracted/oem_bom.md) at oem_bom.md:18, oem_bom.md:19, oem_bom.md:20, oem_bom.md:21, oem_bom.md:22, oem_bom.md:23, oem_bom.md:47, and oem_bom.md:52; and in [interface_table.md](schema/extracted/interface_table.md) at interface_table.md:45 and interface_table.md:49.

Normative clauses are ISO/IEC/IEEE 29148:2018 clause 6.4.2, INCOSE SEH v5.0 clause 4.6, AMC1 UAS.SPEC.050 clause 3.3, JARUS SORA v2.5 Annex E clause E.14, and ASTM F3269-17 clause 5.3, as listed in [RESEARCH_INVENTORY.md](docs/research/RESEARCH_INVENTORY.md) at RESEARCH_INVENTORY.md:26, RESEARCH_INVENTORY.md:27, RESEARCH_INVENTORY.md:31, and RESEARCH_INVENTORY.md:38.

The declared 20 percent reserve constraint is grounded in [SKILL.md](skills/spec-conops-engineering/SKILL.md) at SKILL.md:115 (clause 2.2).