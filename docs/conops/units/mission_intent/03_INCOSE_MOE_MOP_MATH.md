| Attribute | Value |
| :--- | :--- |
| **Title** | Tactical Mission Intent: INCOSE MoE & MoP Metrics |
| **Version** | 1.0.0 |
| **Date** | 2026-09-02 |

## 3. Measures of Effectiveness (MoE) & Measures of Performance (MoP) Metrics

In accordance with the INCOSE Systems Engineering Handbook v5.0 (§3.2, §3.3) and NATO STANAG 4586, operational objectives and technical performance parameters are quantitatively characterized through formal Measures of Effectiveness (MoE) and Measures of Performance (MoP).

### 3.1 Mathematical Formulations

#### 3.1.1 Operational Availability ($A_o$)
Operational Availability represents the probability that the system operates satisfactorily at any given point in time under stated conditions in an actual operational environment:

$$
\begin{aligned}
A_o &= \frac{\mathrm{MTBM}}{\mathrm{MTBM} + \mathrm{MDT}} \\
\mathrm{MDT} &= \mathrm{MTTR} + \mathrm{MLDT} + \mathrm{MADT} \\
\mathrm{MTBM} &= \frac{T_{\mathrm{operating}}}{N_{\mathrm{maintenance\_actions}}}
\end{aligned}
$$

Where and Operational Parameters:

| Parameter | Symbol | Units | Constraint / Rule | Description |
| :--- | :--- | :--- | :--- | :--- |
| Operational Availability | A_o | Dimensionless | A_o >= 0.95 | Operational availability probability |
| Mean Time Between Maintenance | MTBM | hr | MTBM >= 150.0 | Mean operating interval between scheduled and unscheduled maintenance actions |
| Mean Down Time | MDT | hr | MDT <= 7.5 | Total non-operational outage duration per maintenance event |
| Mean Time to Repair | MTTR | hr | MTTR <= 1.5 | Active corrective maintenance and component replacement duration |
| Mean Logistics Delay Time | MLDT | hr | MLDT <= 4.0 | Spare parts, battery charging, and ground support supply chain latency |
| Mean Administrative Delay Time | MADT | hr | MADT <= 2.0 | Operational inspection sign-off, logging, and administrative overhead |
| Total Operating Time | T_operating | hr | Cumulative Flight Time | Total logged operational flight and system operating hours |
| Maintenance Action Count | N_maintenance_actions | Count | Integer Count | Total count of unscheduled corrective maintenance interventions |

---

#### 3.1.2 Extended Kalman Filter (EKF) State Covariance & Innovation Residual Gating
The precision of target tracking, vehicle state estimation, and sensor anomaly / spoofing rejection is governed by the discrete-time Extended Kalman Filter (EKF) recursion with Chi-Square innovation gating:

$$
\begin{aligned}
\hat{\mathbf{x}}_{k|k-1} &= \mathbf{f}(\hat{\mathbf{x}}_{k-1|k-1}, \mathbf{u}_k) \\
\mathbf{P}_{k|k-1} &= \mathbf{F}_k \mathbf{P}_{k-1|k-1} \mathbf{F}_k^T + \mathbf{Q}_k \\
\mathbf{y}_k &= \mathbf{z}_k - \mathbf{h}(\hat{\mathbf{x}}_{k|k-1}) \\
\mathbf{S}_k &= \mathbf{H}_k \mathbf{P}_{k|k-1} \mathbf{H}_k^T + \mathbf{R}_k \\
\mathbf{K}_k &= \mathbf{P}_{k|k-1} \mathbf{H}_k^T \mathbf{S}_k^{-1} \\
\hat{\mathbf{x}}_{k|k} &= \hat{\mathbf{x}}_{k|k-1} + \mathbf{K}_k \mathbf{y}_k \\
\mathbf{P}_{k|k} &= (\mathbf{I} - \mathbf{K}_k \mathbf{H}_k) \mathbf{P}_{k|k-1} (\mathbf{I} - \mathbf{K}_k \mathbf{H}_k)^T + \mathbf{K}_k \mathbf{R}_k \mathbf{K}_k^T \\
\gamma_k &= \mathbf{y}_k^T \mathbf{S}_k^{-1} \mathbf{y}_k \le \chi^2_{\alpha, m}
\end{aligned}
$$

Where and Operational Parameters:

| Parameter | Symbol | Units | Constraint / Rule | Description |
| :--- | :--- | :--- | :--- | :--- |
| A Priori State Estimate | x_hat_k\|k-1 | State Vector | Real-Time Dynamic | Predicted system navigation state vector [p, v, q, b_a, b_g]^T |
| A Priori State Covariance | P_k\|k-1 | m^2 | P_k\|k-1 > 0 | Predicted state error covariance matrix |
| State Transition Jacobian | F_k | Dimensionless | Deterministic | Linearized kinematic state transition Jacobian matrix |
| Process Noise Covariance | Q_k | m^2/s^2 | Q_k >= 0 | Sensor and aerodynamic disturbance stochastic process noise matrix |
| Measurement Innovation Residual | y_k | Measurement Vector | E[y_k] = 0 | Disparity between actual sensor observation z_k and predicted observation |
| Innovation Covariance Matrix | S_k | Measurement Units^2 | Positive Definite | Measurement residual error covariance matrix |
| Kalman Gain Matrix | K_k | Dimensionless | Optimal Gain | Minimum-mean-square-error observation weighting matrix |
| Observation Jacobian Matrix | H_k | Dimensionless | Measurement Map | Sensor observation geometry transformation Jacobian matrix |
| Measurement Noise Covariance | R_k | Measurement Units^2 | R_k > 0 | Sensor measurement uncertainty matrix |
| A Posteriori State Covariance | P_k\|k | m^2 | norm(P_cov) <= 1.5 | Updated state error covariance norm |
| Normalized Innovation Squared (NIS) | gamma_k | Dimensionless | gamma_k <= chi2_alpha_m | Chi-Square statistical distance for measurement residual gating |
| Chi-Square Critical Threshold | chi2_alpha_m | Dimensionless | chi2_0.001_3 = 16.27 | Gating threshold for outlier/spoof rejection at alpha=0.001 with 3 DOF |

---

#### 3.1.3 End-to-End C2 Transport Latency ($\tau_{\text{C2}}$) and Packet Delivery Ratio ($\mathrm{PDR}$)
The end-to-end command-and-control communication latency is bounded by the summation of discrete serialization, propagation, and parsing delays:

$$
\begin{aligned}
\tau_{\mathrm{C2}} &= \tau_{\mathrm{encode}} + \tau_{\mathrm{tx}} + \tau_{\mathrm{prop}} + \tau_{\mathrm{rx}} + \tau_{\mathrm{decode}} \\
\tau_{\mathrm{tx}} &= \frac{L_{\mathrm{packet}}}{B_{\mathrm{link}}} \\
\tau_{\mathrm{prop}} &= \frac{d_{\mathrm{LOS}}}{c} \\
\mathrm{PDR} &= \frac{N_{\mathrm{received}}}{N_{\mathrm{transmitted}}}
\end{aligned}
$$

Where and Operational Parameters:

| Parameter | Symbol | Units | Constraint / Rule | Description |
| :--- | :--- | :--- | :--- | :--- |
| Total C2 Transport Latency | tau_C2 | ms | tau_C2 <= 100.0 | Total end-to-end communication latency bound |
| Telemetry Encoding Delay | tau_encode | ms | tau_encode <= 15.0 | Message serialization, framing, and AES-256-GCM encryption latency |
| RF Transmission Delay | tau_tx | ms | tau_tx <= 20.0 | Physical layer packet framing, FEC interleaving, and COFDM modulation delay |
| Packet Length | L_packet | bits | L_packet <= 4096 | C2 command and telemetry payload packet size |
| Physical Link Bitrate | B_link | bps | B_link >= 12.0 Mbps | Primary physical link transmission bit rate |
| Speed-of-Light Propagation Delay | tau_prop | ms | tau_prop <= 0.05 | Speed-of-light propagation over 15.0 km Line-of-Sight RF path |
| Line-of-Sight Standoff Distance | d_LOS | m | d_LOS <= 15000.0 | Slant range distance between GCS and airborne vehicle |
| Physical Speed of Light Constant | c | m/s | c = 299792458.0 | Standard vacuum speed of light constant |
| Reception & Buffer Delay | tau_rx | ms | tau_rx <= 25.0 | Demodulation, preamble sync, CRC check, and DMA buffer transfer |
| Telemetry Decoding Delay | tau_decode | ms | tau_decode <= 15.0 | Decryption, MAC authentication verification, and parser ingestion |
| Packet Delivery Ratio | PDR | Dimensionless | PDR >= 0.98 | Ratio of successfully received and authenticated packets to transmitted |

---

#### 3.1.4 Multi-Spectral Area Coverage Dynamics ($\dot{A}_{\text{cov}}$) and Area Coverage Ratio ($C_{\text{area}}$)
Sensor payload geometric sweeping dynamics over a planar surveillance footprint:

$$
\begin{aligned}
W_{\mathrm{swath}} &= 2 \cdot h_{\mathrm{AGL}} \cdot \tan\left(\frac{\theta_{\mathrm{FOV}}}{2}\right) \\
\dot{A}_{\mathrm{cov}} &= W_{\mathrm{swath}} \cdot v_{\mathrm{ground}} \cdot (1 - \eta_{\mathrm{overlap}}) \\
\dot{A}_{\mathrm{cov}} &= 2 \cdot h_{\mathrm{AGL}} \cdot \tan\left(\frac{\theta_{\mathrm{FOV}}}{2}\right) \cdot v_{\mathrm{ground}} \cdot (1 - \eta_{\mathrm{overlap}}) \\
C_{\mathrm{area}} &= \frac{A_{\mathrm{surveyed}}}{A_{\mathrm{total}}}
\end{aligned}
$$

Where and Operational Parameters:

| Parameter | Symbol | Units | Constraint / Rule | Description |
| :--- | :--- | :--- | :--- | :--- |
| Instantaneous Coverage Rate | A_dot_cov | km^2/min | A_dot_cov >= 0.15 | Instantaneous mapped area per unit time |
| Ground Swath Footprint Width | W_swath | m | W_swath >= 41.4 | Optical sensor cross-track ground footprint width at nominal altitude |
| Altitude Above Ground Level | h_AGL | m | 50.0 <= h_AGL <= 120.0 | Operating altitude above target terrain |
| Payload Field of View Angle | theta_FOV | deg | theta_FOV = 45.0 | Sensor angular optical aperture |
| Ground Speed Velocity | v_ground | m/s | 12.0 <= v_ground <= 22.0 | Operational cruising ground track velocity |
| Swath Overlap Factor | eta_overlap | Dimensionless | eta_overlap = 0.20 | Overlap ratio to eliminate surveillance blind spots |
| Area Coverage Ratio | C_area | Dimensionless | C_area >= 0.90 | Ratio of surveyed area to total mission area |
| Total Surveyed Ground Area | A_surveyed | km^2 | Measured Online | Cumulative unique ground surface area mapped by optical payload |
| Total Mission AOI Area | A_total | km^2 | Mission Defined | Total assigned Area of Interest (AOI) geographic boundary |

---

#### 3.1.5 Complete RF Link Budget Equation & Free Space Path Loss (FSPL)
The RF link budget characterizes transmission robustness, receiver sensitivity, and propagation attenuation over the Line-of-Sight (LOS) communications channel:

$$
\begin{aligned}
P_{\mathrm{rx}} &= P_{\mathrm{tx}} + G_{\mathrm{tx}} + G_{\mathrm{rx}} - \mathrm{FSPL} - L_{\mathrm{misc}} \\
\mathrm{FSPL} &= 20 \log_{10}(d) + 20 \log_{10}(f) + 32.44 \\
\mathrm{SNR}_{\mathrm{rx}} &= P_{\mathrm{rx}} - N_0 - 10 \log_{10}(B_{\mathrm{channel}}) - \mathrm{NF} \\
M_{\mathrm{link}} &= P_{\mathrm{rx}} - P_{\mathrm{sensitivity}}
\end{aligned}
$$

Where and Operational Parameters:

| Parameter | Symbol | Units | Constraint / Rule | Description |
| :--- | :--- | :--- | :--- | :--- |
| Received RF Power | P_rx | dBm | P_rx >= -85.0 | Total received carrier signal power at receiver frontend |
| Transmitter Output Power | P_tx | dBm | P_tx = 30.0 (1.0 W) | Airborne RF transmitter output power |
| Transmitter Antenna Gain | G_tx | dBi | G_tx = 3.0 | Omnidirectional airborne antenna gain |
| Receiver Antenna Gain | G_rx | dBi | G_rx = 12.0 | Directional ground control station tracking antenna gain |
| Free Space Path Loss | FSPL | dB | FSPL <= 131.3 | Geometric free-space path loss over 15.0 km LOS distance at 5.8 GHz |
| Standoff Slant Distance | d | km | d <= 15.0 | Operational slant range distance between transmitter and receiver |
| Carrier RF Frequency | f | MHz | f = 5800.0 | Operating center frequency of primary datalink |
| Miscellaneous Losses | L_misc | dB | L_misc <= 4.0 | Atmospheric absorption, coaxial cable, connector, and polarization losses |
| Thermal Noise Power Density | N_0 | dBm/Hz | N_0 = -174.0 | Thermal noise floor spectral density at standard temperature T = 290 K |
| Channel Bandwidth | B_channel | Hz | B_channel = 10000000.0 | Primary COFDM RF channel bandwidth (10.0 MHz) |
| Receiver Noise Figure | NF | dB | NF <= 4.0 | Receiver frontend low-noise amplifier noise figure |
| Received Signal-to-Noise Ratio | SNR_rx | dB | SNR_rx >= 15.0 | Demodulated carrier signal-to-noise ratio |
| Receiver Sensitivity Threshold | P_sensitivity | dBm | P_sensitivity = -97.0 | Minimum detectable signal power for Bit Error Rate BER <= 10^-6 |
| Operating RF Link Margin | M_link | dB | M_link >= 12.0 | Operating safety link margin above receiver sensitivity threshold |

---

### 3.2 INCOSE SEH v5.0 Metrics Summary Table

The complete set of 10 formal Measures of Effectiveness (MoE) and Measures of Performance (MoP) governing the tactical mission lifecycle:

| Metric ID | Metric Type | Metric Name | Formulation / Equation | Threshold | Objective | Unit | Public Clause Citation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `MoE-01` | MoE | Operational Availability | Ao = MTBM / (MTBM + MDT) | 0.95 | 0.99 | Dimensionless | INCOSE SEH v5.0 §3.2 |
| `MoE-02` | MoE | Mission Area Coverage Ratio | C_area = A_surveyed / A_total | 0.90 | 0.98 | Dimensionless | INCOSE SEH v5.0 §3.2 |
| `MoE-03` | MoE | Target Identification Probability | P_ID = N_correct / N_targets | 0.95 | 0.99 | Dimensionless | NATO STANAG 4586 Annex B §3.5 |
| `MoP-01` | MoP | Cross-Track Waypoint Deviation | max norm(p_act - p_cmd)_2D | 2.0 | 0.5 | m | RTCA DO-365B §2.2.3 |
| `MoP-02` | MoP | C2 Telemetry Transport Latency | tau_C2 = tau_enc + tau_tx + tau_prop + tau_rx + tau_dec | 100.0 | 25.0 | ms | NATO STANAG 4586 §4.5 |
| `MoP-03` | MoP | Navigation State Covariance Norm | norm(P_cov)_2D | 1.5 | 0.3 | m | IEEE Std 1558-2020 §4.2 |
| `MoP-04` | MoP | RF Packet Delivery Ratio | PDR = N_received / N_transmitted | 0.98 | 0.999 | Dimensionless | MIL-STD-188-220E §5.3 |
| `MoP-05` | MoP | Target Location Error (CEP90) | TLE_CEP90 = 0.589 * (sigma_x + sigma_y) | 2.5 | 1.0 | m | NATO STANAG 4586 Annex B §3.5 |
| `MoP-06` | MoP | Bingo Energy Statutory Reserve Ratio | Ratio = E_reserve / E_capacity | 0.20 | 0.25 | Dimensionless | JARUS SORA v2.5 Annex E §2.1 |
| `MoP-07` | MoP | RF Datalink Operating Margin | M_link = P_rx - P_sensitivity | 12.0 | 20.0 | dB | RTCA DO-362A §2.2.1 |
