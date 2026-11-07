# System Interface Table

Level 0 PDF-grounded interface extraction for the Avenger 5 system. Topology follows `schema/avenger_v2_5_sysml_v2_ingestion.md`, which is the authoritative engineering system diagram transcription. ESAD ICD rows carry `[prototype-reference] [Derived]` because the ICD describes an Avenger 3 board-level prototype.

CAN 1 is the autopilot and ruddervator bus: a 970 cm trunk, a 150 cm branch, then four 120 cm stubs to Ruddervator Servos #1 to #4. CAN 2 is the wing servo bus: autopilot to CAN/power splitter PCB, then a series daisy chain through Wing Servos #5 to #8 and onward to the magnetometers and pitot tube. Servo power is an 8 V rail from the EPS module.

| Port Name | Direction | Protocol | Data Type | Refresh Rate | Associated Subsystem | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| CAN 1 Trunk 970 cm | Bidirectional | CAN bus DroneCAN | CAN frame | Not stated | Autopilot Computing Board Cube Orange Plus | avenger_v2_5_sysml_v2_ingestion.md:72, avenger_v2_5_sysml_v2_ingestion.md:171 |
| CAN 1 EPS Tap | Bidirectional | CAN bus DroneCAN | CAN frame | Not stated | EPS Module | avenger_v2_5_sysml_v2_ingestion.md:73 |
| CAN 1 Branch 150 cm | Bidirectional | CAN bus DroneCAN | CAN frame | Not stated | CAN 1 Power Meter Junction Node | avenger_v2_5_sysml_v2_ingestion.md:74, avenger_v2_5_sysml_v2_ingestion.md:172 |
| CAN 1 Ruddervator Servo #1 Branch 120 cm | Bidirectional | CAN bus DroneCAN | Servo command and status frame | Not stated | Ruddervator Servo #1 | avenger_v2_5_sysml_v2_ingestion.md:75, avenger_v2_5_sysml_v2_ingestion.md:173 |
| CAN 1 Ruddervator Servo #2 Branch 120 cm | Bidirectional | CAN bus DroneCAN | Servo command and status frame | Not stated | Ruddervator Servo #2 | avenger_v2_5_sysml_v2_ingestion.md:76, avenger_v2_5_sysml_v2_ingestion.md:173 |
| CAN 1 Ruddervator Servo #3 Branch 120 cm | Bidirectional | CAN bus DroneCAN | Servo command and status frame | Not stated | Ruddervator Servo #3 | avenger_v2_5_sysml_v2_ingestion.md:77, avenger_v2_5_sysml_v2_ingestion.md:173 |
| CAN 1 Ruddervator Servo #4 Branch 120 cm | Bidirectional | CAN bus DroneCAN | Servo command and status frame | Not stated | Ruddervator Servo #4 | avenger_v2_5_sysml_v2_ingestion.md:78, avenger_v2_5_sysml_v2_ingestion.md:173 |
| Servo Power 8V Ruddervator Servo #1 | Out | DC power | 8 V DC | Continuous | Ruddervator Servo #1 | avenger_v2_5_sysml_v2_ingestion.md:79, avenger_v2_5_sysml_v2_ingestion.md:155 |
| Servo Power 8V Ruddervator Servo #2 | Out | DC power | 8 V DC | Continuous | Ruddervator Servo #2 | avenger_v2_5_sysml_v2_ingestion.md:80, avenger_v2_5_sysml_v2_ingestion.md:155 |
| Servo Power 8V Ruddervator Servo #3 | Out | DC power | 8 V DC | Continuous | Ruddervator Servo #3 | avenger_v2_5_sysml_v2_ingestion.md:81, avenger_v2_5_sysml_v2_ingestion.md:155 |
| Servo Power 8V Ruddervator Servo #4 | Out | DC power | 8 V DC | Continuous | Ruddervator Servo #4 | avenger_v2_5_sysml_v2_ingestion.md:82, avenger_v2_5_sysml_v2_ingestion.md:155 |
| Servo Power 8V Splitter Input #1 | Out | DC power | 8 V DC | Continuous | CAN/power splitter PCB | avenger_v2_5_sysml_v2_ingestion.md:83, avenger_v2_5_sysml_v2_ingestion.md:157 |
| Servo Power 8V Splitter Input #2 | Out | DC power | 8 V DC | Continuous | CAN/power splitter PCB | avenger_v2_5_sysml_v2_ingestion.md:84, avenger_v2_5_sysml_v2_ingestion.md:157 |
| Servo Power 8V Splitter Input #3 | Out | DC power | 8 V DC | Continuous | CAN/power splitter PCB | avenger_v2_5_sysml_v2_ingestion.md:85, avenger_v2_5_sysml_v2_ingestion.md:157 |
| Servo Power 8V Splitter Input #4 | Out | DC power | 8 V DC | Continuous | CAN/power splitter PCB | avenger_v2_5_sysml_v2_ingestion.md:86, avenger_v2_5_sysml_v2_ingestion.md:157 |
| Servo Power 8V Wing Servo #5 | Out | DC power | 8 V DC | Continuous | Wing Servo #5 | avenger_v2_5_sysml_v2_ingestion.md:87, avenger_v2_5_sysml_v2_ingestion.md:156 |
| Servo Power 8V Wing Servo #6 | Out | DC power | 8 V DC | Continuous | Wing Servo #6 | avenger_v2_5_sysml_v2_ingestion.md:88, avenger_v2_5_sysml_v2_ingestion.md:156 |
| Servo Power 8V Wing Servo #7 | Out | DC power | 8 V DC | Continuous | Wing Servo #7 | avenger_v2_5_sysml_v2_ingestion.md:89, avenger_v2_5_sysml_v2_ingestion.md:156 |
| Servo Power 8V Wing Servo #8 | Out | DC power | 8 V DC | Continuous | Wing Servo #8 | avenger_v2_5_sysml_v2_ingestion.md:90, avenger_v2_5_sysml_v2_ingestion.md:156 |
| CAN 2 Splitter Input | Out | CAN bus DroneCAN | CAN frame | Not stated | CAN/power splitter PCB | avenger_v2_5_sysml_v2_ingestion.md:91, avenger_v2_5_sysml_v2_ingestion.md:157 |
| CAN 2 Daisy Chain Segment 5 to 6 | Bidirectional | CAN bus DroneCAN | Servo command and status frame | Not stated | Wings | avenger_v2_5_sysml_v2_ingestion.md:92, avenger_v2_5_sysml_v2_ingestion.md:99 |
| CAN 2 Daisy Chain Segment 6 to 7 | Bidirectional | CAN bus DroneCAN | Servo command and status frame | Not stated | Wings | avenger_v2_5_sysml_v2_ingestion.md:99, avenger_v2_5_sysml_v2_ingestion.md:103 |
| CAN 2 Daisy Chain Segment 7 to 8 | Bidirectional | CAN bus DroneCAN | Servo command and status frame | Not stated | Wings | avenger_v2_5_sysml_v2_ingestion.md:103, avenger_v2_5_sysml_v2_ingestion.md:105 |
| CAN 2 Magnetometer Continuation | Bidirectional | CAN bus DroneCAN | Sensor frame | Not stated | Magnetometer mRo RM3100 Lower | avenger_v2_5_sysml_v2_ingestion.md:106, avenger_v2_5_sysml_v2_ingestion.md:108 |
| ETH Backbone | Bidirectional | Ethernet | IP packet | Continuous | ETH Switch | avenger_v2_5_sysml_v2_ingestion.md:114, avenger_v2_5_sysml_v2_ingestion.md:122 |
| Camera Module ETH | Bidirectional | Ethernet | IP packet | Continuous | Camera Compute Module Trip6 | avenger_v2_5_sysml_v2_ingestion.md:114 |
| RPI ETH | Bidirectional | Ethernet | IP packet | Continuous | RPI CM5004032 | avenger_v2_5_sysml_v2_ingestion.md:118 |
| External ETH | Bidirectional | Ethernet | IP packet | Continuous | External Interface Board USB ETH | avenger_v2_5_sysml_v2_ingestion.md:116 |
| Autopilot Camera Serial | Out | UART serial | Serial data | Not stated | Camera Compute Module Trip6 | avenger_v2_5_sysml_v2_ingestion.md:115 |
| Autopilot GNSS Serial | Out | UART serial | Serial data | Not stated | GNSS Module Septentrio Asterx-m3 pro | avenger_v2_5_sysml_v2_ingestion.md:120 |
| GNSS RF Feed | Out | Coaxial RF | GNSS signal | Continuous | GNSS Antenna Talysman TW3972EXF | avenger_v2_5_sysml_v2_ingestion.md:121 |
| Autopilot RPI Serial | Bidirectional | UART serial | Serial data | Not stated | RPI CM5004032 | avenger_v2_5_sysml_v2_ingestion.md:119 |
| Autopilot Radio Serial | Out | UART serial | Serial data | Not stated | Radio Module DTC | avenger_v2_5_sysml_v2_ingestion.md:123 |
| Radio RF Feed Upper | Out | Coaxial RF | RF signal | Continuous | Radio Antenna MPSL4400 Upper | avenger_v2_5_sysml_v2_ingestion.md:125 |
| Radio RF Feed Lower | Out | Coaxial RF | RF signal | Continuous | Radio Antenna MPSL4400 Lower | avenger_v2_5_sysml_v2_ingestion.md:126 |
| External USB | Out | USB | USB data | Not stated | External Interface Board USB ETH | avenger_v2_5_sysml_v2_ingestion.md:117 |
| RPI ESAD RS-485 | Out | RS-485 half duplex | Binary message frame | 100 Hz | ESAD | avenger_v2_5_sysml_v2_ingestion.md:130, esad-icd-excalibur-ab00-0054.md:306, esad-icd-excalibur-ab00-0054.md:307 [prototype-reference] [Derived] |
| RPI ESAD Analog Trigger | Out | Discrete GPIO | Analog trigger level | Event-driven | ESAD | avenger_v2_5_sysml_v2_ingestion.md:131 |
| Proximity Sensor Trigger | Out | Discrete active low | Trigger event | Event-driven | ESAD | avenger_v2_5_sysml_v2_ingestion.md:132, esad-icd-excalibur-ab00-0054.md:203 [prototype-reference] [Derived] |
| ESAD Warhead Initiation | Out | Pyrotechnic initiation | In-line initiation sequence | Event-driven | Warhead | avenger_v2_5_sysml_v2_ingestion.md:133 |
| ESAD Power Input J100 | In | DC power | 14 to 32 V DC, nominal 28 V | Continuous | ESAD | esad-icd-excalibur-ab00-0054.md:272 [prototype-reference] [Derived] |
| ESAD Arm Enable DSC_IN1 | In | Discrete PWM | 1 ms period, 50 percent duty | 1 kHz | ESAD | esad-icd-excalibur-ab00-0054.md:285 [prototype-reference] [Derived] |
| ESAD Umbilical Continuity | In | Analog continuity | Resistance below 0.5 Ohm at 20 mA | Continuous | ESAD | esad-icd-excalibur-ab00-0054.md:284 [prototype-reference] [Derived] |
| ESAD Sensor Board UART | Bidirectional | UART | Sensor data frame | Not stated | ESAD Sensor Board | esad-icd-excalibur-ab00-0054.md:201 [prototype-reference] [Derived] |
| ESAD Sensor Board Power 5V | Out | DC power | 5 V DC | Continuous | ESAD Sensor Board | esad-icd-excalibur-ab00-0054.md:205 [prototype-reference] [Derived] |
| ESAD Sensor IRQ | In | Discrete active low | Trigger event | Event-driven | ESAD Sensor Board | esad-icd-excalibur-ab00-0054.md:203 [prototype-reference] [Derived] |
| ESAD Detonator High Voltage | Out | High voltage | Firing pulse up to 1800 V | Event-driven | ESAD Detonator | esad-icd-excalibur-ab00-0054.md:213, esad-icd-excalibur-ab00-0054.md:613 [prototype-reference] [Derived] |
| ESAD Safe Arm Interlock | In | Discrete interlock | Safe or armed state | Event-driven | ESAD RBF Key | avenger_v2_5_sysml_v2_ingestion.md:134 |
| UAV Power Interlock | In | Discrete interlock | Power ON or OFF | Event-driven | UAV RBF Key | avenger_v2_5_sysml_v2_ingestion.md:70 |
| Warhead RBF Interlock | In | Discrete interlock | Safe or armed | Event-driven | Safety RBF Devices | a5-prep-and-safety-rev7.md:321 |
| Payload Bay Cable | Out | Discrete firing circuit | Detonator firing pulse | Event-driven | Warhead | a5-prep-and-safety-rev7.md:112 |
| Launcher Pneumatic Supply | Out | Pneumatic | Air at 14 bar maximum | Continuous | PL-40 Rail | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:132 |
| Launcher Trigger Command | Out | Electrical discrete | Dual-switch launch command | Event-driven | PL-40 Trigger Handle | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:82 |
| Launcher Trigger Power | Out | DC power | 18 V DC | Continuous | PL-40 Trigger Handle | uav_launcher_pl_40_sysml_v2_ingestion_manual.md:81 |
| GCS UAV Telemetry Link | Bidirectional | RF 4.4 to 5.0 GHz | Telemetry and command frames | Continuous | GCS Radio Box | a5-user-manual-2.md:1273 |
| GCS Antenna RF | Bidirectional | RF 4.4 to 5.0 GHz | RF link | Continuous | GCS MARS Antenna | a5-user-manual-2.md:1687 |
| GCS Rotator Control | Out | Rotator control | Azimuth command | Event-driven | GCS Rotator | a5-user-manual-2.md:1681 |
| GCS Tablet Network | Bidirectional | IP Ethernet or Wi-Fi | Application data | Continuous | GCS Tablet FZ-G2 | a5-user-manual-2.md:404 |
| GCS Ground Radio Power | Out | RF control | 2 W output setting | Event-driven | GCS Radio Box | a5-user-manual-2.md:1690 |
