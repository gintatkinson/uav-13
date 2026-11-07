# PDF Versus Markdown Validation

Validation record for the six source PDFs and their Markdown transcriptions. The values below were established during PDF-versus-Markdown checking and are the evidence base for the R2 rebuild. No PDF was re-extracted during R2.

## 1. Per-File Status

| PDF Source | Markdown Transcription | Status | Coverage Note |
| :--- | :--- | :--- | :--- |
| `schema/Avenger5_V2.5_block_diagram_rev5.pdf` | `schema/avenger_v2_5_sysml_v2_ingestion.md` | Validated | Component decomposition, Fins and Wings boundaries, Servo #1 to #8 topology, CAN 1 and CAN 2 routing, 8 V servo rails, and harness lengths confirmed |
| `schema/A5-user-manual 2.pdf` | `schema/a5-user-manual-2.md` | Validated | Flight limits, dimensions, Ruddervator term, wing panel counts, GCS contents, and ESAD states confirmed |
| `schema/A5_prep and safety_rev7.pdf` | `schema/a5-prep-and-safety-rev7.md` | Validated | Tail stabiliser synonym, four wing panels, eight wing bolts, RBF gates, and warhead and ESAD installation confirmed |
| `schema/AVENGER 5 Spec sheet_rev3.pdf` | `schema/avenger-5-spec-sheet-rev3.md` | Validated | Endurance, cruise, maximum horizontal, stall, maximum dive, wingspan, length, MTOW, RLOS, and warhead mass confirmed |
| `schema/UAV_launcher_PL-40_user_manual_rev_2.6.pdf` | `schema/uav_launcher_pl_40_sysml_v2_ingestion_manual.md` | Validated | 30 kg MTOW, 25 m/s launch velocity, 12 deg launch angle, and 14 bar working pressure confirmed |
| `schema/ESAD ICD_for Excalibur_AB00-0054-01AA-0005 2 1.pdf` | `schema/esad-icd-excalibur-ab00-0054.md` | Validated | Avenger 3 applicability, GE_POW 14/28/32 V, RS-485 115200 bps, Harwin and Molex connector part numbers confirmed |
| `schema/UAV_launcher_PL-40_user_manual_rev_2.6 (1).pdf` | None | Ignored duplicate | Byte-level duplicate role of the launcher PDF; not read, not cited, not used |

## 2. Key-Value Validation Table

| Fact ID | Fact | Validated Value | Source |
| :--- | :--- | :--- | :--- |
| KV-01 | Ruddervator servo group in the drawing | `Fins` box contains Servos #1 to #4 | avenger_v2_5_sysml_v2_ingestion.md:21, avenger_v2_5_sysml_v2_ingestion.md:22 |
| KV-02 | Ruddervator servo positions | Servo #1 Left-up, Servo #2 Right-up, Servo #3 Right-down, Servo #4 Left-down | avenger_v2_5_sysml_v2_ingestion.md:22, avenger_v2_5_sysml_v2_ingestion.md:25 |
| KV-03 | Ruddervator servo model | HV6160-DroneCAN | avenger_v2_5_sysml_v2_ingestion.md:22, avenger_v2_5_sysml_v2_ingestion.md:155 |
| KV-04 | Ruddervator CAN branch lengths | Four CAN 1 120 cm wires branching from the CAN 1 150 cm wire | avenger_v2_5_sysml_v2_ingestion.md:74, avenger_v2_5_sysml_v2_ingestion.md:75, avenger_v2_5_sysml_v2_ingestion.md:173 |
| KV-05 | Wing servo group in the drawing | `Wings` box contains Servos #5 to #8 | avenger_v2_5_sysml_v2_ingestion.md:27, avenger_v2_5_sysml_v2_ingestion.md:28 |
| KV-06 | Wing servo positions | Servo #5 Left-up, Servo #6 Right-up, Servo #7 Right-down, Servo #8 Left-down | avenger_v2_5_sysml_v2_ingestion.md:28, avenger_v2_5_sysml_v2_ingestion.md:31 |
| KV-07 | Wing servo bus | CAN 2 from autopilot to CAN/power splitter PCB, then series daisy chain to Servos #5 to #8 | avenger_v2_5_sysml_v2_ingestion.md:26, avenger_v2_5_sysml_v2_ingestion.md:91, avenger_v2_5_sysml_v2_ingestion.md:105 |
| KV-08 | Servo power rail | 8 V servo rails from EPS module to Servos #1 to #8 | avenger_v2_5_sysml_v2_ingestion.md:79, avenger_v2_5_sysml_v2_ingestion.md:87, avenger_v2_5_sysml_v2_ingestion.md:155 |
| KV-09 | User manual cruise speed | 30 m/s | a5-user-manual-2.md:307 |
| KV-10 | User manual maximum horizontal speed | 38 m/s | a5-user-manual-2.md:308 |
| KV-11 | User manual maximum dive speed | 55 m/s | a5-user-manual-2.md:309 |
| KV-12 | User manual maximum dive angle | 22 deg | a5-user-manual-2.md:310 |
| KV-13 | User manual minimum speed | 26 m/s | a5-user-manual-2.md:311 |
| KV-14 | User manual flight time | 90 min | a5-user-manual-2.md:312 |
| KV-15 | User manual launch type | Catapult/Tube | a5-user-manual-2.md:313 |
| KV-16 | User manual recovery system | No | a5-user-manual-2.md:314 |
| KV-17 | User manual RLOS range | 60 km and 180 km | a5-user-manual-2.md:315 |
| KV-18 | Spec sheet endurance | 90 min | avenger-5-spec-sheet-rev3.md:53 |
| KV-19 | Spec sheet cruise speed | 31 m/s | avenger-5-spec-sheet-rev3.md:54 |
| KV-20 | Spec sheet maximum horizontal speed | 42 m/s | avenger-5-spec-sheet-rev3.md:55 |
| KV-21 | Spec sheet stall speed | 24 m/s | avenger-5-spec-sheet-rev3.md:56 |
| KV-22 | Spec sheet maximum dive speed | 80 m/s | avenger-5-spec-sheet-rev3.md:57 |
| KV-23 | Spec sheet wingspan | 1.8 m | avenger-5-spec-sheet-rev3.md:67 |
| KV-24 | Spec sheet overall length | 1.6 m | avenger-5-spec-sheet-rev3.md:68 |
| KV-25 | Spec sheet MTOW | 17 kg | avenger-5-spec-sheet-rev3.md:69 |
| KV-26 | Spec sheet RLOS range | 60 km and 90 km with relay | avenger-5-spec-sheet-rev3.md:79 |
| KV-27 | Spec sheet warhead mass | 5 kg | avenger-5-spec-sheet-rev3.md:133 |
| KV-28 | ESAD platform scope | Board-level prototype for the Avenger 3 UAV | esad-icd-excalibur-ab00-0054.md:7 |
| KV-29 | ESAD power levels | GE_POW minimum 14 V, nominal 28 V, maximum 32 V | esad-icd-excalibur-ab00-0054.md:272 |
| KV-30 | ESAD RS-485 baud rate | 115200 bps | esad-icd-excalibur-ab00-0054.md:306 |
| KV-31 | ESAD J100 mating connector | Harwin G125-2241696F1 | esad-icd-excalibur-ab00-0054.md:167 |
| KV-32 | ESAD J102 mating connector | Harwin G125-2241096F1 | esad-icd-excalibur-ab00-0054.md:193 |
| KV-33 | ESAD crimps | Harwin G125-0020005 | esad-icd-excalibur-ab00-0054.md:167, esad-icd-excalibur-ab00-0054.md:193 |
| KV-34 | ESAD sensor board connector | Molex 501330-0800 | esad-icd-excalibur-ab00-0054.md:233 |
| KV-35 | Preparation tail surfaces | Four tail stabilisers | a5-prep-and-safety-rev7.md:242 |
| KV-36 | Preparation wing panels | Four wing panels, two left and two right | a5-prep-and-safety-rev7.md:220, a5-user-manual-2.md:337, a5-user-manual-2.md:338 |
| KV-37 | Preparation wing bolts | Eight wing mounting bolts | a5-prep-and-safety-rev7.md:225 |
| KV-38 | Launcher maximum plane mass | 30 kg | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:718 |
| KV-39 | Launcher maximum launch velocity | 25 m/s | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:719 |
| KV-40 | Launcher launch angle | 12 deg | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:712 |
| KV-41 | Launcher working pressure | 14 bar maximum | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:132 |

## 3. Application Rule

- User manual values govern all flight limits.
- Spec sheet values are used only for warhead mass 5 kg and endurance 90 min.
- The block diagram governs topology, servo assignment, CAN routing, servo power, and harness lengths.
- The ESAD ICD is prototype reference data for an Avenger 3 board-level prototype and never a qualified Avenger 5 requirement.
- Contradictory spec sheet performance values are recorded in this table and resolved in `schema/SOURCE_REGISTER.md`.
