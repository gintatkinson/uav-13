| Attribute | Value |
| :--- | :--- |
| **Title** | Operational Information Exchange (Op-Tx) Matrix |
| **Version** | 1.0.0 |
| **Date** | 2026-09-02 |

## 7. Operational Information Exchange (Op-Tx) Matrix

### 7.1 Inter-Node Communication Architecture
The Operational Information Exchange (Op-Tx) architecture defines all mission-critical, control, telemetry, payload, and safety data exchanges between system nodes. The architecture is structured to support deterministic internal bus protocols and wireless RF datalink protocols in compliance with NATO STANAG 4586 Annex B (Data Link Interface).

### 7.2 Operational Information Exchange (Op-Tx) Matrix Table
In accordance with OMG UAF v1.2 / v2.0 Operational Information Views (Op-Tx) and the JSON Schema data contract, the information exchanges are specified with parametric message rates, throughputs, latency bounds, and Design Assurance Levels (DAL):

| Exchange ID | Source Node | Destination Node | Information Element / Payload Description | Message Frequency (f_sample) | Nominal Throughput (Throughput_nom) | Max Latency Bound (tau_max) | Criticality Level (DAL_req) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **OpTx-01** | PrimarySensorSubsystem | ControllerLogicSubsystem | Raw IMU Delta Angles, Delta Velocities, Barometric Static Pressure, Magnetometer Heading | 250 Hz | 512 kbps | 4.0 ms | High (DO-178C DAL-A) |
| **OpTx-02** | ControllerLogicSubsystem | PropulsionActuators | Motor RPM Demands, Actuator Deflection Commands, Current Limiter Flags | 250 Hz | 256 kbps | 2.0 ms | High (DO-178C DAL-A) |
| **OpTx-03** | GNSSReceiverNode | NavigationFilterSubsystem | Multi-Constellation Satellite PVT Solution, Carrier Phase Residuals, RAIM Integrity Status | 10 Hz | 128 kbps | 20.0 ms | High (DO-178C DAL-A) |
| **OpTx-04** | OpticalPayloadNode | EdgeVisionProcessor | Raw Video Stream Frames, Timestamp Metadata, Radiometric Thermal Matrix | 60 Hz | 1.2 Gbps | 16.0 ms | Low (DO-178C DAL-D) |
| **OpTx-05** | EdgeVisionProcessor | TelemetryTransceiver | Encoded Video Stream (H.265), Target Bounding Boxes, Feature Detections, KLV Geospatial Metadata | 30 Hz | 8.0 Mbps | 33.0 ms | Medium (DO-178C DAL-C) |
| **OpTx-06** | TelemetryTransceiver | GroundControlStation | Downlink Consolidated Flight Telemetry (Attitude, Altitude, Energy SoC, Link Quality, Geofence Margin) | 20 Hz | 2.0 Mbps | 50.0 ms | Medium (DO-178C DAL-B) |
| **OpTx-07** | GroundControlStation | ControllerLogicSubsystem | Uplink C2 Flight Commands, Dynamic Waypoint Updates, ROE Arming Keys, Manual Override Vectors | 50 Hz | 256 kbps | 50.0 ms | High (DO-178C DAL-A) |
| **OpTx-08** | SafetyWatchdogNode | TerminationPyrotechnic | Hardware Flight Abort Trigger, Emergency Recovery Deploy Signal, Power Bus Isolation Strobe | Event-Driven (1000 Hz) | 64 kbps | 5.0 ms | Critical (DO-254 DAL-A) |

### 7.3 Network Quality of Service (QoS) & Protocol Stack Allocation
To guarantee latency bounds and prevent message collisions across operational buses:
1. **Critical Avionics Bus:** Transports `OpTx-01`, `OpTx-02`, and `OpTx-03` over CAN FD and dual-redundant SPI with deterministic priority arbitration; worst-case bus utilization is restricted to $\le 45\%$ under peak load.
2. **Payload & Vision Bus:** Dedicated high-bandwidth PCIe Gen3 and Gigabit Ethernet channels carrying `OpTx-04` and `OpTx-05` logically and electrically isolated from the safety-critical flight control network.
3. **Wireless C2 Datalink:** Authenticated AES-256 encrypted datalink incorporating Forward Error Correction (FEC) and dynamic channel switching across PACE communication tiers (`OpTx-06`, `OpTx-07`).
4. **Safety Watchdog Discrete Line:** Isolated hardware discrete signal path for `OpTx-08` with dual-switch interlocks to eliminate false-trigger risks while providing guaranteed sub-millisecond actuation ($t_{\mathrm{actuate}} \le 5.0\text{ ms}$).
