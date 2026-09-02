| Attribute | Value |
| :--- | :--- |
| **Title** | Tactical Mission Intent: Bingo Energy Mathematics |
| **Version** | 1.0.0 |
| **Date** | 2026-09-02 |

## 9. Bingo Energy Mathematics & Secondary Divert Protocols

In accordance with JARUS SORA v2.5 (Annex E §2.1), NATO STANAG 4586 Annex B (§3.4), and EASA GM1 UAS.SPEC.050(1)(g), safe vehicle recovery is guaranteed by continuous parametric computation of the dynamic Bingo Energy state $E_{\mathrm{bingo}}(t)$ and rigorous enforcement of the mandatory statutory energy reserve ratio $\text{Ratio}_{\mathrm{reserve}} \ge 0.20$.

---

### 9.1 Dynamic Closed-Loop Bingo Formulation & Power Model

The dynamic Bingo energy threshold represents the minimum onboard stored energy required to complete the primary return transit, execute a secondary diversion if the primary site is obstructed, and perform a precision touchdown with statutory safety reserves intact:

$$
\begin{aligned}
E_{\mathrm{bingo}}(t) &= E_{\mathrm{return}}(\mathbf{p}(t), \mathbf{p}_{\mathrm{dest}}) + E_{\mathrm{divert}}(\mathbf{p}_{\mathrm{dest}}, \mathbf{p}_{\mathrm{alt}}) + E_{\mathrm{reserve}} + E_{\mathrm{contingency}} \\
E_{\mathrm{reserve}} &\ge 0.20 \cdot E_{\mathrm{capacity}}
\end{aligned}
$$

Total instantaneous electrical power consumption $P_{\mathrm{total}}(t)$ integrates aerodynamic propulsion power, avionics base load, payload sensor dissipation, and environmental anti-icing heater demands:

$$
\begin{aligned}
P_{\mathrm{total}}(t) &= P_{\mathrm{prop}}(v(t), \mathbf{w}(t)) + P_{\mathrm{avionics}} + P_{\mathrm{payload}} + P_{\mathrm{heaters}} \\
P_{\mathrm{prop}}(v, \mathbf{w}) &= T(v, \mathbf{w}) \cdot v_{\mathrm{induced}} + \frac{1}{2} \rho v_{\mathrm{airspeed}}^3 S C_{D0} + \frac{2 k m^2 g^2}{\rho v_{\mathrm{airspeed}} S}
\end{aligned}
$$

The dynamic transit and divert components are evaluated via continuous integral path energy modeling across the forward flight trajectory:

$$
\begin{aligned}
E_{\mathrm{return}}(\mathbf{p}(t), \mathbf{p}_{\mathrm{dest}}) &= \int_{t}^{t_{\mathrm{dest}}} \left( P_{\mathrm{prop}}(v_{\mathrm{airspeed}}(\tau), \mathbf{w}(\tau)) + P_{\mathrm{avionics}} + P_{\mathrm{payload}} + P_{\mathrm{heaters}} \right) d\tau \\
E_{\mathrm{divert}}(\mathbf{p}_{\mathrm{dest}}, \mathbf{p}_{\mathrm{alt}}) &= \int_{t_{\mathrm{dest}}}^{t_{\mathrm{alt}}} P_{\mathrm{total}}(\tau) d\tau = \frac{\|\mathbf{p}_{\mathrm{dest}} - \mathbf{p}_{\mathrm{alt}}\|_2}{v_{\mathrm{cruise}}} \cdot P_{\mathrm{total,cruise}} + E_{\mathrm{climb\_divert}}
\end{aligned}
$$

Where and Operational Parameters:

#### Aerodynamic, Power, and Battery Storage Parameter Table

| Energy Parameter | Symbol | Value | Units | Constraint Rule | Public Clause Citation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Vehicle Maximum Takeoff Mass | m | 12.5 | kg | Maximum operational airframe mass | JARUS SORA v2.5 Annex E |
| Gravitational Acceleration | g | 9.80665 | m/s^2 | Standard gravitational acceleration constant | ISO 80000-3 |
| Ambient Air Density | rho | 1.225 | kg/m^3 | Sea level ISA standard air density | ISO 2533:1975 |
| Wing Lifting Surface Area | S | 0.85 | m^2 | Effective aerodynamic wing planform area | NATO STANAG 4586 Annex B §3.4 |
| Zero-Lift Parasitic Drag Coeff | CD0 | 0.028 | Dimensionless | Airframe profile and parasitic drag coefficient | NATO STANAG 4586 Annex B §3.4 |
| Induced Drag Proportionality | k | 0.045 | Dimensionless | Oswald efficiency induced drag factor k = 1 / (pi * AR * e) | NATO STANAG 4586 Annex B §3.4 |
| Nominal Cruise Airspeed | v_cruise | 18.0 | m/s | Best Specific Air Range (SAR) cruising speed | NATO STANAG 4586 Annex B §3.4 |
| Avionics Base Electrical Load | P_avionics | 45.0 | W | Flight computer, navigation sensors, and bus power | RTCA DO-365B §2.3 |
| Payload Active Electrical Load | P_payload | 35.0 | W | Multi-spectral gimbal and video compression engine | NATO STANAG 4586 §4.5 |
| Anti-Icing Heaters Load | P_heaters | 20.0 | W | Electro-thermal pitot and optical lens de-icing | MIL-STD-810H Method 521.4 |
| Total Nominal Energy Capacity | E_capacity | 1080000.0 | J | 6S 14Ah @ 22.2V nominal capacity (300.0 Wh) | JARUS SORA v2.5 Annex E |
| Primary Return Transit Energy | E_return | 350000.0 | J | Energy for 15.0 km primary return transit (97.2 Wh) | NATO STANAG 4586 Annex B §3.4 |
| Secondary Divert Transit Energy | E_divert | 120000.0 | J | Energy for 5.0 km divert to secondary LZ (33.3 Wh) | NATO STANAG 4586 Annex B §3.4 |
| Mandatory Statutory Reserve | E_reserve | 216000.0 | J | Strict statutory reserve: E_reserve >= 0.20 * E_capacity (60.0 Wh) | EASA GM1 UAS.SPEC.050(1)(g) |
| Dynamic Contingency Buffer | E_contingency | 100000.0 | J | Dynamic headwind and loiter holding reserve (27.8 Wh) | JARUS SORA v2.5 Annex E |
| Total Critical Bingo Threshold | E_bingo | 786000.0 | J | Critical return threshold: E_return + E_divert + E_res + E_cont (218.3 Wh) | NATO STANAG 4586 Annex B §3.4 |
| Calculated Statutory Reserve Ratio | Ratio_reserve | 0.20 | Dimensionless | Ratio = E_reserve / E_capacity >= 0.20 | EASA GM1 UAS.SPEC.050(1)(g) |

---

### 9.2 Secondary and Tertiary Divert Recovery Protocols

When the primary landing zone is unavailable (runway incursion, severe localized microburst, or C2 loss), the flight executive autonomously executes secondary or tertiary divert sequencing:

| Recovery Site ID | Site Classification | Geodetic Location | Elevation | Runway / Pad Dimension | Priority Order | Ingress Clearance | Public Clause Citation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `LZ-PRIMARY` | Primary Base Recovery Pad | 45.1234 N, 14.5678 E | 150.0 m MSL | 10.0 m x 10.0 m Pad | Priority 1 (Nominal) | Unrestricted Line-of-Sight | NATO STANAG 4586 Annex B §3.4 |
| `LZ-DIVERT-ALPHA` | Secondary Divert Field | 45.1500 N, 14.6100 E | 140.0 m MSL | 50.0 m x 15.0 m Strip | Priority 2 (Secondary) | Obstacle Clearance Verified | NATO STANAG 4586 Annex B §3.4 |
| `LZ-DIVERT-BRAVO` | Tertiary Emergency Clearing | 45.1050 N, 14.5100 E | 165.0 m MSL | 25.0 m x 25.0 m Clearing | Priority 3 (Contingency) | Power Line Standoff Verified | NATO STANAG 4586 Annex B §3.4 |

- **Autonomous Divert Trigger Decision:** If $E_{\mathrm{current}}(t) \le E_{\mathrm{bingo}}(t)$ and `LZ-PRIMARY` reports obstruction or unmitigated incursion, the flight executive commands an immediate divert to `LZ-DIVERT-ALPHA` within response latency $t_{\mathrm{resp}} \le 200.0\text{ ms}$, optimizing airspeed and climb gradient for maximum specific air range (SAR).
- **Public Clause Citation:** NATO STANAG 4586 Annex B §3.4
