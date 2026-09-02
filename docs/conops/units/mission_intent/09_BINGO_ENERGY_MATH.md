| Attribute | Value |
| :--- | :--- |
| **Title** | Tactical Mission Intent: Bingo Energy Mathematics |
| **Version** | 1.0.0 |
| **Date** | 2026-09-02 |

## 9. Bingo Energy Mathematics & Secondary Divert Protocols

In accordance with JARUS SORA v2.5 (Annex E §2.1), NATO STANAG 4586 Annex B (§3.4), and EASA GM1 UAS.SPEC.050(1)(g), safe recovery is guaranteed by continuous parametric computation of the dynamic Bingo Energy state $E_{\mathrm{bingo}}(t)$ and enforcement of the mandatory statutory energy reserve ratio $\text{Ratio}_{\mathrm{reserve}} \ge 0.20$.

### 9.1 Parametric Closed-Loop Bingo Formulation

The dynamic Bingo energy threshold represents the minimum onboard stored energy required to transit from the current operating position to the primary destination, divert to an alternate recovery point if the primary site is fouled, and complete landing with statutory safety reserves intact:

$$
\begin{aligned}
E_{\mathrm{bingo}}(t) &= E_{\mathrm{return}}(\mathbf{p}(t), \mathbf{p}_{\mathrm{dest}}) + E_{\mathrm{divert}}(\mathbf{p}_{\mathrm{dest}}, \mathbf{p}_{\mathrm{alt}}) + E_{\mathrm{reserve}} + E_{\mathrm{contingency}} \\
E_{\mathrm{reserve}} &\ge 0.20 \cdot E_{\mathrm{capacity}}
\end{aligned}
$$

The dynamic transit and divert components are evaluated via continuous integral path energy modeling:

$$
\begin{aligned}
E_{\mathrm{return}}(\mathbf{p}(t), \mathbf{p}_{\mathrm{dest}}) &= \int_{t}^{t_{\mathrm{land}}} \left( P_{\mathrm{prop}}(v_{\mathrm{airspeed}}(\tau), \mathbf{v}_{\mathrm{wind}}(\tau)) + P_{\mathrm{avionics}} + P_{\mathrm{payload}} \right) d\tau \\
E_{\mathrm{divert}}(\mathbf{p}_{\mathrm{dest}}, \mathbf{p}_{\mathrm{alt}}) &= \frac{\|\mathbf{p}_{\mathrm{dest}} - \mathbf{p}_{\mathrm{alt}}\|_2}{v_{\mathrm{cruise}}} \cdot P_{\mathrm{cruise}} + E_{\mathrm{climb\_divert}}
\end{aligned}
$$

Where and Operational Parameters:

| Energy Parameter | Symbol | Value | Units | Constraint Rule | Public Clause Citation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Total Storage Capacity | E_capacity | 1080000.0 | J | 6S 14Ah @ 22.2V nominal capacity (300.0 Wh) | JARUS SORA v2.5 Annex E |
| Return Transit Energy | E_return | 350000.0 | J | Energy required for 15.0 km primary return transit | NATO STANAG 4586 Annex B §3.4 |
| Secondary Divert Energy | E_divert | 120000.0 | J | Energy required for 5.0 km divert to secondary field | NATO STANAG 4586 Annex B §3.4 |
| Mandatory Statutory Reserve | E_reserve | 216000.0 | J | Strict statutory reserve: E_reserve >= 0.20 * E_capacity | EASA GM1 UAS.SPEC.050(1)(g) |
| Contingency Buffer | E_contingency | 100000.0 | J | Dynamic headwind and loiter holding reserve | JARUS SORA v2.5 Annex E |
| Total Bingo Threshold | E_bingo | 786000.0 | J | Critical return threshold: E_return + E_divert + E_res + E_cont | NATO STANAG 4586 Annex B §3.4 |
| Calculated Reserve Ratio | Ratio_reserve | 0.20 | Dimensionless | Ratio = E_reserve / E_capacity >= 0.20 | EASA GM1 UAS.SPEC.050(1)(g) |

---

### 9.2 Secondary and Tertiary Divert Recovery Protocols

When the primary landing zone is unavailable (runway incursion, localized weather hazard, or C2 loss), the flight manager autonomously executes secondary or tertiary divert sequencing:

| Recovery Site ID | Site Classification | Geodetic Location | Elevation | Runway / Pad Dimension | Priority Order | Ingress Clearance |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `LZ-PRIMARY` | Primary Base Recovery Pad | 45.1234 N, 14.5678 E | 150.0 m MSL | 10.0 m x 10.0 m Pad | Priority 1 (Nominal) | Unrestricted Line-of-Sight |
| `LZ-DIVERT-ALPHA` | Secondary Divert Field | 45.1500 N, 14.6100 E | 140.0 m MSL | 50.0 m x 15.0 m Strip | Priority 2 (Secondary) | Obstacle Clearance Verified |
| `LZ-DIVERT-BRAVO` | Tertiary Emergency Clearing | 45.1050 N, 14.5100 E | 165.0 m MSL | 25.0 m x 25.0 m Clearing | Priority 3 (Contingency) | Power Line Standoff Verified |

- **Autonomous Divert Protocol:** If $E_{\mathrm{current}} \le E_{\mathrm{bingo}}$ and `LZ-PRIMARY` reports obstruction, the flight executive commands immediate divert to `LZ-DIVERT-ALPHA` within $t_{\mathrm{resp}} \le 200.0\text{ ms}$, adjusting climb profile and airspeed for optimal specific air range (SAR).
- **Public Clause Citation:** NATO STANAG 4586 Annex B §3.4
