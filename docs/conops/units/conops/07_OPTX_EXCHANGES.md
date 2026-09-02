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
| **OpTx-01** | PrimarySensorSubsystem | ControllerLogicSubsystem | Primary Inertial Telemetry (Raw IMU Delta Angles Δθ, Delta Velocities Δv, Barometric Static Pressure, Magnetometer Heading) | 250 Hz | 512 kbps | 4.0 ms | High (DO-178C DAL-A) |
| **OpTx-02** | ControllerLogicSubsystem | PropulsionActuators | Flight Actuator Commands (Motor RPM Demands, Control Surface Deflections, Current Limiter Flags) | 250 Hz | 256 kbps | 2.0 ms | High (DO-178C DAL-A) |
| **OpTx-03** | GNSSReceiverNode | NavigationFilterSubsystem | Multi-GNSS Satellite PVT & RAIM Integrity Stream (Carrier Phase Residuals, Ephemeris, Fix Quality) | 10 Hz | 128 kbps | 20.0 ms | High (DO-178C DAL-A) |
| **OpTx-04** | OpticalPayloadNode | EdgeVisionProcessor | Raw High-Bandwidth Video & Radiometric Thermal Matrix (Uncompressed Frames, Timestamp Metadata) | 60 Hz | 1.2 Gbps | 16.0 ms | Low (DO-178C DAL-D) |
| **OpTx-05** | EdgeVisionProcessor | TelemetryTransceiver | Encoded Video (H.265) & KLV MISB 0601 Metadata Stream (Bounding Boxes, Real-Time Target Tracks) | 30 Hz | 8.0 Mbps | 33.0 ms | Medium (DO-178C DAL-C) |
| **OpTx-06** | TelemetryTransceiver | GroundControlStation | Downlink Consolidated Flight Telemetry (Attitude, Altitude, Energy SoC, Link Quality, Geofence Margin) | 20 Hz | 2.0 Mbps | 50.0 ms | Medium (DO-178C DAL-B) |
| **OpTx-07** | GroundControlStation | ControllerLogicSubsystem | Uplink C2 Flight Commands & ROE Arming Keys (Dynamic Waypoint Updates, Authorization Tokens) | 50 Hz | 256 kbps | 50.0 ms | High (DO-178C DAL-A) |
| **OpTx-08** | SafetyWatchdogNode | TerminationPyrotechnic | Safety Watchdog Hardware Discrete Strobe & Abort (Emergency Deploy Signal, Bus Isolation Strobe) | Event-Driven (1000 Hz) | 64 kbps | 5.0 ms | Critical (DO-254 DAL-A) |
| **OpTx-09** | DAASensorArray | ControllerLogicSubsystem | Detect and Avoid (DAA) Radar Tracks & ADS-B In Targets (Intruder Range, Bearing, Relative Velocity) | 10 Hz | 256 kbps | 50.0 ms | Medium (DO-178C DAL-B) |
| **OpTx-10** | RemoteIDTransmitter | BroadcastRFEnvironment | Direct RF Remote ID Broadcast (ASTM F3411-22a Message Pack: Serial, Location, Velocity, Timestamp) | 1 Hz | 64 kbps | 100.0 ms | Medium (DO-178C DAL-C) |
| **OpTx-11** | BatteryManagementSystem | PowerDistributionUnit | Smart Battery Management (BMS) Cell Voltages & Thermal Telemetry (Individual Cell V, Current, Temp) | 10 Hz | 64 kbps | 100.0 ms | Medium (DO-178C DAL-B) |
| **OpTx-12** | PrecisionLandingSensor | ControllerLogicSubsystem | Optical Fiducial Landing Guidance & RTK Corrections (Fiducial Tag Relative Pose, Carrier Corrections) | 20 Hz | 128 kbps | 25.0 ms | High (DO-178C DAL-A) |
| **OpTx-13** | UTMGatewayNode | GroundControlStation | U-space / UTM Dynamic Geo-Zone Update Ingestion (Dynamic Corridors, Temporary Flight Restrictions) | 1 Hz | 128 kbps | 500.0 ms | Medium (DO-178C DAL-C) |
| **OpTx-14** | GSEHealthMonitor | GroundControlStation | Ground Support Equipment (GSE) Diagnostic Health Bus (Battery Charger Status, Tether Tension, Mast Health) | 5 Hz | 128 kbps | 200.0 ms | Low (DO-178C DAL-D) |
| **OpTx-15** | SatcomRelayNode | EmergencyRescueCenter | Emergency Satellite Relay (Iridium SBD / Geo-Beacon Telemetry: Last Known Position, Crash Beacon) | 0.1 Hz | 2.4 kbps | 5.0 s | Medium (DO-178C DAL-B) |
| **OpTx-16** | IndependentTerminationUnit | BallisticParachuteActuator | Pyrotechnic Parachute Squib & Flight Termination Strobe (Direct Solid-State Squib Firing Pulse) | Event-Driven | 16 kbps | 1.0 ms | Critical (DO-254 DAL-A) |

### 7.3 Network Quality of Service (QoS) & Protocol Stack Allocation
To guarantee latency bounds and prevent message collisions across operational buses:
1. **Critical Avionics & Actuation Bus (CAN FD / SPI):** Transports `OpTx-01`, `OpTx-02`, `OpTx-03`, `OpTx-11`, and `OpTx-12` over dual-redundant CAN FD (1 Mbps arbitration / 5 Mbps data) and isolated high-speed SPI with deterministic priority arbitration; worst-case bus utilization is restricted to $\le 45\%$ under peak flight loads.
2. **Payload, Vision & Tracking Bus (PCIe Gen3 / GbE):** Dedicated high-bandwidth PCIe Gen3 and Gigabit Ethernet channels carrying `OpTx-04`, `OpTx-05`, and `OpTx-09` logically and electrically isolated from the safety-critical flight control network.
3. **Wireless C2 & Telemetry Datalinks:** Authenticated AES-256 encrypted datalinks incorporating Forward Error Correction (FEC) and dynamic frequency hopping across PACE communication tiers (`OpTx-06`, `OpTx-07`).
4. **Broadcast & Electronic Conspicuity:** Conforms to ASTM F3411-22a broadcasting direct Remote ID (`OpTx-10`) over simultaneous Bluetooth 5.0 Long Range and Wi-Fi Beacon channels.
5. **External Interfaces & Ground Support Bus:** Ingests dynamic U-space/UTM geo-zone restrictions (`OpTx-13`) via secure TLS/HTTPS REST/WebSocket APIs, while GSE diagnostic telemetry (`OpTx-14`) is monitored over RS-485 / Ethernet field interfaces.
6. **Safety Watchdog & Pyrotechnic Flight Termination Paths:** Isolated hardware discrete signal lines and independent solid-state firing circuits for `OpTx-08`, `OpTx-15` (emergency Iridium SBD satellite relay), and `OpTx-16` (pyrotechnic squib trigger) ensuring sub-millisecond activation latency ($\tau \le 1.0\text{ ms}$) immune to main flight processor crashes.
