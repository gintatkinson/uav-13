# Interface Control Document (ICD)

For Electronic Safe and Arm Device (ESAD)

Board-Level Prototype

For the Integration onto UDS's Avenger 3 UAV

to Excalibur International

## CONTENTS

1 GENERAL -- 5
1.1 SCOPE -- 5
1.2 SYSTEM DEFINITION -- 5
1.3 ESAD OPERATIONAL FLOW SEQUENCE -- 6
1.4 ESAD INTERFACES -- 8
1.4.1 Electrical Interface -- 8
1.4.1.1 J100 Connector on ESAD Board -- 10
1.4.1.2 J102 Connector on ESAD Board -- 10
1.4.1.3 J401 Connector on ESAD Board -- 12
1.4.2 Necessary Mating Connector Pinouts -- 12
1.4.3 Cabling Between ESAD Board J102 Connector and Sensor Board J1 Connector -- 13
1.4.4 ESAD Power Interface -- 14
1.4.5 ESAD Discrete Input/Continuity Signal Interface -- 14
1.4.6 Communication Interface -- 14
1.4.6.1 RS-485 Datalink Definition -- 14
1.4.6.1.1 Physical Layer -- 14
1.4.6.1.2 RS-485 Bus Message Structure -- 15
1.4.6.1.3 CRC Calculation -- 16
1.4.6.2 RS-485 Command & Response (Suggested as Draft) -- 17
1.4.6.2.1 Power-On BIT Command (PBIT) -- 17
1.4.6.2.2 Exchange Command -- 19
1.4.6.2.3 Welcome Message -- 24
1.4.6.2.4 Version Command -- 24
1.4.6.2.5 HighVoltage Command -- 26
1.4.7 Mechanical Interface -- 28
1.4.7.1 ESAD Board Mounting Interfaces -- 28
1.4.7.2 Sensor Board Mounting Interfaces -- 28
1.4.7.3 Proximity Sensor Board Dimension -- 32

## FIGURES

Figure 1: ESAD Board System Interfaces -- 5
Figure 2: ESAD Operational Block Diagram -- 6
Figure 3: ESAD Software Flowchart -- 7
Figure 4: ESAD Board Connectors -- 9
Figure 5: ESAD Board Connectors -- 9
Figure 6: Sensor Board Connectors -- 10
Figure 7: ESAD Board J100 16-Pin Mating Connector Pinout -- 12
Figure 8: ESAD Board J102 10-Pin Mating Connector Pinout -- 12
Figure 9: Sensor Board J1 8-Pin Mating Connector Pinout -- 13
Figure 10 Mounting Interfaces on ESAD Board -- 28
Figure 11 Mounting Interfaces on Sensor Board -- 28
Figure 12: Detonator Integration -- 29
Figure 13: Detonator Integration -- 29
Figure 14: Detonator Integration -- 30
Figure 15: ESAD Board Pyhsical Characteristics -- 31
Figure 16 Proximity Sensor Board Pyhsical Characteristics -- 32

## TABLES

Table 1 J100 Connector Suggested Pinout -- 10
Table 2 J012 Connector Suggested Pinout -- 11
Table 3 J401 Connector Pinout -- 12
Table 4 ESAD Power Input -- 14
Table 5 ESAD Discrete Input and Continuity Signals -- 14
Table 6 Communication Specifications -- 15
Table 7 Bit Sequence -- 15
Table 8 Message Structure -- 16

## ABBREVIATIONS

BIT : Built-In Test
EFI : Exploding Foil Initiator
ESAD : Electronic Safe and Arm Device
HEX : Hexadecimal
IO : Input Output
LEEFI : Low Energy Exploding Foil Initiator
LSB : Least-Significant Bit
MSB : Most-Significant Bit
NA : Not Applicable
OC : Onboard Computer
UAV : Unmanned Air Vehicle

## 1 GENERAL

### 1.1 SCOPE

This document defines and controls the interfaces between the Electronic Safe and Arm Device
(ESAD) and the UAV platform for integration of a HE warhead. It establishes the technical and
operational interface parameters, describing both electrical and mechanical (and where applicable,
software) interactions. The goal is to ensure safe, secure, and reliable functioning of the warhead's
ESAD, including the incorporation of proximity and impact switch functionalities, throughout the
system's lifecycle.

### 1.2 SYSTEM DEFINITION

In general, an electronic safe and arm device is a high-voltage, all-electronic safety device used to
control in-line the initiation sequence of a pyrotechnic train on warhead modules. Essentially, it is
a safety device used to prevent the accidental arming or firing of a pyrotechnic event by eliminating
system sensitivities to environmental stimuli, such as electromagnetic fields, electrostatic
discharge, and stray voltages.

Here the Artron's offered generic Electronic Safe and Arm Device (ESAD) solution provides safety
critical energetic systems initiation on command, when commanded for warhead operations and
activates the warhead upon impact. Designed for applications where a reliable arming and firing
sequence with precise timing events is vital. The ESAD described here is compatible with the EFI
/ LEEFI type detonator. Depending on the final chosen detonator manufacturer, mechanical
interface with the detonator part is subject to revision.

ESAD has Input Power interface and Communication interfaces with Onboard Computer / Flight
Control Computer. It has also interfaces with Umbilical connection, warhead LEEFI detonator and
proximity sensor sub-units.

[Figure 1: ESAD Board System Interfaces]

The key features of the ESAD can be listed as follows:

- Design compatible with STANAG 4187 – Fuze Safety Design Requirements
- Design compatible with MIL-STD-461 for EMI/EMC.
- Customizable safety logic, safe separation timers, break wires, acceleration set points, and I/O configurations
- Alternative mechanical packaging options in coordination with the upper System's designers.
- Proximity sensor board should be placed in front face of the upper system, separated from the ESAD unit.
- High dynamic and thermal environmental qualification heritage
- Internal high voltage generation for Low Energy Exploding Foil Initiators
- Static and dynamic switches for safety checks
- Power on self-test and arm status outputs

### 1.3 ESAD OPERATIONAL FLOW SEQUENCE

Main Operational Flowchart for ESAD is given in below Figure. Draft version of the detailed ESAD
Operational Flow Sequence is given show in figure.

[Figure 2: ESAD Operational Block Diagram]

[Figure 3: ESAD Software Flowchart]

### 1.4 ESAD INTERFACES

#### 1.4.1 Electrical Interface

This section describes the electrical interfaces of ESAD and Sensor Boards. There are discrete
signals between ESAD and Onboard Computer (communication and discrete input), Umbilical
connection (if available) and LEEFI detonator. Also there is an interface for ESAD Board and
Sensor Board

ESAD Board has three dedicated interface connectors (J100 for System, J102 for Sensor Board,
J401 for Detonator) and one reserved connector (J101). Pinout tables are as shown in the section
below. NA pins are not used for the generic configuration, but can be used in accordance with the
system design when necessary. Depending on the system design of the main platform that the
ESAD will be integrated onto, it is always possible to revise the interfaces and operational sequence
of the ESAD.

[Figure 4: ESAD Board Connectors]

[Figure 5: ESAD Board Connectors]

Sensor Board has one USER dedicated interface connector (J1 for ESAD Board) and one
ARTRON reserved connector (J2). Pinout tables are as shown in the section below.

[Figure 6: Sensor Board Connectors]

##### 1.4.1.1 J100 Connector on ESAD Board

J100 connector on ESAD Board is used for System interface connector. The mating connector
model number is G125-2241696F1 and crimps model number is G125-0020005 from Harwin.

**Table 1 J100 Connector Suggested Pinout**

| Pin No | Signal Name | Description |
|---|---|---|
| 1 | VDC_IN | ESAD Power Input |
| 2 | VDC_IN | ESAD Power Input |
| 3 | GND | Common Ground |
| 4 | GND | Common Ground |
| 5 | UMB | Umbilical Continuity Line. |
| 6 | UMB_RTN | Umbilical Continuity Return Line. |
| 7 | NA | - |
| 8 | NA | - |
| 9 | RS485_AB_P | RS-485 Communication Interface (Differential Positive Line) |
| 10 | RS485_AB_N | RS-485 Communication Interface (Differential Negative Line) |
| 11 | EXT_RS485_P | RS-485 Communication Interface (Differential Positive Line) (Spare) |
| 12 | EXT_RS485_N | RS-485 Communication Interface (Differential Negative Line) (Spare) |
| 13 | DSC_IN1 | Arm Enable Discrete Input Signal. |
| 14 | DSC_IN2 | Discrete Input 2 |
| 15 | DSC_OUT1 | Discrete Output 1 |
| 16 | DSC_OUT2 | Discrete Output 2 |

##### 1.4.1.2 J102 Connector on ESAD Board

J102 connector on ESAD Board is used for Sensor Board interface connector. The mating
connector model number is G125-2241096F1 and crimps model number is G125-0020005 from
Harwin.

**Table 2 J012 Connector Suggested Pinout**

| Pin No | Signal Name | Description |
|---|---|---|
| 1 | DIST_SPARE | Spare Line |
| 2 | DIST_COMM1 | Communication Line (UART RX) (Receiver for ESAD) |
| 3 | DIST_COMM2 | Communication Line (UART TX) (Transmitter for ESAD) |
| 4 | IRQ_L | Sensor Trigger Signal |
| 5 | NA | - |
| 6 | VOUT | Sensor Board Power |
| 7 | VOUT | Sensor Board Power |
| 8 | GND | Common Ground |
| 9 | GND | Common Ground |
| 10 | NA | - |

##### 1.4.1.3 J401 Connector on ESAD Board

J401 connector on ESAD Board is used for detonator custom interface.

**Table 3 J401 Connector Pinout**

| Pin No | Signal Name | Description |
|---|---|---|
| 1,2,3 | HV_OUT | High Voltage |
| 5,6,7 | HV_GND | High Voltage Ground |
| 4,8 | NA | - (Pins removed) |

#### 1.4.2 Necessary Mating Connector Pinouts

ESAD Board's J100 mating connector (Harwin / G125-2241696F1) pinout is given below.

[Figure 7: ESAD Board J100 16-Pin Mating Connector Pinout]

ESAD Board's J102 mating connector (Harwin / G125-2241096F1) pinout is given below.

[Figure 8: ESAD Board J102 10-Pin Mating Connector Pinout]

Sensor Board's J1 mating connector (Molex / 501330-0800) pinout is given below.

[Figure 9: Sensor Board J1 8-Pin Mating Connector Pinout]

#### 1.4.3 Cabling Between ESAD Board J102 Connector and Sensor Board J1 Connector

The cabling between Sensor Board J1 Connector and ESAD Board J102 connector should be
made due to the table below. Pinout information of mating connectors are given with Figure 9 and
Figure 8.

| Sensor Board J1 Mating Connector (Molex / 501330-0800) |  | Cable AWG | ESAD Board J102 Mating Connector (Harwin / G125-2241096F1) |  |
|---|---|---|---|---|
| Pin # | Signal Name |  | Pin # | Signal Name |
| 1 | DIST_SPARE | 28AWG | 1 | DIST_SPARE |
| 2 | IR_ESAD_L | 28AWG | 4 | IRQ_L |
| 3 | DIST_COMM2 | 28AWG | 2 | DIST_COMM1 |
| 4 | DIST_COMM1 | 28AWG | 3 | DIST_COMM2 |
| 5 | GND | 28AWG | 9 | GND |
| 6 | GND | 28AWG | 8 | GND |
| 7 | 5V0 | 28AWG | 7 | VOUT |
| 8 | 5V0 | 28AWG | 6 | VOUT |
| - | - | 28AWG | 5* | - |
| - | - | 28AWG | 10* | - |

(\*) There should be cables on ESAD Board J102 mating connector's 5th and 10th pins but these
two cables should not be connected to Sensor Board side mating connector. These two cables
should be isolated and terminated in the middle. After all the crimps inserted to the housing epoxy
should be applied to Harwin / G125-2241096F1 back side.

#### 1.4.4 ESAD Power Interface

There is a power interface between the ESAD and the GE that enables the ESAD to perform its
defined functions. The suggested signal characteristics defined for this interface are shown below.

**Table 4 ESAD Power Input**

| Signal Name | Description | Source | Target | Level |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  | Min. | Nominal | Max. |
| GE_POW | Power Input of ESAD | Missile | ESAD | 14V | 28V | 32V |

#### 1.4.5 ESAD Discrete Input/Continuity Signal Interface

ESAD has a continuity circuit line and one discrete input lines to control the flow. The table below
contains the directions and characteristics of these suggested signals.

**Table 5 ESAD Discrete Input and Continuity Signals**

| Signal Name | Description | Source | Target | Level |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  | Min. Voltage | Max. Voltage |
| UMB | Continuity | ESAD | ESAD | Resistance | <0.5 Ohm (22-28AWG) 20mA current |  |
| DSC_IN1 | Arm Enable PWM Signal 1ms period %50 duty cycle 2 square wave | OC | ESAD | LOW | 0VDC | 0.7VDC |
|  |  |  |  | HIGH | 2.5V | 3.3VDC |

#### 1.4.6 Communication Interface

##### 1.4.6.1 RS-485 Datalink Definition

###### 1.4.6.1.1 Physical Layer

ESAD will use RS-485 interface to communicate with the Onboard Computer. Data will be sent and
received over RS-485 electrical signals according to the protocol specified in the next section. The
specifications of this layer are given in Table 6.

**Table 6 Communication Specifications**

| Spec. Type | Value |
|---|---|
| Data Bits | 8 |
| Parity | None |
| Start Bit | 1 |
| Stop Bit | 1 |
| Baudrate | 115200bps |
| Communication Mode | Half Duplex / 100Hz Interval commands |

The suggested Bit sequence that is meaningful and descriptive on its own is shown in Table 7.
ESAD will send and receive data in the Bit order shown in Table 7. The Bit sequence size is 10
Bits including the start-stop Bits.

**Table 7 Bit Sequence**

| Bit9 (Last Bit) | Bit8 | Bit7 | Bit6 | Bit5 | Bit4 | Bit3 | Bit2 | Bit1 | Bit0 (First Bit) |
|---|---|---|---|---|---|---|---|---|---|
| Stop Bit | Data Bit (MSB) | Data Bit | Data Bit | Data Bit | Data Bit | Data Bit | Data Bit | Data Bit (LSB) | Start Bit |

A differential line will be used for sending and receiving data. If OC is not sending data, it will remain
in receive mode.

###### 1.4.6.1.2 RS-485 Bus Message Structure

ESAD will operate in slave mode in accordance with the master/slave concept, waiting for
messages to be initiated by the master. ESAD will not send messages unless requested by the
OC. Bus management will be done by the OC.

ESAD will be capable of responding to messages sent from the bus in a 100ms period.

The ESAD will have the capability to send the last Bit of the reply message to the bus within 5 ms
after the last Bit of the message from the external system is received.

In case the message sent from the external system to the ESAD is interrupted, the ESAD will check
the total length of the message to be received, recognize that the message is incomplete and wait
10 ms. If the message is not completed within this time, ESAD does not continue the process and
waits for the next command.

The Bit sequence size is 10 Bits including the start-stop Bits. This is the smallest data package.
These small packages combine to form larger meaningful packages. The structure of the messages
sent by the master or by ESAD will be as shown in Table 8.

**Table 8 Message Structure**

| Message Length | Header | Command | Data | CRC |
|---|---|---|---|---|
| Min. 5 Byte | 1 Byte | 1 Byte | 0-9 Byte | 2 Byte |

"Message Length" indicates the length of the sent message in bytes. A message without data
should have a value of 5 in the Message Length section. The details of the message will be defined
by the finalization of the ESAD electronic board design.

###### 1.4.6.1.3 CRC Calculation

A 16-bit CRC value is added to the end of all ESAD messages . The CRC value is calculated
bitwise according to CRC-16 XModem algorithm with initial value 0x0000 and 0x1021
polynomial.The CRC calculation algorithm to be used is as follows.

[Figure: CRC-16 XModem calculation algorithm (illustration)]

For example, the 16-bit CRC value of the 10-byte sequence consisting of the values [0x10 0x11
0x12 0x13 0x14 0x15 0x16 0x17 0x18 0x19] should be calculated as 0xB987.

##### 1.4.6.2 RS-485 Command & Response (Suggested as Draft)

###### 1.4.6.2.1 Power-On BIT Command (PBIT)

| Command Name | PBIT |
|---|---|
| Command Number | 0x11 |
| Description | This is the message sent by OC to request PBIT result information from ESAD. ESAD sends the requested information to the OC with this message. |
| Pre-Conditions | None |
| Subsequent Conditions | None |

**Command Parameters**

| Message Length | 0x05 |
|---|---|
| Header | 0x01 |

| Data | Type | Offset | Range | Unit | Description |
|---|---|---|---|---|---|
| - | - | - | - | - | - |

| Notes | - |

**Command Response Parameters**

| Message Length | 0x07 |
|---|---|
| Header | 0x02 |

| Data | Type | Offset | Range | Unit | Description |
|---|---|---|---|---|---|
| PBITResult | UINT16 | 0 | [0 ; 2^16-1] | - | ESAD PBIT Command Response |

| Bit No* | Description |
|---|---|
| 0 | 0: PBIT Successful<br>1: PBIT Unsuccessful |
| 1 | 0: Discrete Input 1 (arm enable) Not Active<br>1: Discrete Input 1 (arm enable) Active |
| 2 | Reserved |
| 3 | 0: Safety Switch 1 Not Active<br>1: Safety Switch 1 Active |
| 4 | 0: Dynamic Switch Not Active<br>1: Dynamic Switch Active |
| 5 | 0: Safety Switch 2 Not Active<br>1: Safety Switch 2 Active |
| 6 | 0: Sensor power-up successful<br>1: Sensor power-up unsuccessful |
| 7 | 0: Detonator Connected<br>1: Detonator Disconnected |
| 8 | 0: Umbilical Cord Connected<br>1: Umbilical Cord Disconnected |
| 9* | 0: Impact Switch Trigger Not Active<br>1: Impact Switch Trigger Active |
| 10* | 0: Proximity Sensor Trigger Not Active<br>1: Proximity Sensor Trigger Active |
| 11 | 0: Accelerometer Selftest Successful<br>1: Accelerometer Selftest Unsuccessful |
| 12 | 0: High Voltage Not Detected (< 50 V)<br>1: High Voltage Detected (>= 50 V) |
| 13 | 0: CPLD Power up Successful<br>1: CPLD Power up Unsuccessful |
| 14-15** | Reserved |

\* Proximity Sensor and Impact Switch Triggers are Ored on the sensor board, and the FPGA receives them as a single trigger input. 9th Bit 10th Bit will have the same value.

\*\*Bit 0-LSB, Bit 15-MSB

| Note | None |

###### 1.4.6.2.2 Exchange Command

| Command Name | EXCHANGE |
|---|---|
| Command Number | 0x10 |
| Description | It is the command sent by the OC to the ESAD to receive data related to the flight and navigation |
| Pre-Conditions | None |
| Subsequent Conditions | None |

**Command Parameters**

| Message Length | 0x08 |
|---|---|
| Header | 0x01 |

| Data | Type | Offset | Range | Unit | Description |
|---|---|---|---|---|---|
| OC_Status | UINT8 | 0 | [0 ; 2^8-1] | - |  |
| SimAccelerationOffset | INT16 | 1 | [0;2^16-1] | 0.0039g | The most significant 3 bits are reserved. The remaining 13 bits represent a signed two's complement value, with a resolution of 0.0039 g/LSB |

| Bit No* | Description |
|---|---|
| 0 | 0: Health Mode<br>1: Fault Mode |
| 1 | 0: Flight Mode<br>1: Simulation Mode |
| 2 | 0: Arm Not Enable<br>1: Arm Enable |
| 3 | 0: Mission Abort Not Enable<br>1: Mission Abort Enable |
| 4 | 0: Arm Abort Not Enable<br>1: Arm Abort Enable |
| 5 | 0: OC Trigger Not Enable<br>1: OC Trigger Enable |
| 6-7** | Reserved |

\*\*Bit 0-LSB, Bit 7-MSB

| Note | None |

**Command Response Parameters**

| Message Length | 0x0E |
|---|---|
| Header | 0x02 |

| Data | Type | Offset | Range | Unit | Description |
|---|---|---|---|---|---|
| Flowstatus | UINT16 | 0 | [0 ; 2^16-1] | - |  |
| ArmState | UINT8 | 2 | [0 ; 2^8-1] | - |  |
| FaultStates | UINT16 | 3 | [0 ; 2^16-1] | - |  |
| FlightTimer | UINT16 | 5 | [0;2^16-1] | s | Flight Timer (s) |
| Acceleration | INT16 | 7 | [0;2^16-1] | 0.0039g | The most significant 3 bits are reserved. The remaining 13 bits represent a signed two's complement value, with a resolution of 0.0039 g/LSB |

**Flowstatus Bit Definitions**

| Bit No* | Description |
|---|---|
| 0 | 0: Arm Counter Not Started<br>1: Arm Counter Started |
| 1 | 0: Flight Counter Not Started<br>1: Flight Counter Started |
| 2 | 0: Flight Mode<br>1: Simulation Mode |
| 3 | 0: Safe Distance Not Exceed<br>1: Safe Distance Exceed |
| 4 | 0: Mission Not Aborted<br>1: Mission Aborted |
| 5 | 0: Detonator Disconnected<br>1: Detonator Connected |
| 6 | 0: Umbilical Cord Disconnected<br>1: Umbilical Cord Connected |
| 7 | 0: Arm Enable Not Received<br>1: Arm Enable Received |
| 8 | 0: Acceleration Not Exceed<br>1: Acceleration Exceed |
| 9 | 0: OC Trigger Not Received<br>1: OC Trigger Received |
| 10* | 0: Proximity Sensor or Impact Switch Not Triggered<br>1: Proximity Sensor or Impact Switch Triggered |
| 11 | 0: Proximity Sensor Not Powered<br>1: Proximity Sensor Powered |
| 12 | 0: Arm Not Aborted<br>1: Arm Aborted |
| 13-15** | Reserved |

\* Proximity Sensor and Impact Switch Triggers are Ored on the Proximity Sensor Board, and the FPGA receives them as a single trigger input.

\*\*Bit 0-LSB, Bit 15-MSB

**ArmState Bit Values**

| Bit No* | Value & Description |
|---|---|
| 0-2 | 0: Safe State<br>1: Arm Stage1 State<br>2: Arm Stage2 State<br>3: Armed State<br>4: Fired State<br>5: Fault State |
| 3-7 | Reserved |

\*Bit 0-LSB, Bit 7-MSB

**FaultStates Bit Definitions**

| Bit No* | Description |
|---|---|
| 0 | 0: ESAD Health State<br>1: ESAD Fault State |
| 1 | 0: PBIT Successful<br>1: PBIT Unsuccessful |
| 2 | 0: Safe Distance Successful<br>1: Safe Distance Unsuccessful |
| 3 | 0: OC Health State<br>1: OC Fault State |
| 4 | 0: Discrete Arm Enable Not Received<br>1: Discrete Arm Enable Received** |
| 5 | 0: Safety Switch 1 No Error<br>1: Safety Switch 1 Error |
| 6 | 0: Safety Switch 2 No Error<br>1: Safety Switch 2 Error |
| 7 | 0: Dynamic Switch No Error<br>1: Dynamic Switch Error |
| 8 | 0: High Voltage No Error<br>1: High Voltage Error |
| 9-15* | Reserved |

\*Bit 0-LSB, Bit 15-MSB

\*\* Discrete Arm Received Before Arm Stage 2

###### 1.4.6.2.3 Welcome Message

| Command Name | WELCOME |
|---|---|
| Command Number | 0xB0 |
| Description | This is the boot message that ESAD sends to the OC at startup. |
| Pre-Conditions | None |
| Subsequent Conditions | None |

**Command Parameters**

| Message Length | 0x05 |
|---|---|
| Header | 0x01 |

| Data | Type | Offset | Range | Unit | Description |
|---|---|---|---|---|---|
| - | - | - | - | - | - |

**Command Response Parameters**

| Message Length | 0x0C |
|---|---|
| Header | 0x02 |

| Data | Type | Offset | Range | Unit | Description |
|---|---|---|---|---|---|
| data[1x7] | UINT8 | 0 |  | - | This is the one-way message information that ESAD sends at startup in ASCII format ("WELCOME") |

| Note | None |

###### 1.4.6.2.4 Version Command

| Command Name | VERSION |
|---|---|
| Command Number | 0x13 |
| Description | This is the message sent by the OC to request embedded firmware version information from ESAD. |
| Pre-Conditions | None |
| Subsequent Conditions | None |

**Command Parameters**

| Message Length | 0x05 |
|---|---|
| Header | 0x01 |

| Data | Type | Offset | Range | Unit | Description |
|---|---|---|---|---|---|
| - | - | - | - | - | - |

| Note | None |

**Command Response Parameters**

| Message Length | 0x0B |
|---|---|
| Header | 0x02 |

| Data | Type | Offset | Range | Unit | Description |
|---|---|---|---|---|---|
| version[1x6] | UINT8 | 0 | [0,255] | - | Format; XXXYYY XXX: FPGA Firmware version (HEX) YYY: CPLD Firmware version (HEX) It will be terminated as \0 |

| Note | None |

###### 1.4.6.2.5 HighVoltage Command

| Command Name | HIGHVOLTAGE |
|---|---|
| Command Number | 0x12 |
| Description | This is the message sent by the OC to request high voltage value and states information from ESAD. |
| Pre-Conditions | None |
| Subsequent Conditions | None |

**Command Parameters**

| Message Length | 0x05 |
|---|---|
| Header | 0x01 |

| Data | Type | Offset | Range | Unit | Description |
|---|---|---|---|---|---|
| - | - | - | - | - | - |

| Note | None |

**Command Response Parameters**

| Message Length | 0x08 |
|---|---|
| Header | 0x02 |

| Data | Type | Offset | Range | Unit | Description |
|---|---|---|---|---|---|
| High_Voltage_Flags | UINT8 | 0 | [0 ; 2^8-1] | - |  |
| High_Voltage_Value | UINT16 | 1 | [0,1800] | V | Resolution : 1V/LSB |

**High_Voltage_Flags Bit Definitions**

| Bit No* | Description |
|---|---|
| 0 | 0: SS1 Not Enabled<br>1: SS1 Enabled |
| 1 | 0: SS1 Not Sensed<br>1: SS1 Sensed |
| 2 | 0: SS2 Not Enabled<br>1: SS2 Enabled |
| 3 | 0: SS2 Not Sensed<br>1: SS2 Sensed |
| 4 | 0: DS Not Enabled<br>1: DS Enabled |
| 5 | 0: DS Not Sensed<br>1: DS Sensed |
| 6 | 0: Charger Not Enabled<br>1: Charger Enabled |
| 7 | 0: HV Not Charged<br>1: HV Charged |

\*Bit 0-LSB, Bit 15-MSB

| Note | None |

#### 1.4.7 Mechanical Interface

Since the payload and the ESAD will be located inside a sealed enclosure on the main drone
platform, it has been decided that the ESAD board will be mounted directly inside that closed
payload compartment on the drone, without an additional mechanical housing. The ESAD board
dimensions are shown below, and the screw/fastening standard to be used for the mechanical
interface will be agreed.

##### 1.4.7.1 ESAD Board Mounting Interfaces

There are three M3 mounting holes on ESAD Board for the mechanical connection interface. The
other 3 big holes on ESAD board is reserved for ARTRON and should not be used by USER.

[Figure 10 Mounting Interfaces on ESAD Board]

##### 1.4.7.2 Sensor Board Mounting Interfaces

There are two M2 mounting holes on Sensor Board for the mechanical connection interface.

[Figure 11 Mounting Interfaces on Sensor Board]

The following figures shows the detonator integration.

[Figure 12: Detonator Integration]

[Figure 13: Detonator Integration]

[Figure 14: Detonator Integration]

[Figure 15: ESAD Board Pyhsical Characteristics]

##### 1.4.7.3 Proximity Sensor Board Dimension

In addition to ESAD unit, the proximity sensor board is given in below in Error! Reference source
not found.. This board should be placed onto the front face of the upper system.

[Figure 16 Proximity Sensor Board Pyhsical Characteristics]

The field of view (FOV) that must be maintained from the sensor lens vertically and horizontally is
as follows.

[Figure: Proximity sensor lens field of view (FOV) requirement, vertical and horizontal (specified in the figure)]
