# Level 0 Engineering Drawing Extraction: AIR VEHICLE Avenger V2.5

## 1. Component & Subsystem Decomposition

| Component Name | Subsystem / Boundary | Symbol Type | Description / Drawing Callout |
| :--- | :--- | :--- | :--- |
| `AIR VEHICLE Avenger V2.5` | Top-Level System Boundary | System Boundary (Dashed Box) | Top-level air vehicle boundary enclosing onboard subsystems and components. |
| `Autopilot stack module ASTK A5 V2.5` | `AIR VEHICLE Avenger V2.5` | Subsystem Boundary (Dashed Box) | Encloses `EPS (electronic power system) module`, `Autopilot computing board + sensors`, `ETH switch`, `RPI`, and `GNSS module`. |
| `EPS (electronic power system) module (DC/DC converters, load switches, MCU)` | `Autopilot stack module ASTK A5 V2.5` | Power / Controller | Responsible for providing different power levels to the UAV's subsystems. |
| `Autopilot computing board + sensors (Cube orange+)` | `Autopilot stack module ASTK A5 V2.5` | Controller / Sensor | Responsible for main UAV control logic, flight stabilization and navigation. Provides attitude, position and kinematics estimation from fusing internal and external sensor data. |
| `ETH switch` | `Autopilot stack module ASTK A5 V2.5` | Controller (Network Switch) | Responsible for interfacing different aircraft systems which use IP network for communication. |
| `RPI (CM5004032)` | `Autopilot stack module ASTK A5 V2.5` | Controller | Responsible for interfacing between aircraft systems and SC2 command and control software. |
| `GNSS module (Septentrio Asterx-m3 pro)` | `Autopilot stack module ASTK A5 V2.5` | Sensor | Responsible for providing absolute position and velocity estimates from received GNSS signal data. |
| `GNSS Antenna (Talysman TW3972EXF)` | `AIR VEHICLE Avenger V2.5` | Sensor (Antenna) | Responsible for receiving GNSS satellite signals. |
| `Propulsion` | `AIR VEHICLE Avenger V2.5` | Subsystem Boundary (Dashed Box) | Encloses `Automotive fuse 200A`, `Power meter`, `ESC`, and `Motor` (with `Battery` grouped under `Propulsion` in the functional notes). |
| `Battery (12S2P Li metal BEI, cells - maximus20, 36-50.4V (removable battery))` | `AIR VEHICLE Avenger V2.5` (`Propulsion` functional group) | Power | Responsible for storing and supplying the electrical power required for UAV flight ($36\text{–}50.4\text{ V}$). |
| `Automotive fuse 200A` | `Propulsion` | Power (Protection) | Automotive Fuse ($200\text{ A}$): Provides protection in the event of a short circuit in the main power line. |
| `Power meter (Voltage & Current sensor, Main power switch)` | `Propulsion` | Power / Sensor / Switch | Power Meter: Responsible for controlling the UAV's ON/OFF state. When the UAV R.B.F. key is removed, the UAV is switched ON. Provides battery voltage and current metrics to the autopilot. |
| `ESC (IBEX160)` | `Propulsion` | Controller / Actuator Drive | ESC (Electronic Speed Controller): Responsible for controlling motor speed. It converts the battery's DC power into the appropriate three-phase electrical signals required to drive the motors. |
| `Motor (AXI 5345/16 HD GOLD LINE V3)` | `Propulsion` | Actuator | Motor: Converts electrical power into mechanical power to generate thrust. |
| `Fins` | `AIR VEHICLE Avenger V2.5` | Subsystem Boundary (Dashed Box) | Encloses `Servos #1` through `Servos #4`. |
| `Servos #1 Left-up (HV6160-DroneCAN)` | `Fins` | Actuator | Servo #1–#4: Responsible for UAV pitch and yaw control. The UAV does not bank during turns like conventional UAVs; instead, it performs skid turns using yaw. All four fins are mixed to provide both pitch and yaw control. |
| `Servos #2 Right-up (HV6160-DroneCAN)` | `Fins` | Actuator | Servo #1–#4: Responsible for UAV pitch and yaw control. The UAV does not bank during turns like conventional UAVs; instead, it performs skid turns using yaw. All four fins are mixed to provide both pitch and yaw control. |
| `Servos #3 Right-down (HV6160-DroneCAN)` | `Fins` | Actuator | Servo #1–#4: Responsible for UAV pitch and yaw control. The UAV does not bank during turns like conventional UAVs; instead, it performs skid turns using yaw. All four fins are mixed to provide both pitch and yaw control. |
| `Servos #4 Left-down (HV6160-DroneCAN)` | `Fins` | Actuator | Servo #1–#4: Responsible for UAV pitch and yaw control. The UAV does not bank during turns like conventional UAVs; instead, it performs skid turns using yaw. All four fins are mixed to provide both pitch and yaw control. |
| `CAN/power splitter PCB (servos CAN data connected in series)` | `AIR VEHICLE Avenger V2.5` | Power / Bus Splitter Module | Distributes four `Servo power 8V` lines and routes `CAN 2` data in series to `Wings` servos (`Servos #5`–`#8`). |
| `Wings` | `AIR VEHICLE Avenger V2.5` | Subsystem Boundary (Dashed Box) | Encloses `Servos #5` through `Servos #8`. |
| `Servos #5 Left-up (HV6160-DroneCAN)` | `Wings` | Actuator | Servo #5–#8: Responsible for UAV roll stabilization. The UAV continuously stabilizes its roll to maintain a level attitude relative to the horizon. During yaw turns, the UAV does not roll; instead, it maintains a level attitude and performs a horizontal skid turn. |
| `Servos #6 Right-up (HV6160-DroneCAN)` | `Wings` | Actuator | Servo #5–#8: Responsible for UAV roll stabilization. The UAV continuously stabilizes its roll to maintain a level attitude relative to the horizon. During yaw turns, the UAV does not roll; instead, it maintains a level attitude and performs a horizontal skid turn. |
| `Servos #7 Right-down (HV6160-DroneCAN)` | `Wings` | Actuator | Servo #5–#8: Responsible for UAV roll stabilization. The UAV continuously stabilizes its roll to maintain a level attitude relative to the horizon. During yaw turns, the UAV does not roll; instead, it maintains a level attitude and performs a horizontal skid turn. |
| `Servos #8 Left-down (HV6160-DroneCAN)` | `Wings` | Actuator | Servo #5–#8: Responsible for UAV roll stabilization. The UAV continuously stabilizes its roll to maintain a level attitude relative to the horizon. During yaw turns, the UAV does not roll; instead, it maintains a level attitude and performs a horizontal skid turn. |
| `Pito tube (CUAV SKYE2 Airspeed sensor)` | `AIR VEHICLE Avenger V2.5` | Sensor | Responsible for measuring airspeed. Has in-built heating and drainage. |
| `Magnetometer (mRo RM3100)` [Unit 1 - Upper] | `AIR VEHICLE Avenger V2.5` | Sensor | Responsible for measuring the UAV's heading. The current magnetometer modules also include barometric sensors, which are used for altitude estimation. |
| `Magnetometer (mRo RM3100)` [Unit 2 - Lower] | `AIR VEHICLE Avenger V2.5` | Sensor | Responsible for measuring the UAV's heading. The current magnetometer modules also include barometric sensors, which are used for altitude estimation. |
| `Gimbal (Nighthawk2UZ)` | `AIR VEHICLE Avenger V2.5` | Actuator / Sensor Payload | Responsible for IR/RGB camera sensor pointing and stabilization. |
| `Camera compute module (Trip6)` | `AIR VEHICLE Avenger V2.5` | Controller | Responsible for controlling the gimbal, providing video feed, target tracking, filtered gimbal kinematic measurements, and target position estimation based on provided UAV position data. |
| `Radio module (DTC 4.4-5 GHz DC IN 8-17V, 2x1W output power)` | `AIR VEHICLE Avenger V2.5` | Controller / Transceiver | Responsible for receiving command and control data, while transmitting telemetry and video. |
| `Radio Antenna (MPSL4400)` [Unit 1 - Upper] | `AIR VEHICLE Avenger V2.5` | Sensor / Actuator (Antenna) | Responsible for transmitting and receiving radio signals to and from the radio module. |
| `Radio Antenna (MPSL4400)` [Unit 2 - Lower] | `AIR VEHICLE Avenger V2.5` | Sensor / Actuator (Antenna) | Responsible for transmitting and receiving radio signals to and from the radio module. |
| `Parachute deployment (optional for RnD UAV)` | `AIR VEHICLE Avenger V2.5` | Subsystem Boundary (Dashed Box) | Encloses two `Igniter` blocks. |
| `Igniter` [Unit 1 - Upper] | `Parachute deployment (optional for RnD UAV)` | Actuator (Pyrotechnic Initiator) | Igniters: Pyrotechnic devices responsible for burning the wire that holds the payload bay cover, where the parachute is installed. |
| `Igniter` [Unit 2 - Lower] | `Parachute deployment (optional for RnD UAV)` | Actuator (Pyrotechnic Initiator) | Igniters: Pyrotechnic devices responsible for burning the wire that holds the payload bay cover, where the parachute is installed. |
| `Proximity sensor` | `AIR VEHICLE Avenger V2.5` | Sensor | Responsible for sending the triggering signal to the ESAD. |
| `Lethal package` | `AIR VEHICLE Avenger V2.5` | Subsystem Boundary (Dashed Box) | Encloses `ESAD` and `Warhead`. |
| `ESAD` | `Lethal package` | Controller (Safety & Arming Device) | ESAD (Electronic Safe and Arm Device): high-voltage, all-electronic safety device used to control in-line the initiation sequence of a pyrotechnic train on warhead modules. |
| `Warhead` | `Lethal package` | Payload | Responsible for explosion. |
| `External Interface board (USB/ETH)` | External to `AIR VEHICLE Avenger V2.5` | Controller / Interface | Responsible for connecting to the UAV's subsystems. |
| `UAV R.B.F Key` | External to `AIR VEHICLE Avenger V2.5` | Safety Interlock / Switch Key | When the UAV R.B.F. key is removed, the UAV is switched ON. |
| `ESAD R.B.F Key` | External to `AIR VEHICLE Avenger V2.5` | Safety Interlock / Switch Key | Responsible for ensuring the safe arming sequence of the ESAD. It must be removed according to the specific arming sequence of the ESAD. |
| `CAN 1 Autopilot/EPS Junction Node` | `Autopilot stack module ASTK A5 V2.5` | Bus Junction Node | Black junction node on `CAN 1` bus linking `Autopilot computing board + sensors`, `EPS (electronic power system) module`, and the `CAN 1 970cm wire` trunk. |
| `CAN 1 Power Meter Junction Node` | `Propulsion` | Bus Junction Node | Black junction node below `Power meter` linking `CAN 1 970cm wire`, `Power meter`, and the `CAN 1 150cm wire` branch to `Fins`. |
| `CAN 1 Fins Splitter Junction Node` | `AIR VEHICLE Avenger V2.5` | Bus Junction Node | Black junction hub splitting the `CAN 1 150cm wire` branch into four `CAN 1 120 cm wire` stubs for `Servos #1`–`#4`. |
| `CAN 2 Servo #5 Series Junction Node` | `AIR VEHICLE Avenger V2.5` | Bus Junction Node | Black junction node between `CAN/power splitter PCB` and `Servos #5 Left-up (HV6160-DroneCAN)`. |
| `CAN 2 Servo #6 Series Junction Node` | `AIR VEHICLE Avenger V2.5` | Bus Junction Node | Black junction node between `CAN/power splitter PCB` and `Servos #6 Right-up (HV6160-DroneCAN)`. |
| `CAN 2 Servo #7 Series Junction Node` | `AIR VEHICLE Avenger V2.5` | Bus Junction Node | Black junction node between `CAN/power splitter PCB` and `Servos #7 Right-down (HV6160-DroneCAN)`. |

---

## 2. Interface & Interconnect Topology

| Source Component | Source Port | Connection Type / Protocol | Target Component | Target Port | Signal / Payload Label | Directionality |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `Battery (12S2P Li metal BEI, cells - maximus20, 36-50.4V (removable battery))` | Right (out) | Power (Red Line) | `Automotive fuse 200A` | Left (in) | `Batt Power` | Unidirectional |
| `Automotive fuse 200A` | Right (out) | Power (Red Line) | `Power meter (Voltage & Current sensor, Main power switch)` | Left (in) | `Batt Power` (fused continuation) | Unidirectional |
| `Power meter (Voltage & Current sensor, Main power switch)` | Right (out) | Power (Red Line) | `ESC (IBEX160)` | Left (in) | Unlabeled (Switched `Batt Power`) | Unidirectional |
| `ESC (IBEX160)` | Right (out) | Power (Red Line, 3-Phase Drive) | `Motor (AXI 5345/16 HD GOLD LINE V3)` | Left (in) | Unlabeled (Three-phase motor drive) | Unidirectional |
| `Motor (AXI 5345/16 HD GOLD LINE V3)` | Left-Bottom (out) | Discrete / Analog Telemetry | `ESC (IBEX160)` | Right-Bottom (in) | `Telemetry (Mot. Temperature)` | Unidirectional |
| `Power meter (Voltage & Current sensor, Main power switch)` | Top-Right (out) | PWM / Control | `ESC (IBEX160)` | Top (in) | `PWM ESC control` | Unidirectional |
| `ESC (IBEX160)` | Bottom-Left (out) | Serial (UART) | `Power meter (Voltage & Current sensor, Main power switch)` | Bottom-Right (in) | `Telemetry data UART (rpm, temp (esc&mot), Current, Voltage)` | Unidirectional |
| `Power meter (Voltage & Current sensor, Main power switch)` | Top (out) | Discrete / Interlock | `UAV R.B.F Key` | Bottom (in) | Unlabeled (ON/OFF state key interlock) | Unidirectional |
| `Power meter (Voltage & Current sensor, Main power switch)` | Top-Left (out) | Power / Harness (Red Line) | `EPS (electronic power system) module (DC/DC converters, load switches, MCU)` | Top (in) | `Batt Power 970cm wire` | Unidirectional |
| `Autopilot computing board + sensors (Cube orange+)` | Right (in/out) | CAN Bus / Harness | `Power meter (Voltage & Current sensor, Main power switch)` | Bottom (in/out) | `CAN 1 970cm wire` (via `CAN 1 Autopilot/EPS Junction Node` and `CAN 1 Power Meter Junction Node`) | Bidirectional |
| `EPS (electronic power system) module (DC/DC converters, load switches, MCU)` | Bottom-Right (in/out) | CAN Bus | `CAN 1 Autopilot/EPS Junction Node` | Top (in/out) | Unlabeled (`CAN 1` tap to `Autopilot computing board + sensors`) | Bidirectional |
| `CAN 1 Power Meter Junction Node` | Bottom (in/out) | CAN Bus / Harness | `CAN 1 Fins Splitter Junction Node` | Top (in/out) | `CAN 1 150cm wire` | Bidirectional |
| `CAN 1 Fins Splitter Junction Node` | Right-Branch 1 (out) | CAN Bus / Harness | `Servos #1 Left-up (HV6160-DroneCAN)` | Left (in) | `CAN 1 120 cm wire` | Unidirectional (Arrow at Servo #1; shared with bidirectional `Power meter` node) |
| `CAN 1 Fins Splitter Junction Node` | Right-Branch 2 (in/out) | CAN Bus / Harness | `Servos #2 Right-up (HV6160-DroneCAN)` | Left (in/out) | `CAN 1 120 cm wire` | Bidirectional |
| `CAN 1 Fins Splitter Junction Node` | Right-Branch 3 (in/out) | CAN Bus / Harness | `Servos #3 Right-down (HV6160-DroneCAN)` | Left (in/out) | `CAN 1 120 cm wire` | Bidirectional |
| `CAN 1 Fins Splitter Junction Node` | Right-Branch 4 (in/out) | CAN Bus / Harness | `Servos #4 Left-down (HV6160-DroneCAN)` | Left (in/out) | `CAN 1 120 cm wire` | Bidirectional |
| `EPS (electronic power system) module (DC/DC converters, load switches, MCU)` | Right-Port 1 (out) | Power (Red Line) | `Servos #1 Left-up (HV6160-DroneCAN)` | Right (in) | `Servo power 8V` | Unidirectional |
| `EPS (electronic power system) module (DC/DC converters, load switches, MCU)` | Right-Port 2 (out) | Power (Red Line) | `Servos #2 Right-up (HV6160-DroneCAN)` | Right (in) | `Servo power 8V` | Unidirectional |
| `EPS (electronic power system) module (DC/DC converters, load switches, MCU)` | Right-Port 3 (out) | Power (Red Line) | `Servos #3 Right-down (HV6160-DroneCAN)` | Right (in) | `Servo power 8V` | Unidirectional |
| `EPS (electronic power system) module (DC/DC converters, load switches, MCU)` | Right-Port 4 (out) | Power (Red Line) | `Servos #4 Left-down (HV6160-DroneCAN)` | Right (in) | `Servo power 8V` | Unidirectional |
| `EPS (electronic power system) module (DC/DC converters, load switches, MCU)` | Left-Port 1 (out) | Power (Red Line) | `CAN/power splitter PCB (servos CAN data connected in series)` | Top-Port 1 (in) | `Servo power 8V` | Unidirectional |
| `EPS (electronic power system) module (DC/DC converters, load switches, MCU)` | Left-Port 2 (out) | Power (Red Line) | `CAN/power splitter PCB (servos CAN data connected in series)` | Top-Port 2 (in) | `Servo power 8V` | Unidirectional |
| `EPS (electronic power system) module (DC/DC converters, load switches, MCU)` | Left-Port 3 (out) | Power (Red Line) | `CAN/power splitter PCB (servos CAN data connected in series)` | Top-Port 3 (in) | `Servo power 8V` | Unidirectional |
| `EPS (electronic power system) module (DC/DC converters, load switches, MCU)` | Left-Port 4 (out) | Power (Red Line) | `CAN/power splitter PCB (servos CAN data connected in series)` | Top-Port 4 (in) | `Servo power 8V` | Unidirectional |
| `CAN/power splitter PCB (servos CAN data connected in series)` | Left-Port 1 (out) | Power (Red Line) | `Servos #5 Left-up (HV6160-DroneCAN)` | Left (in) | `Servo power 8V` | Unidirectional |
| `CAN/power splitter PCB (servos CAN data connected in series)` | Left-Port 2 (out) | Power (Red Line) | `Servos #6 Right-up (HV6160-DroneCAN)` | Left (in) | `Servo power 8V` | Unidirectional |
| `CAN/power splitter PCB (servos CAN data connected in series)` | Left-Port 3 (out) | Power (Red Line) | `Servos #7 Right-down (HV6160-DroneCAN)` | Left (in) | `Servo power 8V` | Unidirectional |
| `CAN/power splitter PCB (servos CAN data connected in series)` | Left-Port 4 (out) | Power (Red Line) | `Servos #8 Left-down (HV6160-DroneCAN)` | Left (in) | `Servo power 8V` | Unidirectional |
| `Autopilot computing board + sensors (Cube orange+)` | Left (out) | CAN Bus | `CAN/power splitter PCB (servos CAN data connected in series)` | Top-Right (in) | `CAN 2` | Unidirectional |
| `CAN/power splitter PCB (servos CAN data connected in series)` | Internal Top-Right (in) | Internal PCB Trace (CAN Bus) | `CAN/power splitter PCB (servos CAN data connected in series)` | Right-Port 1 (out) | Unlabeled (Internal series pass-through 1) | Unidirectional |
| `CAN/power splitter PCB (servos CAN data connected in series)` | Right-Port 1 (in/out) | CAN Bus | `CAN 2 Servo #5 Series Junction Node` | Top-Right (in/out) | `CAN2` | Bidirectional |
| `Servos #5 Left-up (HV6160-DroneCAN)` | Right (out) | CAN Bus | `CAN 2 Servo #5 Series Junction Node` | Left (in) | Unlabeled (`CAN 2` stub) | Unidirectional |
| `CAN 2 Servo #5 Series Junction Node` | Bottom-Right (in/out) | CAN Bus | `CAN/power splitter PCB (servos CAN data connected in series)` | Right-Port 2 (in/out) | `CAN 2` | Bidirectional |
| `CAN/power splitter PCB (servos CAN data connected in series)` | Right-Port 2 (in/out) | Internal PCB Trace (CAN Bus) | `CAN/power splitter PCB (servos CAN data connected in series)` | Right-Port 3 (in/out) | Unlabeled (Internal series pass-through 2) | Bidirectional |
| `CAN/power splitter PCB (servos CAN data connected in series)` | Right-Port 3 (in/out) | CAN Bus | `CAN 2 Servo #6 Series Junction Node` | Top-Right (in/out) | `CAN 2` | Bidirectional |
| `Servos #6 Right-up (HV6160-DroneCAN)` | Right (in/out) | CAN Bus | `CAN 2 Servo #6 Series Junction Node` | Left (in/out) | Unlabeled (`CAN 2` stub) | Undirected / Bus Stub |
| `CAN 2 Servo #6 Series Junction Node` | Bottom-Right (in/out) | CAN Bus | `CAN/power splitter PCB (servos CAN data connected in series)` | Right-Port 4 (in/out) | `CAN 2` | Bidirectional |
| `CAN/power splitter PCB (servos CAN data connected in series)` | Right-Port 4 (in/out) | Internal PCB Trace (CAN Bus) | `CAN/power splitter PCB (servos CAN data connected in series)` | Right-Port 5 (in/out) | Unlabeled (Internal series pass-through 3) | Bidirectional |
| `CAN/power splitter PCB (servos CAN data connected in series)` | Right-Port 5 (in/out) | CAN Bus | `CAN 2 Servo #7 Series Junction Node` | Top-Right (in/out) | `CAN 2` | Bidirectional |
| `Servos #7 Right-down (HV6160-DroneCAN)` | Right (in/out) | CAN Bus | `CAN 2 Servo #7 Series Junction Node` | Left (in/out) | Unlabeled (`CAN 2` stub) | Undirected / Bus Stub |
| `CAN 2 Servo #7 Series Junction Node` | Bottom-Right (in/out) | CAN Bus | `CAN/power splitter PCB (servos CAN data connected in series)` | Right-Port 6 (in/out) | `CAN 2` | Bidirectional |
| `CAN/power splitter PCB (servos CAN data connected in series)` | Right-Port 6 (in/out) | Internal PCB Trace (CAN Bus) | `CAN/power splitter PCB (servos CAN data connected in series)` | Right-Port 7 (in/out) | Unlabeled (Internal series pass-through 4) | Bidirectional |
| `CAN/power splitter PCB (servos CAN data connected in series)` | Right-Port 7 (in/out) | CAN Bus | `Servos #8 Left-down (HV6160-DroneCAN)` | Right-Upper (in/out) | `CAN 2` | Bidirectional |
| `Servos #8 Left-down (HV6160-DroneCAN)` | Right-Lower (out) | CAN Bus | `Magnetometer (mRo RM3100)` [Unit 2 - Lower] | Right-Bottom (in) | `CAN 2` | Unidirectional |
| `Magnetometer (mRo RM3100)` [Unit 2 - Lower] | Right-Middle (in/out) | CAN Bus | `Magnetometer (mRo RM3100)` [Unit 1 - Upper] | Right-Bottom (in/out) | `CAN 2` | Bidirectional |
| `Magnetometer (mRo RM3100)` [Unit 1 - Upper] | Right-Top (in/out) | CAN Bus | `Pito tube (CUAV SKYE2 Airspeed sensor)` | Right-Bottom (in/out) | `CAN 2` | Bidirectional |
| `EPS (electronic power system) module (DC/DC converters, load switches, MCU)` | Left-Lower 1 (out) | Power (Red Line) | `Pito tube (CUAV SKYE2 Airspeed sensor)` | Right-Top (in) | `Pito power` | Unidirectional |
| `EPS (electronic power system) module (DC/DC converters, load switches, MCU)` | Bottom-Left 1 (out) | Power (Red Line) | `Magnetometer (mRo RM3100)` [Unit 1 - Upper] | Right-Middle (in) | `Mag Power` | Unidirectional |
| `EPS (electronic power system) module (DC/DC converters, load switches, MCU)` | Bottom-Left 2 (out) | Power (Red Line) | `Magnetometer (mRo RM3100)` [Unit 2 - Lower] | Right-Top (in) | `Mag Power` | Unidirectional |
| `EPS (electronic power system) module (DC/DC converters, load switches, MCU)` | Left-Lower 2 (out) | Power (Red Line) | `Camera compute module (Trip6)` | Top (in) | `Gimbal + Camera compute module power` | Unidirectional |
| `Camera compute module (Trip6)` | Left (in/out) | Power + Video/Data | `Gimbal (Nighthawk2UZ)` | Right (in/out) | `Power + HDMI data` | Bidirectional |
| `ETH switch` | Bottom-Right (in/out) | Ethernet (ETH) | `Camera compute module (Trip6)` | Right (in/out) | `ETH` | Bidirectional |
| `Autopilot computing board + sensors (Cube orange+)` | Right-Lower (out) | Serial | `Camera compute module (Trip6)` | Bottom (in) | `Serial` | Unidirectional |
| `ETH switch` | Right (in/out) | Ethernet (ETH) | `External Interface board (USB/ETH)` | Bottom-Left (in/out) | `ETH` | Bidirectional |
| `Autopilot computing board + sensors (Cube orange+)` | Right-Upper (out) | USB | `External Interface board (USB/ETH)` | Bottom-Right (in) | `USB` | Unidirectional |
| `ETH switch` | Bottom (in/out) | Ethernet (ETH) | `RPI (CM5004032)` | Top (in/out) | `ETH` | Bidirectional |
| `Autopilot computing board + sensors (Cube orange+)` | Bottom-Middle (in/out) | Serial | `RPI (CM5004032)` | Left (in/out) | `Serial` | Bidirectional |
| `Autopilot computing board + sensors (Cube orange+)` | Bottom-Left (out) | Serial | `GNSS module (Septentrio Asterx-m3 pro)` | Right (in) | `Serial` | Unidirectional |
| `GNSS module (Septentrio Asterx-m3 pro)` | Left (out) | RF / Coaxial | `GNSS Antenna (Talysman TW3972EXF)` | Right (in) | Unlabeled (GNSS RF signal line) | Unidirectional |
| `ETH switch` | Left (in/out) | Ethernet (ETH) | `Radio module (DTC 4.4-5 GHz DC IN 8-17V, 2x1W output power)` | Right-Middle (in/out) | `ETH` | Bidirectional |
| `Autopilot computing board + sensors (Cube orange+)` | Bottom-Right (out) | Serial | `Radio module (DTC 4.4-5 GHz DC IN 8-17V, 2x1W output power)` | Right-Top (in) | `Serial` | Unidirectional |
| `EPS (electronic power system) module (DC/DC converters, load switches, MCU)` | Right-Top (out) | Power (Red Line) | `Radio module (DTC 4.4-5 GHz DC IN 8-17V, 2x1W output power)` | Right-Bottom (in) | `Radio power 12V` | Unidirectional |
| `Radio module (DTC 4.4-5 GHz DC IN 8-17V, 2x1W output power)` | Left-Top (out) | RF / Coaxial | `Radio Antenna (MPSL4400)` [Unit 1 - Upper] | Right (in) | Unlabeled (RF antenna feed 1) | Unidirectional |
| `Radio module (DTC 4.4-5 GHz DC IN 8-17V, 2x1W output power)` | Left-Bottom (out) | RF / Coaxial | `Radio Antenna (MPSL4400)` [Unit 2 - Lower] | Right (in) | Unlabeled (RF antenna feed 2) | Unidirectional |
| `EPS (electronic power system) module (DC/DC converters, load switches, MCU)` | Bottom-Right 1 (out) | Power (Red Line) | `Igniter` [Unit 1 - Upper] | Left (in) | `Power 50V` | Unidirectional |
| `EPS (electronic power system) module (DC/DC converters, load switches, MCU)` | Bottom-Right 2 (out) | Power (Red Line) | `Igniter` [Unit 2 - Lower] | Left (in) | `Power 50V` | Unidirectional |
| `EPS (electronic power system) module (DC/DC converters, load switches, MCU)` | Right-Lower (out) | Power (Red Line) | `ESAD` | Top (in) | `ESAD power 14V` | Unidirectional |
| `RPI (CM5004032)` | Right (out) | Serial (RS-485) | `ESAD` | Left-Top (in) | `RS-485` | Unidirectional |
| `RPI (CM5004032)` | Bottom (out) | Discrete / Analog (GPIO) | `ESAD` | Left-Bottom (in) | `Analog trigger (GPIO)` | Unidirectional |
| `Proximity sensor` | Bottom (out) | Discrete / Trigger | `ESAD` | Bottom (in) | Unlabeled (Triggering signal to ESAD) | Unidirectional |
| `ESAD` | Right (out) | Pyrotechnic / Initiation | `Warhead` | Left (in) | Unlabeled (In-line initiation sequence) | Unidirectional |
| `ESAD` | Right-Bottom (out) | Discrete / Interlock | `ESAD R.B.F Key` | Top (in) | Unlabeled (Safe arming sequence interlock) | Unidirectional |

---

## 3. Drawing Notes & Physical Constraints

| Note / Constraint ID | Scope (Component or System) | Parameter / Constraint Statement | Value & Units |
| :--- | :--- | :--- | :--- |
| `NOTE-SYS-01` | `AIR VEHICLE Avenger V2.5` | System Designation / Version Callout | `Avenger V2.5` |
| `NOTE-ASTK-00` | `Autopilot stack module ASTK A5 V2.5` | Subsystem Module Version Callout | `ASTK A5 V2.5` |
| `NOTE-ASTK-01` | `Autopilot computing board + sensors (Cube orange+)` | Autopilot computing board + sensors: Responsible for main UAV control logic, flight stabilization and navigation. Provides attitude, position and kinematics estimation from fusing internal and external sensor data. | Hardware: `Cube orange+` |
| `NOTE-ASTK-02` | `EPS (electronic power system) module` | EPS (electronic power system) module: Responsible for providing different power levels to the UAV's subsystems. | Architecture: `DC/DC converters, load switches, MCU`; Outputs: $8\text{ V}$ ($\times 8$ `Servo power 8V`), $12\text{ V}$ (`Radio power 12V`), $14\text{ V}$ (`ESAD power 14V`), $50\text{ V}$ ($\times 2$ `Power 50V`), `Pito power`, `Mag Power` ($\times 2$), `Gimbal + Camera compute module power` |
| `NOTE-ASTK-03` | `ETH switch` | ETH switch: Responsible for interfacing different aircraft systems which use IP network for communication. | Protocol: `IP network` / `ETH` |
| `NOTE-ASTK-04` | `RPI (CM5004032)` | RPI: Responsible for interfacing between aircraft systems and SC2 command and control software. | Part Number: `CM5004032` |
| `NOTE-ASTK-05` | `GNSS module (Septentrio Asterx-m3 pro)` | GNSS module: Responsible for providing absolute position and velocity estimates from received GNSS signal data. | Model: `Septentrio Asterx-m3 pro` |
| `NOTE-ASTK-06` | `GNSS Antenna (Talysman TW3972EXF)` | GNSS Antenna: Responsible for receiving GNSS satellite signals. | Model: `Talysman TW3972EXF` |
| `NOTE-PROP-01` | `Battery` | Battery: Responsible for storing and supplying the electrical power required for UAV flight. | Configuration: $12\text{S}2\text{P}$ `Li metal BEI, cells - maximus20`, Voltage: $36\text{–}50.4\text{ V}$, Type: `removable battery` |
| `NOTE-PROP-02` | `Automotive fuse 200A` | Automotive Fuse ($200\text{ A}$): Provides protection in the event of a short circuit in the main power line. | Current Rating: $200\text{ A}$ (`200A`) |
| `NOTE-PROP-03` | `Power meter` | Power Meter: Responsible for controlling the UAV's ON/OFF state. When the UAV R.B.F. key is removed, the UAV is switched ON. Provides battery voltage and current metrics to the autopilot. | Sub-elements: `Voltage & Current sensor, Main power switch` |
| `NOTE-PROP-04` | `ESC (IBEX160)` | ESC (Electronic Speed Controller): Responsible for controlling motor speed. It converts the battery's DC power into the appropriate three-phase electrical signals required to drive the motors. | Model: `IBEX160` |
| `NOTE-PROP-05` | `Motor (AXI 5345/16 HD GOLD LINE V3)` | Motor: Converts electrical power into mechanical power to generate thrust. | Model: `AXI 5345/16 HD GOLD LINE V3` |
| `NOTE-FINS-01` | `Fins` (`Servos #1`–`#4`) | Servo #1–#4: Responsible for UAV pitch and yaw control. The UAV does not bank during turns like conventional UAVs; instead, it performs skid turns using yaw. All four fins are mixed to provide both pitch and yaw control. | Model: `HV6160-DroneCAN` ($\times 4$); Servo Power: $8\text{ V}$ |
| `NOTE-WINGS-01` | `Wings` (`Servos #5`–`#8`) | Servo #5–#8: Responsible for UAV roll stabilization. The UAV continuously stabilizes its roll to maintain a level attitude relative to the horizon. During yaw turns, the UAV does not roll; instead, it maintains a level attitude and performs a horizontal skid turn. | Model: `HV6160-DroneCAN` ($\times 4$); Servo Power: $8\text{ V}$ |
| `NOTE-SPLIT-01` | `CAN/power splitter PCB` | Callout on component box: `(servos CAN data connected in series)` | Topology: Series `CAN 2` daisy-chain; Power: $4\times$ `Servo power 8V` inputs to $4\times$ `Servo power 8V` outputs |
| `NOTE-PITO-01` | `Pito tube (CUAV SKYE2 Airspeed sensor)` | Pito tube: Responsible for measuring airspeed. Has in-built heating and drainage. | Model: `CUAV SKYE2 Airspeed sensor` |
| `NOTE-MAG-01` | `Magnetometer (mRo RM3100)` ($\times 2$) | Magnetometer: Responsible for measuring the UAV's heading. The current magnetometer modules also include barometric sensors, which are used for altitude estimation. | Model: `mRo RM3100` ($2\text{ units}$) |
| `NOTE-GIMB-01` | `Gimbal (Nighthawk2UZ)` | Gimbal: Responsible for IR/RGB camera sensor pointing and stabilization. | Model: `Nighthawk2UZ` |
| `NOTE-CAM-01` | `Camera compute module (Trip6)` | Camera compute module: Responsible for controlling the gimbal, providing video feed, target tracking, filtered gimbal kinematic measurements, and target position estimation based on provided UAV position data. | Model: `Trip6` |
| `NOTE-RAD-01` | `Radio module` | Radio module: Responsible for receiving command and control data, while transmitting telemetry and video. | Model: `DTC`, Frequency: $4.4\text{–}5\text{ GHz}$, Input Voltage: `DC IN` $8\text{–}17\text{ V}$, RF Output Power: $2 \times 1\text{ W}$ `output power`, Supplied Power: `Radio power 12V` |
| `NOTE-ANT-01` | `Radio Antenna (MPSL4400)` ($\times 2$) | Radio Antenna: Responsible for transmitting and receiving radio signals to and from the radio module. | Model: `MPSL4400` ($2\text{ units}$) |
| `NOTE-LETH-01` | `ESAD` | ESAD (Electronic Safe and Arm Device): high-voltage, all-electronic safety device used to control in-line the initiation sequence of a pyrotechnic train on warhead modules. | Supplied Power: `ESAD power 14V`; Control Interfaces: `RS-485`, `Analog trigger (GPIO)` |
| `NOTE-LETH-02` | `ESAD R.B.F Key` | ESAD R.B.F Key: Responsible for ensuring the safe arming sequence of the ESAD. It must be removed according to the specific arming sequence of the ESAD. | N/A |
| `NOTE-LETH-03` | `Proximity sensor` | Proximity sensor: Responsible for sending the triggering signal to the ESAD. | N/A |
| `NOTE-LETH-04` | `Warhead` | Warhead: Responsible for explosion. | N/A |
| `NOTE-PARA-01` | `Parachute deployment (optional for RnD UAV)` / `Igniter` ($\times 2$) | Parachute deployment — Igniters: Pyrotechnic devices responsible for burning the wire that holds the payload bay cover, where the parachute is installed. | Configuration: `optional for RnD UAV`; Igniter Power: `Power 50V` ($\times 2$) |
| `NOTE-EXT-01` | `External Interface board (USB/ETH)` | External interface board: Responsible for connecting to the UAV's subsystems. | Interfaces: `USB`, `ETH` (`USB/ETH`) |
| `CONSTRAINT-HARNESS-01` | `Power meter` to `EPS module` Harness | Physical wire length callout on `Batt Power` harness | $970\text{ cm}$ (`Batt Power 970cm wire`) |
| `CONSTRAINT-HARNESS-02` | `Autopilot computing board` to `Power meter` Harness | Physical wire length callout on `CAN 1` main trunk | $970\text{ cm}$ (`CAN 1 970cm wire`) |
| `CONSTRAINT-HARNESS-03` | `CAN 1 Power Meter Junction Node` to `CAN 1 Fins Splitter Junction Node` Harness | Physical wire length callout on `CAN 1` branch to `Fins` | $150\text{ cm}$ (`CAN 1 150cm wire`) |
| `CONSTRAINT-HARNESS-04` | `CAN 1 Fins Splitter Junction Node` to `Servos #1`–`#4` Harnesses | Physical wire length callouts on all four `CAN 1` fin servo branches | $120\text{ cm}$ ($4\times$ `CAN 1 120 cm wire`) |

---

## 4. Verbatim Transcription of Drawing Legend ("Main component functions")

### Autopilot stack module ASTK A5 V2.5
* **Autopilot computing board + sensors**: Responsible for main UAV control logic, flight stabilization and navigation. Provides attitude, position and kinematics estimation from fusing internal end external sensor data.
* **EPS (electronic power system) module**: Responsible for providing different power levels to the UAV's subsystems
* **ETH switch**: Responsible for interfacing different aircraft system which use IP network for communication.
* **RPI**: Responsible for interfacing between aircraft systems and SC2 command and control software.
* **GNSS module**: Responsible for providing absolute position and velocity estimates from received GNSS signal data.
* **GNSS Antenna**: Responsible for receiving GNSS satellite signals.

### Propulsion
* **Battery**: Responsible for storing and supplying the electrical power required for UAV flight.
* **Automotive Fuse ($200\text{ A}$)**: Provides protection in the event of a short circuit in the main power line.
* **Power Meter**: Responsible for controlling the UAV's ON/OFF state. When the UAV R.B.F. key is removed, the UAV is switched ON. Provides battery voltage and current metrics to the autopilot.
* **ESC (Electronic Speed Controller)**: Responsible for controlling motor speed. It converts the battery's DC power into the appropriate three-phase electrical signals required to drive the motors.
* **Motor**: Converts electrical power into mechanical power to generate thrust.

### Fins
* **Servo #1-#4**: Responsible for UAV pitch and yaw control. The UAV does not bank during turns like conventional UAVs; instead, it performs skid turns using yaw. All four fins are mixed to provide both pitch and yaw control.

### Wings
* **Servo #5-#8**: Responsible for UAV roll stabilization. The UAV continuously stabilizes its roll to maintain a level attitude relative to the horizon. During yaw turns, the UAV does not roll; instead, it maintains a level attitude and performs a horizontal skid turn.

### Pito tube
* Responsible for measuring airspeed. Has in-built heating and drainage.

### Magnetometer
* Responsible for measuring the UAV's heading. The current magnetometer modules also include barometric sensors, which are used for altitude estimation.

### Gimbal
* Responsible for IR/RGB camera sensor pointing and stabilization.

### Camera compute module
* Responsible for controlling the gimbal, providing video feed, target tracking, filtered gimbal kinematic measurements, and target position estimation based on provided UAV position data.

### Radio module
* Responsible for receiving command and control data, while transmitting telemetry and video.

### Radio Antenna
* Responsible for transmitting and receiving radio signals to and from the radio module.

### Lethal package
* **ESAD (Electronic Safe and Arm Device)**: is a high-voltage, all-electronic safety device used to control in-line the initiation sequence of a pyrotechnic train on warhead modules. Essentially, it is a safety device used to prevent the accidental arming or firing of a pyrotechnic event by eliminating system sensitivities to environmental stimuli, such as electromagnetic fields, electrostatic discharge, and stray voltages.
* **ESAD R.B.F Key**: Responsible for ensuring the safe arming sequence of the ESAD. It must be removed according to the specific arming sequence of the ESAD
* **Proximity sensor**: Responsible for sending the triggering signal to the ESAD
* **Warhead**: Responsible for explosion

### Parachute deployment
* **Igniters**: Pyrotechnic devices responsible for burning the wire that holds the payload bay cover, where the parachute is installed

### External interface board
* Responsible for connecting to the UAV's subsystems.