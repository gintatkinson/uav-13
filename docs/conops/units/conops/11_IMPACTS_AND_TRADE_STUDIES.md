| Attribute | Value |
| :--- | :--- |
| **Title** | Operational Impacts, System Limitations & Documented Trade Studies |
| **Version** | 1.0.0 |
| **Date** | 2026-09-02 |

## 11. Operational Impacts, System Limitations & Documented Trade Studies

### 11.1 Operational Workflow & Deployment Impacts
The transition from legacy manual piloting systems to the Tactical UAS introduces substantial positive impacts across operational workflows:
1. **Reduced Crew Staging Footprint:** The operational crew footprint required to maintain continuous surveillance is minimized through supervisory automation (1 Remote Pilot in Command supervisory operator and 1 Payload Operator).
2. **Automated Launch & Mission Staging:** Pre-flight preparation time is compressed to $t_{\mathrm{prep}} \le 10.0\text{ min}$ due to automated digital PBIT routines and tool-less modular interfaces.
3. **Automated Airspace Authorization:** Integration with U-space / UTM service providers automates digital flight plan filing, dynamic geo-zone deconfliction, and electronic conspicuity broadcast.

### 11.2 Organizational Roles & Training Impacts
- **Operator Reskilling:** The primary operator role transitions from continuous manual flight control to supervisory systems management, airspace deconfliction, and tactical payload exploitation.
- **Formal Training Syllabus:** Personnel complete a certified 40-hour training syllabus covering STANAG 4586 UCS software operations, human-in-the-loop emergency matrix execution, and SORA risk buffer monitoring.
- **Maintenance Specialization:** Maintenance technicians transition from purely mechanical repairs to digital bus diagnostics (CAN FD analysis, optical boresight alignment, and cryptographic key loading).

### 11.3 System Limitations & Operational Boundaries
While the system provides robust multi-mission capability, formal operational boundaries and statutory constraints must be observed:
- **Maximum Operational Ceiling:** $120.0\text{ m}$ AGL ($h_{\mathrm{operating\_ceiling}} = 120.0\text{ m}$) in accordance with civil and tactical airspace authorizations.
- **Operational C2 Radius:** $15.0\text{ km}$ ($R_{\mathrm{C2}} = 15.0\text{ km}$) line-of-sight communications range from the primary GCS antenna mast.
- **Flight Endurance:** Flight endurance of $90.0\text{ min}$ ($t_{\mathrm{endurance\_nominal}} = 90.0\text{ min}$) under standard atmospheric conditions; adjusts to $70.0\text{ min}$ at the minimum operating temperature limit $-40^\circ\text{C}$.
- **Maximum Takeoff Weight:** Maximum Takeoff Weight of $25.0\text{ kg}$ ($m_{\mathrm{MTOW}} = 25.0\text{ kg}$) with a dedicated mission payload capacity of $5.0\text{ kg}$ ($m_{\mathrm{payload}} = 5.0\text{ kg}$).
- **Severe Weather Constraints:** Flight is prohibited in atmospheric icing conditions exceeding liquid water content $\text{LWC} = 0.5\text{ g/m}^3$ or convective weather exceeding maximum steady wind limits of $15.0\text{ m/s}$ ($20.0\text{ m/s}$ gusts).

### 11.4 Documented Engineering Trade Studies
To establish the optimal architectural configuration, three formal engineering trade studies were conducted across physical, electrical, and computational design spaces:

#### Trade Study 1: Propulsion & Energy Storage Architecture
- **Objective:** Select energy storage chemistry balancing cold-weather performance at $-40^\circ\text{C}$, gravimetric energy density, and cycle lifetime.
- **Options Evaluated:**
  - Option A: High-Discharge LiPo Chemistry Cells (180 Wh/kg, severe capacity degradation at sub-zero temperatures).
  - Option B: High-Capacity Cylindrical 21700 Li-ion Chemistry with Integrated Thermal Heating Jackets (250 Wh/kg, robust cold-weather discharge with active BMS thermal management).
  - Option C: Solid-State Battery Cells (350 Wh/kg, developmental TRL-4 and prohibitive unit acquisition cost).
- **Decision:** **Option B (High-Capacity 21700 Li-ion Chemistry with Heating Jackets)** was selected. It provides optimal energy density ($250\text{ Wh/kg}$), robust low-temperature performance down to $-40^\circ\text{C}$, and verified 500+ cycle life.

| Metric / Parameter | Option A: High-Discharge LiPo | Option B: 21700 Li-ion + Heat (Selected) | Option C: Solid-State Cells |
| :--- | :--- | :--- | :--- |
| **Gravimetric Energy Density** | 180 Wh/kg | 250 Wh/kg (Selected) | 350 Wh/kg |
| **Cold Temperature Performance** | Degraded (< 50% at -20 deg C) | Nominal (>= 85% at -40 deg C with heat) | Degraded discharge rate |
| **Cycle Lifetime** | 200 cycles | 500 cycles | < 150 cycles |
| **Technology Readiness Level (TRL)** | TRL-9 (Mature) | TRL-8 (Production) | TRL-4 (Developmental) |
| **Unit Pack Cost Impact** | Baseline | +15% Moderate | +300% High |

#### Trade Study 2: Edge Neural Compute vs High-Bandwidth Datalink Compression
- **Objective:** Determine balance between onboard edge AI processing and raw sensor downlink transmission.
- **Options Evaluated:**
  - Option A: Raw Video Streaming with Centralized Ground Station AI Processing (Requires high-power RF link with 1.2 Gbps throughput demand, vulnerable to jamming).
  - Option B: Onboard Edge Neural Inference Accelerator (NVIDIA Jetson Orin NX) with Dynamic H.265 Compression (Requires $15\text{ W}$ onboard power budget, downlink throughput compressed to $8.0\text{ Mbps}$).
- **Decision:** **Option B (Onboard Edge AI Processing)** was selected. Edge processing ensures autonomous object tracking and geo-tagging continue uninterrupted even during datalink degradation or lost-link return phases.

#### Trade Study 3: Autonomous Parachute Recovery vs Airframe Propulsion Redundancy
- **Objective:** Achieve JARUS SORA v2.5 Mitigation M2 ground risk reduction (reducing kinetic impact severity to $E_k \le 34.0\text{ J}$).
- **Options Evaluated:**
  - Option A: Hexarotor / Octocopter Propulsion Motor Redundancy (Provides single-motor-out capability; does not mitigate catastrophic structural failure or complete power bus loss).
  - Option B: Integrated Autonomous Ballistic Parachute Recovery Subsystem with Fast Pyrotechnic Deployment and Motor Cutoff Interlock (Ensures descent velocity $v_{\mathrm{impact}} \le 1.65\text{ m/s}$ and impact energy $E_k \le 34.0\text{ J}$).
- **Decision:** **Option B (Autonomous Ballistic Parachute Subsystem)** was selected. It provides certified SORA M2 High-Integrity containment credit and guarantees ground impact risk reduction ($GRC-3 \rightarrow GRC-2$).
