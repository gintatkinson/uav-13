| Attribute | Specification Detail |
| :--- | :--- |
| **Title** | Operational Impacts, System Limitations & Documented Trade Studies |
| **Version** | 1.0.0 |
| **Date** | 2026-09-02 |
| **issue_id** | 118, 129, 132 |
| **type** | Concept of Operations |
| **generation_mode** | Specification Unit Synthesis |
| **specification_source** | docs/conops/units/conops/11_IMPACTS_AND_TRADE_STUDIES.md |

## 11. Operational Impacts, System Limitations & Documented Trade Studies

This unit records the operational impacts of the Avenger V2.5 air vehicle and PL-40 launcher concept, the system limitations that bound its employment, and the documented engineering trade studies that shaped the concept. Normative quantitative limits are grounded in `schema/extracted/parametric_limits.md` or in an OEM source line. Trade-study weights, scores, and alternative technology performance estimates are non-normative engineering assessments and are explicitly marked as such; OEM sources are silent on those values.

### 11.1 Operational Workflow & Deployment Impacts

1. **Reduced Crew Staging Footprint:** The concept of operations assumes a two-person supervisory crew comprising one System Operator and one Payload / Data Specialist. Crew composition and manning limits are Not stated in OEM sources; the two-person allocation is a non-normative operational assumption.
2. **Launcher Setup Time:** The PL-40 launcher setup time is bounded at 5 min maximum (PL-72, `schema/extracted/parametric_limits.md at line 78`). This replaces manual rail preparation with a documented pneumatic launcher setup sequence.
3. **Charging and Turnaround:** The DC18RC charger time is 0 to 55 min (PL-89, `schema/extracted/parametric_limits.md at line 95`) and the DC18SD charger time is 0 to 130 min (PL-90, `schema/extracted/parametric_limits.md at line 96`). Aircraft turnaround time beyond battery charging is Not stated in OEM sources.
4. **Consumable Replacement Planning:** The PL-40 pulling rope replacement interval is 100 launches maximum (PL-80, `schema/extracted/parametric_limits.md at line 86`), which establishes a recurring maintenance action in the deployment workflow.
5. **Automated External Coordination:** The concept assumes automated mission-plan registration, boundary deconfliction, and electronic conspicuity exchange with external service providers. The specific external protocols and service interfaces are Not stated in OEM sources; the operational assumption is non-normative.

### 11.2 Organizational Roles & Training Impacts

- **Operator Reskilling:** The primary operator role shifts from continuous manual control to supervisory systems management, state deconfliction, and payload data analysis. The required transition syllabus is Not stated in OEM sources.
- **Formal Training Syllabus:** Personnel complete a certified training syllabus covering supervisory software operation, human-in-the-loop emergency matrix execution, and safety-buffer monitoring. Syllabus content and duration are Not stated in OEM sources.
- **Maintenance Specialization:** Maintenance technicians shift from purely mechanical repair to digital bus diagnostics, sensor alignment, and cryptographic key loading. The required training standard is Not stated in OEM sources.
- **Weapon Safety Qualification:** Personnel handling the ESAD and warhead must complete weapon-safety qualification consistent with the Critical (DAL-A) classification of the ESAD (`schema/extracted/oem_bom.md at line 52`) and the human-judgement interlock obligations of DoD Directive 3000.09 Section 3.1.b. Qualification records are Not stated in OEM sources.

### 11.3 System Limitations & Operational Boundaries

- **Maximum Direct Radio Range:** The direct radio line-of-sight range is 60 km maximum (PL-07, `schema/extracted/parametric_limits.md at line 13`). Extended range is 60 to 180 km (PL-08, `schema/extracted/parametric_limits.md at line 14`). A 90 km operating claim is Not stated in OEM sources.
- **Flight Endurance:** Flight endurance is 90 min maximum (PL-06, `schema/extracted/parametric_limits.md at line 12`). Cold-soak endurance and any endurance derating at low temperature are Not stated in OEM sources.
- **Mass and Payload Ceiling:** Maximum take-off weight is 17 kg (PL-12, `schema/extracted/parametric_limits.md at line 18`) and warhead mass is 5 kg (PL-13, `schema/extracted/parametric_limits.md at line 19`). Payload capacity beyond the warhead is Not stated in OEM sources.
- **Speed Envelope:** Cruise speed is 30 m/s (PL-01, `schema/extracted/parametric_limits.md at line 7`), maximum horizontal speed is 38 m/s (PL-02, `schema/extracted/parametric_limits.md at line 8`), maximum dive speed is 55 m/s (PL-03, `schema/extracted/parametric_limits.md at line 9`), and minimum flight speed is 26 m/s (PL-05, `schema/extracted/parametric_limits.md at line 11`).
- **Altitude and Loiter Geometry:** Minimum mission waypoint altitude is 50 m (PL-36, `schema/extracted/parametric_limits.md at line 42`) and loiter radius is 300 m (PL-37, `schema/extracted/parametric_limits.md at line 43`).
- **Launcher Thermal Envelope:** PL-40 launcher working temperature is minus twenty degrees Celsius to plus fifty degrees Celsius (PL-73 and PL-74, `schema/extracted/parametric_limits.md at line 79` and `schema/extracted/parametric_limits.md at line 80`). Air vehicle operating temperature limits are Not stated in OEM sources.
- **Environmental Limits:** Precipitation, wind, gust, and icing limits for the air vehicle are Not stated in OEM sources. MIL-STD-810H Method 506.6 Section 4.2 and Method 521.4 Section 4.2 are recorded in `docs/research/RESEARCH_INVENTORY.md` as applicable verification baselines, but no numeric air vehicle limit is asserted here.
- **ESAD Electrical Boundary:** ESAD power input is 14 V to 32 V with 28 V nominal (PL-46, PL-47, and PL-48, `schema/extracted/parametric_limits.md at line 52` to `schema/extracted/parametric_limits.md at line 54`). The ESAD high-voltage measurement range is 0 V to 1800 V (PL-60, `schema/extracted/parametric_limits.md at line 66`). The ESAD arm-enable high level is 2.5 V to 3.3 V (PL-52 and PL-53, `schema/extracted/parametric_limits.md at line 58` and `schema/extracted/parametric_limits.md at line 59`).
- **Servo Power Boundary:** The servo power rail is 8 V (PL-22, `schema/extracted/parametric_limits.md at line 28`). Ruddervator quantity is four units (PL-14, `schema/extracted/parametric_limits.md at line 20`); the ruddervator is the canonical tail control surface assembly (`schema/extracted/oem_bom.md at line 23`).
- **Command Link Power:** Ground radio output power is 2 W (PL-39, `schema/extracted/parametric_limits.md at line 45`) in the 4.4 GHz to 5.0 GHz band recorded in `schema/extracted/interface_table.md at line 63`.
- **Recovery Limitation:** The parachute deployment module is a non-mission configuration with baseline false (`schema/extracted/oem_bom.md at line 47`). It is excluded from mission recovery credit and from mission baseline analysis.

### 11.4 Documented Engineering Trade Studies

The three trade studies below follow the decision-analysis process of INCOSE SEH v5.0 Section 4.3 and the ConOps content requirements of ISO/IEC/IEEE 29148:2018 Section 6.4.2. All weights, scores, and alternative performance estimates in this subsection are non-normative engineering assessments. They are Not stated in OEM sources. The OEM-grounded system limits used to bound the studies are those cited in Section 11.3.

#### 11.4.1 Trade Study 1: Electrical Storage Architecture (non-normative)

- **Objective:** Select an electrical storage architecture that preserves discharge capability at the cold-soak boundary, provides adequate cycle life, contains runaway hazards, and remains integrable within the air vehicle mass envelope.
- **Normative Baseline:** INCOSE SEH v5.0 Section 4.3; ISO/IEC/IEEE 29148:2018 Section 6.4.2; MIL-STD-810H Method 502.7 Section 4.2.
- **Alternatives:**
  - **Option A (Baseline):** High-discharge cells with high peak current capability, lower specific storage capacity, and degraded cold-soak capacity.
  - **Option B (Selected):** High-capacity cylindrical cells with internal heating, providing higher specific storage capacity and active cold-soak heating.
  - **Option C:** Solid-state cells with high theoretical specific storage capacity and a non-flammable core, but low cold-soak ionic conductivity, low maturity, and high unit cost.
- **Decision:** Option B was selected. Option A was rejected for cold-soak degradation. Option C was deferred for low maturity and cost.

The Pugh-style decision matrix uses criterion weights that sum to 100 percent. Each option score is a percentage of the maximum attainable score for that criterion. Each weighted contribution is expressed in percentage points. All numeric entries are non-normative engineering assessments and are Not stated in OEM sources.

| Evaluation Criterion | Criterion ID | Weight | Option A Score | Option A Weighted | Option B Score | Option B Weighted | Option C Score | Option C Weighted |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Specific storage capacity | C_1 | 25 % | 40 % | 10 percentage points | 80 % | 20 percentage points | 100 % | 25 percentage points |
| Cold-soak discharge capability | C_2 | 25 % | 20 % | 5 percentage points | 80 % | 20 percentage points | 40 % | 10 percentage points |
| Cycle life | C_3 | 15 % | 40 % | 6 percentage points | 100 % | 15 percentage points | 40 % | 6 percentage points |
| Runaway containment | C_4 | 15 % | 40 % | 6 percentage points | 80 % | 12 percentage points | 100 % | 15 percentage points |
| Technology maturity | C_5 | 10 % | 100 % | 10 percentage points | 100 % | 10 percentage points | 40 % | 4 percentage points |
| Acquisition and integration cost | C_6 | 10 % | 80 % | 8 percentage points | 60 % | 6 percentage points | 20 % | 2 percentage points |
| Composite score | Total | 100 % | 45 % | 45 percentage points | 83 % | 83 percentage points | 62 % | 62 percentage points |
| Ranking and decision | Rank | -- | Rank 3 | Rejected | Rank 1 | Selected | Rank 2 | Deferred |

##### Composite Score Formulation (Trade Study 1)

$$
\begin{aligned}
S_j &= \sum_{i=1}^{n} w_i s_{ij}
\end{aligned}
$$

- Parameter Definitions & Engineering Units:

| Parameter | Symbol | Value | Units | Description |
| :--- | :--- | :--- | :--- | :--- |
| Composite decision score | S_j | 0 to 100 | percent | Weighted score for candidate architecture j |
| Criterion weight | w_i | 25 | percent | Normalized importance of criterion i |
| Candidate criterion score | s_ij | 0 to 100 | percent | Score of option j on criterion i |
| Number of criteria | n | 6 | criteria | Count of evaluation criteria in the matrix |

#### 11.4.2 Trade Study 2: Edge Inference Versus Downlink Compression (non-normative)

- **Objective:** Determine the balance between onboard inference and downlink transmission under contested, degraded, or denied radio-frequency conditions.
- **Normative Baseline:** INCOSE SEH v5.0 Section 4.3; ISO/IEC/IEEE 29148:2018 Section 6.4.2; NIST SP 800-82r3 Section 6.2; RTCA DO-362A Section 3.4; NATO STANAG 4586 Section 5.1.
- **Alternatives:**
  - **Option A (Baseline):** Raw sensor streaming to the supervisory station with centralized processing. Onboard resource demand is low, but downlink load is high and mission execution fails during link denial.
  - **Option B (Selected):** Onboard edge inference with dynamic context compression. The air vehicle transmits compact semantic state vectors and retains autonomous execution authority during link loss.
  - **Option C:** Hybrid adaptive splitting that moves inference between the air vehicle and the supervisory station based on link margin. This adds synchronization complexity and variable response time.
- **Decision:** Option B was selected. Option A was rejected for link-denial failure. Option C was rejected for software complexity and non-deterministic response.

The matrix uses the same percentage scoring convention as Trade Study 1. All numeric entries are non-normative engineering assessments and are Not stated in OEM sources.

| Evaluation Criterion | Criterion ID | Weight | Option A Score | Option A Weighted | Option B Score | Option B Weighted | Option C Score | Option C Weighted |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Contested radio-frequency resilience | C_1 | 30 % | 20 % | 6 percentage points | 100 % | 30 percentage points | 60 % | 18 percentage points |
| Downlink load | C_2 | 20 % | 20 % | 4 percentage points | 100 % | 20 percentage points | 60 % | 12 percentage points |
| Inference response time | C_3 | 20 % | 40 % | 8 percentage points | 80 % | 16 percentage points | 60 % | 12 percentage points |
| Onboard resource impact | C_4 | 15 % | 100 % | 15 percentage points | 60 % | 9 percentage points | 60 % | 9 percentage points |
| Lost-link autonomy | C_5 | 10 % | 20 % | 2 percentage points | 100 % | 10 percentage points | 60 % | 6 percentage points |
| Software and verification complexity | C_6 | 5 % | 80 % | 4 percentage points | 60 % | 3 percentage points | 20 % | 1 percentage point |
| Composite score | Total | 100 % | 39 % | 39 percentage points | 88 % | 88 percentage points | 58 % | 58 percentage points |
| Ranking and decision | Rank | -- | Rank 3 | Rejected | Rank 1 | Selected | Rank 2 | Rejected |

#### 11.4.3 Trade Study 3: Failsafe Containment Versus Actuator Redundancy (non-normative)

- **Objective:** Select a safety-assurance architecture that bounds terminal impact severity under uncommanded actuation, bus collapse, or structural failure and that supports ground-risk mitigation credit.
- **Normative Baseline:** INCOSE SEH v5.0 Section 4.3; ISO/IEC/IEEE 29148:2018 Section 6.4.2; JARUS SORA v2.5 Annex B Section B.2; MIL-STD-882E Task 205 Section 4.2; SAE ARP4761 Section 4.3.1.
- **Alternatives:**
  - **Option A (Baseline):** Multi-channel actuator redundancy. It provides actuator fail-operational capability but does not arrest unpowered descent, does not protect against main bus collapse or structural failure, and adds parasitic integration weight.
  - **Option B (Selected):** Integrated failsafe containment with an independent safety watchdog, isolated power, actuator power cutoff, and a deployable deceleration mechanism. The watchdog deployment latency and the resulting terminal descent speed are Not stated in OEM sources; they are non-normative design targets.
  - **Option C:** Passive crushable structure. It adds no active deployment complexity but provides no terminal descent deceleration, adds structural deadweight, and does not prevent boundary containment excursions.
- **Decision:** Option B was selected. Option A was rejected as insufficient. Option C was rejected as insufficient for terminal impact bounding.

The matrix uses the same percentage scoring convention as Trade Study 1. All numeric entries are non-normative engineering assessments and are Not stated in OEM sources. The maximum system weight used to bound the study is 17 kg (PL-12, `schema/extracted/parametric_limits.md at line 18`).

| Evaluation Criterion | Criterion ID | Weight | Option A Score | Option A Weighted | Option B Score | Option B Weighted | Option C Score | Option C Weighted |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Terminal impact severity reduction | C_1 | 30 % | 20 % | 6 percentage points | 100 % | 30 percentage points | 40 % | 12 percentage points |
| Bus and structural failure mitigation | C_2 | 20 % | 20 % | 4 percentage points | 100 % | 20 percentage points | 40 % | 8 percentage points |
| Certification credit | C_3 | 20 % | 40 % | 8 percentage points | 100 % | 20 percentage points | 20 % | 4 percentage points |
| Integration weight penalty | C_4 | 15 % | 40 % | 6 percentage points | 80 % | 12 percentage points | 20 % | 3 percentage points |
| Common-cause failure immunity | C_5 | 10 % | 40 % | 4 percentage points | 100 % | 10 percentage points | 80 % | 8 percentage points |
| Pre-operation verification simplicity | C_6 | 5 % | 60 % | 3 percentage points | 80 % | 4 percentage points | 100 % | 5 percentage points |
| Composite score | Total | 100 % | 31 % | 31 percentage points | 96 % | 96 percentage points | 40 % | 40 percentage points |
| Ranking and decision | Rank | -- | Rank 3 | Rejected | Rank 1 | Selected | Rank 2 | Rejected |

### 11.5 OEM-Silent Fields & Non-Normative Content Register

The following fields are explicitly recorded as silent in the OEM source set. They are not to be inferred from the trade studies or from operational assumptions.

| Field | Grounding Status |
| :--- | :--- |
| Air vehicle operating temperature limits | Not stated in OEM sources |
| Cold-soak endurance and low-temperature endurance derating | Not stated in OEM sources |
| Precipitation, wind, gust, and icing limits for the air vehicle | Not stated in OEM sources |
| Payload capacity beyond the 5 kg warhead | Not stated in OEM sources |
| Aircraft turnaround time beyond battery charging | Not stated in OEM sources |
| Crew composition and manning limits | Not stated in OEM sources |
| Training syllabus content and duration | Not stated in OEM sources |
| Trade-study weights, scores, and composite rankings | Not stated in OEM sources (non-normative) |
| Alternative technology performance estimates | Not stated in OEM sources (non-normative) |
| Failsafe watchdog deployment latency and safe descent speed | Not stated in OEM sources (non-normative design targets) |
| Parachute recovery credit | Non-mission configuration per `schema/extracted/oem_bom.md at line 47` |

### Source References

- Parametric limits: [schema/extracted/parametric_limits.md](schema/extracted/parametric_limits.md#L7-L96)[^1]
- OEM bill of materials: [schema/extracted/oem_bom.md](schema/extracted/oem_bom.md#L47-L52)[^2]
- System interface table: [schema/extracted/interface_table.md](schema/extracted/interface_table.md#L63-L64)[^3]
- SysML v2 SSOT: [.pipeline/schema.sysml](.pipeline/schema.sysml)[^4]
- Cited research inventory: [docs/research/RESEARCH_INVENTORY.md](docs/research/RESEARCH_INVENTORY.md)[^5]

[^1]: schema/extracted/parametric_limits.md, lines 7 through 96, PL-01 through PL-94 parametric limits.
[^2]: schema/extracted/oem_bom.md, lines 47 through 52, ESAD Critical (DAL-A) classification and parachute non-mission configuration.
[^3]: schema/extracted/interface_table.md, lines 63 through 64, radio band and ESAD interface rows.
[^4]: .pipeline/schema.sysml, SysML v2 SSOT part definitions and PL-range constraints.
[^5]: docs/research/RESEARCH_INVENTORY.md, normative baseline and public clause citations.
