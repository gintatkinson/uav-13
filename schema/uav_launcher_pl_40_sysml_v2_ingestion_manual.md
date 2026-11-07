# Level 0 Engineering Manual & Drawing Extraction: UAV Pneumatic Launcher PL-40 (REV 2.6)

## 1. Component & Subsystem Decomposition

| Component Name | Subsystem / Boundary | Symbol Type | Description / Drawing Callout |
| :--- | :--- | :--- | :--- |
| `UAV pneumatic launcher PL-40` | Top-Level System | System Boundary | Light-weight, battery-operated pneumatic catapult intended to accelerate UAVs and aircraft with MTOW up to $30\text{ kg}$ and launch speed up to $25\text{ m/s}$ (puller and pusher configurations). |
| `Rear part of the rail (1)` / `RAIL 1` | Rail Assembly (`UAV pneumatic launcher PL-40`) | Structural / Pneumatic Actuator Cylinder | Rear rail module (`RAIL 1`, `SERIAL No 1000`) housing the carriage initial launch position, carriage safety lock mechanism, and rear support leg mount. |
| `Rear support leg (2)` | `Rear part of the rail (1)` | Structural Support | Unfolding rear support leg attached to the rear part of the rail; connects to the anchor disk (`9`) and ground anchors (`8`). |
| `Middle part of the rail (3)` / `RAIL 2` | Rail Assembly (`UAV pneumatic launcher PL-40`) | Structural / Pneumatic Cylinder Tube | Center rail module (`RAIL 2`) with quick-release toggle clamps, O-ring seals, and end plates. |
| `Front part of the rail (4)` / `RAIL 3` | Rail Assembly (`UAV pneumatic launcher PL-40`) | Structural / Pneumatic Actuator Cylinder | Front rail module (`RAIL 3`, `SERIAL No 1000`) containing the internal pneumatic piston, pulling rope (`6`), roller block, front support legs (`5`), launcher air inlet port, and front shock absorbers/buffers. |
| `Front support legs (5)` | `Front part of the rail (4)` | Structural Support | Bipod folding front support legs with locking pin mechanism attached to the front rail module (`4`). |
| `Pulling rope (6)` | `Front part of the rail (4)` | Mechanical Transmission Element | High-strength pulling rope routed from the internal pneumatic piston around the roller block to the carriage (`7`). Replaced every $100$ launches via `PL-40 pulling rope replacement kit`. |
| `Carriage (7)` | Rail Assembly (`UAV pneumatic launcher PL-40`) | Mechanical Payload Carrier / Actuator Sled | Rolling sled assembly with four support levers, wheel bearings, rope attachment slots (3 slots), tension regulating screw, and rear lock mechanism. |
| `Carriage support levers` (Forward & Rear pairs, 4 pcs total) | `Carriage (7)` | Mechanical Payload Interface | Four pivoting upright arms (two forward, two rear) that engage the aircraft's drone-side connection hooks/hardpoints. |
| `Carriage safety lock pin` | `Rear part of the rail (1)` / `Carriage (7)` | Safety Interlock Pin | Red-handled quick-release safety pin with pull ring that secures the carriage (`7`) in the rear launch position prior to launch. |
| `Carriage locking mechanism` | `Rear part of the rail (1)` / `Carriage (7)` | Mechanical Latch / Release Mechanism | Rear latch mechanism that holds the carriage and releases when the safety lock pin is removed and the pulling rope (`6`) is pulled by the pressurized piston. |
| `Carriage lever lock pads` | `Carriage (7)` | Mechanical Adjustment Interface | Adjustable pads at the base of the carriage support levers adjusted to `ZERO GAP` via the `Holding bolt`, `Adjustment screw stopper`, and `Adjustment screw`. |
| `Carriage wheel bearings` (8 wheels on carriage; 4 pcs per replacement kit) | `Carriage (7)` | Mechanical Bearing Element | Guide rollers running in the white-lithium-greased rail groove; secured with threadlocker on threaded shafts (replaced every $100$ launches). |
| `Rail clamps` (Toggle clamps with `Clamp force adjustment screw`) | `Rear part of the rail (1)`, `Middle part of the rail (3)`, `Front part of the rail (4)` | Mechanical Fastener / Coupling | Hand-operated over-center clamps with force adjustment screws that lock the rail sections together with zero gap between tubes. |
| `Rail O-rings and end plates` | `Rear part of the rail (1)`, `Middle part of the rail (3)`, `Front part of the rail (4)` | Pneumatic Seal | Elastomeric O-ring seals seated in the rail end plates to seal the pneumatic cylinder tube across rail joints. |
| `Internal pneumatic piston` | `Front part of the rail (4)` | Pneumatic Actuator | Internal sliding piston inside the rail cylinder connected to the pulling rope (`6`) via a bolt and pin. |
| `Pneumatic safety mechanism (Over-acceleration shutoff valve)` | `Front part of the rail (4)` | Pneumatic Safety Valve | Internal pneumatic safety valve that shuts down inlet pressure if piston over-acceleration occurs (e.g., due to loose levers or launching without payload). |
| `Roller block` (Pulley assembly with green top guide plates and side plates) | `Front part of the rail (4)` | Mechanical Pulley / Rope Guide | Dual-pulley roller block mounted at the front rail with four bolts; redirects the pulling rope (`6`) $180^\circ$ from the internal piston to the carriage (`7`). |
| `Air supply system / Launcher inlet port` | `Front part of the rail (4)` | Pneumatic Port / Manifold | Angled male cam-lock pneumatic intake manifold bolted to the underside of the front rail (`4`); includes internal `Rope guide bushing`. |
| `Rope guide bushing` | `Air supply system / Launcher inlet port` | Mechanical / Pneumatic Seal Bushing | Threaded brass bushing through which the pulling rope (`6`) passes inside the air supply manifold. |
| `Front rail shock absorbers / buffers` (2 blue/silver cylinders at front end of `RAIL 3`) | `Front part of the rail (4)` | Mechanical Damper | Dual forward hydraulic/pneumatic shock absorbers mounted at the front end of `RAIL 3` to arrest the carriage at the end of the launch stroke. |
| `Ground anchors (8)` (3 pcs) | Anchoring Subsystem | Structural Ground Anchor | Three serrated metal ground stakes driven through the `Anchor disk (9)` into the soil using `Hammer (10)` or boot. |
| `Anchor disk (9)` / `Support disc` | Anchoring Subsystem | Structural Baseplate | Slotted metal baseplate mounted to the tip of `Rear support leg (2)` by turning $90^\circ$; receives three `Ground anchors (8)`. |
| `Hammer (10)` | Support Equipment | Hand Tool | Mallet/hammer used to drive `Ground anchors (8)` into the soil. |
| `Bag for ground anchors and hammer (11)` | Support Equipment | Storage Container | Storage pouch for `Ground anchors (8)`, `Anchor disk (9)`, and `Hammer (10)`. |
| `Compressor unit (12)` | Pneumatic Power & Control Subsystem | Power / Controller / Pneumatic Source | Self-contained wheeled flight case housing the battery-operated air compressor, main tank, electronic controller, valves, gauge, batteries, and trigger spool. |
| `Compressor (1)` | `Compressor unit (12)` | Pneumatic Actuator / Pump | $18\text{ V}$ DC battery-operated air compressor capable of pressurizing the main reservoir up to $14\text{ bar}$ in up to $8\text{ minutes}$. |
| `Tank side pressure connector (2)` | `Compressor unit (12)` | Pneumatic Port | Male cam-lock outlet fitting on the pneumatic main valve assembly where `Connection hose (14)` / `Pressure connecting hose (13)` attaches. |
| `Remote controlled release valve (3)` / `Main valve` | `Compressor unit (12)` | Pneumatic Valve / Actuator | Pneumatically/electrically actuated main launch valve triggered by `Trigger handle (13)` / `(15)` to release air from `Main tank (6)` into the launcher rail. |
| `Main reservoir outlet valve (4)` / `Main valve` (Manual ball valve) | `Compressor unit (12)` | Pneumatic Isolation Valve | Manual lever ball valve between `Main tank (6)` and `Remote controlled release valve (3)` used to isolate tank pressure before/after launch. |
| `Spare battery slot (5)` | `Compressor unit (12)` | Mechanical / Storage Holder | Slot in the compressor unit case for holding the second $18\text{ V}$ battery cartridge. |
| `Main tank (6)` / `Compressed air reservoir` | `Compressor unit (12)` | Pneumatic Energy Storage | High-pressure compressed air reservoir inside the compressor unit case (working pressure up to $14\text{ bar}$, or up to $16\text{ bar}$ via auxiliary source). |
| `Main battery (7)` / `2 Makita-type 18V batteries (15)` | `Compressor unit (12)` / `Trigger handle (13)` | Electrical Power Source | Makita $18\text{ V}$ Li-Ion $6000\text{ mAh}$ battery cartridges (Makita part nr. `BL1860B`). One powers the compressor unit; one attaches to the trigger handle. |
| `Pressure gauge (8)` / `Manometer` | `Compressor unit (12)` | Sensor (Visual Indicator) | Analog dial pressure manometer showing real-time air reservoir pressure in $\text{bar}$. |
| `Main battery slot (9)` | `Compressor unit (12)` | Electrical Connector / Dock | Active battery terminal dock on the compressor unit (`ATTENTION! 18V Li-ion BATTERY ONLY`). |
| `Power ON/OFF switch (10)` (`PWR LED`) | `Compressor unit (12)` | Controller Switch / Visual Indicator | Push-button ON/OFF switch with integrated green LED (`PWR LED`) illumination. |
| `Power switching circuit (11)` / `Electronic controller` | `Compressor unit (12)` | Electronic Controller | Electronic control unit with non-volatile memory, pressure sensor feedback ($0.05\text{ bar}$ hysteresis), overpressure protection ($14\text{ bar}$ max), and battery over-discharge protection ($14.5\text{ V}$ cutoff / $16\text{ V}$ recovery). |
| `SET button (12)` (`SET LED`) | `Compressor unit (12)` | Controller Input / Visual Indicator | Push-button with integrated red LED (`SET LED`) used to enter `SET MODE` and save target pressure to non-volatile memory. |
| `Connection hose (14)` / `Pressure connecting hose (13)` | Pneumatic Interconnect Subsystem | Pneumatic Hose / Harness | Flexible high-pressure hose with female cam-lock couplings (`Cam locks`) and `Securing ring` at both ends. |
| `Tank draining valve (14)` / `Pressure release valve` | `Compressor unit (12)` | Pneumatic Valve | Manual drain/bleed valve on the compressor unit panel used to release excess tank pressure or drain condensate. |
| `Trigger handle (13)` / `(15)` (`Remote trigger unit`) | Command & Launch Control Subsystem | Operator Controller | Dual-button handheld remote launch controller with two red safety levers/covers, two launch switches, red status LED, circular cable receptacle, and $18\text{ V}$ battery dock. |
| `Trigger handle cord spool (16)` | `Compressor unit (12)` | Electrical Cable / Spool | Orange multi-conductor control cable wound on a black reel connecting the `Compressor unit (12)` to the `Trigger handle (13)` / `(15)`. |
| `Spare air filters for the compressor (17)` | `Compressor unit (12)` | Maintenance Component | Replacement intake air filter elements stored inside the compressor unit lid. |
| `External filling port DIN 8 mm PCP (18)` | `Compressor unit (12)` | Pneumatic Port | External high-pressure pneumatic fill fitting (`DIN 8 mm PCP`) for charging via an external/auxiliary pressure source (up to $16\text{ bar}$). |
| `User manual (16)` | Documentation | Document | Physical user manual stored inside the lid of the rail transportation case (`17`). |
| `Transportation case for the rails (17)` | Packaging / Transport Subsystem | Structural Container | Wheeled hard flight case ($1480 \times 440 \times 170\text{ mm}$, $43\text{ kg}$ loaded) housing `RAIL 1`, `RAIL 2`, `RAIL 3`, `Carriage (7)`, `Bag (11)`, and `User manual (16)`. |
| `PL-40 pulling rope replacement kit` | Maintenance Kit | Spare Part Kit | Manufacturer replacement pulling rope assembly with pre-swaged eye terminals and rope guide bushing. |
| `Carriage wheel bearing replacement kit` | Maintenance Kit | Spare Part Kit | Kit containing `Wheel bearings - 4 pcs`, `Hex wrench - 1 pc`, and `Threadlocker - 1pc`. |
| `Makita battery charger DC18RC or DC18SD` | External Support Equipment | Electrical Charger | External battery charger (not provided) for charging Makita `BL1860B` $18\text{ V}$ batteries ($55\text{ min}$ for `DC18RC`, $130\text{ min}$ for `DC18SD`). |
| `Plane / Launched Payload` | External Payload System | Payload (Air Vehicle) | Fixed-wing UAV (puller or pusher configuration, MTOW up to $30\text{ kg}$) interfaced to `Carriage (7)` via `Plane connection hook option A`, `B`, or `C`. |
| `Plane connection hook option A` (`FRONT RIGHT CONNECTOR` & `REAR RIGHT CONNECTOR`) | `Plane / Launched Payload` Interface | Mechanical Hardpoint Interface | Separate front and rear hook brackets (Aluminum `6061-T6`, natural anode coating, $0.004\text{ kg}$, left side parts are mirrors of right side parts). |
| `Plane connection hook option B` | `Plane / Launched Payload` Interface | Mechanical Hardpoint Interface | Single-piece $225\text{ mm}$ longitudinal rail hook bar with dual notches engaging forward and rear carriage support levers. |
| `Plane connection hook option C` | `Plane / Launched Payload` Interface | Mechanical Hardpoint Interface | Threaded M8 flanged launch lugs/pins (Material: `AISI 304`, surface area $1390.16\text{ mm}^2$, natural anode coating) engaging notched carriage levers. |

---

## 2. Interface & Interconnect Topology

| Source Component | Source Port | Connection Type / Protocol | Target Component | Target Port | Signal / Payload Label | Directionality |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `Main battery (7)` (`18V Li-ion BL1860B`) | Battery Terminals | Electrical DC Power ($18\text{ V}$) | `Main battery slot (9)` (`Compressor unit (12)`) | Dock Contacts | $18\text{ V}$ DC Power (`18V Li-ion BATTERY ONLY`) | Unidirectional |
| `Main battery slot (9)` | Internal Wiring | Electrical DC Power | `Power switching circuit (11)` | Power In | Battery Voltage ($14.5\text{ V}$ cutoff / $>16\text{ V}$ recovery) | Unidirectional |
| `Power ON/OFF switch (10)` | Switch Contacts | Discrete Electrical Control | `Power switching circuit (11)` | `ON/OFF` Input | System Power ON/OFF Command | Unidirectional |
| `SET button (12)` | Button Contacts | Discrete Electrical Control | `Power switching circuit (11)` | `SET` Input | Target Pressure Set Mode / Save Command | Unidirectional |
| `Power switching circuit (11)` | LED Driver Out | Electrical / Optical Indicator | `Power ON/OFF switch (10)` (`PWR LED`) | Green LED | `PWR LED` State (OFF / ON / Blinking) | Unidirectional |
| `Power switching circuit (11)` | LED Driver Out | Electrical / Optical Indicator | `SET button (12)` (`SET LED`) | Red LED | `SET LED` State (OFF / ON / Blinking) | Unidirectional |
| `Power switching circuit (11)` | Motor Power Out | Electrical DC Power | `Compressor (1)` | Motor Terminals | `MOTOR STATE` (`ON` / `OFF`) | Unidirectional |
| `Compressor (1)` | Pneumatic Outlet | Pneumatic Line | `Main tank (6)` | Tank Inlet | Compressed Air (up to $14\text{ bar}$) | Unidirectional |
| `External filling port DIN 8 mm PCP (18)` | `DIN 8 mm PCP` Port | Pneumatic Line | `Main tank (6)` | Auxiliary Inlet | Auxiliary Compressed Air (up to $16\text{ bar}$) | Unidirectional |
| `Main tank (6)` | Pressure Sensing Port | Pneumatic Pressure | `Pressure gauge (8)` (`Manometer`) | Gauge Inlet | Reservoir Pressure ($\text{bar}$) | Unidirectional |
| `Main tank (6)` | Pressure Sensing Port | Pneumatic / Transducer Feedback | `Power switching circuit (11)` | Pressure Sensor In | Reservoir Pressure Feedback ($0.05\text{ bar}$ hysteresis) | Unidirectional |
| `Main tank (6)` | Drain Port | Pneumatic Line | `Tank draining valve (14)` | Valve Inlet | Air / Condensate Release | Unidirectional |
| `Main tank (6)` | Main Outlet | Pneumatic Manifold | `Main reservoir outlet valve (4)` | Valve Inlet | High-Pressure Air ($5\text{–}16\text{ bar}$) | Unidirectional |
| `Main reservoir outlet valve (4)` | Valve Outlet | Pneumatic Manifold | `Remote controlled release valve (3)` | Valve Inlet | Pressurized Air Supply to Main Valve | Unidirectional |
| `Main battery (15)` (2nd `18V Li-ion` unit) | Battery Terminals | Electrical DC Power ($18\text{ V}$) | `Trigger handle (13)` / `(15)` | Bottom Battery Dock | $18\text{ V}$ Trigger Power Supply (Figure 5-2) | Unidirectional |
| `Trigger handle (13)` / `(15)` | Circular Multi-Pin Plug | Electrical Control Harness (`Trigger handle cord spool (16)`) | `Compressor unit (12)` (`Remote controlled release valve (3)`) | Panel Circular Receptacle | Launch Start Command (Dual-switch simultaneous press $\ge 2\text{ s}$) | Unidirectional |
| `Remote controlled release valve (3)` | Valve Outlet | Pneumatic Port | `Tank side pressure connector (2)` | Male Cam-Lock Port | Rapid Launch Air Pulse | Unidirectional |
| `Tank side pressure connector (2)` | Male Cam-Lock Fitting | Pneumatic Hose (`Connection hose (14)` / `(13)`) | `Air supply system / Launcher inlet port` (`Front part of the rail (4)`) | Male Cam-Lock Fitting | High-Pressure Launch Air (Secured via `Locked Cam locks` & `Locked securing ring`) | Unidirectional |
| `Air supply system / Launcher inlet port` | Internal Cylinder Port | Pneumatic Flow | `Internal pneumatic piston` (`Front part of the rail (4)`) | Piston Face | Pneumatic Pressure Driving Piston Rearward | Unidirectional |
| `Internal pneumatic piston` | Piston Clevis (Bolt & Pin) | Mechanical Tension (`Pulling rope (6)`) | `Roller block` (`Front part of the rail (4)`) | Lower Pulley Entry (via `Rope guide bushing`) | Linear Pulling Force | Unidirectional |
| `Roller block` | Upper Pulley Exit | Mechanical Tension (`Pulling rope (6)`) | `Carriage (7)` | Rope Attachment Socket (3 slots + safety pin) | Forward Launch Traction Force | Unidirectional |
| `Carriage (7)` | 4 Support Levers | Mechanical Hardpoint Engagement (`TIGHT FIT`) | `Plane / Launched Payload` | `Plane connection hook option A / B / C` | Acceleration Force (up to $25\text{ m/s}$ at $12^\circ$ launch angle) | Unidirectional |
| `Rear part of the rail (1)` | Rear End Folding Joint | Mechanical Pivot (Step 1 & Step 2 Arrows) | `Rear support leg (2)` | Leg Hinge & End Stop | Unfolding Rotation & End-Position Seating (`ZERO GAP` / Seated Stop) | Unidirectional |
| `Rear part of the rail (1)` | Top Rail Track Groove | Mechanical Sliding Interface (Step 3 Arrow) | `Carriage (7)` | Wheel Bearings | Slide Carriage onto Rear Rail Section | Unidirectional |
| `Carriage safety lock pin` | Locking Pin Shaft | Mechanical Interlock (Step 4 & Step 5 Arrows) | `Carriage (7)` & `Rear part of the rail (1)` | Rear Lock Block Bore | Pin Insertion Securing Carriage & Support Levers in Upper Position | Unidirectional |
| `Middle part of the rail (3)` (`RAIL 2`) | Rear End Plate & O-Ring | Mechanical / Pneumatic Mating (Step 6, 7, 8, 10, 11 Arrows) | `Rear part of the rail (1)` (`RAIL 1`) | Front End Plate & Clamp Hooks | Rail Alignment, Clamp Release, Merging, Clamp Locking, and Screw Tensioning | Bidirectional |
| `Front part of the rail (4)` (`RAIL 3`) | Locking Pin & Bracket | Mechanical Release & Pivot (Step 12, 13, 14 Arrows) | `Front support legs (5)` | Leg Pivot Slots | Pin Push Release, Bipod Unfolding, and Lock Engagement | Unidirectional |
| `Front part of the rail (4)` (`RAIL 3`) | Rear End Plate & O-Ring | Mechanical / Pneumatic Mating (Step 15 Arrows) | `Middle part of the rail (3)` (`RAIL 2`) | Front End Plate & Clamp Hooks | Front Rail Alignment and Clamp Locking | Bidirectional |
| `Anchor disk (9)` (`Support disc`) | Central Bayonet Slot | Mechanical Twist-Lock (Step 16 Arrows) | `Rear support leg (2)` | Bottom Foot Stud | Upward Insertion and $90^\circ$ Rotation Lock | Unidirectional |
| `Ground anchors (8)` (3 pcs) | Anchor Stakes | Mechanical Ground Fastening (Step 17 & 18 Arrows) | `Anchor disk (9)` & Ground Soil | 3 Slotted Holes in Anchor Disk | Downward Insertion and Hammer/Boot Anchoring | Unidirectional |
| `Carriage (7)` | Wheel Bearings | Mechanical Track Check (Step 19 Bidirectional Arrows) | Assembled Rail (`RAIL 1`–`RAIL 2`–`RAIL 3`) | Greased Rail Groove | Smooth Forward and Rearward Motion Verification | Bidirectional |
| `Pulling rope (6)` | Swaged Eye Terminal | Mechanical Pin Joint (Step 20, 21, 22, 23, 25, 26 Arrows) | `Carriage (7)` | 3 Adjustment Slots, Groove, & Regulating Screw | Rope Attachment, Pin Locking, Groove Routing, and Tension Regulation | Unidirectional |
| `Carriage (7)` | Lever Lock Pad Assembly | Mechanical Screw Adjustment (Step 27 & 28 Arrows) | `Carriage support levers` | Lever Base Contact Pad | `Holding bolt`, `Adjustment screw stopper`, and `Adjustment screw` setting `ZERO GAP` | Unidirectional |
| `Compressor unit (12)` | Hinged Top Lid, Spool (`16`), & Hose (`14`) | Mechanical Deployment (Step 29 Arrows) | Operator / Field Setup | Unwound Trigger Cable & Attached Hose | Lid Opening, Hose Extraction, Trigger Unwinding, and Hose Connection | Unidirectional |
| `Connection hose (14)` | Female Cam-Lock Coupling | Mechanical Cam-Lock (Step 30 & 31 Arrows) | `Air supply system / Launcher inlet port` & `Tank side pressure connector (2)` | Male Cam-Lock Adapter | Turn Securing Ring $90^\circ$, Mate Coupling, Lock Cam Locks, Lock Securing Ring | Bidirectional |
| `Plane / Launched Payload` | Forward & Rear Slots / Hooks | Mechanical Placement Sequence (Figure 5-1 Green Arrows `STEP 1` & `STEP 2`) | `Carriage (7)` | Forward Support Levers (`STEP 1`) & Rear Support Levers (`STEP 2`) | Insert Forward Levers First (`STEP 1`), Lower Tail onto Rear Levers (`STEP 2`) | Unidirectional |
| `External Air Blow Source` (Maintenance) | Air Nozzle | Pneumatic Pressure (Figure 7-2 Arrow) | `Air supply system / Launcher inlet port` | Intake Port | Blow Air to Extract Internal Piston from `Front part of the rail (4)` | Unidirectional |
| `Internal pneumatic piston` | Retaining Bolt & Pin | Mechanical Disassembly (Figure 7-3 Arrows) | `Pulling rope (6)` | Rear Eye Terminal | Unscrew Bolt (Upward Arrow), Remove Pin (Downward Arrow), Extract Rope (Right Arrow) | Unidirectional |
| `Front part of the rail (4)` (`RAIL 3`) | 4 Mounting Bolts | Mechanical Disassembly (Figure 7-4 & 7-5 Arrows) | `Roller block` & `Air supply system` | Side Bolt Holes | Unscrew 4 Bolts (Outward Arrows), Extract Roller Block (Upward Arrow) & Air Supply System (Downward Arrow) | Unidirectional |
| `Air supply system / Launcher inlet port` | Threaded Bore | Mechanical Disassembly (Figure 7-6 & 7-7 Arrows) | `Rope guide bushing` & `Pulling rope (6)` | Bushing Threads | Unscrew Bushing (Curved Arrow) and Slide Air Supply Manifold Off Rope (Left/Right Arrows) | Unidirectional |
| `Roller block` | Side Plate Retaining Bolt | Mechanical Disassembly (Figure 7-8 & 7-9 Arrows) | `Roller block side plate` | Side Plate Threads | Unscrew Bolt and Remove Side Plate to Access Rope Around Pulleys | Unidirectional |
| `Carriage wheel bearing shaft` | Left-Hand Threaded Shaft ($250^\circ\text{C}$ heated) | Mechanical Maintenance (Figure 7-11 & 7-12 Arrows) | `Carriage (7)` Frame | Threaded Boss | Heat to $250^\circ\text{C}$, Turn Clockwise to Unscrew/Remove; Apply Threadlocker and Turn Counterclockwise to Reinstall with Support Washer | Bidirectional |
| `Environment (Wind)` | Ambient Airflow | Aerodynamic Vector (Page 40 Schematic Blue Arrows) | `UAV pneumatic launcher PL-40` | Front of Rail | `WIND DIRECTION` (Directly opposing `LAUNCH DIRECTION`) | Unidirectional |
| `UAV pneumatic launcher PL-40` | Rail Axis | Kinematic Vector (Page 40, 43, 44, 45 Green Arrows) | `Plane / Launched Payload` | Trajectory | `LAUNCH DIRECTION` (Forward along rail; defines forward `DANGER ZONE / KEEP CLEAR` vs. rear `SAFETY AREA`) | Unidirectional |
| `Plane / Launched Payload` | Center of Mass (`G`) | Gravitational / Mass Envelope (Page 42 Green Arrow `G`) | `Carriage (7)` Support Envelope | $200\text{ mm} \times 100\text{ mm}$ Hatched Box | `ALLOWED CENTER OF MASS POSITION FOR LAUNCHED PAYLOAD` relative to `GROUND LEVEL` | Unidirectional |

---

## 3. Drawing Notes & Physical Constraints

| Note / Constraint ID | Scope (Component or System) | Parameter / Constraint Statement | Value & Units |
| :--- | :--- | :--- | :--- |
| `SPEC-SYS-01` | `UAV pneumatic launcher PL-40` | Launch angle | $12\text{ degrees}$ ($12^\circ$) |
| `SPEC-SYS-02` | `UAV pneumatic launcher PL-40` | Overall rail length when assembled | $5\text{ m}$ |
| `SPEC-SYS-03` | `UAV pneumatic launcher PL-40` | Rail length when disassembled | $1.28\text{ m}$ |
| `SPEC-SYS-04` | `UAV pneumatic launcher PL-40` | Weight of catapult set, 2 boxes | $\text{Total } 68\text{ kg}$ |
| `SPEC-SYS-05` | `Transportation case for the rails (17)` | Launcher case external dimensions and mass | $1480 \times 440 \times 170\text{ mm}$, $43\text{ kg}$ |
| `SPEC-SYS-06` | `Compressor unit (12)` | Compressor case external dimensions and mass | $360 \times 360 \times 680\text{ mm}$, $25\text{ kg}$ |
| `SPEC-SYS-07` | `Plane / Launched Payload` | Maximum plane mass (MTOW) | $30\text{ kg}$ |
| `SPEC-SYS-08` | `Plane / Launched Payload` | Maximum allowed launch velocity | $25\text{ m/s}$ (meter per second) |
| `SPEC-SYS-09` | `Plane / Launched Payload` | Puller configuration aircraft compatibility | `YES` |
| `SPEC-SYS-10` | `Plane / Launched Payload` | Pusher configuration aircraft compatibility | `YES` |
| `SPEC-SYS-11` | `UAV pneumatic launcher PL-40` | Set-up time | $5\text{ min}$ |
| `SPEC-SYS-12` | `UAV pneumatic launcher PL-40` | Working temperature | $-20\dots+50\text{ }^\circ\text{C}$ |
| `SPEC-COMP-01` | `Power switching circuit (11)` | Pressure regulation hysteresis | $0.05\text{ bar}$ |
| `SPEC-COMP-02` | `Compressor unit (12)` | Maximum internal compressor working pressure | $14\text{ bar}$ (takes up to $8\text{ minutes}$ to reach) |
| `SPEC-COMP-03` | `External filling port DIN 8 mm PCP (18)` | Auxiliary pressure source maximum pressure | Up to $16\text{ bar}$ via `DIN 8 mm PCP` port |
| `SPEC-BATT-01` | `Main battery (7)` / `(15)` | Battery specification & part number | Makita $18\text{ V}$ Li-Ion $6000\text{ mAh}$, Part nr. `BL1860B` |
| `SPEC-BATT-02` | `Power switching circuit (11)` | Over-discharge protection cutoff voltage | $\le 14.5\text{ V}$ (turns compressor off, `ON LED` flashes) |
| `SPEC-BATT-03` | `Power switching circuit (11)` | Over-discharge recovery voltage and delay | $> 16\text{ V}$ with a $5\text{ s}$ delay before restarting compressor |
| `SPEC-BATT-04` | `Makita battery charger DC18RC / DC18SD` | Battery charging time & ambient temperature range | `DC18RC`: $\approx 55\text{ min}$; `DC18SD`: $\approx 130\text{ min}$ at $10^\circ\text{C}\text{–}40^\circ\text{C}$ ($50^\circ\text{F}\text{–}104^\circ\text{F}$) |
| `SPEC-MAINT-01` | `Pulling rope (6)` & `Carriage wheel bearings` | Scheduled replacement interval | Every $100\text{ launches}$ (and visual check before/after every launch) |
| `SPEC-MAINT-02` | `Carriage wheel bearings` | Bearing removal heating temperature & thread direction | Heat threaded shaft area to $\approx 250^\circ\text{C}$; turn **clockwise** to unscrew/remove, **counterclockwise** to reinstall |
| `SPEC-MAINT-03` | Rail Groove Lubrication | Recommended lubricant | White lithium grease (`WD-40 White Lithium Grease`) on all sides of the rail groove |
| `DIM-INST-01` | `Carriage (7)` Front View (Page 41) | Upper lever inner/outer spacing & tip height | Outer width: $156\text{ mm}$; Inner width: $140\text{ mm}$; Upper tip slot height: $30\text{ mm}$; Lower carriage width: $103\text{ mm}$ / $162\text{ mm}$ |
| `DIM-INST-02` | `Carriage (7)` Side View (Page 41) | Longitudinal & vertical carriage dimensions | Overall length: $271\text{ mm}$; Lever tip-to-tip span: $206.5\text{ mm}$; Overall height: $232.5\text{ mm}$; Forward lever clearance: $145\text{ mm}$; Rear lever clearance: $155.5\text{ mm}$ |
| `DIM-INST-03` | `UAV pneumatic launcher PL-40` Rear View (Page 41) | Overall height and front bipod stance width | Overall height: $1115\text{ mm}$; Front support leg footprint width: $602\text{ mm}$ |
| `DIM-INST-04` | `Plane / Launched Payload` Center of Mass (Page 42) | Allowed Center of Mass (`G`) envelope | $200\text{ mm}$ (longitudinal) $\times 100\text{ mm}$ (normal to rail) hatched zone above carriage support levers |
| `DIM-HOOK-A` | `Plane connection hook option A` (Page 43) | Hook geometry and material properties | Span between hooks: $186\text{ mm}$ / $178\text{ mm}$ / $206\text{ mm}$; Bracket length: $20\text{ mm}$, width: $16\text{ mm}$, thickness $s = 8\text{ mm}$; Holes: $\varnothing 3.2$, `CSNK` $\varnothing 6.3 \times 90^\circ$ (Front) / $\varnothing 6.94 \times 90^\circ$ (Rear), $2\text{ holes}$; Material: `Aluminum 6061-T6`, Surface area: $1117.53\text{ mm}^2$, Coating: `Natural anode`, Mass: $0.004\text{ kg}$, Tolerances: `ISO 2768-m`, Surface roughness: $Ra\text{ }6.3$ |
| `DIM-HOOK-B` | `Plane connection hook option B` (Page 44) | Hook bar geometry | Total length: $225\text{ mm}$; Mounting hole spacing: $165\text{ mm}$ ($35\text{ mm}$ from front end); Height: $16\text{ mm}$; Thickness: $s = 8\text{ mm}$; Holes: $\varnothing 5.3$ ($2\text{ holes}$); Chamfers: $4 \times 45^\circ$ ($2\text{ chamfers}$); Notch length: $24\text{ mm}$, depth: $7.5\text{ mm}$ / $2\text{ mm}$, radii: $R3$, angles: $45^\circ$; Tolerances: `ISO 2768-m`, Surface roughness: $Ra\text{ }6.3$ |
| `DIM-HOOK-C` | `Plane connection hook option C` (Page 45) | Launch pin geometry and material properties | Lever span: $320\text{ mm}$ longitudinal, $156\text{ mm}$ / $140\text{ mm}$ upper width, $103\text{ mm}$ base width; Pin total length: $33.5\text{ mm}$ ($17.5\text{ mm}$ head side, $16\text{ mm}$ threaded shaft, $10\text{ mm}$ thread length, $10\text{ mm}$ neck length, $2.5\text{ mm}$ flange thickness, $30^\circ$ taper); Thread: `M8` ($1 \times 45^\circ$ chamfer); Flange diameter: $\varnothing 13$ ($1 \times 45^\circ$), neck diameter: $\varnothing 8$, hex across flats: $13\text{ mm}$; Material: `AISI 304`, Surface area: $1390.16\text{ mm}^2$, Coating: `Natural anode` |
| `SAFE-01` | Global System Safety | Payload requirement | `NEVER LAUNCH WITHOUT PAYLOAD as it will damage the device and surrounding persons!` |
| `SAFE-02` | Global System Safety | Rear leg ground anchoring | `NEVER LAUNCH WITHOUT SECURING LAUNCHERS REAR LEG TO THE GROUND` |
| `SAFE-03` | Global System Safety | Personal protective equipment | `ALWAYS USE GLOVES AND GOGGLES when servicing the plane or the launcher!` |
| `SAFE-04` | Global System Safety | Personnel safety zone | `ATTENTION! Before launching make sure that all team members are in safety area behind the launcher!` |
| `SAFE-05` | Global System Safety | Carriage safety lock pin timing | `ATTENTION! Remove the carriage safety lock only just before the launch!` |
| `SAFE-06` | Global System Safety | Pneumatic tubing handling | `ATTENTION! Do not handle any pneumatic tubing until making sure that the valve of the main pressure tank is closed!` |
| `SAFE-07` | Global System Safety | Pre-pressurization interlock | `ATTENTION! Carriage has to be secured by the safety lock pin before opening the main valve!` |
| `SAFE-08` | Global System Safety | Main valve operation | `WARNING! Open the main valve only before launch and close it after launch as soon as possible! Ignoring that may cause accidental sled or pressure release and lead to serious injuries or death!` |

---

## 4. Complete Verbatim Manual Transcription (Pages 1–45)

### [Page 1] Cover Page

* **Manufacturer Logo**: `Eli`
* **Title**: `UAV pneumatic launcher PL-40`
* **Subtitle**: `user manual`
* **Illustration**: Full isometric rendering of the assembled PL-40 launcher rail supported by the front bipod legs and rear anchored leg, connected via the black pressure hose and orange trigger cord to the compressor unit and remote trigger handle.
* **Footer**: `Tallinn 2026` | `ELI Military Simulations` | `REV 2.6`

---

### [Page 2] Contents

| Section | Title | Page |
| :--- | :--- | :--- |
| — | Introduction | 3 |
| 1 | Important safety instruction | 3 |
| 2 | Overview | 4 |
| 3 | Rail assembling procedure | 7 |
| 4 | Compressor unit | 21 |
| 4.1 | Overview | 21 |
| 4.2 | Operation | 22 |
| 4.3 | Setting the target pressure | 22 |
| 4.4 | Over discharge protection | 23 |
| 5 | Launching procedure | 24 |
| 6 | Disassembly procedure | 27 |
| 7 | Maintenance | 28 |
| 7.1 | Battery maintenance | 28 |
| 7.2 | Launcher maintenance | 28 |
| 7.3 | Pulling rope replacement | 29 |
| 7.4 | Wheel bearing replacement | 34 |
| 8 | Technical Specifications | 37 |
| 9 | Safety area schematics | 40 |
| 10 | Plane installation documentation in standard configuration | 41 |

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `2 Page`

---

### [Page 3] Introduction & 1 Important safety instruction

#### Introduction

The UAV pneumatic launcher is intended to accelerate UAV-s and other aircraft at takeoff with MTOW up to $30\text{ kg}$ and launch speed $25\text{ m/s}$. The launcher is light-weight, battery-operated and is quickly assembled. Device can be used for both puller and pusher propeller configuration aircraft.

The scope of this manual is to describe guidelines and procedures of the launcher assembly, disassembly and operation. These instructions must be strictly followed to ensure launch safety and trouble-free operation of the launcher.

#### 1 Important safety instruction

Read these instructions carefully to avoid possible injury or property damage.

* **[!] NEVER LAUNCH WITHOUT PAYLOAD** as it will damage the device and surrounding persons!
* **[!] NEVER LAUNCH WITHOUT SECURING LAUNCHERS REAR LEG TO THE GROUND** Backlash can move launcher and throw plane off it prematurely resulting in possible crash or other accident!
* **[Gloves & Goggles Icon] ALWAYS USE GLOVES AND GOGGLES** when servicing the plane or the launcher!
* **[!] ATTENTION!** Before launching make sure that all team members are in safety area behind the launcher!
* **[!] ATTENTION!** Remove the carriage safety lock only just before the launch!
* **[!] ATTENTION!** Do not handle any pneumatic tubing until making sure that the valve of the main pressure tank is closed!
* **[!] ATTENTION!** Carriage has to be secured by the safety lock pin before opening the main valve!
* **[Warning Triangle Icon] WARNING!** Open the main valve only before launch and close it after launch as soon as possible! Ignoring that may cause accidental sled or pressure release and lead to serious injuries or death!

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `3 Page`

---

### [Page 4] 2 Overview

All components are packed into two cases for easy transportation and handling (Figure 2-2 & Figure 2-3).

The launcher has following parts (Figure 2-1):
* Rear part of the rail (`1`) with rear support leg (`2`)
* Middle part of the rail (`3`)
* Front part of the rail (`4`) with front support legs (`5`) and pulling rope (`6`)
* Carriage (`7`)
* Ground anchors (`8`)
* Anchor disk (`9`) (The appearance may vary depending on the configuration)
* Hammer (`10`) (The appearance may vary depending on the configuration)
* Bag for ground anchors and hammer (`11`)
* Compressor unit (`12`)
* Trigger handle (`13`)
* Connection hose (`14`)
* 2 Makita-type $18\text{V}$ batteries (`15`)
* User manual (`16`)
* Transportation case for the rails (`17`)

**Figure 2-1**: *Launcher kit parts (Design and equipment may vary depending on the configuration)* — Callouts `(1)` through `(17)` pointing to each component in exploded isometric view.

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `4 Page`

---

### [Page 5] Figure 2-2 Packed launcher rails

* **Illustration**: Top-down view of the open `Transportation case for the rails (17)` showing:
  * Left lid interior: `User manual (16)` held by a strap.
  * Right main compartment:
    * Left rail slot: `RAIL 3` (`Front part of the rail (4)`) with blue `Pulling rope (6)`, green `Roller block`, and dual front shock buffers.
    * Center rail slot: `RAIL 1` (`Rear part of the rail (1)`) with `Carriage (7)` mounted at the top end (secured by red safety lock pin) and orange `Bag for ground anchors and hammer (11)` stowed alongside. Rail placards visible: `DO NOT LAUNCH WITHOUT PAYLOAD!`.
    * Right rail slot: `RAIL 2` (`Middle part of the rail (3)`).
* **Caption**: *Figure 2-2 Packed launcher rails*
* **Footer**: `REV 2.6` | `ELI Military Simulations` | `5 Page`

---

### [Page 6] Figure 2-3 Packed pneumatic system

* **Illustration**: Photograph of the open `Compressor unit (12)` case showing the internal compressor, Makita $18\text{V}$ battery installed on the dock with yellow warning placard `ATTENTION! 18V Li-ion BATTERY ONLY`, pressure gauge, blue-handled manual ball valve, cam-lock outlet port, orange trigger cable wound on the black spool, and spare air filters mounted in the top lid.
* **Caption**: *Figure 2-3 Packed pneumatic system*
* **Footer**: `REV 2.6` | `ELI Military Simulations` | `6 Page`

---

### [Page 7] 3 Rail assembling procedure (Steps 1–3)

Before assembling the launcher choose the appropriate place and direction for takeoff. Determine wind direction and prefer to launch the pane directly into the wind.

* **[i] It is recommended to use an assistant when assembling the rails!**
* **Step 1**: Take the rear rail and unfold the support leg. *(Illustration shows `Rear part of the rail (1)` and curved red arrow indicating downward unfolding of `Rear support leg (2)`)*
* **Step 2**: Make sure that the rear leg is properly seated at the end position. *(Illustration shows red arrow pointing to the zero-gap seated joint between the rear leg and the rear rail stop block; placards on leg read `ATTENTION! REMOVE SAFETY LOCK BEFORE LAUNCH` and `ATTENTION! OPEN VALVE BEFORE LAUNCH`)*
* **Step 3**: Place the carriage on rail and slide it to the end section. *(Illustration shows `Carriage (7)` being slid onto the front end of `Rear part of the rail (1)` with a red directional arrow pointing toward the rear end)*

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `7 Page`

---

### [Page 8] Rail assembling procedure (Steps 4–5)

* **Step 4**: Secure the carriage with the safety lock pin. *(Illustration shows red arrow pointing left into the rear lock block for inserting the red `Carriage safety lock pin`; placard on rear leg reads `ATTENTION! OPEN VALVE BEFORE LAUNCH`)*
* **Step 5**: Make sure, that carriage support levers are in the upper position when locking the safety lock pin. *(Side-view illustration of `Carriage (7)` showing red arrow pointing to the rear lever lug engaged by the safety lock pin while the support levers are upright)*

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `8 Page`

---

### [Page 9] Rail assembling procedure (Steps 6–7)

* **Step 6**: Line up the rear and the middle part of the rail. *(Illustration shows two red arrows pointing from the middle rail section toward the rear rail section)*
* **Step 7**: Release the clamps and merge the rails. Check that the O-rings are properly seated and that the end plates are clean. *(Close-up illustration of the rail joint showing `RAIL 1 SERIAL No 1000`, `ATTENTION! DANGEROUS AREA`, the circular O-ring in the end plate, two red arrows indicating clamp release, and two red arrows indicating rail mating)*

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `9 Page`

---

### [Page 10] Rail assembling procedure (Steps 8–9)

* **Step 8**: Lock the clamps and make sure that they are tightly secured in the locking position. *(Two illustrations showing red straight and curved arrows hooking the clamp loops over the catches and pressing the clamp levers flat; placards read `RAIL 1 SERIAL No 1000` and `ATTENTION! DANGEROUS AREA`)*
* **Step 9**: There should be no gaps or slacks between the tubes. *(Side view of an improperly joined rail seam with a V-shaped gap between end plates, marked with a large red `X` and curved red arrow at the bottom gap; placard reads `ATTENTION! DANGEROUS AREA`)*

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `10 Page`

---

### [Page 11] Rail assembling procedure (Steps 10–11)

* **Step 10**: Use the clamp force adjustment screw to tighten the connection. *(Close-up view of the rail toggle clamp showing a red arrow pointing to the hex socket cap screw and a bidirectional rotational arrow)*
* **Step 11**: When adjusted correctly, the tubes should have no gaps and operator is able to open and close the clamps by hand force. *(Side view of flush rail joint marked with a large green checkmark and two red arrows pointing to the tight upper and lower joint seams; placard reads `ATTENTION! DANGEROUS AREA`)*

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `11 Page`

---

### [Page 12] Rail assembling procedure (Steps 12–14)

* **Step 12**: Push the locking pin to release the front support legs. *(Illustration of `Front part of the rail (4)` showing a straight red arrow pointing to the leg bracket locking pin and two curved red arrows showing the folded legs swinging downward)*
* **Step 13**: Move the legs into position. *(Illustration of `Front part of the rail (4)` upright on `Front support legs (5)` with two curved red arrows showing the two legs spreading apart into a bipod)*
* **Step 14**: Make sure that the leg is secured and the lock has been engaged. *(Close-up of the front leg bracket showing a red arrow pointing outward along the locking pin axis to verify engagement)*

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `12 Page`

---

### [Page 13] Rail assembling procedure (Steps 15–17)

* **Step 15**: Merge the front rail with the rest of the launcher assembly using the same method as in Step 6 & Step 7. *(Illustration showing two red arrows mating `Front part of the rail (4)` onto `Middle part of the rail (3)`)*
* **Step 16**: Mount the support disc turning it $90\text{ degrees}$. *(Close-up of the bottom tip of `Rear support leg (2)` showing `Anchor disk (9)` moving upward along a straight red arrow and rotating $90^\circ$ along a curved red arrow)*
* **Step 17**: Make sure that the front rail support legs are in their end position before placing the anchors. The appearance of the anchor and support disc may vary depending on the configuration. *(Illustration showing three `Ground anchors (8)` moving downward along three red arrows into the slots of `Anchor disk (9)`)*

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `13 Page`

---

### [Page 14] Rail assembling procedure (Steps 18–19)

* **Step 18**: Secure the anchor using hammer or boot. Make sure that the soil is strong enough to withstand the launch forces. If not, the launch may fail and cause serious damage or injury. The catapult's anchoring to the ground must ensure that it cannot move during launch. The catapult operator is responsible for making sure the catapult is properly secured to the ground, using additional anchors in soft soil, etc. *(Illustration showing the three ground anchors fully driven through the support disc at the base of the rear support leg)*
* **Step 19**: By moving the carriage back and forth make sure that the carriage is moving smoothly and have no jams or obstacles. After completion move the carriage back to the rear end of the rail and secure it with safety lock pin. *(Full view of assembled rail with two long red arrows pointing forward and backward along the rail from `Carriage (7)`)*

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `14 Page`

---

### [Page 15] Rail assembling procedure (Steps 20–21)

* **Step 20**: Connect the pulling rope to the furthest socket that the rope reaches and secure it with the safety pin. Make sure, that the rope is undamaged and clean, if not, then the rope must be replaced (see paragraph 7.3 on page 29). *(Close-up of `Carriage (7)` showing two red arrows pointing to the blue `Pulling rope (6)` eye terminal and the cotter/safety pin inside the carriage tension link)*
* **Step 21**: Make sure that the rope is passing the groove as above. *(Front-angled close-up of `Carriage (7)` showing a red arrow pointing to the blue pulling rope seated cleanly inside the front guide pulley/groove between the forward support levers)*

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `15 Page`

---

### [Page 16] Rail assembling procedure (Steps 22–23)

* **Step 22**: There are three slots for attaching and are used to compensate the length changes of the pulling rope. *(Close-up of `Carriage (7)` with three red arrows pointing to the three sequential attachment slots on the carriage rope link)*
* **Step 23**: Attached rope must have enough tension. Make sure to check it before every launch. If the tension cannot be achieved then the rope must be replaced as shown on (paragraph 7.3). *(Isometric view of `Carriage (7)` locked at the rear of the rail with a red arrow pointing to the taut blue pulling rope)*

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `16 Page`

---

### [Page 17] Rail assembling procedure (Steps 24–26)

* **Step 24**: It is not recommended to launch with an unregulated pulling rope. If it is not possible to achieve the correct rope tension, it is important to ensure that the rope moves freely along the rail and that nothing obstructs its movement. A loose pulling rope may create a strong shock load at the moment of launch, which could result in excessive acceleration of the airframe. *(Side view of rear rail showing a slack blue rope resting on the rail surface, marked with a large red `X` and two red arrows pointing to the carriage link and the sagging rope)*
* **Step 25**: Use the available three rope slots and/or the regulating screw to obtain the proper pulling rope tension. *(Close-up of the rear of `Carriage (7)` showing a straight red arrow and bidirectional rotation arrows pointing to the hex socket regulating screw)*
* **Step 26**: Properly adjusted rope should not be leaning on the rail but in the same time the tension should not be able to disengage the locking mechanism in the rear of the carriage. The carriage locking mechanism should engage only when the safety pin is removed and rope is pulled by a pressurized piston. *(Side view of the rail marked with a large green checkmark and three red arrows pointing to the engaged rear lock mechanism and the taut, elevated pulling rope clear of the rail)*

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `17 Page`

---

### [Page 18] Rail assembling procedure (Steps 27–28)

* **Step 27**: Make sure that levers are tightly inserted into plane's connection hooks. There should be no gap between levers lock pads. No lever movement should be present when the plane engine is throttled up and down. Inside the launcher are pneumatic safety mechanisms for shutting down the inlet pressure when piston over-acceleration occurs. Loose levers will momentarily over-accelerate the piston engaging the safety valve and the launch will fail.
  * *Drawing Callouts*: `TIGHT FIT` (two red arrows pointing to forward and rear lever tips engaged with a longitudinal hook bar), `ZERO GAP` (red arrow pointing to the rear lever lock pad contact point).
* **Step 28**: For adjusting the gap release the holding bolt and adjusting screw stopper. Change the height of the lock pad with the adjusting screw until there is no gap between lock bad and lever. Tighten the bolt and adjusting screw stopper. Same procedure must be completed for both levers.
  * *Drawing Callouts*:
    * `Zero cap` *(points to zero-gap contact interface between lever lug and lock pad)*
    * `Holding bolt` *(points to side clamping bolt on lock pad block)*
    * `Adjustment screw stopper` *(points to lock nut on vertical adjustment screw)*
    * `Adjustment screw` *(points to bottom vertical adjustment screw head)*

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `18 Page`

---

### [Page 19] Rail assembling procedure (Steps 29–30)

* **Step 29**: Open the lid of the compressor unit. Unwind the trigger handle and attach the connection hose. *(Two isometric views of `Compressor unit (12)`: Left view shows a curved red arrow opening the lid and two upward red arrows extracting the orange trigger cable spool and connection hose; Right view shows an inward red arrow attaching `Connection hose (14)` to the tank-side pressure connector and a downward red arrow unwinding the orange trigger cable)*
* **Step 30**: Connect one end of the connection tubing to the launcher inlet port and the other end of the tubing to the tank-side pressure connector. Before connecting the hoses, loosen the cam lock securing ring and the cam locks.
  * *Drawing Callouts*:
    * Rail placards: `ATTENTION! OPEN VALVE BEFORE LAUNCH`, `ATTENTION! DANGEROUS AREA`
    * `Open cam locks` *(two red arrows pointing to the open cam-lock arms)*
    * `The securing ring is in the closed position. Turn 90° to set it to the open position` *(red arrow pointing to the black knurled securing collar on `Connection hose (14)`)*

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `19 Page`

---

### [Page 20] Rail assembling procedure (Steps 31–32)

* **Step 31**: After connecting both ends of the connection hoses, ensure that the cam locks are locked and that the cam lock secure ring is preventing the cam locks from opening.
  * *Drawing Callouts*:
    * `Locked Cam locks` *(two red arrows pointing to folded cam-lock levers)*
    * `Locked securing ring` *(red arrow pointing to the rotated securing ring tab blocking the cam-lock levers)*
* **Step 32**: Move the remote trigger unit to the determined position behind the rails. The launcher is now assembled and ready for start. *(Full isometric view of the assembled launcher with the orange trigger cord routed behind the rear support leg anchor to the trigger handle)*

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `20 Page`

---

### [Page 21] 4 Compressor unit — 4.1 Overview

#### 4.1 Overview

The catapult has battery operated air compressor with compressed air reservoir, electronic controller, and pneumatically operated main valve with remote trigger, pressure release valve, pressure gauge and safety valve.

The air compressor is operated by electronic controller that enables setting desired target pressure and protects system from overpressure and battery over discharge. The controller has ON/OFF switch with green LED illumination and SET button with red LED illumination.

The main parts of the compressor unit are shown in Figure 4-1:
* `1` - Compressor
* `2` - Tank side pressure connector
* `3` - Remote controlled release valve
* `4` - Main reservoir outlet valve
* `5` - Spare battery slot
* `6` - Main tank
* `7` - Main battery
* `8` - Pressure gauge
* `9` - Main battery slot
* `10` - Power ON/OFF switch
* `11` - Power switching circuit
* `12` - SET button
* `13` - Pressure connecting hose
* `14` - Tank draining valve
* `15` - Trigger handle
* `16` - Trigger handle cord spool
* `17` - Spare air filters for the compressor
* `18` - External filling port DIN $8\text{ mm}$ PCP

**Figure 4-1**: *Main parts of the compressor unit* — Callouts `1` to `18` plus placard `ATTENTION! 18V Li-ion BATTERY ONLY`.

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `21 Page`

---

### [Page 22] 4.2 Operation & 4.3 Setting the target pressure

#### 4.2 Operation

The controller is turned on by pushing ON/OFF switch to ON position. The controller checks battery voltage and pressure inside air reservoir. If the battery voltage is higher than cutoff voltage, ON LED is illuminated and if air pressure is lower than preset target pressure, the controller turns on the compressor and lights SET LED up. When target pressure is reached the controller stops the compressor. The controller hold determined pressure with $0.05\text{ bar}$ hysteresis and the catapult is ready for launch. After launch the controller charges the reservoir to the target pressure again.

If during initial check up the pressure in the reservoir is higher than target pressure, the compressor stays switched off and the SET LED flashes.

##### Table 1 Compressor unit LED states (illuminated push-buttons)

| PWR LED | SET LED | MOTOR STATE | SYSTEM STATUS |
| :--- | :--- | :--- | :--- |
| LED off | LED off | `OFF` | Turned OFF |
| LED on | LED off | `OFF` | Target pressure reached |
| LED on | LED blinking | `OFF` | Pressure in the tank is over the target pressure |
| LED on | LED on | `ON` | Pressurizing to target pressure |
| LED on | LED off | `ON` | SET MODE (Pressurizing tank) |
| LED blinking | LED off | `OFF` | SET MODE (Maximum pressure reached to $14\text{ bar}$) |
| LED blinking | `X` (Any state) | `OFF` | Battery voltage too low |

*Legend*: Green Solid Square = `LED on` | White Empty Square = `LED off` | Hatched Square = `LED blinking` | `X` = `Any state`

* **[!] ATTENTION!** Before launching the plane always check the pressure on the manometer, making sure, that the target pressure is achieved.

#### 4.3 Setting the target pressure

To set or change target pressure the controller must be started in set mode. To enter SET MODE turn the device off, hold SET button pressed and turn it on again and release SET button. The controller enters SET MODE, turns SET LED off and starts the compressor. Monitor the pressure gauge and press the SET button when desired pressure is reached.

The controller stops the compressor, writes the new target pressure to the non-volatile memory, lights the SET LED up and resumes the normal operation.

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `22 Page`

---

### [Page 23] 4.3 Setting the target pressure (cont.) & 4.4 Over discharge protection

**NB!** Make sure that the pressure in the reservoir is lower than the new target pressure before entering SET MODE. Use pressure release valve if necessary.

If the controller is in the SET MODE and the maximum pressure $14\text{ bar}$ is reached before SET button is pressed the compressor stops. If now the SET button is pressed then this maximum pressure is saved as new target pressure.

By turning off the controller before SET button is pressed, the set mode is canceled and previous target pressure remains in the memory.

#### 4.4 Over discharge protection

The controller protects battery from destructive over discharge. When the battery voltage is fallen to or is below $14.5\text{V}$, controller turns the compressor off and keeps ON LED flashing. When the battery recovers and voltage rises over $16\text{V}$, the controller turns, after a $5\text{ second}$ delay, the compressor on again. It enables to get all remaining charge out of the battery. However, it is recommended to change the battery immediately after the protection engages.

* **[!] ATTENTION!** Do not handle any pneumatic tubing until making sure that the valve of the main pressure tank is closed!
* **[!] ATTENTION!** Carriage has to be secured by the safety lock pin before opening the main valve!
* **[Warning Triangle Icon] WARNING!** Open the main valve only before launch and close it after launch as soon as possible! Ignoring that may cause accidental sled or pressure release and lead to serious injuries or death!

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `23 Page`

---

### [Page 24] 5 Launching procedure (Steps 1–10)

* **[!] WARNING!** Never use launcher without the plane! It can damage the device!
* **[!] ATTENTION!** It is user responsibility to maintain relationship between plane mass and determined launch pressure so, that maximum launch velocity $25\text{ m/s}$ is not exceeded. Consult Table 2 in Technical Specifications section.

For launching the plane perform the following steps:
1. Unpack and assemble the rail (Chapter 3, on page 7)
2. Make sure, that the carriage is in its initial position and secured with safety lock pin.
3. Make sure that the pulling rope is attached to the carriage and tensioned properly.
4. Make sure, that the compressor unit ON/OFF switch (`10`) is in OFF position and the main reservoir outlet valve (`4`) is in closed position.
5. Install pressure hose connecting main valve outlet and the launcher inlet (`13`). Make sure that the clamps are perfectly locked and securing ring also locked Step 31.
6. Insert a fully charged battery cartridge into its connection slot (`9`) on the compressor unit.
7. Turn the automatic ON/OFF switch (`10`) ON. The compressor starts working and stops automatically when the pressure in the reservoir reaches preset value (up to $14\text{bar}$). It can take up to $8\text{ minutes}$ until the maximum working pressure is achieved. The value of the determined pressure can be regulated via SET MODE (Chapter 4.3, on page 22).
8. When the determined pressure is achieved, compressor stops. Check the pressure manometer on the pressure regulation valve to assure that the determined pressure is achieved. It is normal for the compressor to switch on from time to time for short periods of time to keep requested pressure.
9. If the compressor stops before the determined pressure is achieved the battery may be empty. Check the indication LED and change battery if necessary.
10. Place the plane on the launcher so that the two forward support levers of the carriage are inserted into their slots first, then lower the tail of the plane so that the rear pair of support levers are inserted into their slots (Figure 5-1). Make sure that all four support levers are correctly in their positions and the plane sits evenly. Ensure that all drone-side hardpoints are straight, parallel, and securely tightened.

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `24 Page`

---

### [Page 25] Launching procedure (Steps 11–12 & Figures 5-1, 5-2)

* **Figure 5-1**: *Placing the plane on the launcher* — Left image shows red aircraft fuselage above carriage with green arrows labeled `STEP 1` (forward lever insertion) and `STEP 2` (rear lever insertion); Right image shows aircraft seated on all four levers.
* **Step 11**: Make sure that carriage safety pin is installed and remote release handle prepared and unengaged. Open slowly the air reservoir outlet valve (`4`) on the compressor to pressurize main valve.
* **Step 12**: When the plane is ready to launch, make sure that all personnel have moved to the safety area (see Chapter 9, on page 40), remove the carriage safety lock pin. For launching move the safety levers up and then press both switches simultaneously. Hold the switches up for at least two seconds. After the start command ends, move the safety levers down again. (Figure 5-3).
* **Figure 5-2**: *Connect the plug at the end of the cable to the trigger handle and connect battery* — Left photo shows operator connecting circular plug to trigger handle; Right photo shows Makita $18\text{V}$ battery attached to underside of trigger handle.

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `25 Page`

---

### [Page 26] Launching procedure (Step 13 & Figure 5-3)

* **Figure 5-3**: *Trigger handle. For launching move the safety levers up and then press both switches simultaneously. Hold the switches up for at least two seconds. When initiating the start command, a red LED lights up on the remote trigger handle. After the start command ends, move the safety levers down again. The launcher is now assembled and ready for launching.*
* **[!] NB!** Keep the trigger handle buttons pressed until the plane has left the catapult! Releasing the trigger button closes the main valve and avoids unnecessary pressure loss.
* **NOTE!** If the carriage safety lock pin has not been removed and launch trigger is pressed by chance then you have to start over and repeat all launch preparation steps as described above!
* **[!] ATTENTION!** Keep the safety cover closed at all times to avoid unwanted launcher release. Ignoring that may cause serious injuries.
* **Step 13**: To prepare for the next launch move the carriage to the initial position and secure it with safety lock. Wait for the compressor to build up determined pressure. For safety reasons it is recommended to close air reservoir outlet valve between launches to avoid accidental carriage release by pressing the trigger handle buttons. It is recommended to change the battery with a fully charged one after the first launch and then change the battery at least after every two consecutive launches.

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `26 Page`

---

### [Page 27] 6 Disassembly procedure

* **[!] WARNING!** Make sure, that the main valve (`4`) is closed before any further actions. Ignoring that may cause serious injuries.

To disassemble the catapult, perform the following steps:
1. Close the air reservoir outlet valve (`4`).
2. Turn the compressor OFF.
3. Disconnect pressure delivery tube from the launcher and the main tank.
4. Move carriage to rail rear module (to the area of launch position) and remove the pulling rope from carriage. Remember to put the fastening pin back to its place.
5. Remove ground anchors
6. Open the clamps and dismantle the rail, leaving carriage to the rear rail module.
7. Pack all the parts into their cases.

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `27 Page`

---

### [Page 28] 7 Maintenance (7.1 Battery maintenance & 7.2 Launcher maintenance)

#### 7.1 Battery maintenance

Option 1: Makita's $18\text{V}$ Li-Ion $6000\text{mAh}$ battery cartridges, Makita part nr. `BL1860B` and Makita battery charger `DC18RC` or `DC18SD`.
Charging time for empty battery is about:
a) $55\text{ min}$ for `DC18RC` charger or
b) $130\text{ min}$ for `DC18SD` charger

**NOTE!** Battery charger is not provided as voltage and socket may vary by country!

**Tips for maintaining maximum battery life:**
* Charge the battery cartridge before completely discharged.
* Never recharge a fully charged battery cartridge. Overcharging shortens the battery service life.
* Charge the battery cartridge with room temperature at $10^\circ\text{C} - 40^\circ\text{C}$ ($50^\circ\text{F} - 104^\circ\text{F}$).
* Let a hot battery cartridge cool down before charging it.

#### 7.2 Launcher maintenance

* Check the pulling rope for broken cords. Change the rope if necessary.
* Check that wheels of the carriage are undamaged and are rotating freely.
* Check that the carriage is moving freely on the rail.
* Check that the parts of the rail are clean. Clean if necessary.
* **[WD-40 Icon]** Check that the catapult rail groove (all sides of the groove) where the carriage moves is covered with white lithium grease as needed. We recommend using WD-40 White Lithium Grease.
* Check for the air leakages from tubing between main reservoir and main valve. Tighten the clamps if necessary.
* Check that carriages support levers are undamaged and are moving freely.
* Check that the rail parts are connected tightly. Tighten the rail clamps if necessary.
* Ensure that all drone-side hardpoints are straight, parallel, and securely tightened.
* **[!] WARNING!** Unmaintained launcher may cause launch failures, damage to the equipment and serious injuries.

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `28 Page`

---

### [Page 29] 7.3 Pulling rope replacement

#### Maintenance instructions

* Pulling rope should be replaced regularly after $100\text{ launches}$.
* Visual checks should be performed before and after every launch.
* The rope must be replaced immediately when significant wear detected, tear or loose fibers have appeared.
* Make sure that the rope is kept away from mud and dirt during launcher assembling and disassemble.
* The rope replacement can be performed using PL-40 pulling rope replacement kit sold by manufacturer.

**Figure 7-1**: *PL-40 pulling rope replacement kit*

* **[!] WARNING!** Unmaintained pulling rope may cause launch failures, damage to the equipment and serious injuries.

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `29 Page`

---

### [Page 30] Pulling rope replacement instructions (Figures 7-2 & 7-3)

* **Figure 7-2**: *Take the front rail and blow some air into the air intake connector to extract the piston.* *(Red arrow pointing to the angled air intake connector on the underside of the front rail while the piston and rope extend from the rear of the front rail)*
* **Figure 7-3**: *Unscrew the bolt and remove the pin.* *(Exploded view of the extracted piston showing an upward red arrow on the locking bolt, a downward red arrow on the clevis pin, and a rightward red arrow on the pulling rope eye terminal)*

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `30 Page`

---

### [Page 31] Pulling rope replacement instructions (Figures 7-4 & 7-5)

* **Figure 7-4**: *Unscrew four bolts holding the roller block.* *(Close-up of `RAIL 3 SERIAL No 1000` showing four outward red arrows on the four socket head bolts securing the green-capped roller block; placards read `ATTENTION! OPEN VALVE BEFORE LAUNCH` and `ATTENTION! DANGEROUS AREA`)*
* **Figure 7-5**: *Extract the roller block and air supply system.* *(Illustration showing an upward red arrow lifting the roller block out of the top slot of the rail and a downward/angled red arrow pulling the air supply intake manifold out from the bottom of the rail)*

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `31 Page`

---

### [Page 32] Pulling rope replacement instructions (Figures 7-6 & 7-7)

* **Figure 7-6**: *Unscrew the rope guide bushing.* *(Close-up of the air supply manifold and roller block showing a curved red arrow unscrewing the brass `rope guide bushing` from the rear of the manifold)*
* **Figure 7-7**: *Remove the air supply system.* *(Illustration showing a leftward red arrow pulling the air supply manifold off the end of the rope and a rightward red arrow sliding the unscrewed bushing along the rope)*

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `32 Page`

---

### [Page 33] Pulling rope replacement instructions (Figures 7-8 & 7-9)

* **Figure 7-8**: *Unscrew bolt holding the side plate.* *(Illustration of the roller block showing a red arrow extracting the lower flat-head screw from the side plate)*
* **Figure 7-9**: *Remove the side plate to gain access to the rope.* *(Illustration showing two red arrows detaching the side plate and green top guide bar from the dual pulleys to expose the pulling rope path)*

Follow same steps in reverse order to complete the rope replacment.

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `33 Page`

---

### [Page 34] 7.4 Wheel bearing replacement

#### Maintenance instructions

* Wheel bearings should be replaced regularly after $100\text{ launches}$.
* Visual checks for signs of wear, damage, or contamination should be performed before and after every launch.
* Keep the bearing area clean and free of contaminants. Dust, dirt, and debris can accelerate wear and damage.
* Use appropriate cleaning methods, such as compressed air or a mild solvent, to remove contaminants from the bearing and track.
* The bearings should be replaced immediately when significant wear, cracks or sealing damage detected.
* The bearing replacement can be performed using carriage replacement kit sold by manufacturer.
  1. Wheel bearings - $4\text{ pcs}$
  2. Hex wrench - $1\text{ pc}$
  3. Threadlocker - $1\text{pc}$

**Figure 7-10**: *Carriage wheel bearing replacement kit*

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `34 Page`

---

### [Page 35] Bearing removal (Figure 7-11)

#### Bearing removal

* **Preparation**: Ensure you have the necessary tools and safety equipment, including the hex wrench provided in the kit.
* **Heat the Threaded Area**: Use a heat source to raise the temperature of the area where the wheel bearing shaft is threaded onto the shaft to approximately $250\text{ degrees Celsius}$. This heating process is essential to soften the thread lock adhesive, making it easier to remove the shaft.
* **Unscrew the Wheel Bearing Shaft**: While heating the threaded area, turn the wheel bearing shaft clockwise using the hex wrench. This action will help loosen and remove the shaft from the assembly. The application of heat aids in breaking the adhesive's grip.
* **Remove the Bearing**: Once the shaft is sufficiently loosened, you can remove the wheel bearing from the shaft either by hand or by using a press tool if it is stuck.
* **ATTENTION!** Without applying heat to soften the adhesive before attempting to remove the wheel bearing, there is a higher risk of damaging the bearing shaft's hex slot during the dismantling process.
* **ATTENTION!** Carefully observe the direction of thread opening.
* **Figure 7-11**: *Wheel bearing removal* *(Shows heat gun icon applying $250\text{ C}^\circ$ to the bearing mount and hex wrench turning clockwise to remove the bearing shaft and washer)*

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `35 Page`

---

### [Page 36] Bearing reassembly (Figure 7-12)

#### Bearing reassembly

* **Preparation**: Ensure you have the necessary tools and safety equipment, including the hex wrench and thread lock glue provided in the kit.
* **Assembly**: Install the bearing and support washer as shown in Figure 1-3 *(Figure 7-12)*. Apply the adhesive to the shaft thread and then proceed to reinstall the bearing shaft turning the wrench counterclockwise.
* After replacing the bearings, ensure that the sled moves freely on the track.

**Figure 7-12**: *Wheel bearing reassembly* *(Exploded view showing the threadlocker tube applying blue adhesive to the bearing shaft threads, aligned with the wheel bearing, support washer, and carriage frame hole)*

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `36 Page`

---

### [Page 37] 8 Technical Specifications & Table 2

#### 8 Technical Specifications

| Parameter | Specification |
| :--- | :--- |
| Launch angle | $12\text{ degrees}$ |
| Overall rail length when assembled | $5\text{ m}$ |
| Rail length when disassembled | $1.28\text{ m}$ |
| Weight of catapult set, 2 boxes | $\text{Total } 68\text{ kg}$ |
| Launcher case external dimensions | $1480 \times 440 \times 170\text{ mm}$, $43\text{ kg}$ |
| Compressor case external dimensions | $360 \times 360 \times 680\text{ mm}$, $25\text{ kg}$ |
| Maximum plane mass | $30\text{ kg}$ |
| Maximum allowed launch velocity | $25\text{ m/s}$ (meter per second) |
| Puller configuration aircraft | `YES` |
| Pusher configuration aircraft | `YES` |
| Set-up time | $5\text{ min}$ |
| Working temperature | $-20\dots+50\text{ C}^\circ$ |

* **[!] ATTENTION!** It is user responsibility to maintain relationship between plane mass and determined launch pressure so, that maximum launch velocity $25\text{ m/s}$ is not exceeded.

#### Table 2 Approximate launch velocities versus plane mass and launching pressure

| Pressure (bar) / Plane mass (kg) | 10 kg | 15 kg | 20 kg | 30 kg |
| :--- | :--- | :--- | :--- | :--- |
| $5\text{ bar}$ | $18.4\text{ m/s}$ | $15.1\text{ m/s}$ | $13.1\text{ m/s}$ | $10.7\text{ m/s}$ |
| $6\text{ bar}$ | $20.2\text{ m/s}$ | $16.5\text{ m/s}$ | $14.3\text{ m/s}$ | $11.7\text{ m/s}$ |
| $7\text{ bar}$ | $21.8\text{ m/s}$ | $17.9\text{ m/s}$ | $15.5\text{ m/s}$ | $12.6\text{ m/s}$ |
| $8\text{ bar}$ | $23.3\text{ m/s}$ | $19.1\text{ m/s}$ | $16.5\text{ m/s}$ | $13.5\text{ m/s}$ |
| $9\text{ bar}$ | $24.8\text{ m/s}$ | $20.3\text{ m/s}$ | $17.6\text{ m/s}$ | $14.3\text{ m/s}$ |
| $10\text{ bar}$ | $26.1\text{ m/s}$ | $21.3\text{ m/s}$ | $18.5\text{ m/s}$ | $15.1\text{ m/s}$ |
| $11\text{ bar}$ | — | $22.4\text{ m/s}$ | $19.4\text{ m/s}$ | $15.8\text{ m/s}$ |
| $12\text{ bar}$ | — | $23.4\text{ m/s}$ | $20.3\text{ m/s}$ | $16.5\text{ m/s}$ |
| $13\text{ bar}$ | — | $24.3\text{ m/s}$ | $21.1\text{ m/s}$ | $17.2\text{ m/s}$ |
| $14\text{ bar}$ | — | $25.3\text{ m/s}$ | $21.9\text{ m/s}$ | $17.9\text{ m/s}$ |
| $15^{*}\text{ bar}$ | — | $26.1\text{ m/s}$ | $22.7\text{ m/s}$ | $18.5\text{ m/s}$ |
| $16^{*}\text{ bar}$ | — | — | $23.4\text{ m/s}$ | $19.1\text{ m/s}$ |

*Notes to Table 2*:
* Actual launch speeds may vary depending on the wind speed, aircraft engine propulsion force and proper support by grounding anchor.
* `*` Auxiliary pressure source up to $16\text{bar}$ needed. Contact seller for more details.

* **Footer**: `REV 2.6` | `ELI Military Simulations` | `37 Page`

---

### [Page 38] COMPRESSOR UNIT Quick guide

* **Header**: `Eli` | `COMPRESSOR UNIT Quick guide`
* **[!] ATTENTION!** Do not handle any pneumatic tubing until making sure that the valve of the main pressure tank is closed!
* **[!] ATTENTION!** Carriage has to be secured by the safety lock pin before opening the main valve!
* **[Warning Triangle Icon] WARNING!** Open the main valve only before launch and close it after launch as soon as possible! Ignoring that may cause accidental sled or pressure release and lead to serious injuries or death!

**Normal operation:** For switching the compressor unit ON or OFF, press ON button.

**Setting the target pressure (SET MODE):** For adjusting the target pressure value make sure, that the system is switched OFF. Hold SET button and then start the system by pressing ON button. Release both buttons and wait until the target pressure is reached. Press SET button to save the target pressure value into memory or ON button to switch the system OFF and maintain previous value.

#### Status LED states (illuminated push-buttons)

| PWR LED | SET LED | MOTOR STATE | SYSTEM STATUS |
| :--- | :--- | :--- | :--- |
| LED off | LED off | `OFF` | Turned OFF |
| LED on | LED off | `OFF` | Target pressure reached |
| LED on | LED blinking | `OFF` | Pressure in the tank over the target pressure |
| LED on | LED on | `ON` | Pressurizing to target pressure |
| LED on | LED off | `ON` | SET MODE (Pressurizing tank) |
| LED blinking | LED off | `OFF` | SET MODE (Maximum pressure reached to $14\text{ bar}$) |
| LED blinking | `X` (Any state) | `OFF` | Battery voltage too low |

* **[!] ATTENTION!** Before launching the plane always check the pressure on the manometer, making sure, that the target pressure is achieved.
* **Footer**: `!!!READ USER MANUAL FOR DETAILED INFORMATION!!!`

---

### [Page 39] LAUNCH PROCEDURE Quick checklist

* **Header**: `Eli` | `LAUNCH PROCEDURE Quick checklist`

For ensuring safe launch procedure perform the following steps:
* [ ] Unpack and assemble the rail.
* [ ] Make sure, that the carriage is in its initial position and secured with safety lock pin.
* [ ] Make sure that the pulling rope is attached to the carriage and installed properly.
* [ ] Make sure, that the compressor unit ON/OFF switch is in OFF position and the main reservoir outlet valve is in closed position.
* [ ] Install pressure hose connecting main valve outlet and the launcher inlet. Make sure that the clamps are perfectly locked and securing ring also locked.
* [ ] Insert a fully charged battery cartridge into its connection slot on the compressor unit.
* [ ] Turn on the compressor unit by pressing ON button and wait until target pressure is reached.
* [ ] Check the pressure manometer on the pressure regulation valve to assure that the determined pressure is achieved.
* [ ] Make sure that carriage safety pin is installed and remote release handle prepared and unengaged.
* [ ] Place the plane on the launcher. Make sure that all four support levers are correctly inserted into throwing slots.
* [ ] When the plane is ready to launch, make sure that all personnel have moved to the safety area
* [ ] Open slowly the main outlet valve on the compressor unit to pressurize main valve.
* [ ] Remove the carriage safety lock pin. To launch, open the safety covers on the trigger handle buttons and press both buttons simultaneously to open the main valve.
* [ ] For safety reasons it is recommended to close air reservoir outlet valve between launches to avoid accidental carriage release by pressing the trigger.

* **[Gloves & Goggles Icon] ALWAYS USE GLOVES AND GOGGLES** when servicing the plane or the launcher!
* **[!] NEVER LAUNCH WITHOUT PAYLOAD** as it will damage the device and surrounding persons!
* **[!] NEVER LAUNCH WITHOUT SECURING LAUNCHERS REAR LEG TO THE GROUND**
* **[!] ATTENTION!** Before launching make sure that all team members are in safety area behind the launcher!
* **[!] ATTENTION!** Carriage has to be secured by the safety lock pin before opening the main valve!
* **[Warning Triangle Icon] WARNING!** Open the main valve only before launch and close it after launch as soon as possible! Ignoring that may cause accidental sled or pressure release and lead to serious injuries or death!
* **[!] ATTENTION!** Remove the carriage safety lock only just before the launch!
* **Footer**: `!!!READ USER MANUAL FOR DETAILED INFORMATION!!!`

---

### [Page 40] 9 Safety area schematics

* **Schematic Diagram Elements**:
  * Top-down view of the launcher rail with a pusher-propeller aircraft positioned at the rear launch point and the blue circular `Anchor disk (9)` at the rear tip.
  * `WIND DIRECTION`: Three blue downward arrows at the front of the launcher pointing opposite to the launch direction.
  * `LAUNCH DIRECTION`: Two green upward arrows pointing forward along the launcher rail.
  * `DANGER ZONE` / `KEEP CLEAR`: Red diagonal-hatched zone extending across the entire area in front of and abeam the aircraft's tail/propeller plane.
  * `SAFETY AREA`: Green cross-hatched zone located strictly behind the aircraft's tail/propeller plane surrounding the rear support leg and anchor disk.
* **[!] ATTENTION!** Before launching make sure that all team members are in safety area behind the launcher!
* **Footer**: `REV 2.6` | `ELI Military Simulations` | `40 Page`

---

### [Page 41] 10 Plane installation documentation in standard configuration

* **Drawing 1: Carriage Front Elevation View**:
  * Outer span across lever tips: $156\text{ mm}$
  * Inner span between lever tips: $140\text{ mm}$
  * Upper hook notch height: $30\text{ mm}$
  * Lower carriage body width: $162\text{ mm}$ ($362\text{ mm}$ OCR artifact; matches carriage base width)
* **Drawing 2: Carriage Side Elevation View**:
  * Overall carriage length: $271\text{ mm}$
  * Span between forward and rear lever tips: $206.5\text{ mm}$
  * Overall carriage height: $232.5\text{ mm}$
  * Forward lever vertical clearance above safezone line: $145\text{ mm}$
  * Rear lever vertical clearance above safezone line: $155.5\text{ mm}$
  * Green callout above red dashed line: `PROPELLER SAFEZONE`
  * Red hatched zone covering carriage body below lever arms: `MAKE SURE THAT THE PROPELLER DOES NOT REACH THIS AREA`
* **Drawing 3: Launcher Front/Rear Elevation View on Bipod**:
  * Overall height from ground level to top of front rail shock absorbers: $1115\text{ mm}$
  * Front bipod leg stance width at ground level: $602\text{ mm}$
* **Footer**: `REV 2.6` | `ELI Military Simulations` | `41 Page`

---

### [Page 42] Allowed Center of Mass Position Drawing

* **Side Profile Engineering Drawing**:
  * Shows a pusher-propeller UAV mounted on the four support levers of `Carriage (7)` on the inclined launcher rail relative to `GROUND LEVEL`.
  * Callout: `ALLOWED CENTER OF MASS POSITION FOR LAUNCHED PAYLOAD`
  * Red cross-hatched rectangular envelope containing the Center of Mass symbol and downward gravity vector `G`:
    * Longitudinal length parallel to rail: $200\text{ mm}$
    * Height normal to rail above fuselage mounting line: $100\text{ mm}$
* **Footer**: `REV 2.6` | `ELI Military Simulations` | `42 Page`

---

### [Page 43] Engineering Drawing: Plane connection hook option A

* **Title Block**:
  * **Title**: `Plane connection hook option A`
  * **Designed by**: `ELI Ltd` | **Checked by**: `Jaan Palm` | **Date**: `4.04.2016`
  * **Mass**: $0.004\text{ kg}$ | **Edition**: `A` | **Sheet**: `1 of 1`
  * **General Tolerances**: `Dimensions are in millimeters`, `Unshown tolerances: ISO 2768-m`, `Unshown radiuses: R 0.2mm`, `Unshown surface roughness: Ra 6.3`
* **Assembly View (Right)**:
  * Shows `Carriage (7)` side profile with `LAUNCH DIRECTION` green arrow pointing left.
  * Longitudinal spacing between front and rear connectors: $178\text{ mm}$ (inner hook face to inner hook face), $186\text{ mm}$ (hook center to hook center), $206\text{ mm}$ (outer end to outer end).
* **Detail View 1: `FRONT RIGHT CONNECTOR`**:
  * Overall length: $20\text{ mm}$ | Overall height: $16\text{ mm}$ | Thickness: $s = 8\text{ mm}$
  * Hole pattern: $2\text{ holes}$ $\varnothing 3.2$, countersink `CSNK` $\varnothing 6.3 \times 90^\circ$, spacing $12\text{ mm}$ ($4\text{ mm}$ from edges), vertical offset $4\text{ mm}$ and $8\text{ mm}$
  * Hook slot geometry: Inner radius $R3$, slot opening $4\text{ mm}$, hook lip height $2\text{ mm}$, lower cutout $7\text{ mm}$, outer corner radii $3 \times R2$
* **Detail View 2: `REAR RIGHT CONNECTOR`**:
  * Overall length: $20\text{ mm}$ | Overall height: $16\text{ mm}$ | Thickness: $s = 8\text{ mm}$
  * Hole pattern: $2\text{ holes}$ $\varnothing 3.2$, countersink `CSNK` $\varnothing 6.94 \times 90^\circ$, spacing $12\text{ mm}$ ($4\text{ mm}$ from front edge), vertical offset $4\text{ mm}$ and $8\text{ mm}$
  * Rear L-lip thickness: $4\text{ mm}$
* **Drawing Notes**:
  * `NOTE: LEFT SIDE PARTS ARE MIRRORS OF THE RIGHT SIDE PARTS`
  * `1. Material: Aluminum 6061-T6`
  * `2. Surface area: 1117,53 mm2`
  * `3. Coating: Natural anode`

---

### [Page 44] Engineering Drawing: Plane connection hook option B

* **Title Block**:
  * **Title**: `Plane connection hook option B`
  * **Designed by**: `ELI Ltd` | **Checked by**: `Jaan Palm` | **Date**: `4.04.2016`
  * **Edition**: `A` | **Sheet**: `1 of 1`
  * **General Tolerances**: `Dimensions are in millimeters`, `Unshown tolerances: ISO 2768-m`, `Unshown radiuses: R 0.2mm`, `Unshown surface roughness: Ra 6.3`
* **Assembly View (Right)**:
  * Shows single-piece longitudinal hook bar engaged with both forward and rear levers of `Carriage (7)` (`LAUNCH DIRECTION` arrow pointing left).
* **Detail Views (Left)**:
  * `LAUNCH DIRECTION` green arrow pointing upward/left.
  * Overall bar length: $225\text{ mm}$ | Overall bar height: $16\text{ mm}$ | Thickness: $s = 8\text{ mm}$
  * Mounting holes: $\varnothing 5.3$, $2\text{ holes}$, center-to-center spacing $165\text{ mm}$ ($35\text{ mm}$ from front end, $8\text{ mm}$ vertical centerline)
  * Front end chamfers: $4 \times 45^\circ$, $2\text{ chamfers}$
  * Front and rear hook notches: $24\text{ mm}$ from ends, $8\text{ mm}$ flat engagement edge, $45^\circ$ lead-in ramp, $R3$ internal fillet, $11\text{ mm}$ / $2\text{ mm}$ front lip, $7.5\text{ mm}$ rear notch depth.

---

### [Page 45] Engineering Drawing: Plane connection hook option C

* **Title Block**:
  * **Title**: `Plane connection hook option C`
  * **Designed by**: `ELI Ltd.` | **Checked by**: `Jaan Palm` | **Date**: `06/10/2025`
  * **Edition**: `A` | **Sheet**: `1 of 1`
  * **General Tolerances**: `Dimensions are in millimeters`, `Unshown tolerances: ISO 2768-m`, `Unshown radiuses: R 0.2mm`, `Unshown surface roughness: Ra 6.3`
* **Assembly Views (Right)**:
  * Side view showing carriage levers with `LAUNCH DIRECTION` arrow pointing left and longitudinal pin center-to-center span of $320\text{ mm}$.
  * Front view showing pin engagement width of $156\text{ mm}$ (outer), $140\text{ mm}$ (inner), and $103\text{ mm}$ lower carriage base width.
  * Perspective detail view showing two `Option C` flanged pins mounted to the underside of an aircraft fuselage wing root.
* **Detail Views of Launch Pin (Left)**:
  * Overall length: $33.5\text{ mm}$ ($17.5\text{ mm}$ head/neck section, $16\text{ mm}$ threaded shaft with $10\text{ mm}$ full thread length)
  * Thread specification: `M8` with $1 \times 45^\circ$ end chamfer
  * Hex flange across flats: $13\text{ mm}$
  * Cylindrical neck length: $10\text{ mm}$, diameter $\varnothing 8$, with $30^\circ$ transition taper to hex shoulder
  * Outer retaining flange: diameter $\varnothing 13$, thickness $2.5\text{ mm}$, with $1 \times 45^\circ$ edge chamfer
* **Drawing Notes**:
  * `1. Material: AISI 304`
  * `2. Surface area: 1390,16 mm2`
  * `3. Coating: Natural anode`