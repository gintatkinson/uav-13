| Attribute | Value |
| :--- | :--- |
| **Title** | Cited Research Inventory & Normative Baseline: UAS Infrastructure Safety |
| **Version** | 1.0.0 |
| **Date** | 2026-09-02 |

# Cited Research Inventory & Normative Baseline: UAS Infrastructure Safety

## 1. Scope & System Identification
- **System Identifier:** `DEAP01-uas-infrastructure-safety`
- **Operational Domain:** `UAS Mission Operations, Ground Infrastructure Safety & Resilient C2 Assurance`
- **Research Scope:** Authoritative standards-obligation population catalog and normative baseline for civil and defense unmanned aircraft systems (UAS), ground control stations (GCS), command and control (C2) data links, electronic warfare (EW) / cyber resiliency, rules of engagement (ROE) interlocks, pre-flight/in-flight Go/No-Go decision matrices, PACE communications planning, SORA OSO-01..24 airworthiness matrix, ASTM F3269-17 Run-Time Assurance (RTA), ASTM F3411-22a / FAA 14 CFR §89.310 Remote ID roster, RTCA DO-365B Detect and Avoid (DAA) well-clear separation, and MIL-STD-1629A / SAE ARP4761 / MIL-STD-882E / RTCA DO-178C FMECA component-class failure mode criticality roster.
- **Applicability Statement:** Defense autonomy and weapon safety interlocks (DoD Directive 3000.09, CJCSI 3121.01B, NATO STANAG 4586), OT/ICS cyber security and counter-EW electromagnetic resilience (NIST SP 800-82r3, MITRE ATT&CK for ICS / D3FEND, MIL-STD-461G, ISO/SAE 21434), civil and specific category operational flight safety (FAA 14 CFR §107.49, EASA AMC1 UAS.SPEC.050, JARUS SORA v2.5), multi-tier robust C2 communications (RTCA DO-362A, ASTM F3411-22a), Specific category airworthiness objectives (JARUS SORA v2.5 Annex E §E.1–§E.24), flight control runtime assurance (ASTM F3269-17), Remote ID tracking (FAA 14 CFR §89.310, ASTM F3411-22a), airborne collision avoidance (RTCA DO-365B), and hardware/software failure mode criticality and automated containment (MIL-STD-1629A §4.3–§4.6, SAE ARP4761 §4.3.1–§4.3.3, MIL-STD-882E Task 205 §4.2, RTCA DO-178C §6.3.1).

## 2. Normative Standards & Baseline Documents Inventory
| Standard / Baseline ID | Issuing Body | Title | Applicable Clauses | Obligation Category | Declared Total | Clause Citation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| DoD Directive 3000.09 | U.S. Department of Defense | Autonomy in Weapon Systems | §3.1 Human Judgement in Force, §3.1.a Autonomous Engagement, §3.1.b Fail-Safe Interlocks, §3.1.c Cyber Safeguards | Weapon & Sensor Interlock Assurance | 4 | DoD Directive 3000.09 §3.1, §3.1.a, §3.1.b, §3.1.c |
| NATO STANAG 4586 | NATO Standardisation Office | Standard Interfaces of UAV Control System (UCS) for NATO UAV Interoperability | §4.2 UCS Architectural Framework, §4.2.2 Interoperability Levels 1-5, §5.1 Data Link Interface Profiles, §5.1.4 C2 Link Handover | C2 & Interoperability Architecture | 4 | NATO STANAG 4586 §4.2, §4.2.2, §5.1, §5.1.4 |
| CJCSI 3121.01B | Chairman of the Joint Chiefs of Staff | Standing Rules of Engagement / Standing Rules for Use of Force for U.S. Forces | Enclosure A §2.a Self-Defense Determination, Enclosure A §4.b Positive Identification, Enclosure B §3.c Collateral Damage Mitigation, Enclosure E §2.d Escalation of Force Interlocks | Rules of Engagement & Authorization | 4 | CJCSI 3121.01B Enclosure A §2.a, Enclosure A §4.b, Enclosure B §3.c, Enclosure E §2.d |
| NIST SP 800-82r3 | NIST | Guide to Operational Technology (OT) Security | §4.2 OT Threat Sources, §5.3 OT Defense-in-Depth Architecture, §6.2 Wireless & RF C2 Security Controls, §6.4 Incident Response & Containment | OT & Cyber Physical Security | 4 | NIST SP 800-82r3 §4.2, §5.3, §6.2, §6.4 |
| MITRE ATT&CK / D3FEND | MITRE Corporation | Adversary Tactics for ICS / Defensive Countermeasures Matrix | §T0814 Denial of Service, §T0855 Unauthorized Command, §T0843 Program Download, §D3-MCR Message Authentication | Adversary Threat & Defensive Countermeasures | 4 | MITRE ATT&CK for ICS §T0814, §T0855, §T0843, MITRE D3FEND §D3-MCR |
| MIL-STD-461G | U.S. Department of Defense | Requirements for the Control of Electromagnetic Interference Characteristics | §5.4 Conducted Susceptibility CS114-CS116, §5.18 Radiated Susceptibility RS103, §5.19 Magnetic Fields RS101, §5.20 Conducted Emissions CE102 | Electromagnetic Environmental Effects & EW | 4 | MIL-STD-461G §5.4, §5.18, §5.19, §5.20 |
| ISO/SAE 21434 | ISO / SAE International | Road vehicles — Cybersecurity engineering | §5.3 Cybersecurity Management, §6.4 Threat Analysis and Risk Assessment, §9.4 Vulnerability Analysis, §10.4 Incident Verification & Validation | Cyber Risk Assessment & Threat Modeling | 4 | ISO/SAE 21434 §5.3, §6.4, §9.4, §10.4 |
| FAA 14 CFR §107.49 | Federal Aviation Administration | Preflight familiarization, inspection, and actions for aircraft operation | §107.49(a) Weather & Airspace Assessment, §107.49(b) GCS & C2 Link Verification, §107.49(c) Vehicle Integrity Inspection, §107.49(d) Non-Participant Safety Check | Civil Pre-Flight Operational Go/No-Go | 4 | FAA 14 CFR §107.49(a), §107.49(b), §107.49(c), §107.49(d) |
| AMC1 UAS.SPEC.050 | European Union Aviation Safety Agency | Easy Access Rules for UAS - Responsibilities of the UAS Operator | §3.2 Pre-Flight Operational Checklist, §3.3 In-Flight Contingency Management, §4.1 Site Survey & Geofence Containment, §4.4 Post-Flight Inspection & Logging | European Operational Safety & Containment | 4 | AMC1 UAS.SPEC.050 §3.2, §3.3, §4.1, §4.4 |
| JARUS SORA v2.5 | JARUS | Specific Operations Risk Assessment | Annex B §B.2 Ground Risk Mitigations M1-M3, Annex C §C.3 Strategic Air Risk Mitigations, Annex D §D.2 Tactical Mitigation Standards, Annex E §E.4 Containment & OSO Objectives | Specific Category Risk Assessment | 4 | JARUS SORA v2.5 Annex B §B.2, Annex C §C.3, Annex D §D.2, Annex E §E.4 |
| RTCA DO-362A | RTCA / EUROCAE | Command and Control (C2) Data Link MOPS | §2.2 Link Availability & Continuity, §2.2.1 Terrestrial LOS Link Allocation, §2.2.4 Satellite C2 Link Handover, §3.4 Lost Link Fallback Switching | C2 Datalink Performance & Redundancy | 4 | RTCA DO-362A §2.2, §2.2.1, §2.2.4, §3.4 |
| ASTM F3411-22a | ASTM International | Standard Specification for Remote ID and Tracking | §5.3 Basic ID, §5.4 Location/Vector, §5.5 Auth, §5.6 Self-ID, §5.7 System, §5.8 Operator ID, §6.1 Direct RF Broadcast, §6.3 RF Handover, §7.2 Net RID Bounds, §7.4 Broker, §8.4 Cryptographic Auth | Remote Identification & Tracking Protocol | 12 | ASTM F3411-22a §5.3, §5.4, §5.5, §5.6, §5.7, §5.8, §6.1, §6.3, §7.2, §7.4, §8.4 |
| JARUS SORA v2.5 Annex E | JARUS | SORA Specific Category Airworthiness Objectives (OSO-01..24) | §E.1 Airworthiness, §E.2 Manufacture, §E.3 Maintenance, §E.4 Environment, §E.5 SSA/SPOF, §E.6 C3, §E.7 Human Error, §E.8 Ops Procedures, §E.9 Training, §E.10 Payload, §E.11 GSE, §E.12 Adverse Weather, §E.13 External Services, §E.14 Containment, §E.15 Multi-Crew, §E.16 Swarm, §E.17 Payload Failure, §E.18 Parachute, §E.19 Fitness, §E.20 Maintenance HF, §E.21 Sustainability, §E.22 Security, §E.23 Icing/HIRF, §E.24 Lithium Fire | Specific Category Airworthiness Assurance | 24 | JARUS SORA v2.5 Annex E §E.1, §E.2, §E.3, §E.4, §E.5, §E.6, §E.7, §E.8, §E.9, §E.10, §E.11, §E.12, §E.13, §E.14, §E.15, §E.16, §E.17, §E.18, §E.19, §E.20, §E.21, §E.22, §E.23, §E.24 |
| ASTM F3269-17 | ASTM International | Standard Practice for Methods to Safely Bound Flight Behavior of UAS Containing Complex Functions | §5.1 RTA Simplex Architecture, §5.2 Attitude/Speed/Geofence Monitors, §5.3 Deterministic State Switching, §5.4 SLDV Invariant Proof Slots | Run-Time Assurance & Safety Net Architecture | 4 | ASTM F3269-17 §5.1, §5.2, §5.3, §5.4 |
| FAA 14 CFR §89.310 | Federal Aviation Administration | Minimum Performance Requirements for Standard Remote Identification Unmanned Aircraft | §89.310(a) Message Elements, §89.310(b) Broadcast Rate & Latency, §89.310(c) Direct Radio Frequency Transmission, §89.310(d) Tamper Resistance & Cyber Integrity | Civil Remote Identification Regulation | 4 | FAA 14 CFR §89.310(a), §89.310(b), §89.310(c), §89.310(d) |
| RTCA DO-365B | RTCA / EUROCAE | MOPS for Detect and Avoid (DAA) Systems | §2.2.4 DAA Well-Clear Definition & Volume, §2.2.4.1 DMOD & HMD Boundaries, §2.2.4.2 ZTHR & Vertical Tau, §2.2.4.3 Warning Alert Horizon, §2.2.5 Maneuver Guidance, §2.2.5.1 Preventative Alert Horizon, §2.2.5.2 Recovery Hysteresis, §2.2.5.3 Multi-Sensor Track Fusion | Detect and Avoid (DAA) & Well-Clear Separation | 8 | RTCA DO-365B §2.2.4, §2.2.4.1, §2.2.4.2, §2.2.4.3, §2.2.5, §2.2.5.1, §2.2.5.2, §2.2.5.3 |
| MIL-STD-1629A | U.S. Department of Defense | Procedures for Performing a Failure Mode, Effects and Criticality Analysis | §4.3 Severity Classification, §4.4 Failure Probability, §4.5 Failure Detection, §4.6 Criticality Analysis | Failure Mode & Effects Criticality Analysis | 4 | MIL-STD-1629A §4.3, §4.4, §4.5, §4.6 |
| SAE ARP4761 | SAE International | Guidelines and Methods for Conducting the Safety Assessment Process on Civil Airborne Systems and Equipment | §4.3.1 Functional Hazard Assessment, §4.3.3 FMECA Process, App. L Failure Probability Allocation, App. M Common Cause Analysis | System Safety Assessment & Failure Analysis | 4 | SAE ARP4761 §4.3.1, §4.3.3, SAE ARP4761 App. L, App. M |
| MIL-STD-882E | U.S. Department of Defense | Standard Practice for System Safety | Task 106 §4.2 Hazard Mitigation, Task 204 §4.2 Probability Levels, Task 205 §4.2 System Hazard Analysis, Task 208 §4.2 Functional Thread Isolation | System Safety & Hazard Analysis | 4 | MIL-STD-882E Task 106 §4.2, Task 204 §4.2, Task 205 §4.2, Task 208 §4.2 |
| RTCA DO-178C | RTCA / EUROCAE | Software Considerations in Airborne Systems and Equipment Certification | §6.3.1 Software Fault Detection, §6.3.2 Software Partitioning, §6.4.3 Redundancy Management, §6.4.4 Structural Coverage | Airborne Software Safety & Fault Detection | 4 | RTCA DO-178C §6.3.1, §6.3.2, §6.4.3, §6.4.4 |

## 3. Declared-Total Population Register
The Declared-Total Population Register catalogs every applicable normative obligation, safety constraint, METL task, and control pattern with its mandatory formal public clause citation. Un-cited additions are strictly prohibited.

| Obligation ID | Category | Standard ID | Target Metric / Obligation Count | Verification Mechanism | Public Clause Citation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `OBL-DOD3000-01` | Weapon & Sensor Interlock Assurance | DoD Directive 3000.09 | 1 | Human Judgement Policy Audit & Multi-Operator Consent Verification | DoD Directive 3000.09 §3.1 |
| `OBL-DOD3000-02` | Weapon & Sensor Interlock Assurance | DoD Directive 3000.09 | 1 | Autonomous Engagement Bounding Simulation & Range-Gate Formal Check | DoD Directive 3000.09 §3.1.a |
| `OBL-DOD3000-03` | Weapon & Sensor Interlock Assurance | DoD Directive 3000.09 | 1 | Hardware-in-the-Loop Safe Switch Disarm & Heartbeat Interlock Inspection | DoD Directive 3000.09 §3.1.b |
| `OBL-DOD3000-04` | Weapon & Sensor Interlock Assurance | DoD Directive 3000.09 | 1 | Anti-Tamper & Cryptographic Zeroization Security Evaluation | DoD Directive 3000.09 §3.1.c |
| `OBL-STANAG4586-01` | C2 & Interoperability Architecture | NATO STANAG 4586 | 1 | UCS Architectural Interface Conformance Test & DLI Protocol Verification | NATO STANAG 4586 §4.2 |
| `OBL-STANAG4586-02` | C2 & Interoperability Architecture | NATO STANAG 4586 | 1 | Level of Interoperability (LOI 1-5) State Machine Transition Check | NATO STANAG 4586 §4.2.2 |
| `OBL-STANAG4586-03` | C2 & Interoperability Architecture | NATO STANAG 4586 | 1 | Data Link Interface (DLI) Channel Redundancy & Bandwidth Profiling | NATO STANAG 4586 §5.1 |
| `OBL-STANAG4586-04` | C2 & Interoperability Architecture | NATO STANAG 4586 | 1 | Seamless C2 Control Station Handover & Authority Arbitration Test | NATO STANAG 4586 §5.1.4 |
| `OBL-CJCSI3121-01` | Rules of Engagement & Authorization | CJCSI 3121.01B | 1 | Hostile Act / Hostile Intent Logic Matrix Audit & Invariant Assertion | CJCSI 3121.01B Enclosure A §2.a |
| `OBL-CJCSI3121-02` | Rules of Engagement & Authorization | CJCSI 3121.01B | 1 | Multi-Spectral Positive Identification (PID) Sensor Fusion Assessment | CJCSI 3121.01B Enclosure A §4.b |
| `OBL-CJCSI3121-03` | Rules of Engagement & Authorization | CJCSI 3121.01B | 1 | Dynamic Collateral Damage Estimation & Blast Radius Bounding Test | CJCSI 3121.01B Enclosure B §3.c |
| `OBL-CJCSI3121-04` | Rules of Engagement & Authorization | CJCSI 3121.01B | 1 | Escalation of Force Tiered Interlock & Operator Veto Timing Test | CJCSI 3121.01B Enclosure E §2.d |
| `OBL-NIST80082-01` | OT & Cyber Physical Security | NIST SP 800-82r3 | 1 | Threat Modeling & Adversary Capability Vector Matrix Review | NIST SP 800-82r3 §4.2 |
| `OBL-NIST80082-02` | OT & Cyber Physical Security | NIST SP 800-82r3 | 1 | Defense-in-Depth Zoning & GCS Perimeter Firewall Inspection | NIST SP 800-82r3 §5.3 |
| `OBL-NIST80082-03` | OT & Cyber Physical Security | NIST SP 800-82r3 | 1 | Wireless C2 Cryptographic Key Management & Mutual Auth Verification | NIST SP 800-82r3 §6.2 |
| `OBL-NIST80082-04` | OT & Cyber Physical Security | NIST SP 800-82r3 | 1 | Incident Response Playbook Execution & Autonomous Quarantine Test | NIST SP 800-82r3 §6.4 |
| `OBL-MITRE-01` | Adversary Threat & Defensive Countermeasures | MITRE ATT&CK / D3FEND | 1 | RF Jamming & Link Saturation DoS Resilience Benchmarking | MITRE ATT&CK for ICS §T0814 |
| `OBL-MITRE-02` | Adversary Threat & Defensive Countermeasures | MITRE ATT&CK / D3FEND | 1 | Unauthorized Command Injection Rejection & Anti-Replay Verification | MITRE ATT&CK for ICS §T0855 |
| `OBL-MITRE-03` | Adversary Threat & Defensive Countermeasures | MITRE ATT&CK / D3FEND | 1 | Unauthorized Firmware/Logic Download Prevention & Secure Boot Audit | MITRE ATT&CK for ICS §T0843 |
| `OBL-MITRE-04` | Adversary Threat & Defensive Countermeasures | MITRE ATT&CK / D3FEND | 1 | Cryptographic Relay & Message Authentication Header Conformance Test | MITRE D3FEND §D3-MCR |
| `OBL-MIL461G-01` | Electromagnetic Environmental Effects & EW | MIL-STD-461G | 1 | Conducted Susceptibility CS114/CS115/CS116 Cable Injection Test | MIL-STD-461G §5.4 |
| `OBL-MIL461G-02` | Electromagnetic Environmental Effects & EW | MIL-STD-461G | 1 | Radiated Susceptibility RS103 High-Power RF Field Chamber Immersion | MIL-STD-461G §5.18 |
| `OBL-MIL461G-03` | Electromagnetic Environmental Effects & EW | MIL-STD-461G | 1 | Low-Frequency Magnetic Field RS101 Sensor Shielding Evaluation | MIL-STD-461G §5.19 |
| `OBL-MIL461G-04` | Electromagnetic Environmental Effects & EW | MIL-STD-461G | 1 | Conducted Emissions CE102 Power Bus Harmonic Distortion Measurement | MIL-STD-461G §5.20 |
| `OBL-ISO21434-01` | Cyber Risk Assessment & Threat Modeling | ISO/SAE 21434 | 1 | Cybersecurity Management System (CSMS) Governance & Audit Review | ISO/SAE 21434 §5.3 |
| `OBL-ISO21434-02` | Cyber Risk Assessment & Threat Modeling | ISO/SAE 21434 | 1 | Threat Analysis and Risk Assessment (TARA) Attack Tree Quantification | ISO/SAE 21434 §6.4 |
| `OBL-ISO21434-03` | Cyber Risk Assessment & Threat Modeling | ISO/SAE 21434 | 1 | Attack Feasibility & Vulnerability Exploitability Rating Assessment | ISO/SAE 21434 §9.4 |
| `OBL-ISO21434-04` | Cyber Risk Assessment & Threat Modeling | ISO/SAE 21434 | 1 | Cybersecurity Verification & Fuzzing / Penetration Test Report Audit | ISO/SAE 21434 §10.4 |
| `OBL-FAA10749-01` | Civil Pre-Flight Operational Go/No-Go | FAA 14 CFR §107.49 | 1 | Meteorological Assessment & Local Airspace NOTAM Authorization Check | FAA 14 CFR §107.49(a) |
| `OBL-FAA10749-02` | Civil Pre-Flight Operational Go/No-Go | FAA 14 CFR §107.49 | 1 | GCS Power, Display, and Primary C2 Link Continuity Pre-Flight Audit | FAA 14 CFR §107.49(b) |
| `OBL-FAA10749-03` | Civil Pre-Flight Operational Go/No-Go | FAA 14 CFR §107.49 | 1 | Aircraft Structural, Propulsion, and Battery Health Built-In Test | FAA 14 CFR §107.49(c) |
| `OBL-FAA10749-04` | Civil Pre-Flight Operational Go/No-Go | FAA 14 CFR §107.49 | 1 | Non-Participant Ground Hazard Isolation & Containment Buffer Review | FAA 14 CFR §107.49(d) |
| `OBL-EASASPEC050-01` | European Operational Safety & Containment | AMC1 UAS.SPEC.050 | 1 | Specific Category Pre-Flight Checklist Verification & Crew Briefing | AMC1 UAS.SPEC.050 §3.2 |
| `OBL-EASASPEC050-02` | European Operational Safety & Containment | AMC1 UAS.SPEC.050 | 1 | In-Flight Contingency Management & Degraded Link Reaction Execution | AMC1 UAS.SPEC.050 §3.3 |
| `OBL-EASASPEC050-03` | European Operational Safety & Containment | AMC1 UAS.SPEC.050 | 1 | 3D Flight Geography and Contingency Volume Containment Validation | AMC1 UAS.SPEC.050 §4.1 |
| `OBL-EASASPEC050-04` | European Operational Safety & Containment | AMC1 UAS.SPEC.050 | 1 | Post-Flight Safety Inspection & Operational Flight Log Maintenance | AMC1 UAS.SPEC.050 §4.4 |
| `OBL-JARUSSORA-01` | Specific Category Risk Assessment | JARUS SORA v2.5 | 1 | Ground Risk Class (GRC) Mitigation M1/M2/M3 Parachute/Tether Verification | JARUS SORA v2.5 Annex B §B.2 |
| `OBL-JARUSSORA-02` | Specific Category Risk Assessment | JARUS SORA v2.5 | 1 | Strategic Air Risk Mitigation (ARC Reduction) Airspace Deconfliction | JARUS SORA v2.5 Annex C §C.3 |
| `OBL-JARUSSORA-03` | Specific Category Risk Assessment | JARUS SORA v2.5 | 1 | Tactical Mitigation Performance Standards (TMPR) DAA Sensor Detection | JARUS SORA v2.5 Annex D §D.2 |
| `OBL-JARUSSORA-04` | Specific Category Risk Assessment | JARUS SORA v2.5 | 1 | Enhanced Containment Envelope & High-Integrity Safe Landing Proof | JARUS SORA v2.5 Annex E §E.4 |
| `OBL-DO362A-01` | C2 Datalink Performance & Redundancy | RTCA DO-362A | 1 | C2 Link Availability (99.99%) and Continuity Performance Verification | RTCA DO-362A §2.2 |
| `OBL-DO362A-02` | C2 Datalink Performance & Redundancy | RTCA DO-362A | 1 | Terrestrial Line-of-Sight (LOS) C-Band / ISM RF Link Margin Testing | RTCA DO-362A §2.2.1 |
| `OBL-DO362A-03` | C2 Datalink Performance & Redundancy | RTCA DO-362A | 1 | Beyond-Line-of-Sight (BLOS) SATCOM Link Handover State Flow Check | RTCA DO-362A §2.2.4 |
| `OBL-DO362A-04` | C2 Datalink Performance & Redundancy | RTCA DO-362A | 1 | Lost C2 Link Dynamic Fallback Switching & Autonomous Hold Verification | RTCA DO-362A §3.4 |
| `OBL-ASTMF3411-01` | Remote Identification & RF Continuity | ASTM F3411-22a | 1 | Broadcast Remote ID Message Set (Bluetooth 5.x / Wi-Fi NAN) Compliance | ASTM F3411-22a §6.1 |
| `OBL-ASTMF3411-02` | Remote Identification & RF Continuity | ASTM F3411-22a | 1 | Direct RF Link Degradation Anomaly Detection & Dual-Broadcast Handover | ASTM F3411-22a §6.3 |
| `OBL-ASTMF3411-03` | Remote Identification & RF Continuity | ASTM F3411-22a | 1 | Network Remote ID Latency Bound (<= 1.0 s) & Cloud Broker Integration | ASTM F3411-22a §7.2 |
| `OBL-ASTMF3411-04` | Remote Identification & RF Continuity | ASTM F3411-22a | 1 | Cryptographic Payload Signature Verification & Remote ID Anti-Spoofing | ASTM F3411-22a §8.4 |
| `OBL-SORA-OSO-01` | Specific Category Airworthiness Assurance | JARUS SORA v2.5 Annex E | 1 | UAS Design Reliability & Airworthiness Standards Conformance | JARUS SORA v2.5 Annex E §E.1 |
| `OBL-SORA-OSO-02` | Specific Category Airworthiness Assurance | JARUS SORA v2.5 Annex E | 1 | UAS Manufacturing Competency & Quality Management System Audit | JARUS SORA v2.5 Annex E §E.2 |
| `OBL-SORA-OSO-03` | Specific Category Airworthiness Assurance | JARUS SORA v2.5 Annex E | 1 | UAS Maintenance System Competency & Part-ML Inspection Verification | JARUS SORA v2.5 Annex E §E.3 |
| `OBL-SORA-OSO-04` | Specific Category Airworthiness Assurance | JARUS SORA v2.5 Annex E | 1 | Operational Environmental Condition Boundaries (Weather/Icing/Wind) | JARUS SORA v2.5 Annex E §E.4 |
| `OBL-SORA-OSO-05` | Specific Category Airworthiness Assurance | JARUS SORA v2.5 Annex E | 1 | System Safety Assessment (SSA) & Single Point of Failure (SPOF) Analysis | JARUS SORA v2.5 Annex E §E.5 |
| `OBL-SORA-OSO-06` | Specific Category Airworthiness Assurance | JARUS SORA v2.5 Annex E | 1 | C3 Datalink Performance, Latency & RF Link Loss Integrity | JARUS SORA v2.5 Annex E §E.6 |
| `OBL-SORA-OSO-07` | Specific Category Airworthiness Assurance | JARUS SORA v2.5 Annex E | 1 | Safe Recovery from Human Error, Crew Competency & CRM Error-Proofing | JARUS SORA v2.5 Annex E §E.7 |
| `OBL-SORA-OSO-08` | Specific Category Airworthiness Assurance | JARUS SORA v2.5 Annex E | 1 | Operational Procedures Definition, Validation & Adherence | JARUS SORA v2.5 Annex E §E.8 |
| `OBL-SORA-OSO-09` | Specific Category Airworthiness Assurance | JARUS SORA v2.5 Annex E | 1 | Remote Flight Crew Training, Licensing & Currency Verification | JARUS SORA v2.5 Annex E §E.9 |
| `OBL-SORA-OSO-10` | Specific Category Airworthiness Assurance | JARUS SORA v2.5 Annex E | 1 | Safe Design & Operation of Payload and External Cargo Equipment | JARUS SORA v2.5 Annex E §E.10 |
| `OBL-SORA-OSO-11` | Specific Category Airworthiness Assurance | JARUS SORA v2.5 Annex E | 1 | Ground Support Equipment (GSE) & Launch/Recovery Maintenance | JARUS SORA v2.5 Annex E §E.11 |
| `OBL-SORA-OSO-12` | Specific Category Airworthiness Assurance | JARUS SORA v2.5 Annex E | 1 | Safe Flight Operations in Adverse Meteorological Conditions | JARUS SORA v2.5 Annex E §E.12 |
| `OBL-SORA-OSO-13` | Specific Category Airworthiness Assurance | JARUS SORA v2.5 Annex E | 1 | External Services (UTM, GNSS, Weather) Reliability & Integrity Assurance | JARUS SORA v2.5 Annex E §E.13 |
| `OBL-SORA-OSO-14` | Specific Category Airworthiness Assurance | JARUS SORA v2.5 Annex E | 1 | Operational Containment Within 3D Volume & Ground Risk Buffer | JARUS SORA v2.5 Annex E §E.14 |
| `OBL-SORA-OSO-15` | Specific Category Airworthiness Assurance | JARUS SORA v2.5 Annex E | 1 | Multi-Crew Coordination, Handover Protocol & Communications Interface | JARUS SORA v2.5 Annex E §E.15 |
| `OBL-SORA-OSO-16` | Specific Category Airworthiness Assurance | JARUS SORA v2.5 Annex E | 1 | Multi-UAS Swarm Coordination & Dynamic Airspace Deconfliction | JARUS SORA v2.5 Annex E §E.16 |
| `OBL-SORA-OSO-17` | Specific Category Airworthiness Assurance | JARUS SORA v2.5 Annex E | 1 | Payload Failure Containment & Hazardous Payload Safe-Lock Release | JARUS SORA v2.5 Annex E §E.17 |
| `OBL-SORA-OSO-18` | Specific Category Airworthiness Assurance | JARUS SORA v2.5 Annex E | 1 | Automatic Flight Termination System (FTS) & Parachute Deployment | JARUS SORA v2.5 Annex E §E.18 |
| `OBL-SORA-OSO-19` | Specific Category Airworthiness Assurance | JARUS SORA v2.5 Annex E | 1 | Flight Crew Fitness to Fly, Duty Limits & Fatigue Risk Management | JARUS SORA v2.5 Annex E §E.19 |
| `OBL-SORA-OSO-20` | Specific Category Airworthiness Assurance | JARUS SORA v2.5 Annex E | 1 | Maintenance Human Factor Mitigations & Independent Inspection Audit | JARUS SORA v2.5 Annex E §E.20 |
| `OBL-SORA-OSO-21` | Specific Category Airworthiness Assurance | JARUS SORA v2.5 Annex E | 1 | Environmental Sustainability, Acoustic Footprint & Chemical Safety | JARUS SORA v2.5 Annex E §E.21 |
| `OBL-SORA-OSO-22` | Specific Category Airworthiness Assurance | JARUS SORA v2.5 Annex E | 1 | Security & Anti-Unlawful Interference Protection (Cyber & Physical) | JARUS SORA v2.5 Annex E §E.22 |
| `OBL-SORA-OSO-23` | Specific Category Airworthiness Assurance | JARUS SORA v2.5 Annex E | 1 | Severe Environmental Resilience (Icing, Lightning, HIRF Shielding) | JARUS SORA v2.5 Annex E §E.23 |
| `OBL-SORA-OSO-24` | Specific Category Airworthiness Assurance | JARUS SORA v2.5 Annex E | 1 | Fire Safety, Lithium Thermal Runaway Containment & Hazardous Materials | JARUS SORA v2.5 Annex E §E.24 |
| `OBL-ASTMF3269-01` | Run-Time Assurance & Safety Net Architecture | ASTM F3269-17 | 1 | Dual-Channel Simplex RTA Architecture Framework Conformance | ASTM F3269-17 §5.1 |
| `OBL-ASTMF3269-02` | Run-Time Assurance & Safety Net Architecture | ASTM F3269-17 | 1 | Simplex Safety Net Monitor & Attitude/Airspeed/Geofence Invariant Assertion | ASTM F3269-17 §5.2 |
| `OBL-ASTMF3269-03` | Run-Time Assurance & Safety Net Architecture | ASTM F3269-17 | 1 | Dynamic Envelope Barrier Function & Deterministic State Switching Logic | ASTM F3269-17 §5.3 |
| `OBL-ASTMF3269-04` | Run-Time Assurance & Safety Net Architecture | ASTM F3269-17 | 1 | Formal Proof Verification Slots & SLDV Property Prover Integration | ASTM F3269-17 §5.4 |
| `OBL-ODID-01` | Remote Identification & Tracking Protocol | ASTM F3411-22a | 1 | Open Drone ID Basic ID Message (Type 0x0) Serial Number Encoding | ASTM F3411-22a §5.3 |
| `OBL-ODID-02` | Remote Identification & Tracking Protocol | ASTM F3411-22a | 1 | Open Drone ID Location/Vector Message (Type 0x1) Kinematic Quantization | ASTM F3411-22a §5.4 |
| `OBL-ODID-03` | Remote Identification & Tracking Protocol | ASTM F3411-22a | 1 | Open Drone ID Authentication Message (Type 0x2) Multi-Page Signature | ASTM F3411-22a §5.5 |
| `OBL-ODID-04` | Remote Identification & Tracking Protocol | ASTM F3411-22a | 1 | Open Drone ID Self-ID Message (Type 0x3) Mission Description Payload | ASTM F3411-22a §5.6 |
| `OBL-ODID-05` | Remote Identification & Tracking Protocol | ASTM F3411-22a | 1 | Open Drone ID System Message (Type 0x4) Operator Coordinates & Area Limit | ASTM F3411-22a §5.7 |
| `OBL-ODID-06` | Remote Identification & Tracking Protocol | ASTM F3411-22a | 1 | Open Drone ID Operator ID Message (Type 0x5) Pilot Registration String | ASTM F3411-22a §5.8 |
| `OBL-ODID-07` | Remote Identification & Tracking Protocol | ASTM F3411-22a | 1 | Message Pack (Type 0xF) Bundling & Direct RF Broadcast Frame Assembly | ASTM F3411-22a §6.1 |
| `OBL-ODID-08` | Remote Identification & Tracking Protocol | ASTM F3411-22a | 1 | Network Remote ID Push Rates, REST/MQTT Broker Integration & Latency | ASTM F3411-22a §7.4 |
| `OBL-FAA89310-01` | Civil Remote Identification Regulation | FAA 14 CFR §89.310 | 1 | Standard Remote ID Broadcast Message Elements & Continuity Mandate | FAA 14 CFR §89.310(a) |
| `OBL-FAA89310-02` | Civil Remote Identification Regulation | FAA 14 CFR §89.310 | 1 | Remote ID Minimum Broadcast Transmission Rates & 1.0s Max Interval | FAA 14 CFR §89.310(b) |
| `OBL-FAA89310-03` | Civil Remote Identification Regulation | FAA 14 CFR §89.310 | 1 | Direct Radio Frequency Unlicensed Broadcast Transmission Conformance | FAA 14 CFR §89.310(c) |
| `OBL-FAA89310-04` | Civil Remote Identification Regulation | FAA 14 CFR §89.310 | 1 | Remote ID Hardware Tamper Resistance & Cyber Integrity Enclosure | FAA 14 CFR §89.310(d) |
| `OBL-DO365B-01` | Detect and Avoid (DAA) & Well-Clear Separation | RTCA DO-365B | 1 | DAA Well-Clear Mathematical Volume Definition (DMOD, HMD, Tau_mod, ZTHR) | RTCA DO-365B §2.2.4 |
| `OBL-DO365B-02` | Detect and Avoid (DAA) & Well-Clear Separation | RTCA DO-365B | 1 | Horizontal Well-Clear Boundary & Modified Tau Collision Avoidance Math | RTCA DO-365B §2.2.4.1 |
| `OBL-DO365B-03` | Detect and Avoid (DAA) & Well-Clear Separation | RTCA DO-365B | 1 | Vertical Well-Clear Cylinder (ZTHR = 450 ft) & Tau-v Co-Altitude Gating | RTCA DO-365B §2.2.4.2 |
| `OBL-DO365B-04` | Detect and Avoid (DAA) & Well-Clear Separation | RTCA DO-365B | 1 | Warning Alert Time Horizon (25 s) & Immediate Maneuver Execution | RTCA DO-365B §2.2.4.3 |
| `OBL-DO365B-05` | Detect and Avoid (DAA) & Well-Clear Separation | RTCA DO-365B | 1 | Corrective Alert Horizon (55 s) & Recommended Pilot Avoidance Guidance | RTCA DO-365B §2.2.5 |
| `OBL-DO365B-06` | Detect and Avoid (DAA) & Well-Clear Separation | RTCA DO-365B | 1 | Preventative Alert Horizon (75 s) & Traffic Advisory Proximity Monitor | RTCA DO-365B §2.2.5.1 |
| `OBL-DO365B-07` | Detect and Avoid (DAA) & Well-Clear Separation | RTCA DO-365B | 1 | Well-Clear Re-establishment HMD Clear Hysteresis & Recovery Guidance | RTCA DO-365B §2.2.5.2 |
| `OBL-DO365B-08` | Detect and Avoid (DAA) & Well-Clear Separation | RTCA DO-365B | 1 | Non-Cooperative Radar & Cooperative ADS-B/TCAS Multi-Sensor Fusion | RTCA DO-365B §2.2.5.3 |
| `OBL-FMECA-MIL1629-01` | Failure Mode & Effects Criticality Analysis | MIL-STD-1629A | 1 | Severity Classification Rubric (1-10 Catastrophic to Negligible) | MIL-STD-1629A §4.3 |
| `OBL-FMECA-MIL1629-02` | Failure Mode & Effects Criticality Analysis | MIL-STD-1629A | 1 | Failure Probability / Occurrence Allocation Rubric (1-10 Frequent to Improbable) | MIL-STD-1629A §4.4 |
| `OBL-FMECA-MIL1629-03` | Failure Mode & Effects Criticality Analysis | MIL-STD-1629A | 1 | Failure Detection & Latency Bounding Rubric (1-10 Immediate BIT to Undetectable) | MIL-STD-1629A §4.5 |
| `OBL-FMECA-MIL1629-04` | Failure Mode & Effects Criticality Analysis | MIL-STD-1629A | 1 | Mode Criticality Number and Composite RPN Mathematical Quantification | MIL-STD-1629A §4.6 |
| `OBL-FMECA-ARP4761-01` | System Safety Assessment & Failure Analysis | SAE ARP4761 | 1 | Functional Hazard Assessment Severity Mapping & Catastrophic Hazard Controls | SAE ARP4761 §4.3.1 |
| `OBL-FMECA-ARP4761-02` | System Safety Assessment & Failure Analysis | SAE ARP4761 | 1 | Quantitative Failure Probability Allocation & Hourly Rate Modeling | SAE ARP4761 App. L |
| `OBL-FMECA-ARP4761-03` | System Safety Assessment & Failure Analysis | SAE ARP4761 | 1 | Piece-Part to Vehicle Level Failure Modes, Effects and Criticality Analysis | SAE ARP4761 §4.3.3 |
| `OBL-FMECA-ARP4761-04` | System Safety Assessment & Failure Analysis | SAE ARP4761 | 1 | Common Cause Analysis & Hardware/Software Partition Independence Check | SAE ARP4761 App. M |
| `OBL-FMECA-MIL882E-01` | System Safety & Hazard Analysis | MIL-STD-882E | 1 | System Hazard Analysis (SHA) Execution & Failure Mode Mapping | MIL-STD-882E Task 205 §4.2 |
| `OBL-FMECA-MIL882E-02` | System Safety & Hazard Analysis | MIL-STD-882E | 1 | Hazard Severity & Probability Risk Assessment Matrix Categorization | MIL-STD-882E Task 204 §4.2 |
| `OBL-FMECA-MIL882E-03` | System Safety & Hazard Analysis | MIL-STD-882E | 1 | Safety-Critical Function Thread Isolation & Bus Separation | MIL-STD-882E Task 208 §4.2 |
| `OBL-FMECA-MIL882E-04` | System Safety & Hazard Analysis | MIL-STD-882E | 1 | Mishap Risk Assessment & Engineering Mitigation Tracking | MIL-STD-882E Task 106 §4.2 |
| `OBL-FMECA-DO178C-01` | Airborne Software Safety & Fault Detection | RTCA DO-178C | 1 | Built-In Test (BIT) Software Fault Detection Latency Bounds & Test Hooks | RTCA DO-178C §6.3.1 |
| `OBL-FMECA-DO178C-02` | Airborne Software Safety & Fault Detection | RTCA DO-178C | 1 | Software Architectural Fault Containment & Memory Partitioning | RTCA DO-178C §6.3.2 |
| `OBL-FMECA-DO178C-03` | Airborne Software Safety & Fault Detection | RTCA DO-178C | 1 | Structural Coverage Analysis for Safety-Critical Software Logic | RTCA DO-178C §6.4.4 |
| `OBL-FMECA-DO178C-04` | Airborne Software Safety & Fault Detection | RTCA DO-178C | 1 | Software Verification of Redundancy Management & State Handover | RTCA DO-178C §6.4.3 |

## 4. External Additions & Domain Extensions Registry
All external additions, proprietary extensions, and domain-specific baselines MUST carry authoritative public clause citations. Un-cited additions are strictly prohibited.

| Extension ID | Category | Standard / Baseline ID | Declared Total | Target Metric / Obligation Count | Verification Mechanism | Public Clause Citation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

## 5. Clause-Level Allocation & Traceability Matrix
| Population ID | Standard ID | Clause Citation | Clause Title / Requirement Excerpt | Specification Phase | Downstream Spec File / Tag |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `OBL-DOD3000-01` | DoD Directive 3000.09 | DoD Directive 3000.09 §3.1 | Human Judgement in Use of Force Policies | Phase 1 (Structural) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-DOD3000-02` | DoD Directive 3000.09 | DoD Directive 3000.09 §3.1.a | Autonomous Engagement Limits & Safe Bounding | Phase 1 (Structural) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-DOD3000-03` | DoD Directive 3000.09 | DoD Directive 3000.09 §3.1.b | Fail-Safe Interlocks & Dynamic Abort Corridors | Phase 2 (Behavioral) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-DOD3000-04` | DoD Directive 3000.09 | DoD Directive 3000.09 §3.1.c | Cyber Safeguards & Anti-Tamper Weapon Arming | Phase 3 (Operational) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-STANAG4586-01` | NATO STANAG 4586 | NATO STANAG 4586 §4.2 | UCS Architectural Framework & Payload Control | Phase 1 (Structural) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-STANAG4586-02` | NATO STANAG 4586 | NATO STANAG 4586 §4.2.2 | Interoperability Levels 1 to 5 Functional Allocation | Phase 1 (Structural) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-STANAG4586-03` | NATO STANAG 4586 | NATO STANAG 4586 §5.1 | Data Link Interface Profiles & Redundancy Profiles | Phase 2 (Behavioral) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-STANAG4586-04` | NATO STANAG 4586 | NATO STANAG 4586 §5.1.4 | C2 Data Link Handover & Control Transfer Protocol | Phase 3 (Operational) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-CJCSI3121-01` | CJCSI 3121.01B | CJCSI 3121.01B Enclosure A §2.a | Unit Self-Defense & Hostile Act Determination | Phase 1 (Structural) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-CJCSI3121-02` | CJCSI 3121.01B | CJCSI 3121.01B Enclosure A §4.b | Positive Identification (PID) Multi-Sensor Fusion | Phase 1 (Structural) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-CJCSI3121-03` | CJCSI 3121.01B | CJCSI 3121.01B Enclosure B §3.c | Collateral Damage Mitigation & Blast Boundary | Phase 2 (Behavioral) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-CJCSI3121-04` | CJCSI 3121.01B | CJCSI 3121.01B Enclosure E §2.d | Escalation of Force & Weapon Arming Interlocks | Phase 3 (Operational) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-NIST80082-01` | NIST SP 800-82r3 | NIST SP 800-82r3 §4.2 | OT Threat Sources & Attack Vector Taxonomy | Phase 1 (Structural) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-NIST80082-02` | NIST SP 800-82r3 | NIST SP 800-82r3 §5.3 | OT Defense-in-Depth Zoning & Segmentation | Phase 1 (Structural) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-NIST80082-03` | NIST SP 800-82r3 | NIST SP 800-82r3 §6.2 | Wireless & RF C2 Cryptographic Controls | Phase 2 (Behavioral) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-NIST80082-04` | NIST SP 800-82r3 | NIST SP 800-82r3 §6.4 | Incident Response & Cyber Containment Isolation | Phase 3 (Operational) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-MITRE-01` | MITRE ATT&CK / D3FEND | MITRE ATT&CK for ICS §T0814 | Denial of Service Resistance & Bandwidth Protection | Phase 1 (Structural) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-MITRE-02` | MITRE ATT&CK / D3FEND | MITRE ATT&CK for ICS §T0855 | Unauthorized Command Message Rejection & HMAC | Phase 1 (Structural) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-MITRE-03` | MITRE ATT&CK / D3FEND | MITRE ATT&CK for ICS §T0843 | Program Download Prevention & Boot Chain Integrity | Phase 2 (Behavioral) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-MITRE-04` | MITRE ATT&CK / D3FEND | MITRE D3FEND §D3-MCR | Message Authentication & Anti-Replay Validation | Phase 3 (Operational) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-MIL461G-01` | MIL-STD-461G | MIL-STD-461G §5.4 | Conducted Susceptibility CS114/CS115/CS116 Bounds | Phase 1 (Structural) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-MIL461G-02` | MIL-STD-461G | MIL-STD-461G §5.18 | Radiated Susceptibility RS103 RF Field Hardening | Phase 1 (Structural) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-MIL461G-03` | MIL-STD-461G | MIL-STD-461G §5.19 | Radiated Susceptibility RS101 Magnetic Shielding | Phase 2 (Behavioral) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-MIL461G-04` | MIL-STD-461G | MIL-STD-461G §5.20 | Conducted Emissions CE102 Power Harmonic Control | Phase 3 (Operational) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-ISO21434-01` | ISO/SAE 21434 | ISO/SAE 21434 §5.3 | Cybersecurity Governance & Organization Policy | Phase 1 (Structural) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-ISO21434-02` | ISO/SAE 21434 | ISO/SAE 21434 §6.4 | Threat Analysis and Risk Assessment (TARA) Trees | Phase 1 (Structural) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-ISO21434-03` | ISO/SAE 21434 | ISO/SAE 21434 §9.4 | Attack Feasibility & Vulnerability Metric Rating | Phase 2 (Behavioral) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-ISO21434-04` | ISO/SAE 21434 | ISO/SAE 21434 §10.4 | Incident Verification & Hardware/Software V&V | Phase 3 (Operational) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-FAA10749-01` | FAA 14 CFR §107.49 | FAA 14 CFR §107.49(a) | Weather Conditions & Airspace Restriction Assessment | Phase 1 (Structural) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-FAA10749-02` | FAA 14 CFR §107.49 | FAA 14 CFR §107.49(b) | Ground Control Station & Link Power Pre-Flight Check | Phase 1 (Structural) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-FAA10749-03` | FAA 14 CFR §107.49 | FAA 14 CFR §107.49(c) | Aircraft Structural, Propulsion, and Battery Health Built-In Test | Phase 2 (Behavioral) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-FAA10749-04` | FAA 14 CFR §107.49 | FAA 14 CFR §107.49(d) | Non-Participant Safety & Flight Buffer Containment | Phase 3 (Operational) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-EASASPEC050-01` | AMC1 UAS.SPEC.050 | AMC1 UAS.SPEC.050 §3.2 | Specific Category Pre-Flight Operational Checklist | Phase 1 (Structural) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-EASASPEC050-02` | AMC1 UAS.SPEC.050 | AMC1 UAS.SPEC.050 §3.3 | In-Flight Contingency Management & Degraded C2 Link | Phase 1 (Structural) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-EASASPEC050-03` | AMC1 UAS.SPEC.050 | AMC1 UAS.SPEC.050 §4.1 | Site Survey & 3D Flight Geography Boundary Definition | Phase 2 (Behavioral) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-EASASPEC050-04` | AMC1 UAS.SPEC.050 | AMC1 UAS.SPEC.050 §4.4 | Post-Flight Safety Inspection & Digital Log Audit | Phase 3 (Operational) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-JARUSSORA-01` | JARUS SORA v2.5 | JARUS SORA v2.5 Annex B §B.2 | Ground Risk Mitigation M1/M2/M3 Parachute Impact | Phase 1 (Structural) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-JARUSSORA-02` | JARUS SORA v2.5 | JARUS SORA v2.5 Annex C §C.3 | Strategic Air Risk Mitigation (ARC Deconfliction) | Phase 1 (Structural) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-JARUSSORA-03` | JARUS SORA v2.5 | JARUS SORA v2.5 Annex D §D.2 | Tactical Mitigation Performance Standards (DAA Detect) | Phase 2 (Behavioral) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-JARUSSORA-04` | JARUS SORA v2.5 | JARUS SORA v2.5 Annex E §E.4 | Containment Integrity & OSO #01 to #24 Compliance | Phase 3 (Operational) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-DO362A-01` | RTCA DO-362A | RTCA DO-362A §2.2 | C2 Link Availability (99.99%) & Continuity Criteria | Phase 1 (Structural) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-DO362A-02` | RTCA DO-362A | RTCA DO-362A §2.2.1 | Terrestrial LOS C-Band/ISM RF Link Budget Margins | Phase 1 (Structural) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-DO362A-03` | RTCA DO-362A | RTCA DO-362A §2.2.4 | Beyond-Line-of-Sight (BLOS) SATCOM Link Handover | Phase 2 (Behavioral) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-DO362A-04` | RTCA DO-362A | RTCA DO-362A §3.4 | Lost C2 Link Dynamic Fallback Switching Execution | Phase 3 (Operational) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-ASTMF3411-01` | ASTM F3411-22a | ASTM F3411-22a §6.1 | Broadcast Remote ID Message Formats & RF Timing | Phase 1 (Structural) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-ASTMF3411-02` | ASTM F3411-22a | ASTM F3411-22a §6.3 | Direct RF Remote ID Handover & Degradation Alert | Phase 1 (Structural) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-ASTMF3411-03` | ASTM F3411-22a | ASTM F3411-22a §7.2 | Network Remote ID Transmit Latency & Broker SLA | Phase 2 (Behavioral) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-ASTMF3411-04` | ASTM F3411-22a | ASTM F3411-22a §8.4 | Cryptographic Auth & Remote ID Spoof Prevention | Phase 3 (Operational) | `docs/catalogs/MISSION_OPERATIONS_CATALOG.md` |
| `OBL-SORA-OSO-01` | JARUS SORA v2.5 Annex E | JARUS SORA v2.5 Annex E §E.1 | UAS Design Reliability & Airworthiness Standards Conformance | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-SORA-OSO-02` | JARUS SORA v2.5 Annex E | JARUS SORA v2.5 Annex E §E.2 | UAS Manufacturing Competency & Quality Management System Audit | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-SORA-OSO-03` | JARUS SORA v2.5 Annex E | JARUS SORA v2.5 Annex E §E.3 | UAS Maintenance System Competency & Part-ML Inspection Verification | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-SORA-OSO-04` | JARUS SORA v2.5 Annex E | JARUS SORA v2.5 Annex E §E.4 | Operational Environmental Condition Boundaries (Weather/Icing/Wind) | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-SORA-OSO-05` | JARUS SORA v2.5 Annex E | JARUS SORA v2.5 Annex E §E.5 | System Safety Assessment (SSA) & Single Point of Failure (SPOF) Analysis | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-SORA-OSO-06` | JARUS SORA v2.5 Annex E | JARUS SORA v2.5 Annex E §E.6 | C3 Datalink Performance, Latency & RF Link Loss Integrity | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-SORA-OSO-07` | JARUS SORA v2.5 Annex E | JARUS SORA v2.5 Annex E §E.7 | Safe Recovery from Human Error, Crew Competency & CRM Error-Proofing | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-SORA-OSO-08` | JARUS SORA v2.5 Annex E | JARUS SORA v2.5 Annex E §E.8 | Operational Procedures Definition, Validation & Adherence | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-SORA-OSO-09` | JARUS SORA v2.5 Annex E | JARUS SORA v2.5 Annex E §E.9 | Remote Flight Crew Training, Licensing & Currency Verification | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-SORA-OSO-10` | JARUS SORA v2.5 Annex E | JARUS SORA v2.5 Annex E §E.10 | Safe Design & Operation of Payload and External Cargo Equipment | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-SORA-OSO-11` | JARUS SORA v2.5 Annex E | JARUS SORA v2.5 Annex E §E.11 | Ground Support Equipment (GSE) & Launch/Recovery Maintenance | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-SORA-OSO-12` | JARUS SORA v2.5 Annex E | JARUS SORA v2.5 Annex E §E.12 | Safe Flight Operations in Adverse Meteorological Conditions | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-SORA-OSO-13` | JARUS SORA v2.5 Annex E | JARUS SORA v2.5 Annex E §E.13 | External Services (UTM, GNSS, Weather) Reliability & Integrity Assurance | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-SORA-OSO-14` | JARUS SORA v2.5 Annex E | JARUS SORA v2.5 Annex E §E.14 | Operational Containment Within 3D Volume & Ground Risk Buffer | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-SORA-OSO-15` | JARUS SORA v2.5 Annex E | JARUS SORA v2.5 Annex E §E.15 | Multi-Crew Coordination, Handover Protocol & Communications Interface | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-SORA-OSO-16` | JARUS SORA v2.5 Annex E | JARUS SORA v2.5 Annex E §E.16 | Multi-UAS Swarm Coordination & Dynamic Airspace Deconfliction | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-SORA-OSO-17` | JARUS SORA v2.5 Annex E | JARUS SORA v2.5 Annex E §E.17 | Payload Failure Containment & Hazardous Payload Safe-Lock Release | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-SORA-OSO-18` | JARUS SORA v2.5 Annex E | JARUS SORA v2.5 Annex E §E.18 | Automatic Flight Termination System (FTS) & Parachute Deployment | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-SORA-OSO-19` | JARUS SORA v2.5 Annex E | JARUS SORA v2.5 Annex E §E.19 | Flight Crew Fitness to Fly, Duty Limits & Fatigue Risk Management | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-SORA-OSO-20` | JARUS SORA v2.5 Annex E | JARUS SORA v2.5 Annex E §E.20 | Maintenance Human Factor Mitigations & Independent Inspection Audit | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-SORA-OSO-21` | JARUS SORA v2.5 Annex E | JARUS SORA v2.5 Annex E §E.21 | Environmental Sustainability, Acoustic Footprint & Chemical Safety | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-SORA-OSO-22` | JARUS SORA v2.5 Annex E | JARUS SORA v2.5 Annex E §E.22 | Security & Anti-Unlawful Interference Protection (Cyber & Physical) | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-SORA-OSO-23` | JARUS SORA v2.5 Annex E | JARUS SORA v2.5 Annex E §E.23 | Severe Environmental Resilience (Icing, Lightning, HIRF Shielding) | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-SORA-OSO-24` | JARUS SORA v2.5 Annex E | JARUS SORA v2.5 Annex E §E.24 | Fire Safety, Lithium Thermal Runaway Containment & Hazardous Materials | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-ASTMF3269-01` | Run-Time Assurance & Safety Net Architecture | ASTM F3269-17 | Dual-Channel Simplex RTA Architecture Framework Conformance | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-ASTMF3269-02` | Run-Time Assurance & Safety Net Architecture | ASTM F3269-17 | Simplex Safety Net Monitor & Attitude/Airspeed/Geofence Invariant Assertion | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-ASTMF3269-03` | Run-Time Assurance & Safety Net Architecture | ASTM F3269-17 | Dynamic Envelope Barrier Function & Deterministic State Switching Logic | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-ASTMF3269-04` | Run-Time Assurance & Safety Net Architecture | ASTM F3269-17 | Formal Proof Verification Slots & SLDV Property Prover Integration | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-ODID-01` | Remote Identification & Tracking Protocol | ASTM F3411-22a | Open Drone ID Basic ID Message (Type 0x0) Serial Number Encoding | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-ODID-02` | Remote Identification & Tracking Protocol | ASTM F3411-22a | Open Drone ID Location/Vector Message (Type 0x1) Kinematic Quantization | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-ODID-03` | Remote Identification & Tracking Protocol | ASTM F3411-22a | Open Drone ID Authentication Message (Type 0x2) Multi-Page Signature | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-ODID-04` | Remote Identification & Tracking Protocol | ASTM F3411-22a | Open Drone ID Self-ID Message (Type 0x3) Mission Description Payload | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-ODID-05` | Remote Identification & Tracking Protocol | ASTM F3411-22a | Open Drone ID System Message (Type 0x4) Operator Coordinates & Area Limit | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-ODID-06` | Remote Identification & Tracking Protocol | ASTM F3411-22a | Open Drone ID Operator ID Message (Type 0x5) Pilot Registration String | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-ODID-07` | Remote Identification & Tracking Protocol | ASTM F3411-22a | Message Pack (Type 0xF) Bundling & Direct RF Broadcast Frame Assembly | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-ODID-08` | Remote Identification & Tracking Protocol | ASTM F3411-22a | Network Remote ID Push Rates, REST/MQTT Broker Integration & Latency | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-FAA89310-01` | Civil Remote Identification Regulation | FAA 14 CFR §89.310 | Standard Remote ID Broadcast Message Elements & Continuity Mandate | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-FAA89310-02` | Civil Remote Identification Regulation | FAA 14 CFR §89.310 | Remote ID Minimum Broadcast Transmission Rates & 1.0s Max Interval | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-FAA89310-03` | Civil Remote Identification Regulation | FAA 14 CFR §89.310 | Direct Radio Frequency Unlicensed Broadcast Transmission Conformance | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-FAA89310-04` | Civil Remote Identification Regulation | FAA 14 CFR §89.310 | Remote ID Hardware Tamper Resistance & Cyber Integrity Enclosure | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-DO365B-01` | Detect and Avoid (DAA) & Well-Clear Separation | RTCA DO-365B | DAA Well-Clear Mathematical Volume Definition (DMOD, HMD, Tau_mod, ZTHR) | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-DO365B-02` | Detect and Avoid (DAA) & Well-Clear Separation | RTCA DO-365B | Horizontal Well-Clear Boundary & Modified Tau Collision Avoidance Math | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-DO365B-03` | Detect and Avoid (DAA) & Well-Clear Separation | RTCA DO-365B | Vertical Well-Clear Cylinder (ZTHR = 450 ft) & Tau-v Co-Altitude Gating | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-DO365B-04` | Detect and Avoid (DAA) & Well-Clear Separation | RTCA DO-365B | Warning Alert Time Horizon (25 s) & Immediate Maneuver Execution | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-DO365B-05` | Detect and Avoid (DAA) & Well-Clear Separation | RTCA DO-365B | Corrective Alert Horizon (55 s) & Recommended Pilot Avoidance Guidance | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-DO365B-06` | Detect and Avoid (DAA) & Well-Clear Separation | RTCA DO-365B | Preventative Alert Horizon (75 s) & Traffic Advisory Proximity Monitor | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-DO365B-07` | Detect and Avoid (DAA) & Well-Clear Separation | RTCA DO-365B | Well-Clear Re-establishment HMD Clear Hysteresis & Recovery Guidance | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-DO365B-08` | Detect and Avoid (DAA) & Well-Clear Separation | RTCA DO-365B | Non-Cooperative Radar & Cooperative ADS-B/TCAS Multi-Sensor Fusion | Phase 1 (Structural) | `docs/catalogs/SORA_AIRWORTHINESS_DAA_CATALOG.md` |
| `OBL-FMECA-MIL1629-01` | Failure Mode & Effects Criticality Analysis | MIL-STD-1629A | Severity Classification Rubric (1-10 Catastrophic to Negligible) | Phase 1 (Structural) | `docs/catalogs/FMECA_COMPONENT_CLASS_ROSTER_CATALOG.md` |
| `OBL-FMECA-MIL1629-02` | Failure Mode & Effects Criticality Analysis | MIL-STD-1629A | Failure Probability / Occurrence Allocation Rubric | Phase 1 (Structural) | `docs/catalogs/FMECA_COMPONENT_CLASS_ROSTER_CATALOG.md` |
| `OBL-FMECA-MIL1629-03` | Failure Mode & Effects Criticality Analysis | MIL-STD-1629A | Failure Detection & Latency Bounding Rubric | Phase 1 (Structural) | `docs/catalogs/FMECA_COMPONENT_CLASS_ROSTER_CATALOG.md` |
| `OBL-FMECA-MIL1629-04` | Failure Mode & Effects Criticality Analysis | MIL-STD-1629A | Mode Criticality Number and Composite RPN Quantification | Phase 2 (Behavioral) | `docs/catalogs/FMECA_COMPONENT_CLASS_ROSTER_CATALOG.md` |
| `OBL-FMECA-ARP4761-01` | System Safety Assessment & Failure Analysis | SAE ARP4761 | Functional Hazard Assessment Severity Mapping & Hazards | Phase 1 (Structural) | `docs/catalogs/FMECA_COMPONENT_CLASS_ROSTER_CATALOG.md` |
| `OBL-FMECA-ARP4761-02` | System Safety Assessment & Failure Analysis | SAE ARP4761 | Quantitative Failure Probability Allocation & Hourly Rates | Phase 1 (Structural) | `docs/catalogs/FMECA_COMPONENT_CLASS_ROSTER_CATALOG.md` |
| `OBL-FMECA-ARP4761-03` | System Safety Assessment & Failure Analysis | SAE ARP4761 | Failure Modes, Effects and Criticality Analysis Process | Phase 1 (Structural) | `docs/catalogs/FMECA_COMPONENT_CLASS_ROSTER_CATALOG.md` |
| `OBL-FMECA-ARP4761-04` | System Safety Assessment & Failure Analysis | SAE ARP4761 | Common Cause Analysis & Independence Verification | Phase 2 (Behavioral) | `docs/catalogs/FMECA_COMPONENT_CLASS_ROSTER_CATALOG.md` |
| `OBL-FMECA-MIL882E-01` | System Safety & Hazard Analysis | MIL-STD-882E | System Hazard Analysis Execution & Failure Mode Mapping | Phase 1 (Structural) | `docs/catalogs/FMECA_COMPONENT_CLASS_ROSTER_CATALOG.md` |
| `OBL-FMECA-MIL882E-02` | System Safety & Hazard Analysis | MIL-STD-882E | Hazard Severity & Probability Risk Assessment Matrix | Phase 1 (Structural) | `docs/catalogs/FMECA_COMPONENT_CLASS_ROSTER_CATALOG.md` |
| `OBL-FMECA-MIL882E-03` | System Safety & Hazard Analysis | MIL-STD-882E | Safety-Critical Function Thread Isolation & Bus Separation | Phase 2 (Behavioral) | `docs/catalogs/FMECA_COMPONENT_CLASS_ROSTER_CATALOG.md` |
| `OBL-FMECA-MIL882E-04` | System Safety & Hazard Analysis | MIL-STD-882E | Mishap Risk Assessment & Engineering Mitigation Tracking | Phase 3 (Operational) | `docs/catalogs/FMECA_COMPONENT_CLASS_ROSTER_CATALOG.md` |
| `OBL-FMECA-DO178C-01` | Airborne Software Safety & Fault Detection | RTCA DO-178C | Built-In Test Software Fault Detection Latency Bounds | Phase 1 (Structural) | `docs/catalogs/FMECA_COMPONENT_CLASS_ROSTER_CATALOG.md` |
| `OBL-FMECA-DO178C-02` | Airborne Software Safety & Fault Detection | RTCA DO-178C | Software Architectural Fault Containment & Partitioning | Phase 1 (Structural) | `docs/catalogs/FMECA_COMPONENT_CLASS_ROSTER_CATALOG.md` |
| `OBL-FMECA-DO178C-03` | Airborne Software Safety & Fault Detection | RTCA DO-178C | Structural Coverage Analysis for Safety-Critical Logic | Phase 2 (Behavioral) | `docs/catalogs/FMECA_COMPONENT_CLASS_ROSTER_CATALOG.md` |
| `OBL-FMECA-DO178C-04` | Airborne Software Safety & Fault Detection | RTCA DO-178C | Software Verification of Redundancy Management & Handover | Phase 3 (Operational) | `docs/catalogs/FMECA_COMPONENT_CLASS_ROSTER_CATALOG.md` |

## 6. Normative Completeness & Gap Analysis
| Metric Parameter | Value | Target Threshold | Compliance Status |
| :--- | :--- | :--- | :--- |
| Declared Total Normative Obligations | 112 | >= 1 | Conforming |
| Declared Total Safety Constraints | 112 | >= 1 | Conforming |
| Declared Total Operational Missions | 8 | >= 1 | Conforming |
| Declared Total Control Interlocks | 16 | >= 1 | Conforming |
| Clause Citation Traceability Percentage | 100% | 100% | Conforming |
| Un-Cited / Speculative Additions | 0 | 0 (Strict Zero Tolerance) | Conforming |
