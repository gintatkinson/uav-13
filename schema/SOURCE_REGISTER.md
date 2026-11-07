# Source Register

PDF-grounded source register for the Avenger 5 system rebuild. This register governs the three extraction tables in `schema/extracted/` and records how PDF evidence was validated into Markdown.

## 1. Purpose and Scope

- Establish deterministic provenance for every row in `schema/extracted/oem_bom.md`, `schema/extracted/interface_table.md`, and `schema/extracted/parametric_limits.md`.
- Restrict all extraction evidence to the six validated PDF-to-Markdown transcriptions listed in Section 2.
- Record the source hierarchy and the authoritative role of the engineering block diagram for topology.
- Record the canonical term map, conflict resolutions, variant rule, duplicate handling, and quarantine state.
- Keep PDF-versus-Markdown validation status in `schema/PDF_VS_MD_VALIDATION.md`.

## 2. PDF Source Hierarchy

| Rank | PDF Source | Markdown Transcription | Revision or Identity | Authority Scope |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `schema/Avenger5_V2.5_block_diagram_rev5.pdf` | `schema/avenger_v2_5_sysml_v2_ingestion.md` | Avenger V2.5 block diagram, revision 5 | Authoritative engineering system diagram for component topology, Servo #1 to #8 assignment, CAN 1 and CAN 2 routing, 8 V servo rails, and harness lengths |
| 2 | `schema/A5-user-manual 2.pdf` | `schema/a5-user-manual-2.md` | UDS-A5UM-001, release 2026-08-07, model AVENGER5V1 | Primary authority for flight limits, dimensions, product contents, component names, operating modes, and ESAD states |
| 3 | `schema/A5_prep and safety_rev7.pdf` | `schema/a5-prep-and-safety-rev7.md` | Preparation and Safety Instructions, revision 7 | Primary authority for assembly, wing panel installation, tail stabiliser installation, RBF safety gates, and warhead and ESAD integration |
| 4 | `schema/AVENGER 5 Spec sheet_rev3.pdf` | `schema/avenger-5-spec-sheet-rev3.md` | Product spec sheet, revision 3 | Limited authority: warhead mass 5 kg and endurance 90 min only |
| 5 | `schema/UAV_launcher_PL-40_user_manual_rev_2.6.pdf` | `schema/uav_launcher_pl_40_sysml_v2_ingestion_manual.md` | PL-40 launcher manual, REV 2.6 | Primary authority for the PL-40 launcher subsystem, launcher limits, and pneumatic and electrical launcher interfaces |
| 6 | `schema/ESAD ICD_for Excalibur_AB00-0054-01AA-0005 2 1.pdf` | `schema/esad-icd-excalibur-ab00-0054.md` | ICD AB00-0054, board-level prototype for Avenger 3 | Reference only: `prototype-reference` and `Derived` tags required on every ICD-derived row |

## 3. Term Map

| Canonical Term | Declared Synonyms | Identity and Boundary | Source |
| :--- | :--- | :--- | :--- |
| `Ruddervator` | `Fins` (drawing); `tail stabiliser` (preparation manual) | Four tail control surfaces, pitch and yaw mixing, driven by Ruddervator Servos #1 to #4 on CAN 1 | avenger_v2_5_sysml_v2_ingestion.md:21, a5-user-manual-2.md:273, a5-prep-and-safety-rev7.md:242 |
| `Ruddervator Servo #1` to `Ruddervator Servo #4` | Fins servos | Left-up, Right-up, Right-down, Left-down HV6160-DroneCAN servos on four CAN 1 120 cm branches from the CAN 1 150 cm branch | avenger_v2_5_sysml_v2_ingestion.md:22, avenger_v2_5_sysml_v2_ingestion.md:25 |
| `Wings` | Wing assembly | Four wing panels plus Wing Servos #5 to #8 for roll stabilization | avenger_v2_5_sysml_v2_ingestion.md:27, avenger_v2_5_sysml_v2_ingestion.md:156 |
| `Wing Panel Left-Upper` / `Left-Lower` / `Right-Upper` / `Right-Lower` | Wing sections left and right, quantity 2 each | Four structural wing panels secured by eight M6 x 30 mm wing bolts | a5-user-manual-2.md:272, a5-user-manual-2.md:337, a5-user-manual-2.md:338, a5-prep-and-safety-rev7.md:225 |
| `Wing Servo #5` to `Wing Servo #8` | Wing servos | Left-up, Right-up, Right-down, Left-down HV6160-DroneCAN servos on CAN 2 | avenger_v2_5_sysml_v2_ingestion.md:28, avenger_v2_5_sysml_v2_ingestion.md:31 |
| `CAN/power splitter PCB` | Servo CAN and power splitter board | Distributes four 8 V servo power inputs and passes CAN 2 in series to the wing servos | avenger_v2_5_sysml_v2_ingestion.md:26, avenger_v2_5_sysml_v2_ingestion.md:157 |
| `ESAD` | Electronic Safe and Arm Device | Critical / DAL-A warhead safety and arming device; ICD values are Avenger 3 prototype reference data | avenger_v2_5_sysml_v2_ingestion.md:45, a5-user-manual-2.md:1984, esad-icd-excalibur-ab00-0054.md:105 |
| `Parachute Deployment Non-Mission` | Parachute deployment module | Non-mission R&D variant with `configuration: non-mission` and `baseline: false` | avenger_v2_5_sysml_v2_ingestion.md:40, a5-user-manual-2.md:262, a5-user-manual-2.md:314 |

## 4. Conflict Resolutions

| ID | Topic | Conflicting Evidence | Resolution | Authority and Rationale |
| :--- | :--- | :--- | :--- | :--- |
| CR-01 | Tail surface naming | Drawing uses `Fins`; preparation manual uses `tail stabiliser`; user manual uses `Ruddervator` | Canonical term `Ruddervator`; other terms retained only as declared synonyms | a5-user-manual-2.md:273, a5-user-manual-2.md:339 |
| CR-02 | Cruise speed | User manual 30 m/s; spec sheet 31 m/s | 30 m/s | a5-user-manual-2.md:307; user manual governs flight limits |
| CR-03 | Maximum horizontal speed | User manual 38 m/s; spec sheet 42 m/s | 38 m/s | a5-user-manual-2.md:308; user manual governs flight limits |
| CR-04 | Maximum dive speed | User manual 55 m/s; spec sheet 80 m/s | 55 m/s | a5-user-manual-2.md:309; user manual governs flight limits |
| CR-05 | Minimum speed | User manual 26 m/s; spec sheet stall speed 24 m/s | 26 m/s | a5-user-manual-2.md:311; user manual governs flight limits |
| CR-06 | RLOS range | User manual 60 km and 180 km; spec sheet 60 km and 90 km with relay | 60 km direct and 180 km extended | a5-user-manual-2.md:315; user manual governs flight limits |
| CR-07 | Flight endurance | User manual 90 min; spec sheet 90 min | 90 min, cited to the spec sheet as designated supplier | avenger-5-spec-sheet-rev3.md:53 |
| CR-08 | Warhead mass | Spec sheet 5 kg; user manual states no mass | 5 kg, cited to the spec sheet as designated supplier | avenger-5-spec-sheet-rev3.md:133 |
| CR-09 | Spec sheet restricted values | Spec sheet cruise, horizontal, stall, dive, wind, ceiling, temperature, and relay range differ from the user manual | Not used; spec sheet limited to warhead mass and endurance | a5-user-manual-2.md:305 through a5-user-manual-2.md:315 |
| CR-10 | Servo boundary | Older extraction treated servos as generic autopilot commands | Servos #1 to #4 belong to Fins, now Ruddervator, on CAN 1; Servos #5 to #8 belong to Wings on CAN 2 through the splitter PCB | avenger_v2_5_sysml_v2_ingestion.md:21 through avenger_v2_5_sysml_v2_ingestion.md:31 |
| CR-11 | CAN topology | Older extraction had no CAN branch topology | CAN 1 uses a 970 cm trunk, a 150 cm branch, and four 120 cm stubs; CAN 2 uses a splitter PCB series daisy chain | avenger_v2_5_sysml_v2_ingestion.md:50 through avenger_v2_5_sysml_v2_ingestion.md:55, avenger_v2_5_sysml_v2_ingestion.md:171 through avenger_v2_5_sysml_v2_ingestion.md:173 |
| CR-12 | Wing quantity and structure | Product contents lists two left and two right wing sections | Four wing panels: left-upper, left-lower, right-upper, right-lower | a5-user-manual-2.md:337, a5-user-manual-2.md:338, a5-prep-and-safety-rev7.md:225 |
| CR-13 | ESAD applicability | Avenger 5 manuals require an ESAD; the ICD is an Avenger 3 board-level prototype | Include ESAD as Critical / DAL-A; tag all ICD rows `prototype-reference` and `Derived` | a5-user-manual-2.md:1984, esad-icd-excalibur-ab00-0054.md:105 |
| CR-14 | Recovery and parachute | User manual offers recoverability but states recovery system No | Baseline has no recovery system; parachute is `configuration: non-mission` and `baseline: false` | a5-user-manual-2.md:262, a5-user-manual-2.md:314 |
| CR-15 | Launcher mass limit | PL-40 maximum plane mass 30 kg; Avenger 5 MTOW 17 kg | No conflict; record both limits separately | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:718, a5-user-manual-2.md:299 |
| CR-16 | Launcher mass consistency | Catapult set 68 kg; launcher case 43 kg plus compressor case 25 kg | Consistent; 43 kg plus 25 kg equals 68 kg | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:715 through uav_launcher_pl_40_sysml_v2_ingestion_manual.md:717 |
| CR-17 | Catapult pressure | User manual pre-flight check says 13 to 14 bar; launcher manual maximum is 14 bar | Launch pressure range 13 to 14 bar; compressor maximum 14 bar | a5-user-manual-2.md:1329, uav_launcher_pl_40_sysml_v2_ingestion_manual.md:132 |

## 5. Variant Rule

- The mission baseline contains only components with `configuration: mission` and `baseline: true`.
- The parachute deployment module is a non-mission R&D variant. It is tagged `configuration: non-mission` and `baseline: false` in `schema/extracted/oem_bom.md`.
- The parachute deployment module must not enter mission baseline analysis, mission mass or power budgets, mission interface allocations, or mission hazard analysis.
- The module remains in the BOM only for traceability of the recoverability option and for R&D configuration control.
- Promotion to the mission baseline requires a new source citation, a baseline change record, and explicit approval.

## 6. ESAD Prototype Reference Rule

- The ESAD ICD describes a board-level prototype for the Avenger 3 UAV, not a qualified Avenger 5 design.
- Every row derived from the ESAD ICD carries both `[prototype-reference]` and `[Derived]` tags in its Source or Verification Source cell.
- ESAD connector pinouts, power ranges, RS-485 timing, discrete levels, and high-voltage ranges are prototype reference data only.
- The ESAD is nevertheless included in the BOM as a Critical / DAL-A safety-critical arming device because the Avenger 5 user manual and preparation manual define it as the principal warhead safety device.
- No ESAD ICD value is treated as an Avenger 5 qualified requirement without separate qualification evidence.

## 7. Duplicate and Quarantine Note

| Artifact | Reason | Status |
| :--- | :--- | :--- |
| `schema/UAV_launcher_PL-40_user_manual_rev_2.6 (1).pdf` | Duplicate copy of the PL-40 launcher PDF | Ignored; not read, not cited, not used |
| `.pipeline/legacy/r2-pre-rebuild-failed/` | Failed R2 predecessor chain with missing servo and CAN topology | Quarantined with SHA-256 manifest; not cited by any extraction row |
| `.pipeline/legacy/pre-rebuild/` | Earlier R1 quarantine snapshot | Superseded; not cited by any extraction row |
| `schema/model.sysml` | Synthesized AST, not an OEM source | Regenerated by the sanctioned ingest command |
| `.pipeline/schema.sysml` and `.pipeline/schema-digest.json` | Synthesized compiled AST and digest, not OEM sources | Regenerated by the sanctioned compile command |

## 8. Table Row Counts

Row counts are maintained from the current table headers and data rows. Header and separator rows are excluded.

| Table | Data Rows |
| :--- | ---: |
| `schema/extracted/oem_bom.md` | 95 |
| `schema/extracted/interface_table.md` | 59 |
| `schema/extracted/parametric_limits.md` | 94 |

## 9. Verification Checklist

- Every data row in all three tables has a non-empty Source or Verification Source cell.
- The block diagram is cited for all Servo #1 to #8, wing panel, splitter PCB, CAN 1, CAN 2, 8 V rail, and harness topology rows.
- Ruddervator is the canonical tail-surface term; Fins and tail stabiliser appear only as declared synonyms.
- Ruddervator quantity is 4; wing panel quantity is 4; servo quantity is 8.
- ESAD is present and tagged Critical / DAL-A with `[prototype-reference] [Derived]` on ICD rows.
- The parachute deployment module is tagged `configuration: non-mission` and `baseline: false`.
- Flight limits are 30 m/s cruise, 38 m/s maximum horizontal, 55 m/s maximum dive, 22 deg maximum dive angle, and 26 m/s minimum speed from `a5-user-manual-2.md`.
- RLOS is 60 km and 180 km from `a5-user-manual-2.md`.
- The spec sheet supplies only warhead mass 5 kg and endurance 90 min.
- `schema/PDF_VS_MD_VALIDATION.md` records the validated PDF facts used by this register.

## 10. Source Line Index

| Topic | Source Lines |
| :--- | :--- |
| Block diagram component decomposition | avenger_v2_5_sysml_v2_ingestion.md:7 through avenger_v2_5_sysml_v2_ingestion.md:55 |
| Block diagram interface topology | avenger_v2_5_sysml_v2_ingestion.md:59 through avenger_v2_5_sysml_v2_ingestion.md:134 |
| Block diagram harness constraints | avenger_v2_5_sysml_v2_ingestion.md:170 through avenger_v2_5_sysml_v2_ingestion.md:173 |
| Avenger 5 physical components | a5-user-manual-2.md:268 through a5-user-manual-2.md:276 |
| Flight characteristics | a5-user-manual-2.md:305 through a5-user-manual-2.md:315 |
| Seeker characteristics | a5-user-manual-2.md:319 through a5-user-manual-2.md:328 |
| Product contents and quantities | a5-user-manual-2.md:334 through a5-user-manual-2.md:340 |
| GCS contents | a5-user-manual-2.md:342 through a5-user-manual-2.md:357 |
| ESAD states and arming conditions | a5-user-manual-2.md:1984 through a5-user-manual-2.md:2000 |
| Wing installation and eight bolts | a5-prep-and-safety-rev7.md:218 through a5-prep-and-safety-rev7.md:225 |
| Tail stabiliser installation | a5-prep-and-safety-rev7.md:240 through a5-prep-and-safety-rev7.md:246 |
| Warhead RBF safety gate | a5-prep-and-safety-rev7.md:321 through a5-prep-and-safety-rev7.md:340 |
| Spec sheet endurance | avenger-5-spec-sheet-rev3.md:53 |
| Spec sheet warhead mass | avenger-5-spec-sheet-rev3.md:133 |
| ESAD power, discrete, and RS-485 interfaces | esad-icd-excalibur-ab00-0054.md:262 through esad-icd-excalibur-ab00-0054.md:350 |
| ESAD connector pinouts | esad-icd-excalibur-ab00-0054.md:164 through esad-icd-excalibur-ab00-0054.md:235 |
| PL-40 launcher components | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:3 through uav_launcher_pl_40_sysml_v2_ingestion_manual.md:59 |
| PL-40 launcher interfaces | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:63 through uav_launcher_pl_40_sysml_v2_ingestion_manual.md:111 |
| PL-40 launcher technical specifications | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:712 through uav_launcher_pl_40_sysml_v2_ingestion_manual.md:723 |
