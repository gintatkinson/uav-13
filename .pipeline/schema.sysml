doc /* Software Level A: Catastrophic failure condition prevention. Requires 100% MC/DC coverage and verified zero heap allocation. */
package DEAP_Safety_Architecture {
    doc /* Software Level A: Catastrophic failure condition prevention. Requires 100% MC/DC coverage and verified zero heap allocation. */
    package Certification_Requirements {
        requirement def DO178C_DAL_A {
            doc /* Software Level A: Catastrophic failure condition prevention. Requires 100% MC/DC coverage and verified zero heap allocation. */
        }
        requirement def DO178C_DAL_B {
            doc /* Software Level B: Hazardous failure condition mitigation. Requires 100% Decision/State coverage. */
        }
        requirement def DO178C_DAL_C {
            doc /* Software Level C: Major failure condition mitigation. Requires 100% Statement coverage. */
        }
        requirement def DO178C_DAL_D {
            doc /* Software Level D: Minor failure condition mitigation. */
        }
        requirement def DO178C_DAL_E {
            doc /* Software Level E: No safety effect. */
        }
        requirement def DO254_DAL_A_Hardware {
            doc /* Hardware Design Assurance Level A for Flight Control Computers and Actuator ICs. */
        }
        requirement def ARP4754A_SafetyAssessment {
            doc /* Functional Hazard Assessment (FHA), Preliminary System Safety Assessment (PSSA), and SSA validation. */
        }
        requirement def ARP4761_FMEA_PSSA {
            doc /* Failure Modes and Effects Analysis coupled with Fault Tree Analysis (FTA). */
        }
        requirement def SORA_SAIL_I {
            doc /* Specific Assurance and Integrity Level I (Low Risk UAS Operation). */
        }
        requirement def SORA_SAIL_II {
            doc /* Specific Assurance and Integrity Level II. */
        }
        requirement def SORA_SAIL_III {
            doc /* Specific Assurance and Integrity Level III (Medium Risk UAS Operation). */
        }
        requirement def SORA_SAIL_IV {
            doc /* Specific Assurance and Integrity Level IV (Controlled Airspace / BVLOS). */
        }
        requirement def SORA_SAIL_V {
            doc /* Specific Assurance and Integrity Level V (High Density Urban Operations). */
        }
        requirement def SORA_SAIL_VI {
            doc /* Specific Assurance and Integrity Level VI (Complex Category / Commercial Airliner Proximity). */
        }
    }
    doc /* Loss of Life / Aircraft Destruction: Complete hull loss and fatal injuries. */
    package System_Losses_And_Hazards {
        requirement def L_1 {
            doc /* Loss of Life / Aircraft Destruction: Complete hull loss and fatal injuries. */
        }
        requirement def L_2 {
            doc /* Loss of Mission / Severe Operational Failure: Total failure of flight objective, emergency divert required. */
        }
        requirement def L_3 {
            doc /* Damage to Ground Infrastructure: Destruction of runway, airport structures, or ground equipment. */
        }
        requirement def L_4 {
            doc /* Loss of System Availability / Margins: Reduction in avionic functional capability or safety margins. */
        }
        requirement def H_1 {
            doc /* Controlled Flight Into Terrain (CFIT): Airworthy aircraft flown into terrain under control or guidance. */
        }
        requirement def H_2 {
            doc /* Loss of Control in Flight (LOC-I): Aircraft attitude, altitude, or aerodynamic state exceeds normal flight envelope. */
        }
        requirement def H_3 {
            doc /* Mid-Air Collision (MAC): Loss of required horizontal or vertical separation between aircraft in controlled airspace. */
        }
        requirement def H_4 {
            doc /* Runway Incursion / Excursion: Aircraft departs runway surface during landing, takeoff, or ground taxi operations. */
        }
        requirement def H_5 {
            doc /* Airframe Structural Overstress: Aerodynamic or structural loads exceed ultimate design limits. */
        }
        requirement def H_6 {
            doc /* Uncommanded Engine Thrust Reversal: In-flight deployment of engine thrust reversers creating catastrophic asymmetric drag. */
        }
    }
    package Aircraft_State_Space {
    }
    doc /* Triple-modular redundant (TMR) primary flight control computer executing control loop laws. */
    package Avionic_System_Parts {
        doc /* Triple-modular redundant (TMR) primary flight control computer executing control loop laws. */
        part def FlightControlComputer {
            doc /* Triple-modular redundant (TMR) primary flight control computer executing control loop laws. */
            attribute redundant_channels : Integer = 3;
            attribute max_loop_latency_ms : Real = 10.0;
        }
        doc /* Trajectory generation and guidance engine providing waypoints and inner-loop commands. */
        part def AutopilotGuidanceEngine {
            doc /* Trajectory generation and guidance engine providing waypoints and inner-loop commands. */
            attribute dal_level : String = "DAL A";
        }
        doc /* Control Surface and Motor ESC actuator driver unit with feedback sensing. */
        part def ActuatorControlUnit {
            doc /* Control Surface and Motor ESC actuator driver unit with feedback sensing. */
            attribute refresh_rate_hz : Real = 400.0;
        }
        doc /* Telemetry command link terminal and operator interface station. */
        part def GroundControlStation {
            doc /* Telemetry command link terminal and operator interface station. */
            attribute link_frequency_mhz : Real = 2400.0;
        }
        doc /* Detect-and-Avoid sensor payload including TCAS, ADS-B In, Radar, and Optical sensors. */
        part def DAASensorSuite {
            doc /* Detect-and-Avoid sensor payload including TCAS, ADS-B In, Radar, and Optical sensors. */
            attribute range_meters : Real = 10000.0;
        }
    }
    doc /* ARINC 429 high-speed avionics serial bus port (100 kbps). */
    package Databus_Port_Definitions {
        port Arinc429Port : Port {
            attribute word_length_bits : Integer = 32;
            attribute parity : String = "Odd";
        }
        port Mil1553Port : Port {
            attribute bitrate_mbps : String = "1.0";
        }
        port C25GLinkPort : Port {
            attribute max_latency_ms : String = "20.0";
            attribute encrypted : String = "true";
        }
        port CanBusPort : Port {
            attribute baudrate_kbps : Integer = 1000;
        }
    }
    doc /* Flight Control Computer fails to provide Pitch Nose-Up Recovery Command during low altitude speed decay. */
    package STPA_Unsafe_Control_Actions {
        requirement def UCA_01 {
        }
        requirement def UCA_02 {
        }
        requirement def UCA_03 {
        }
        requirement def UCA_04 {
        }
        requirement def UCA_05 {
        }
        requirement def UCA_06 {
        }
        requirement def UCA_07 {
        }
        requirement def UCA_08 {
        }
        requirement def UCA_09 {
        }
        requirement def UCA_10 {
        }
        requirement def UCA_11 {
        }
        requirement def UCA_12 {
        }
        requirement def UCA_13 {
        }
        requirement def UCA_14 {
        }
        requirement def UCA_15 {
        }
        requirement def UCA_16 {
        }
    }
    doc /* FCC shall not command control surface deflection exceeding structural load limit +/- 30 deg. */
    package STPA_Safety_Control_Constraints {
        requirement def SC_1 {
        }
        requirement def SC_2 {
        }
        requirement def SC_3 {
        }
        requirement def SC_4 {
        }
        requirement def SC_5 {
        }
        requirement def SC_6 {
        }
        requirement def SC_7 {
        }
        requirement def SC_8 {
        }
        requirement def SC_9 {
        }
        requirement def SC_10 {
        }
        requirement def SC_11 {
        }
        requirement def SC_12 {
        }
        requirement def SC_13 {
        }
        requirement def SC_14 {
        }
        requirement def SC_15 {
        }
        requirement def SC_16 {
        }
        requirement def SC_17 {
        }
        requirement def SC_18 {
        }
        requirement def SC_19 {
        }
        requirement def SC_20 {
        }
        requirement def SC_21 {
        }
        requirement def SC_22 {
        }
        requirement def SC_23 {
        }
        requirement def SC_24 {
        }
        requirement def SC_25 {
        }
        requirement def SC_26 {
        }
        requirement def SC_27 {
        }
        requirement def SC_28 {
        }
        requirement def SC_29 {
        }
        requirement def SC_30 {
        }
        requirement def SC_31 {
        }
        requirement def SC_32 {
        }
    }
    doc /* FCC Processor Single-Event Upset (SEU) Stuck-at-Fault. */
    package FMECA_Risk_Profiles {
    }
    doc /* 100ms Major Frame cyclic executive schedule for partitioned avionics. */
    package Stateflow_Execution_State_Machines {
        state def ARINC653_MajorFrameSchedule {
        }
        state def Failsafe_StateMachine {
        }
    }
    doc /* Annotates SysML part definition as a MATLAB Simulink block subsystem. */
    package Simulink_Export_Profile {
    }
    doc /* Layer 1 (Domain State & Signal Model): Defines primary flight control data structures, continuous state vectors, and telemetry signal models. Binds to Certification_Requirements. */
    package Avionic_Control_Structure {
        doc /* Layer 1 (Domain State & Signal Model): Defines primary flight control data structures, continuous state vectors, and telemetry signal models. Binds to Certification_Requirements. */
        part def FlightControlStructure {
            attribute control_frequency_hz : Real = 400.0;
        }
    }
    doc /* Layer 2 (Logic & Safety State Management): Formal finite state machines, safety statecharts, and Mode Logic transition laws. Binds Layer 1 to Layer 3. */
    package Safety_Statecharts {
        doc /* Layer 2 (Logic & Safety State Management): Formal finite state machines, safety statecharts, and Mode Logic transition laws. Binds Layer 1 to Layer 3. */
        state def FailsafeStatechart {
        }
    }
    doc /* Layer 3 (Display & Actuator Interface Binding): Binding CDS widgets, ARINC 661 binary parameter buffers, vector symbology renders, and actuator control interfaces. */
    package ARINC661_Display_Interfaces {
        doc /* Layer 3 (Display & Actuator Interface Binding): Binding CDS widgets, ARINC 661 binary parameter buffers, vector symbology renders, and actuator control interfaces. */
        port ARINC661_WidgetBindingPort : Port {
            attribute widget_id : String = "Integer";
            attribute parameter_id : String = "Integer";
        }
        doc /* Physical interface binding display kernel rendering engines and actuator servo drivers. */
        part def DisplayActuatorBinding {
            attribute refresh_rate_hz : Real = 60.0;
        }
    }
}