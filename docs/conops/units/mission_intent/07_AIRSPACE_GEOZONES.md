| Attribute | Specification Detail |
| :--- | :--- |
| **Title** | Tactical Mission Intent: Airspace Deconfliction and Geo-Zones |
| **Issue ID** | MI-07 |
| **Type** | Mission Intent Unit |
| **Generation Mode** | Native Rust Compiler Assembly |
| **Specification Source** | .pipeline/schema.sysml |
| **Version** | 1.0.0 |
| **Date** | 2026-10-31 |

## 7. Airspace Deconfliction & U-space Dynamic Geo-Zones

Airspace deconfliction is bounded by the OEM-derived radio line-of-sight envelope, the OEM-derived minimum mission altitude, and externally sourced dynamic geo-zone volumes. Strategic air risk mitigation follows JARUS SORA v2.5 Annex C Section C.3 and containment follows JARUS SORA v2.5 Annex E Section E.14. Detect and Avoid (DAA) separation is governed by RTCA DO-365B Section 2.2.4. No numeric geo-zone value is asserted where the OEM sources are silent; such fields are marked "Not stated in OEM sources".

The airborne system under design is the Avenger 5 air vehicle, whose boundary encloses all onboard subsystems (oem_bom.md:9). Deconfliction maneuvers are executed through the canonical Ruddervator assembly, quantity 4, driven by Servos #1 to #4 on the CAN 1 bus (oem_bom.md:23 through oem_bom.md:27; interface_table.md:12 through interface_table.md:15). The Ruddervator term is the canonical OEM designation for the tail control surface assembly; the OEM drawing synonym and preparation synonym are not used in this unit (oem_bom.md:23).

### 7.1 Primary Boundary Perimeter

- **Horizontal Boundary Geometry:** The primary operational airspace is an authorized convex polygon defined by geodetic vertices supplied by the site survey required by AMC1 UAS.SPEC.050 Section 4.1. The polygon is contained inside the direct radio line-of-sight range limit of 60 km (PL-07; a5-user-manual-2.md:315). Extended-range operations are bounded by the extended RLOS range of 60 km to 180 km (PL-08; a5-user-manual-2.md:315).
- **Vertical Boundary Geometry:** The altitude floor is the minimum mission waypoint altitude of 50 m (PL-36; a5-user-manual-2.md:1195). The operating ceiling is "Not stated in OEM sources"; no ceiling is asserted in this unit. The assembled air vehicle height is 1.1 m (PL-11; a5-user-manual-2.md:289) and is the physical vertical extent carried inside the envelope.
- **Containment Buffers:** The lateral containment buffer and the vertical containment buffer are both "Not stated in OEM sources". No inward margin is fabricated. Buffer geometry is defined at mission planning inside the authorized polygon and is monitored by the run-time geofence monitor required by ASTM F3269-17 Section 5.2.
- **Perimeter Action:** Crossing the configured containment buffer commands a closed-loop turnaround executed through the four Ruddervator servos (oem_bom.md:23 through oem_bom.md:27; interface_table.md:12 through interface_table.md:15). The available turnaround rate is "Not stated in OEM sources"; maneuver authority is bounded by the maximum horizontal speed of 38 m/s (PL-02; a5-user-manual-2.md:308), the minimum flight speed of 26 m/s (PL-05; a5-user-manual-2.md:311), and the maximum dive angle of 22 deg (PL-04; a5-user-manual-2.md:310).
- **No Parachute Credit:** The parachute deployment module is a non-mission configuration and is excluded from the mission baseline (oem_bom.md:47); it provides no containment credit for perimeter excursion recovery.

### 7.2 Dynamic Exclusion and Keep-Out Zones

- **Dynamic Geo-Zone Ingestion:** Dynamic exclusion volumes are received as external tactical geofence updates over the command and control link operating in the 4.4 GHz to 5.0 GHz band (interface_table.md:63; a5-user-manual-2.md:1273). Ingested volumes are treated as keep-out constraints by the flight guidance function before any trajectory update is accepted.
- **Critical Infrastructure Standoff:** The minimum standoff radius around critical infrastructure and populated assemblies is "Not stated in OEM sources". No exclusion radius is fabricated. The keep-out volume vertical span starts at the 50 m minimum mission waypoint altitude (PL-36; a5-user-manual-2.md:1195) and extends upward to the operating ceiling, which is "Not stated in OEM sources".
- **Temporary Restrictions:** Temporary airspace restrictions are handled as externally sourced keep-out polygons on the same ingestion path as dynamic geo-zones. Strategic deconfliction credit is taken only under JARUS SORA v2.5 Annex C Section C.3, and the re-plan is bounded by the run-time geofence monitor and deterministic state switching of ASTM F3269-17 Section 5.2 and Section 5.3.
- **Payload Isolation:** Dynamic exclusion zone avoidance does not arm or safe the ESAD. The ESAD is a Critical / DAL-A assembly (oem_bom.md:52) and remains governed by its discrete safe/arm interlock (interface_table.md:56); geo-zone re-planning has no authority over that interlock.

### 7.3 Inclusion Zones and Authorized Operating Volume

- **Authorized Operating Volume:** The inclusion zone is the volume inside the primary polygon of Section 7.1, above the 50 m minimum mission waypoint altitude (PL-36; a5-user-manual-2.md:1195), inside the 60 km direct RLOS range (PL-07; a5-user-manual-2.md:315), and outside every current dynamic keep-out volume of Section 7.2.
- **Loiter Inclusion:** The on-station loiter geometry uses the OEM loiter radius of 300 m (PL-37; a5-user-manual-2.md:1497). The loiter center is an inclusion-zone waypoint and not a keep-out center.
- **Extended-Range Inclusion:** Operations beyond the 60 km direct RLOS range and up to the 180 km extended RLOS range (PL-08; a5-user-manual-2.md:315) remain inside the same horizontal polygon only when the extended-range link condition is satisfied. The enabling extended-range configuration is "Not stated in OEM sources".
- **Engagement Sub-Envelope:** The engagement inclusion sub-envelope is bounded by the maximum engagement elevation of 15 deg (PL-44; a5-user-manual-2.md:2056), the maximum engagement airspeed of 55 m/s (PL-45; a5-user-manual-2.md:2061), and the maximum dive angle of 22 deg (PL-04; a5-user-manual-2.md:310). Engagement geometry does not expand the authorized perimeter.
- **Inclusion Enforcement:** Inclusion-zone conformance is continuously monitored under ASTM F3269-17 Section 5.2, and the safety net takes deterministic authority under ASTM F3269-17 Section 5.3. Operational containment objectives follow JARUS SORA v2.5 Annex E Section E.14.

### 7.4 Horizontal and Vertical Separation Minima

| Separation Parameter | Applicable Boundary | Minimum Value | Units | Grounding and Operational Definition |
| :--- | :--- | :--- | :--- | :--- |
| Horizontal separation minimum | DAA well-clear horizontal boundary | Not stated in OEM sources | m | No OEM numeric separation is stated. Boundary definition follows RTCA DO-365B Section 2.2.4.1. |
| Vertical separation minimum | DAA well-clear vertical boundary | Not stated in OEM sources | m | No OEM numeric separation is stated. Boundary definition follows RTCA DO-365B Section 2.2.4.2. |
| Modified tau warning threshold | Time to closest point of approach | Not stated in OEM sources | s | No OEM numeric threshold is stated. Threshold definition follows RTCA DO-365B Section 2.2.4.3. |
| Corrective alert horizon | Advisory to maneuver transition | Not stated in OEM sources | s | No OEM numeric horizon is stated. Horizon definition follows RTCA DO-365B Section 2.2.5. |
| Preventative alert horizon | Traffic proximity advisory | Not stated in OEM sources | s | No OEM numeric horizon is stated. Horizon definition follows RTCA DO-365B Section 2.2.5.1. |
| Multi-asset separation minimum | Inter-vehicle horizontal and vertical spacing | Not stated in OEM sources | m | No OEM numeric swarm spacing is stated. Coordination follows JARUS SORA v2.5 Annex E Section E.16. |

- **Well-Clear Definition:** The DAA well-clear volume is the RTCA DO-365B Section 2.2.4 volume defined by its horizontal distance, horizontal miss distance, modified tau, and vertical threshold terms. The numeric terms are not restated in this unit because no OEM numeric value is stated; they are instantiated from the controlling DAA standard at mission planning.
- **Maneuver Rule:** When the well-clear boundary is predicted to be breached, the guidance function commands a horizontal or vertical avoidance maneuver through the four Ruddervator servos (oem_bom.md:23 through oem_bom.md:27). The commanded turn rate is "Not stated in OEM sources"; the maneuver remains inside the speed and dive limits of Section 7.1.
- **Recovery Hysteresis:** Well-clear re-establishment uses the recovery hysteresis defined by RTCA DO-365B Section 2.2.5.2. The numerical hysteresis value is "Not stated in OEM sources".
- **Sensor Basis:** Cooperative and non-cooperative traffic tracks are fused per RTCA DO-365B Section 2.2.5.3. No datalink protocol beyond the OEM command and control link of interface_table.md:63 is asserted.

### 7.5 Boundary Containment Mathematics

The containment condition is evaluated by the run-time safety net on every navigation update. The horizontal containment radius is measured from the mission polygon center, and the vertical condition is bounded below by the OEM minimum mission waypoint altitude. The operating ceiling term remains unbounded in this unit because the OEM sources are silent.

$$
\begin{aligned}
R_{\mathrm{containment}}(t) &= \left\| \mathbf{p}_{\mathrm{xy}}(t) - \mathbf{p}_{\mathrm{center}} \right\| \\
R_{\mathrm{containment}}(t) &\le R_{\mathrm{boundary}} - d_{\mathrm{lateral}} \\
h_{\mathrm{floor}} + d_{\mathrm{vertical}} &\le h(t) \le h_{\mathrm{ceiling}}
\end{aligned}
$$

Parameter Definitions and Engineering Units:

| Parameter | Symbol | Value | Units | Grounding and Description |
| :--- | :--- | :--- | :--- | :--- |
| Containment radius | R_containment | Computed online | m | Horizontal distance from the polygon center to the vehicle position |
| Boundary radius | R_boundary | 60000 m | m | PL-07 maximum direct RLOS range of 60 km (a5-user-manual-2.md:315) |
| Minimum mission waypoint altitude | h_floor | 50 m | m | PL-36 (a5-user-manual-2.md:1195) |
| Vehicle altitude | h | Computed online | m | Barometric and satellite-referenced altitude estimate |
| Lateral containment buffer | d_lateral | Not stated in OEM sources | m | No OEM numeric buffer is stated; site survey defines it under AMC1 UAS.SPEC.050 Section 4.1 |
| Vertical containment buffer | d_vertical | Not stated in OEM sources | m | No OEM numeric buffer is stated |
| Operating ceiling | h_ceiling | Not stated in OEM sources | m | No OEM ceiling is stated |
| On-station loiter radius | R_loiter | 300 m | m | PL-37 (a5-user-manual-2.md:1497) |
| Cruise speed | v_cruise | 30 m/s | m/s | PL-01 (a5-user-manual-2.md:307) |
| Maximum horizontal speed | v_max | 38 m/s | m/s | PL-02 (a5-user-manual-2.md:308) |
| Minimum flight speed | v_min | 26 m/s | m/s | PL-05 (a5-user-manual-2.md:311) |
| Flight endurance | t_endurance | 90 min | min | PL-06 (avenger-5-spec-sheet-rev3.md:53) |

- **Deterministic Switch:** When the containment predicate is false, the safety net switches to the bounded recovery state under ASTM F3269-17 Section 5.3, and the recovery is recorded for post-flight review under AMC1 UAS.SPEC.050 Section 4.4.

### 7.6 Control Authority Handover and Multi-Asset Deconfliction

- **Control Authority Handover:** Handover of control authority between ground control stations follows the Level of Interoperability framework of NATO STANAG 4586 Section 4.2.2 and the control handover interface of NATO STANAG 4586 Section 5.1.4. The handover expiry interval is "Not stated in OEM sources"; no interval is fabricated. The ground control station radio interface is the 4.4 GHz to 5.0 GHz link of interface_table.md:63.
- **Multi-Asset Coordination:** Multi-air-vehicle coordination follows JARUS SORA v2.5 Annex E Section E.16. Inter-vehicle separation minima are "Not stated in OEM sources". No inter-vehicle mesh protocol, frequency plan, or asset identifier is asserted beyond the OEM command and control link.
- **Perimeter Consistency:** Every handover preserves the active primary polygon, the active dynamic keep-out set, and the 50 m altitude floor (PL-36; a5-user-manual-2.md:1195). A handover does not reset nor relax the containment buffers of Section 7.1.

### 7.7 Escalation, Safety Interlocks, and ESAD Boundary

- **Boundary Breach Escalation:** A confirmed containment breach escalates from the run-time safety net to the deterministic recovery state under ASTM F3269-17 Section 5.3. Additional escalation to lethal effect initiation is outside the geo-zone plan and is governed by the ESAD safety chain.
- **ESAD Criticality:** The ESAD is classified Critical / DAL-A (oem_bom.md:52). Any ESAD state transition remains subject to the discrete safe/arm interlock (interface_table.md:56), the arm-enable input (interface_table.md:50), and the human judgement and fail-safe interlock obligations of DoD Directive 3000.09 Section 3.1 and Section 3.1.b. Geo-zone logic has no authority to arm, safe, or initiate the ESAD.
- **Parachute Non-Mission:** The parachute deployment module is non-mission and carries no containment, recovery, or deconfliction function in the mission baseline (oem_bom.md:47).
- **Ruddervator Authority:** All geo-zone avoidance and recovery maneuvers remain within the authority of the four Ruddervator servos on the CAN 1 bus (oem_bom.md:23 through oem_bom.md:27; interface_table.md:12 through interface_table.md:15). The autonomous engagement bounding obligation of DoD Directive 3000.09 Section 3.1.a and the escalation-of-force interlock obligation of CJCSI 3121.01B Enclosure E Section 2.d remain in force inside the authorized volume.

## Source References

All numeric values in this unit are cited from the OEM extraction set. The controlling references are [parametric_limits.md:7](schema/extracted/parametric_limits.md#L7), [oem_bom.md:9](schema/extracted/oem_bom.md#L9), [interface_table.md:9](schema/extracted/interface_table.md#L9), and [RESEARCH_INVENTORY.md:27](docs/research/RESEARCH_INVENTORY.md#L27).

- [S1] `schema/extracted/parametric_limits.md at line 7` - OEM numeric limits with source line citations.
- [S2] `schema/extracted/oem_bom.md at line 9` - OEM component identity, criticality, and mission baseline status.
- [S3] `schema/extracted/interface_table.md at line 9` - OEM interface, protocol, and link characteristics.
- [S4] `docs/research/RESEARCH_INVENTORY.md at line 27` - normative public clause baseline for SORA, DO-365B, STANAG 4586, ASTM F3269-17, and AMC1 UAS.SPEC.050.
- [S5] `.pipeline/schema.sysml:4` - AST parameter nodes PL-01 through PL-94 and ESAD/Ruddervator part definitions.
