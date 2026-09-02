| Attribute | Value |
| :--- | :--- |
| **Title** | Tactical Mission Intent: Multi-Domain Threat Matrix |
| **Version** | 1.0.0 |
| **Date** | 2026-09-02 |

## 4. Threat & Electronic Warfare (EW) / Cyber Environment Matrix

In accordance with MIL-STD-882E (§4.3), NATO STANAG 4586, and JARUS SORA v2.5, the Tactical UAS operates across contested, multi-domain operating environments. The threat matrix establishes deterministic autonomous mitigation rules spanning all operational threat domains: Kinetic, Mechanical, Propulsion / Power / Thermal, Environmental, Electronic Warfare, and Cybersecurity / OT.

| Threat ID | Domain | Threat Vector | Technical Description | Severity | Detection Mechanism | Autonomous Mitigation Rule | Public Clause Citation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `THR-KIN-01` | Kinetic | Cooperative Air Collision | Transponder/ADS-B equipped intruder penetrating DAA Well-Clear volume (DMOD = 1200.0 m, HSEP <= 137.0 m, tau_mod <= 35.0 s) | Catastrophic | Dual ADS-B In receiver + TCAS correlation filter (latency <= 1.0 s) | Autonomous horizontal heading escape Delta psi >= 15 deg or vertical rate climb/descent >= 500 ft/min | RTCA DO-365B §2.2.4 |
| `THR-KIN-02` | Kinetic | Non-Cooperative Air Collision | Non-broadcasting airborne hazard closing on collision trajectory without active beacon | Catastrophic | Airborne primary radar + EO/IR multi-spectral sensor fusion tracker (latency <= 2.0 s) | Emergency tactical break maneuver; dynamic vertical/horizontal separation outside track horizon | RTCA DO-365B §2.2.5.3 |
| `THR-KIN-03` | Kinetic | Operational Geofence Escape | Kinematic drift or navigation bias driving vehicle across 3D containment boundary into unsegregated airspace | Critical | Simplex RTA dynamic geofence barrier monitor evaluating boundary proximity (latency <= 50 ms) | Simplex RTA safe-turn override (180 deg course reversal); if containment breached > 2.0 s, triggers emergency motor cutoff | JARUS SORA v2.5 Annex E §E.14 |
| `THR-KIN-04` | Kinetic | High-Energy Ground Impact | Uncontrolled kinetic energy descent over populated ground risk buffer resulting in critical surface strike | Catastrophic | Continuous vertical rate and attitude accelerometer divergence monitor (latency <= 20 ms) | Autonomous ballistic parachute deployment (ASTM F3322-18) constraining terminal impact energy E_impact <= 34.0 J | JARUS SORA v2.5 Annex B §B.2 |
| `THR-MEC-01` | Mechanical | Actuator Jam & Hardover | Servo gear fracture, mechanical binding, or resolver sensor loss causing flight control surface freeze or hardover | Critical | Dual-lane resolver disparity check and motor drive current monitor (latency <= 20 ms) | Split-surface clutch disengagement; differential thrust and paired aileron/elevon re-trimming to maintain wings-level | MIL-STD-1629A §4.3 |
| `THR-MEC-02` | Mechanical | Structural Airframe Failure | Carbon composite delamination, structural wing spar fracture, or rotor blade shedding from aerodynamic flutter | Catastrophic | High-frequency 3-axis vibration FFT analysis and aerodynamic roll/pitch rate divergence (latency <= 10 ms) | Immediate thrust shutdown on faulted arm, multi-rotor asymmetrical mixer recalculation; emergency parachute deployment | MIL-STD-1629A §4.3 |
| `THR-MEC-03` | Mechanical | Parachute Ejection Jam | Pyrotechnic initiator squib open-circuit, mechanical mortar barrel jam, or spring latch freeze | Catastrophic | Continuous bridge-wire squib continuity test and optical deployment sensor (latency <= 5 ms) | Dual-redundant independent pyrotechnic cutters with secondary pneumatic backup release circuit | MIL-STD-882E Task 205 §4.2 |
| `THR-PWR-01` | Power / Thermal | Battery Thermal Runaway | Internal dendrite growth or mechanical puncture inducing catastrophic exothermic reaction (T_cell > 65 deg C, V_cell < 2.8 V) | Catastrophic | Active Smart BMS multi-node thermistor and voltage monitoring at 100 Hz (latency <= 10 ms) | Active BMS string disconnection, auxiliary reserve power engagement, maximum thrust limit reduction, forced emergency descent | JARUS SORA v2.5 Annex E §E.24 |
| `THR-PWR-02` | Power / Thermal | ESC Inverter Phase Loss | High-current thermal breakdown in inverter bridge causing single-phase open or short circuit on BLDC motor | Critical | ESC back-EMF zero-crossing detector and phase current comparator (latency <= 5 ms) | Dynamic motor mixer recalculation reallocating thrust authority to remaining operational rotors; executes immediate RTL | SAE ARP4761 §4.3.1 |
| `THR-PWR-03` | Power / Thermal | Main DC Bus Short-to-Ground | 28V DC regulator failure shorting primary power distribution bus rail to ground chassis | Catastrophic | Solid-state eFuse overcurrent sensing and bus voltage dropout monitor (latency <= 50 us) | Dual-isolated diode OR-ing architecture maintains secondary Bus B power; electronic circuit breaker isolates shorted branch | MIL-STD-882E Task 205 §4.2 |
| `THR-ENV-01` | Environmental | Severe Icing Accretion | Supercooled liquid droplet accretion on pitot probes, leading edges, and rotor blades increasing weight and drag | Critical | Dual-pitot dynamic pressure disparity detector + optical ice accretion sensor (latency <= 1.0 s) | Automated resistive electro-thermal leading edge/pitot heater activation; commanded descent out of icing altitude layer | MIL-STD-810H Method 521.4 §4.2 |
| `THR-ENV-02` | Environmental | Wind Shear & Microburst | Sudden localized vertical downdraft (> 10 m/s) and horizontal wind vector inversion destabilizing hover/glide | Critical | High-rate IMU / ADU total energy rate estimator (E_dot_mech < threshold) (latency <= 100 ms) | Total Energy Control System (TECS) pitch-up escape climb with maximum continuous power; aborts landing approach | MIL-STD-810H Method 506.6 §4.2 |
| `THR-ENV-03` | Environmental | Sand & Particulate Ingestion | Blowing sand and fine silica particulate eroding rotor leading edges and infiltrating optical sensor gimbals | Moderate | Motor bearing temperature rise and optical encoder tracking error monitor (latency <= 5.0 s) | Commands gimbal stow/park position; initiates diversion to clean alternate landing zone | MIL-STD-810H Method 510.7 §4.2 |
| `THR-ENV-04` | Environmental | Extreme Temperature Excursion | Ambient temperature outside operational envelope (-40 deg C to +55 deg C) degrading battery discharge capacity | Moderate | Calibrated avionics and battery bay ambient temperature sensors (latency <= 1.0 s) | Pre-flight launch inhibit; in-flight throttle derating and conservative bingo energy recalculation | MIL-STD-810H Method 501.7 / 502.7 |
| `THR-EW-01` | Electronic Warfare | GNSS Jamming | High-power intentional RF noise swamping L1/L2 GNSS receiver frontend, dropping carrier-to-noise ratio | Critical | Receiver AGC attenuation monitor and Jammer-to-Signal (J/S) power estimator (latency <= 200 ms) | Automatic failover to tightly-coupled INS dead-reckoning + optical flow visual odometry; engages GPS-denied contingency hold | MIL-STD-461G §5.18 |
| `THR-EW-02` | Electronic Warfare | GNSS Spoofing | False ephemeris/pseudorange RF signal transmission inducing continuous spatial drift and altitude offset | Critical | Receiver Autonomous Integrity Monitoring (RAIM) + Chi-Square Kalman Filter Innovation residual gating (latency <= 100 ms) | Immediate exclusion of spoofed GNSS signals; lockstep transition to magnetic/visual dead-reckoning; alarms GCS | NIST SP 800-82r3 §4.2 |
| `THR-EW-03` | Electronic Warfare | C2 Link Jamming DoS | Narrowband / swept RF noise jamming directed at primary C2 uplink, degrading signal-to-noise margin | Moderate | Uplink heartbeat loss monitor and Packet Error Rate (PER > 0.05 for 2.0 s) (latency <= 1.0 s) | Automated PACE link switching to 915 MHz FHSS mesh / SATCOM; if unestablished within 5 s, initiates DO-362A Lost-Link RTH | MITRE ATT&CK for ICS §T0814 |
| `THR-EW-04` | Electronic Warfare | HIRF & EMP Pulse | Electromagnetic pulse or radar illumination inducing transient voltage spikes in avionic wiring harnesses | Catastrophic | TVS surge clamp voltage threshold sensors and power rail ripple detectors (latency <= 10 us) | Faradic shielded enclosure, double-braided conduit grounding, TVS clamping diodes shunt transient currents to chassis | MIL-STD-461G §5.4 |
| `THR-CYB-01` | Cybersecurity | Unauthorized Command Injection | Adversary transmitting forged flight mode change, disarm, or waypoint redirect commands over RF uplink | Catastrophic | Ed25519 cryptographic signature verification and high-water mark nonce validation (latency <= 5 ms) | Immediate drop of unauthenticated packets; security alarm dispatch to GCS; temporary uplink source lockout | MITRE ATT&CK for ICS §T0855 |
| `THR-CYB-02` | Cybersecurity | C2 Replay Attack | Intercepting valid legacy command packets and retransmitting during unauthorized operational phase | Critical | Monotonically increasing 64-bit sequence counters + timestamp epoch skew checking (latency <= 5 ms) | Reject stale/replayed packets; increment replay counter; isolate transmitting node if replay burst persists | MITRE D3FEND §D3-MCR |
| `THR-CYB-03` | Cybersecurity | GCS Lateral Compromise | Malware pivot from external internet network to internal GCS flight control bridge and telemetry stream | Critical | Unidirectional data diode flow monitor + zero-trust microsegmentation policy engine (latency <= 50 ms) | Hardware-enforced optical data diode isolates internal C2 bridge; revokes compromised GCS authorization token | NIST SP 800-82r3 §5.3 |
| `THR-CYB-04` | Cybersecurity | Firmware & Bus Tamper | Flashing unauthorized autopilot bootloader or injecting anomalous frame IDs onto internal CAN/Ethernet bus | Catastrophic | Hardware Root of Trust (TPM 2.0 / Secure Boot) + CAN ID message frequency / payload rate anomaly monitor (latency <= 10 ms) | Secure Boot halts execution on hash mismatch; CAN bus firewall isolates compromised transceiver node | ISO/SAE 21434 §9.4 |

---

### 4.1 Kinetic Threat Domain Formulations & Mitigation Profiles

#### 4.1.1 THR-KIN-01: Cooperative Air Collision
- **Detection Threshold:** Horizontal distance $D_{\mathrm{horizontal}} \le 1200.0\text{ m} \land |H_{\mathrm{vertical}}| \le 137.0\text{ m} \land \tau_{\mathrm{mod}} \le 35.0\text{ s}$
- **Primary Sensing Hardware & Algorithm:** Dual 1090 MHz Extended Squitter / 978 MHz UAT ADS-B In receiver array coupled with TCAS kinematic track correlation and modified tau closest point of approach (CPA) projection filter.
- **Deterministic Autonomous Mitigation Sequence:**
  - **Step 1 (Trajectory Computation):** Compute optimal Well-Clear escape vector issuing minimum $\Delta \psi \ge 15.0^\circ$ heading deflection or $\dot{z} \ge 500.0\text{ ft/min}$ climb/descent rate.
  - **Step 2 (Guidance Override):** Simplex RTA preempts baseline mission trajectory and loads reactive avoidance waypoint into the primary flight guidance controller within $\le 50.0\text{ ms}$.
  - **Step 3 (Intent Broadcast):** Transmit immediate dynamic traffic advisory to GCS and broadcast revised intent vector over Direct RF Remote ID.
  - **Verification:** Continuous sensor fusion verifies horizontal separation $D \ge 1200.0\text{ m}$ and vertical separation $|H| \ge 137.0\text{ m}$ maintained for $\ge 10.0\text{ s}$ before resuming nominal mission flight plan.
- **Public Clause Citation:** RTCA DO-365B §2.2.4

#### 4.1.2 THR-KIN-02: Non-Cooperative Air Collision
- **Detection Threshold:** Non-broadcasting radar/optical target track with $d_{\mathrm{CPA}} \le 800.0\text{ m} \land t_{\mathrm{CPA}} \le 25.0\text{ s} \land |h_{\mathrm{rel}}| \le 100.0\text{ m}$
- **Primary Sensing Hardware & Algorithm:** 77 GHz FMCW airborne phased-array radar paired with multi-spectral EO/IR optical tracking sensor executing Hungarian association and Unscented Kalman Filter (UKF) kinematic state estimation.
- **Deterministic Autonomous Mitigation Sequence:**
  - **Step 1 (Tactical Break):** Execute immediate reactive tactical turn ($30.0^\circ$ bank angle turn) away from the target line-of-sight vector.
  - **Step 2 (Sensor Slew):** Command payload optical tracking gimbal to slave to target coordinates to maintain continuous track lock during avoidance maneuvering.
  - **Step 3 (Airspace Rescan):** Re-scan forward 120° azimuth sector to ensure the escape trajectory does not create secondary collision geometry.
  - **Verification:** Sensor fusion verifies relative target range rate $dd/dt > 0$ with distance expanding beyond $1200.0\text{ m}$ for $\ge 10.0\text{ s}$.
- **Public Clause Citation:** RTCA DO-365B §2.2.5.3

#### 4.1.3 THR-KIN-03: Operational Geofence Escape
- **Detection Threshold:** Distance to 3D operational geofence boundary $d_{\mathrm{boundary}} \le 50.0\text{ m}$ or predicted time-to-boundary traversal $t_{\mathrm{breach}} \le 3.0\text{ s}$
- **Primary Sensing Hardware & Algorithm:** Dual-channel Simplex Run-Time Assurance (RTA) safety monitor executing ray-casting point-in-polygon containment checks against onboard 3D boundary polygon at $50\text{ Hz}$.
- **Deterministic Autonomous Mitigation Sequence:**
  - **Step 1 (Simplex Intervention):** Simplex RTA hardware gate trips, disconnecting unverified mission planner and commanding maximum-rate wings-level $180.0^\circ$ turn-around.
  - **Step 2 (Speed Regulation):** Derate forward airspeed to minimum turning radius velocity $v_{\mathrm{min\_turn}} = 14.0\text{ m/s}$ to minimize containment excursion.
  - **Step 3 (Termination Gate):** If vehicle position remains outside 3D boundary for $t > 2.0\text{ s}$, trigger emergency motor cutoff and parachute deployment.
  - **Verification:** EKF navigation state confirms vehicle position interior to boundary with spatial clearance $d_{\mathrm{boundary}} \ge 100.0\text{ m}$.
- **Public Clause Citation:** JARUS SORA v2.5 Annex E §E.14

#### 4.1.4 THR-KIN-04: High-Energy Ground Impact
- **Detection Threshold:** Uncontrolled vertical descent rate $\dot{z} < -8.0\text{ m/s} \land \theta_{\mathrm{pitch}} < -45.0^\circ \land \Delta h_{\mathrm{AGL}}/\Delta t < -10.0\text{ m/s}$ or dual-engine propulsion failure
- **Primary Sensing Hardware & Algorithm:** Triple-redundant MEMS accelerometers, barometric altimeter, and FMCW radar altimeter coupled with discrete kinetic energy rate estimator.
- **Deterministic Autonomous Mitigation Sequence:**
  - **Step 1 (Motor Cutoff):** Force hardware-level PWM disarm on all Electronic Speed Controllers within $\le 10.0\text{ ms}$ to stop rotor rotation.
  - **Step 2 (Parachute Ejection):** Fire ASTM F3322-18 compliant pyrotechnic mortar canopy ejection circuit within $\le 20.0\text{ ms}$.
  - **Step 3 (Airbag & Beacon):** Deploy lower airframe impact absorption airbags and activate 406 MHz COSPAS-SARSAT emergency beacon.
  - **Verification:** Deceleration profile confirms terminal descent velocity $v_{\mathrm{terminal}} \le 4.5\text{ m/s}$ and impact kinetic energy $E_{\mathrm{impact}} \le 34.0\text{ J}$.
- **Public Clause Citation:** JARUS SORA v2.5 Annex B §B.2

---

### 4.2 Mechanical Threat Domain Formulations & Mitigation Profiles

#### 4.2.1 THR-MEC-01: Actuator Jam & Hardover
- **Detection Threshold:** Commanded vs measured flight surface deflection error $|\delta_{\mathrm{cmd}} - \delta_{\mathrm{act}}| > 5.0^\circ$ for $t > 100.0\text{ ms}$ or motor driver stall current $I_{\mathrm{act}} > 4.5\text{ A}$ for $t > 50.0\text{ ms}$
- **Primary Sensing Hardware & Algorithm:** Dual-channel resolver / optical shaft encoders and high-side shunt current monitors executing analytic redundancy parity equations.
- **Deterministic Autonomous Mitigation Sequence:**
  - **Step 1 (Clutch Disengagement):** De-energize electromagnetic clutch on the jammed servo to prevent rigid aerodynamic surface lock.
  - **Step 2 (Aerodynamic Re-Trim):** Flight computer reconfigures control allocation matrix, utilizing differential motor thrust and paired split-surface ailerons to compensate for roll/pitch bias.
  - **Step 3 (Degraded RTB):** Declare Degraded Flight Mode and command immediate return-to-base on direct ingress corridor.
  - **Verification:** Flight dynamics observer confirms vehicle attitude error $|\theta_{\mathrm{err}}| \le 2.0^\circ$ under reconfigured control laws.
- **Public Clause Citation:** MIL-STD-1629A §4.3

#### 4.2.2 THR-MEC-02: Structural Airframe Failure
- **Detection Threshold:** Accelerometer vibration spectral density $a_{\mathrm{vib}} > 3.5\text{ g RMS}$ in flutter band ($f \in [120, 400]\text{ Hz}$) or uncommanded angular roll acceleration $|\dot{p}| > 180.0^\circ/\text{s}^2$
- **Primary Sensing Hardware & Algorithm:** High-rate (1 kHz) piezoelectric vibration sensors and airframe strain gauges evaluated via onboard Fast Fourier Transform (FFT) spectral energy analyzer.
- **Deterministic Autonomous Mitigation Sequence:**
  - **Step 1 (Asymmetrical Power Cut):** Cut throttle to damaged rotor/arm within $\le 10.0\text{ ms}$ to eliminate destructive rotational resonance.
  - **Step 2 (Mixer Re-allocation):** Recalculate multi-rotor control mixer to sustain level flight using remaining operational rotors.
  - **Step 3 (Emergency Ejection):** If attitude stability cannot be maintained within $t \le 500.0\text{ ms}$, fire emergency ballistic parachute.
  - **Verification:** Structural vibration drops below $0.8\text{ g RMS}$ or ballistic parachute inflation confirmed via optical canopy switch.
- **Public Clause Citation:** MIL-STD-1629A §4.3

#### 4.2.3 THR-MEC-03: Parachute Ejection Jam
- **Detection Threshold:** Primary pyrotechnic squib ignition pulse confirmed without canister separation signal within $t_{\mathrm{deploy}} > 300.0\text{ ms}$
- **Primary Sensing Hardware & Algorithm:** Bridge-wire continuity monitor + micro-switch mortar status contacts + optical parachute canister exit detector.
- **Deterministic Autonomous Mitigation Sequence:**
  - **Step 1 (Secondary Squib Fire):** Fire independent Channel B pyrotechnic squib across isolated secondary circuit within $\le 5.0\text{ ms}$.
  - **Step 2 (Pneumatic Release):** Puncture high-pressure CO2 pneumatic backup ejection cartridge.
  - **Step 3 (Aerodynamic Deep Stall):** Command full elevator pitch-up flare to enter controlled aerodynamic deep-stall and bleed kinetic energy.
  - **Verification:** Optical canister exit sensor confirms full canopy deployment and line stretch within $\le 500.0\text{ ms}$.
- **Public Clause Citation:** MIL-STD-882E Task 205 §4.2

---

### 4.3 Power, Propulsion & Thermal Threat Domain Formulations & Mitigation Profiles

#### 4.3.1 THR-PWR-01: Battery Thermal Runaway
- **Detection Threshold:** Battery cell temperature $T_{\mathrm{cell}} \ge 65.0^\circ\text{C}$ or heating rate $dT_{\mathrm{cell}}/dt \ge 1.5^\circ\text{C/s}$ or cell voltage $V_{\mathrm{cell}} \le 2.8\text{ V}$ under nominal load
- **Primary Sensing Hardware & Algorithm:** Multi-point NTC thermistor matrix on every cell pair coupled with Smart BMS cell voltage telemetry sampled at $100\text{ Hz}$.
- **Deterministic Autonomous Mitigation Sequence:**
  - **Step 1 (String Isolation):** Solid-state power switch disconnects the compromised battery pack string within $\le 10.0\text{ ms}$.
  - **Step 2 (Auxiliary Power Engagement):** Secondary isolated auxiliary battery bus assumes avionics and flight computer power loads.
  - **Step 3 (Emergency Descent):** Throttle propulsion to maximum glide descent angle and execute forced touchdown at nearest clear terrain.
  - **Verification:** Faulted string current reads $I_{\mathrm{string}} == 0.0\text{ A}$ and avionics bus voltage stabilizes at $V_{\mathrm{bus}} \ge 22.0\text{ V}$.
- **Public Clause Citation:** JARUS SORA v2.5 Annex E §E.24

#### 4.3.2 THR-PWR-02: ESC Inverter Phase Loss
- **Detection Threshold:** Phase current imbalance $\Delta I_{\mathrm{phase}} > 15.0\text{ A}$ or back-EMF zero-crossing detection failure for $> 3$ consecutive electrical cycles
- **Primary Sensing Hardware & Algorithm:** Electronic Speed Controller (ESC) shunt current amplifiers and hardware back-EMF zero-crossing comparator circuits.
- **Deterministic Autonomous Mitigation Sequence:**
  - **Step 1 (Bridge De-energize):** Disable gate drive PWM to faulted inverter bridge within $\le 5.0\text{ ms}$ to prevent power MOSFET cross-conduction.
  - **Step 2 (Dynamic Thrust Re-allocation):** Flight controller updates motor mixing matrix to redistribute thrust and torque across active rotors.
  - **Step 3 (Direct RTL):** Abort active mission objectives and command direct straight-line Return-to-Launch.
  - **Verification:** Telemetry confirms zero current on faulted phase and stable vehicle attitude ($\theta_{\mathrm{err}} \le 2.0^\circ$).
- **Public Clause Citation:** SAE ARP4761 §4.3.1

#### 4.3.3 THR-PWR-03: Main DC Bus Short-to-Ground
- **Detection Threshold:** DC bus voltage drop $V_{\mathrm{bus}} < 18.0\text{ V}$ with simultaneous bus current surge $I_{\mathrm{bus}} > 120.0\text{ A}$ ($dI/dt > 1000.0\text{ A/ms}$)
- **Primary Sensing Hardware & Algorithm:** Solid-state electronic circuit breakers (eFuses) and high-speed Hall-effect current sensors with hardware comparator circuits.
- **Deterministic Autonomous Mitigation Sequence:**
  - **Step 1 (eFuse Trip):** Solid-state eFuse trips, opening faulted power rail branch within $\le 50.0\,\mu\text{s}$.
  - **Step 2 (Diode OR-ing Backup):** Dual-isolated diode OR-ing architecture transfers critical avionics loads to redundant Bus B.
  - **Step 3 (Load Shedding):** Automatically shed high-power non-essential payload systems and initiate emergency recovery.
  - **Verification:** Bus B voltage stabilizes at $V_{\mathrm{bus,B}} \ge 24.0\text{ V}$ with nominal current draw.
- **Public Clause Citation:** MIL-STD-882E Task 205 §4.2

---

### 4.4 Environmental Threat Domain Formulations & Mitigation Profiles

#### 4.4.1 THR-ENV-01: Severe Icing Accretion
- **Detection Threshold:** Pitot dynamic pressure disparity $|q_1 - q_2| > 15.0\text{ Pa}$ or optical sensor ice thickness $\delta_{\mathrm{ice}} \ge 1.0\text{ mm}$ or aerodynamic drag rise $\Delta C_D > 20\%$
- **Primary Sensing Hardware & Algorithm:** Dual heated pitot-static probes, resonant optical surface ice accretion sensors, and real-time aircraft drag polar observer.
- **Deterministic Autonomous Mitigation Sequence:**
  - **Step 1 (Electro-Thermal De-Ice):** Energize leading-edge resistive heater elements and pitot de-ice coils at $100\%$ duty cycle within $\le 100.0\text{ ms}$.
  - **Step 2 (Altitude Escape):** Command descent out of the supercooled droplet icing inversion layer ($h_{\mathrm{cmd}} = h_{\mathrm{current}} - 300.0\text{ m}$).
  - **Step 3 (Airspeed Margin Boost):** Increase target cruising airspeed by $+15\%$ to maintain stall safety margin.
  - **Verification:** Optical ice sensor confirms $\delta_{\mathrm{ice}} < 0.2\text{ mm}$ and pitot disparity converges to $< 3.0\text{ Pa}$.
- **Public Clause Citation:** MIL-STD-810H Method 521.4 §4.2

#### 4.4.2 THR-ENV-02: Wind Shear & Microburst
- **Detection Threshold:** Vertical downdraft velocity $w_{\mathrm{down}} > 10.0\text{ m/s}$ or total mechanical energy rate degradation $\dot{E}_{\mathrm{mech}} = \dot{h} + (v/g)\dot{v} < -3.0\text{ m/s}$
- **Primary Sensing Hardware & Algorithm:** High-rate IMU and Air Data Unit (ADU) coupled with Total Energy Control System (TECS) longitudinal energy observer.
- **Deterministic Autonomous Mitigation Sequence:**
  - **Step 1 (Max Power Application):** Command maximum continuous propulsion power ($P_{\mathrm{cmd}} = P_{\mathrm{max}}$) within $\le 50.0\text{ ms}$.
  - **Step 2 (Optimal Pitch Angle):** Pitch up to best climb angle speed ($V_x$) while clamping maximum angle of attack $\alpha \le \alpha_{\mathrm{stall}} - 3.0^\circ$.
  - **Step 3 (Approach Abort):** Abort landing approach or loiter orbit and climb out along clear emergency escape corridor.
  - **Verification:** Vehicle establishes positive climb rate $\dot{z} \ge +2.0\text{ m/s}$ sustained for $\ge 5.0\text{ s}$.
- **Public Clause Citation:** MIL-STD-810H Method 506.6 §4.2

#### 4.4.3 THR-ENV-03: Sand & Particulate Ingestion
- **Detection Threshold:** Motor bearing temperature rise $\Delta T_{\mathrm{bearing}} > 15.0^\circ\text{C}$ above ambient or optical gimbal encoder friction torque increase $> 50\%$
- **Primary Sensing Hardware & Algorithm:** Embedded motor bearing thermistors and brushless gimbal motor drive torque estimation observer.
- **Deterministic Autonomous Mitigation Sequence:**
  - **Step 1 (Gimbal Stow):** Command optical sensor gimbal to sealed aerodynamic STOW/PARK position to shield optical lenses.
  - **Step 2 (Avionics Positive Pressure):** Increase positive-pressure filtered air purge across internal avionics bay.
  - **Step 3 (Alternate Divert):** Divert to paved secondary recovery landing zone to minimize ground sand ingestion during touchdown.
  - **Verification:** Gimbal park position switch confirmed; motor bearing temperatures stabilize within normal bounds ($T \le 75.0^\circ\text{C}$).
- **Public Clause Citation:** MIL-STD-810H Method 510.7 §4.2

#### 4.4.4 THR-ENV-04: Extreme Temperature Excursion
- **Detection Threshold:** Ambient temperature $T_{\mathrm{amb}} < -40.0^\circ\text{C}$ or $T_{\mathrm{amb}} > +55.0^\circ\text{C}$ or battery core temperature $T_{\mathrm{core}} < 0.0^\circ\text{C}$
- **Primary Sensing Hardware & Algorithm:** Calibrated RTD temperature sensors across external airframe, avionics compartment, and battery core.
- **Deterministic Autonomous Mitigation Sequence:**
  - **Step 1 (Launch Inhibit):** Pre-launch: Assert hardware launch inhibit; activate internal battery core pre-heaters if cold-soaked.
  - **Step 2 (In-Flight Derating):** In-flight: Derate peak continuous motor current by $20\%$ if over-temperature; open ram-air thermal vents.
  - **Step 3 (Bingo Recalculation):** Dynamically recompute Bingo energy threshold with derated discharge curve ($E_{\mathrm{capacity,eff}} = 0.85 \cdot E_{\mathrm{capacity}}$).
  - **Verification:** Internal electronics and battery temperatures remain within operating envelope ($-20.0^\circ\text{C}$ to $+65.0^\circ\text{C}$).
- **Public Clause Citation:** MIL-STD-810H Method 501.7 / 502.7

---

### 4.5 Electronic Warfare (EW) Threat Domain Formulations & Mitigation Profiles

#### 4.5.1 THR-EW-01: GNSS Jamming
- **Detection Threshold:** Carrier-to-Noise density ratio $C/N_0 < 28.0\text{ dB-Hz}$ across all tracked GNSS satellites or RF frontend AGC attenuation $> 30.0\text{ dB}$ (Jammer-to-Signal $J/S > 15.0\text{ dB}$)
- **Primary Sensing Hardware & Algorithm:** Multi-band GNSS receiver RF frontend AGC monitor + satellite carrier-to-noise tracking filter.
- **Deterministic Autonomous Mitigation Sequence:**
  - **Step 1 (GNSS Measurement Gate):** Flag GNSS measurements untrusted and decouple satellite observation matrix from navigation EKF within $\le 50.0\text{ ms}$.
  - **Step 2 (VIO Odometry Transition):** Transition navigation state propagation to tightly-coupled INS + downward optical flow visual-inertial odometry.
  - **Step 3 (Contingency Navigation):** Engage GPS-denied loiter holding pattern or execute dead-reckoning return along pre-computed clear route.
  - **Verification:** Navigation state covariance norm remains bounded ($\|\mathbf{P}_{\mathrm{cov}}\| \le 1.5\text{ m}$) with zero discontinuous state jumps.
- **Public Clause Citation:** MIL-STD-461G §5.18

#### 4.5.2 THR-EW-02: GNSS Spoofing
- **Detection Threshold:** Chi-Square innovation residual $\gamma_k = \mathbf{y}_k^T \mathbf{S}_k^{-1} \mathbf{y}_k > 16.27$ ($\chi^2_{0.001, 3}$) or RAIM pseudorange residual error $> 10.0\text{ m}$
- **Primary Sensing Hardware & Algorithm:** Multi-constellation Receiver Autonomous Integrity Monitoring (RAIM) + EKF innovation residual gating filter + dual-antenna carrier phase disparity detector.
- **Deterministic Autonomous Mitigation Sequence:**
  - **Step 1 (Pseudorange Rejection):** Immediately reject and isolate spoofed satellite signals from flight computer navigation filters within $\le 20.0\text{ ms}$.
  - **Step 2 (Magnetic / Optical Lock):** Revert navigation reference to magnetic heading, barometric altitude, and visual odometry.
  - **Step 3 (GCS Alert):** Dispatch spoofing incident alert with RF spectrum capture to GCS and initiate return-to-home.
  - **Verification:** EKF innovation residual returns to nominal statistical bounds ($\gamma_k \le 7.81$) under pure visual-inertial state estimation.
- **Public Clause Citation:** NIST SP 800-82r3 §4.2

#### 4.5.3 THR-EW-03: C2 Link Jamming DoS
- **Detection Threshold:** Primary C2 datalink Packet Error Rate $\mathrm{PER} > 0.05$ for $t > 1.0\text{ s}$ or heartbeat loss duration $\Delta t_{\mathrm{loss}} \ge 1.0\text{ s}$
- **Primary Sensing Hardware & Algorithm:** Datalink transceiver hardware RSSI/SNR signal-quality detector and frame heartbeat watchdog timer.
- **Deterministic Autonomous Mitigation Sequence:**
  - **Step 1 (PACE Failover Tier 2):** Autonomously switch active C2 transceiver to Alternate 915 MHz FHSS mesh link within $\le 1.0\text{ s}$.
  - **Step 2 (PACE Failover Tier 3):** If Alternate link unavailable after $\tau_{\mathrm{timeout}} \ge 2.0\text{ s}$, failover to Contingency LTE/5G encrypted tunnel.
  - **Step 3 (Lost-Link Execution):** If all C2 tiers lost for $t \ge 5.0\text{ s}$, initiate RTCA DO-362A Lost-Link autonomous RTH profile.
  - **Verification:** Telemetry heartbeat restored on secondary tier or vehicle commences autonomous return transit to recovery base.
- **Public Clause Citation:** MITRE ATT&CK for ICS §T0814

#### 4.5.4 THR-EW-04: High-Intensity Radiated Fields (HIRF) & EMP Pulse
- **Detection Threshold:** Power rail transient voltage surge $V_{\mathrm{spike}} > 36.0\text{ V}$ or induced transient current rate $dI/dt > 500.0\text{ A/}\mu\text{s}$ on internal harnesses
- **Primary Sensing Hardware & Algorithm:** Fast-response Transient Voltage Suppression (TVS) clamp monitoring circuits and Faradic shielded chassis voltage sensors.
- **Deterministic Autonomous Mitigation Sequence:**
  - **Step 1 (Transient Clamping):** High-speed bidirectional TVS diodes clamp transient overvoltage spikes directly to airframe chassis within $\le 1.0\,\text{ns}$.
  - **Step 2 (Optocoupler Isolation):** Galvanic optocouplers isolate signal lines, preventing surge propagation into core microcontroller registers.
  - **Step 3 (Power Bus Recovery):** Power regulation filters reset and stabilize internal power rails without triggering processor lockup.
  - **Verification:** Core avionics power rails (3.3V, 5.0V, 28.0V) stabilize within $\pm 2.0\%$ nominal with zero register corruption.
- **Public Clause Citation:** MIL-STD-461G §5.4

---

### 4.6 Cybersecurity & Operational Technology (OT) Threat Domain Formulations & Mitigation Profiles

#### 4.6.1 THR-CYB-01: Unauthorized Command Injection
- **Detection Threshold:** Cryptographic signature verification failure ($\mathrm{Ed25519\_Verify} == \mathrm{FALSE}$) or HMAC-SHA256 digest mismatch on incoming C2 frame
- **Primary Sensing Hardware & Algorithm:** Hardware Cryptographic Engine (TPM 2.0 / Secure MPU) validating Ed25519 digital signatures on every packet.
- **Deterministic Autonomous Mitigation Sequence:**
  - **Step 1 (Packet Drop):** Instantly drop and discard unauthenticated command frames without passing to the flight executive within $\le 5.0\text{ ms}$.
  - **Step 2 (Security Logging):** Log cryptographic violation incident, source MAC/IP, and signature payload into tamper-evident secure audit log.
  - **Step 3 (Uplink Lockout):** Impose temporary rate-limiting lockout ($t_{\mathrm{lockout}} = 2.0\text{ s}$) on the offending interface and dispatch security alert to GCS.
  - **Verification:** Flight executive confirms $100\%$ of accepted flight commands carry valid, authenticated cryptographic signatures.
- **Public Clause Citation:** MITRE ATT&CK for ICS §T0855

#### 4.6.2 THR-CYB-02: C2 Replay Attack
- **Detection Threshold:** Monotonic 64-bit sequence counter value $N_{\mathrm{rx}} \le N_{\mathrm{high\_water}}$ or packet timestamp epoch skew $|\Delta t_{\mathrm{msg}}| > 50.0\text{ ms}$
- **Primary Sensing Hardware & Algorithm:** Real-time communications stack anti-replay sliding window validator and monotonic hardware counter register.
- **Deterministic Autonomous Mitigation Sequence:**
  - **Step 1 (Replay Drop):** Immediately reject and drop stale, duplicated, or out-of-order command packets within $\le 1.0\text{ ms}$.
  - **Step 2 (Replay Metric Tracking):** Increment replay attack detection counter and log source packet headers in diagnostic memory.
  - **Step 3 (Session Key Rekey):** If replay frequency exceeds 10 frames/sec, trigger automated AES-256 session key re-negotiation over secondary PACE link.
  - **Verification:** Sequence counter high-water mark advances strictly monotonically with zero duplicate command execution.
- **Public Clause Citation:** MITRE D3FEND §D3-MCR

#### 4.6.3 THR-CYB-03: GCS Lateral Compromise
- **Detection Threshold:** Unauthenticated flight plan re-tasking or mode override request lacking dual-officer cryptographic authorization tokens
- **Primary Sensing Hardware & Algorithm:** Hardware-enforced unidirectional optical data diode + Dual-Consent Cryptographic Authorization Policy Engine.
- **Deterministic Autonomous Mitigation Sequence:**
  - **Step 1 (Command Hold):** Freeze execution of incoming re-tasking command; retain current authenticated safe mission plan.
  - **Step 2 (Dual Token Requirement):** Require simultaneous presentation of Mission Commander and Safety Officer Ed25519 cryptographic tokens.
  - **Step 3 (Containment Loiter):** If valid dual tokens are not supplied within $30.0\text{ s}$, transition to autonomous safe loiter and alert authorized GCS terminal.
  - **Verification:** Policy engine confirms dual cryptographic token validation (`SIG_CMD && SIG_SO == TRUE`) prior to unlocking mission changes.
- **Public Clause Citation:** NIST SP 800-82r3 §5.3

#### 4.6.4 THR-CYB-04: Firmware & Bus Tamper
- **Detection Threshold:** Secure Boot cryptographic hash mismatch on bootloader/firmware image ($\mathrm{SHA256} \ne \mathrm{Hash}_{\mathrm{golden}}$) or unauthorized CAN message ID injection
- **Primary Sensing Hardware & Algorithm:** Hardware Root of Trust (TPM 2.0 / ARM TrustZone) + CAN Bus Hardware Firewall with deterministic ID whitelist.
- **Deterministic Autonomous Mitigation Sequence:**
  - **Step 1 (Boot Inhibit / Dual-Bank Fallback):** Secure Boot halts execution upon hash mismatch; reverts to authenticated golden dual-bank flash image within $\le 50.0\text{ ms}$.
  - **Step 2 (Bus Isolation):** CAN hardware firewall isolates and disables the transceiver node injecting unauthorized message IDs.
  - **Step 3 (Hardware Write-Lock):** Hardware write-protect lines assert on all internal flash banks during airborne operations.
  - **Verification:** Bootloader verifies running firmware matches cryptographic golden hash manifest; CAN bus error passive count is 0.
- **Public Clause Citation:** ISO/SAE 21434 §9.4
