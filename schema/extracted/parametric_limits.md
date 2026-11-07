# Parametric Limits Table

Level 0 PDF-grounded parametric extraction for the Avenger 5 system. Flight limits come from `schema/a5-user-manual-2.md` Table 1.3. The spec sheet supplies only warhead mass 5 kg and endurance 90 min. Drawing harness lengths and the 8 V servo rail come from the block diagram transcription. ESAD ICD rows carry `[prototype-reference] [Derived]`.

| Parameter ID | Parameter Name | Min | Max | Units | Verification Source |
| :--- | :--- | :--- | :--- | :--- | :--- |
| PL-01 | Cruise speed | 30 | 30 | m/s | a5-user-manual-2.md:307 |
| PL-02 | Maximum horizontal speed | Not stated | 38 | m/s | a5-user-manual-2.md:308 |
| PL-03 | Maximum dive speed | Not stated | 55 | m/s | a5-user-manual-2.md:309 |
| PL-04 | Maximum dive angle | Not stated | 22 | deg | a5-user-manual-2.md:310 |
| PL-05 | Minimum flight speed | 26 | Not stated | m/s | a5-user-manual-2.md:311 |
| PL-06 | Flight endurance | 0 | 90 | min | avenger-5-spec-sheet-rev3.md:53 |
| PL-07 | RLOS direct range | 0 | 60 | km | a5-user-manual-2.md:315 |
| PL-08 | RLOS extended range | 60 | 180 | km | a5-user-manual-2.md:315 |
| PL-09 | Wingspan | 1.8 | 1.8 | m | a5-user-manual-2.md:287 |
| PL-10 | Assembled UAV length | 1.6 | 1.6 | m | a5-user-manual-2.md:288 |
| PL-11 | Assembled UAV height | 1.1 | 1.1 | m | a5-user-manual-2.md:289 |
| PL-12 | Maximum take-off weight | Not stated | 17 | kg | a5-user-manual-2.md:299 |
| PL-13 | Warhead mass | Not stated | 5 | kg | avenger-5-spec-sheet-rev3.md:133 |
| PL-14 | Ruddervator quantity | 4 | 4 | units | a5-user-manual-2.md:339, avenger_v2_5_sysml_v2_ingestion.md:21 |
| PL-15 | Wing panel quantity | 4 | 4 | units | a5-user-manual-2.md:337, a5-user-manual-2.md:338 |
| PL-16 | Ruddervator servo quantity | 4 | 4 | units | avenger_v2_5_sysml_v2_ingestion.md:22, avenger_v2_5_sysml_v2_ingestion.md:25 |
| PL-17 | Wing servo quantity | 4 | 4 | units | avenger_v2_5_sysml_v2_ingestion.md:28, avenger_v2_5_sysml_v2_ingestion.md:31 |
| PL-18 | Total servo quantity | 8 | 8 | units | avenger_v2_5_sysml_v2_ingestion.md:22, avenger_v2_5_sysml_v2_ingestion.md:31 |
| PL-19 | CAN 1 trunk harness length | 970 | 970 | cm | avenger_v2_5_sysml_v2_ingestion.md:171 |
| PL-20 | CAN 1 ruddervator branch length | 150 | 150 | cm | avenger_v2_5_sysml_v2_ingestion.md:172 |
| PL-21 | CAN 1 servo stub length | 120 | 120 | cm | avenger_v2_5_sysml_v2_ingestion.md:173 |
| PL-22 | Servo power rail voltage | 8 | 8 | V | avenger_v2_5_sysml_v2_ingestion.md:79, avenger_v2_5_sysml_v2_ingestion.md:155 |
| PL-23 | Battery minimum voltage | 36 | 36 | V | avenger_v2_5_sysml_v2_ingestion.md:16 |
| PL-24 | Battery maximum voltage | 50.4 | 50.4 | V | avenger_v2_5_sysml_v2_ingestion.md:16 |
| PL-25 | Seeker pitch angle | -45 | 135 | deg | a5-user-manual-2.md:327 |
| PL-26 | Seeker yaw and roll angle | -165 | 165 | deg | a5-user-manual-2.md:328 |
| PL-27 | Seeker zoom factor | 1 | 40 | X | a5-user-manual-2.md:324 |
| PL-28 | Day camera horizontal resolution | 1280 | 1280 | pixels | a5-user-manual-2.md:325 |
| PL-29 | Day camera vertical resolution | 720 | 720 | pixels | a5-user-manual-2.md:325 |
| PL-30 | Thermal camera horizontal resolution | 1280 | 1280 | pixels | a5-user-manual-2.md:326 |
| PL-31 | Thermal camera vertical resolution | 720 | 720 | pixels | a5-user-manual-2.md:326 |
| PL-32 | UAV battery pre-flight voltage minimum | 49 | 49 | V | a5-user-manual-2.md:1366 |
| PL-33 | UAV battery pre-flight voltage maximum | 50 | 50 | V | a5-user-manual-2.md:1366 |
| PL-34 | Pitot static airspeed limit | 0 | 3 | m/s | a5-user-manual-2.md:1368 |
| PL-35 | Pitot blow-test airspeed | 10 | Not stated | m/s | a5-user-manual-2.md:1369 |
| PL-36 | Minimum mission waypoint altitude | 50 | Not stated | m | a5-user-manual-2.md:1195 |
| PL-37 | Avenger 5 loiter radius | 300 | 300 | m | a5-user-manual-2.md:1497 |
| PL-38 | Mission name length | 0 | 24 | chars | a5-user-manual-2.md:1174 |
| PL-39 | Ground radio power | 2 | 2 | W | a5-user-manual-2.md:1690 |
| PL-40 | Catapult launch pressure minimum | 13 | 13 | bar | a5-user-manual-2.md:1329 |
| PL-41 | Catapult launch pressure maximum | 14 | 14 | bar | a5-user-manual-2.md:1329 |
| PL-42 | Target track duration minimum | 2 | 2 | s | a5-user-manual-2.md:2055 |
| PL-43 | Target track duration maximum | 5 | 5 | s | a5-user-manual-2.md:2055 |
| PL-44 | Maximum engagement elevation | Not stated | 15 | deg | a5-user-manual-2.md:2056 |
| PL-45 | Maximum engagement airspeed | Not stated | 55 | m/s | a5-user-manual-2.md:2061 |
| PL-46 | ESAD power input minimum | 14 | 14 | V | esad-icd-excalibur-ab00-0054.md:272 [prototype-reference] [Derived] |
| PL-47 | ESAD power input maximum | 32 | 32 | V | esad-icd-excalibur-ab00-0054.md:272 [prototype-reference] [Derived] |
| PL-48 | ESAD power input nominal | 28 | 28 | V | esad-icd-excalibur-ab00-0054.md:272 [prototype-reference] [Derived] |
| PL-49 | ESAD umbilical continuity resistance | 0 | 0.5 | Ohm | esad-icd-excalibur-ab00-0054.md:284 [prototype-reference] [Derived] |
| PL-50 | ESAD umbilical continuity current | 20 | 20 | mA | esad-icd-excalibur-ab00-0054.md:284 [prototype-reference] [Derived] |
| PL-51 | ESAD arm enable low voltage | 0 | 0.7 | VDC | esad-icd-excalibur-ab00-0054.md:285 [prototype-reference] [Derived] |
| PL-52 | ESAD arm enable high voltage minimum | 2.5 | 2.5 | VDC | esad-icd-excalibur-ab00-0054.md:286 [prototype-reference] [Derived] |
| PL-53 | ESAD arm enable high voltage maximum | 3.3 | 3.3 | VDC | esad-icd-excalibur-ab00-0054.md:286 [prototype-reference] [Derived] |
| PL-54 | ESAD arm enable period | 1 | 1 | ms | esad-icd-excalibur-ab00-0054.md:285 [prototype-reference] [Derived] |
| PL-55 | ESAD arm enable duty cycle | 50 | 50 | percent | esad-icd-excalibur-ab00-0054.md:285 [prototype-reference] [Derived] |
| PL-56 | ESAD RS-485 baud rate | 115200 | 115200 | bps | esad-icd-excalibur-ab00-0054.md:306 [prototype-reference] [Derived] |
| PL-57 | ESAD RS-485 command interval | 100 | 100 | Hz | esad-icd-excalibur-ab00-0054.md:307 [prototype-reference] [Derived] |
| PL-58 | ESAD response latency | 0 | 5 | ms | esad-icd-excalibur-ab00-0054.md:330 [prototype-reference] [Derived] |
| PL-59 | ESAD incomplete message wait | 0 | 10 | ms | esad-icd-excalibur-ab00-0054.md:335 [prototype-reference] [Derived] |
| PL-60 | ESAD high voltage measurement range | 0 | 1800 | V | esad-icd-excalibur-ab00-0054.md:613 [prototype-reference] [Derived] |
| PL-61 | ESAD message length minimum | 5 | 5 | bytes | esad-icd-excalibur-ab00-0054.md:346 [prototype-reference] [Derived] |
| PL-62 | ESAD message length maximum | 14 | 14 | bytes | esad-icd-excalibur-ab00-0054.md:346 [prototype-reference] [Derived] |
| PL-63 | ESAD acceleration resolution | 0.0039 | 0.0039 | g | esad-icd-excalibur-ab00-0054.md:438 [prototype-reference] [Derived] |
| PL-64 | Maximum launched plane mass | Not stated | 30 | kg | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:718 |
| PL-65 | Maximum launch velocity | Not stated | 25 | m/s | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:719 |
| PL-66 | Launcher launch angle | 12 | 12 | deg | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:712 |
| PL-67 | Maximum compressor working pressure | Not stated | 14 | bar | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:132 |
| PL-68 | Auxiliary filling pressure | Not stated | 16 | bar | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:133 |
| PL-69 | Launcher set mass | 68 | 68 | kg | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:715 |
| PL-70 | Launcher case mass | 43 | 43 | kg | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:716 |
| PL-71 | Compressor case mass | 25 | 25 | kg | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:717 |
| PL-72 | Launcher setup time | 0 | 5 | min | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:722 |
| PL-73 | Launcher working temperature minimum | -20 | -20 | degC | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:723 |
| PL-74 | Launcher working temperature maximum | 50 | 50 | degC | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:723 |
| PL-75 | Launcher battery nominal voltage | 18 | 18 | V | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:134 |
| PL-76 | Launcher battery capacity | 6000 | 6000 | mAh | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:134 |
| PL-77 | Battery over-discharge cutoff | Not stated | 14.5 | V | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:135 |
| PL-78 | Battery over-discharge recovery | 16 | Not stated | V | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:136 |
| PL-79 | Battery recovery delay | 5 | 5 | s | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:136 |
| PL-80 | Pulling rope replacement interval | Not stated | 100 | launches | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:138 |
| PL-81 | Carriage overall length | 271 | 271 | mm | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:142 |
| PL-82 | Carriage lever tip span | 206.5 | 206.5 | mm | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:142 |
| PL-83 | Carriage overall height | 232.5 | 232.5 | mm | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:142 |
| PL-84 | Allowed center of mass longitudinal envelope | 0 | 200 | mm | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:144 |
| PL-85 | Allowed center of mass normal envelope | 0 | 100 | mm | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:144 |
| PL-86 | Launcher overall height | 1115 | 1115 | mm | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:143 |
| PL-87 | Front bipod stance width | 602 | 602 | mm | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:143 |
| PL-88 | Trigger hold time | 2 | Not stated | s | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:530 |
| PL-89 | DC18RC charger time | 0 | 55 | min | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:137 |
| PL-90 | DC18SD charger time | 0 | 130 | min | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:137 |
| PL-91 | Battery charging temperature minimum | 10 | 10 | degC | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:137 |
| PL-92 | Battery charging temperature maximum | 40 | 40 | degC | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:137 |
| PL-93 | Launcher rail length assembled | 5 | 5 | m | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:713 |
| PL-94 | Launcher rail length disassembled | 1.28 | 1.28 | m | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:714 |
