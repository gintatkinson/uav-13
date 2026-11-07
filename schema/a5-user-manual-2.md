# AVENGER 5

long-range, high-performance heavy loitering munition UAV platform

USER MANUAL

Model AVENGER5V1
Version UDS-A5UM-001
Release Date 2026-08-07

PROPRIETARY BUSINESS INFORMATION – FOR AUTHORIZED PERSONNEL ONLY!
© Unmanned Defense Systems, UAB. All rights reserved.

# Contents

- 1 Introduction 7
  - 1.1 Scope of the Document 7
  - 1.2 General Features 7
  - 1.3 General Overview 8
  - 1.4 Mechanical Dimensions 9
  - 1.5 Weight and Balance 9
  - 1.6 Flight Characteristics 10
  - 1.7 Seeker Characteristics 10
  - 1.8 Product Contents 11
- 2 Overview 13
  - 2.1 Access and Installation 13
  - 2.2 Standalone Mode 14
  - 2.3 Operation Mode 14
- 3 Interface 15
  - 3.1 Main Menu 16
    - 3.1.1 Display Settings 17
    - 3.1.2 General Settings 18
    - 3.1.3 Configuration 19
    - 3.1.4 Advanced Configuration 19
  - 3.2 Main Window Panels 19
    - 3.2.1 Flight Panel 19
    - 3.2.2 Instrument Panel 19
    - 3.2.3 GCS Panel 20
    - 3.2.4 Virtual Joystick Panel 20
    - 3.2.5 Screen Mode Panel 20
    - 3.2.6 Pinned Functions Panel 21
    - 3.2.7 Map Position Panel 21
    - 3.2.8 Map Scale 22
    - 3.2.9 Video/Map Panel 22
    - 3.2.10 Payload Control Panel 22
  - 3.3 Main Window Layouts 22
    - 3.3.1 Payload Layout 23
    - 3.3.2 Pilot Layout 24
  - 3.4 Map Controls 24
    - 3.4.1 Symbols 25
    - 3.4.2 Map View Layers 25
    - 3.4.3 Function Menu 25
- 4 Authentication 27
  - 4.1 When sign-in is required 27
  - 4.2 Signing in 27
    - 4.2.1 Login dialog 28
    - 4.2.2 After a successful login 28
    - 4.2.3 Sign-in errors 28
  - 4.3 Changing the factory default password 29
    - 4.3.1 Set new password form 29
  - 4.4 Signing out 30
- 5 UAV Status and Settings 31
  - 5.1 Telemetry 31
  - 5.2 Logs 32
  - 5.3 Safety 33
    - 5.3.1 Return To Launch (RTL) 33
    - 5.3.2 Failsafe Triggers 34
    - 5.3.3 GPS 34
    - 5.3.4 Mission Options 35
    - 5.3.5 Logging 35
    - 5.3.6 Safety Actions 35
  - 5.4 Utilities 36
    - 5.4.1 Compass Calibration 36
    - 5.4.2 Simple Compass Calibration 37
    - 5.4.3 Reboot Commands 38
- 6 Mission Planning 39
  - 6.1 Start Screen 40
  - 6.2 Sync Mission Plan 41
  - 6.3 Mission Workflow 41
    - 6.3.1 Vehicle Type Selection 41
    - 6.3.2 Mission Plan Structure 42
    - 6.3.3 Mission Path Editing 43
    - 6.3.4 Rally Points 44
    - 6.3.5 Editable Parameters 46
  - 6.4 Saving and Reusing Missions 47
    - 6.4.1 Saving Missions 47
    - 6.4.2 Saved Missions 47
  - 6.5 Mission Validation 47
  - 6.6 Mission Upload 49
  - 6.7 Geofence Planning 50
    - 6.7.1 Polygon Geofences 51
    - 6.7.2 Uploading Geofences 51
- 7 Operation 52
  - 7.1 Connecting to the Ground Station 52
  - 7.2 Pre-Flight Checklist 52
    - 7.2.1 Opening Pre-Flight Checklist 53
    - 7.2.2 Checklist Behaviour 53
    - 7.2.3 Checklist Structure 54
  - 7.3 Arming and Launching 57
    - 7.3.1 Launch procedure 58
- 8 Controlling the UAV 59
  - 8.1 Flight Modes 59
    - 8.1.1 Auto Mode 59
    - 8.1.2 Cruise Mode 61
    - 8.1.3 Loiter Mode 61
    - 8.1.4 RTL Mode 62
    - 8.1.5 Manual Mode 62
    - 8.1.6 Guided Mode 62
    - 8.1.7 Attack Mode 63
  - 8.2 Additional Vehicle Commands 64
    - 8.2.1 Change Altitude 64
    - 8.2.2 Change Airspeed 64
- 9 Map Operations 67
  - 9.1 Five Whiskey Report 67
    - 9.1.1 Edit Report 68
  - 9.2 Call For Fire 69
  - 9.3 Calculate Distance between 2 Points 70
  - 9.4 Points of Interest 70
- 10 Radio Controls 72
  - 10.1 Set antenna location 73
  - 10.2 Antenna Rotator Map calibration 73
    - 10.2.1 Pre-flight Rotator map calibration procedure 73
  - 10.3 Antenna In-Flight calibration 74
    - 10.3.1 In-flight fine tune calibration procedure 74
    - 10.3.2 Rotator direction indicators 75
- 11 Payload Controls 76
  - 11.1 Camera View 77
  - 11.2 Payload configuration 78
    - 11.2.1 Camera mode 79
    - 11.2.2 Camera Display 79
    - 11.2.3 IR Color Mode 80
    - 11.2.4 IR Polarity 80
  - 11.3 Camera Control 81
    - 11.3.1 Live video 81
    - 11.3.2 Map 81
    - 11.3.3 Joystick (gimbal) 81
  - 11.4 Multitrack 82
    - 11.4.1 Example: assigning and promoting a tracker 82
- 12 Target Engagement 83
  - 12.1 Warhead Safety 83
  - 12.2 Engagement Profiles 86
  - 12.3 Engagement 88
  - 12.4 Engaging Abort 90
- 13 Operation Scenarios 91
  - 13.1 GNSS Denied Operation 91
    - 13.1.1 Takeoff Without GNSS 91
    - 13.1.2 UAV Location Correction in GNSS Denied Environments 91
    - 13.1.3 GNSS Disabling in Spoofing Conditions 91
- 14 Terminology Glossary 93
  - 14.1 Core System Terms 93
  - 14.2 Navigation and Positioning 94
  - 14.3 Flight Modes and Behaviors 94
  - 14.4 Payload and Video Terms 95
  - 14.5 Reporting and Tactical Map Functions 95
  - 14.6 Connectivity and Integration 96
  - 14.7 Hardware and Safety Terms 96

# List of Figures

- 1.1 Avenger 5 physical component map 8
- 1.2 General launcher and UAV dimensions 9
- 2.1 Swarm C2 Setup 13
- 3.1 Payload layout main window 15
- 3.2 Main menu 16
- 3.3 Display settings 17
- 3.4 General settings 18
- 3.5 Flight panel 19
- 3.6 Instrument Panel 20
- 3.7 Pinned functions 21
- 3.8 Payload layout main window 23
- 3.9 Pilot layout main window 24
- 3.10 Function menu 26
- 4.1 Logged Out Overview 27
- 4.2 Login Pop-up window 28
- 4.3 Password Reset 29
- 5.1 UAV Panel header 31
- 5.2 System log messages 33
- 5.3 RTL configuration 33
- 5.4 Failsafe action triggers 34
- 5.5 GPS safety configuration 35
- 5.6 Delete mission on reboot 35
- 5.7 Log enable 35
- 5.8 Compass calibration menu 36
- 5.9 Compass calibration rotation axes 37
- 5.10 Compass calibration menu 37
- 5.11 Compass calibration menu 38
- 6.1 Open mission planning 39
- 6.2 Mission planning menu 40
- 6.3 Mission type 41
- 6.4 Mission planning 42
- 6.5 Rally points on the mission map 44
- 6.6 Rally Points list in the mission planner 45
- 6.7 Saved missions 47
- 6.8 Upload mission 49
- 6.9 Geofence inclusion and exclusion zones 50
- 7.1 Pre-flight Checklist overview 52
- 7.2 Preflight warnings and errors 53
- 7.3 Catapult 54
- 7.4 Mission & parameters 55
- 7.5 Preparation & mounting 55
- 7.6 System checks 56
- 7.7 Video checks 57
- 7.8 Warhead and Safety 57
- 7.9 Pre-flight complete and ready to arm 58
- 8.1 Changing flight mode 60
- 8.2 Pilot joystick control axis 61
- 8.3 Set new loiter pattern 63
- 8.4 Change altitude panel 65
- 8.5 Change airspeed panel 66
- 9.1 Five Whiskey report 67
- 9.2 Edit Five W/BDA 68
- 9.3 Call For Fire Request 69
- 9.4 Total distance 70
- 9.5 POI markers 71
- 10.1 Rotator Control Interface 72
- 10.2 Rotator Fine Tune 74
- 10.3 Rotator visualization 75
- 10.4 Rotator Auto Follow without GNSS 75
- 11.1 Payload control panel 76
- 11.2 Camera 77
- 11.3 Camera configuration menu 78
- 11.4 Camera Modes 79
- 11.5 IR color modes 80
- 11.6 Multitrack 82
- 11.7 Payload Multitrack 82
- 12.1 engagement and warhead controls 83
- 12.2 arming the warhead 85
- 12.3 changing engagement profile 87
- 12.4 engagement angle 88
- 12.5 tracker behavior 89
- 13.1 Disable GNSS 92

# 1 Introduction

## 1.1 Scope of the Document

The purpose of this user manual is to provide information about the Avenger 5 loitering munition platform and accompanying Swarm C2 command and control system.

The document covers:

- Technical information about the platform.
- Preparation of the Avenger 5 loitering munition for flight.
- Operational procedures of the Avenger 5 UAV.
- Using the Swarm C2 application for mission planning and flight.

**WARNING: Read Before Operation**

This document must be used together with all applicable user manuals and supporting documentation covering systems safety, handling, storage, transportation, preparation, operation, and associated equipment.

Do not handle, prepare, power on, or operate the system or any associated equipment unless you have read and understood the applicable documentation and received the required training and authorization.

## 1.2 General Features

A long-range, high-performance heavy loitering munition UAV, engineered for high electronic warfare resilience and offering a modular warhead payload option. Designed for versatility and accuracy, the Avenger 5 seamlessly integrates with various explosive payloads. After target acquisition, it autonomously executes its mission without reliance on ongoing radio communication or GNSS signals, delivering powerful and precise strikes, even in complex battlefield conditions.

- EW resiliency (frequency hopping, dead-reckoning in GNSS-denied environments).
- Fully automatic guidance system using gimbaled sensor (EO/IR).
- Auto-targeting using visual tracking or geolocation reference.
- Low visual, acoustic, thermal, and radar signature.
- Integration with SitaWare HQ, ATAK, DELTA.
- Pneumatic catapult launch system.
- Option for recoverability.

**NOTE:** Vehicle capabilities strongly depend on the concept of operations during use. This document provides nominal characteristics measured under standard conditions.

## 1.3 General Overview

Key physical components of the Avenger 5 UAV:

- EO/IR gimballed seeker.
- Fuselage and payload bay.
- Wings (Left/Right upper and lower panels).
- Ruddervators.
- Foldable propeller.
- Antennas.

[Figure 1.1: Avenger 5 physical component map]

**NOTE:** Placement of particular components might differ according to specific configuration of the product.

## 1.4 Mechanical Dimensions

**Table 1.1: Mechanical dimensions**

| Parameter | Value |
| --- | --- |
| Wingspan | 1.8m |
| Assembled UAV length | 1.6m |
| Assembled UAV height | 1.1m |

[Figure 1.2: General launcher and UAV dimensions]

## 1.5 Weight and Balance

**Table 1.2: Weight and balance**

| Parameter | Value |
| --- | --- |
| Maximum take-off weight | 17kg |

## 1.6 Flight Characteristics

**Table 1.3: Flight characteristics**

| Parameter | Value |
| --- | --- |
| Cruise speed | 30m/s |
| Max horizontal speed | 38m/s |
| Max dive speed | 55m/s |
| Max dive angle | 22deg |
| Min speed | 26m/s |
| Flight time | 90min |
| Launch type | Catapult/Tube |
| Recovery system | No |
| Command and control range (RLOS, depending on configuration) | 60km/180km |

## 1.7 Seeker Characteristics

**Table 1.4: Seeker Characteristics**

| Parameter | Value |
| --- | --- |
| Type | Gimballed EO/IR sensor. |
| Zoom | X40 (X20 + X2 digital) |
| Day camera | 1280x720 (HD) |
| Thermal camera | 1280x720 (HD) |
| Pitch | -45° to +135° |
| Yaw/Roll | -165° to +165° |

## 1.8 Product Contents

**Table 1.5: Avenger 5 UAV**

| # | Component | Qty. | Comment |
| --- | --- | --- | --- |
| 1 | Fuselage assembly with all hatches closed and vertical stabilizer attached. Battery included | 1 | - |
| 2 | Wing section left | 2 | - |
| 3 | Wing section right | 2 | - |
| 4 | Ruddervator | 4 | - |
| 5 | RBF flag | 2 | - |

**Table 1.6: Ground Control System (GCS)**

| # | Component | Qty. | Comment |
| --- | --- | --- | --- |
| 1 | Radio BOX | 1 | - |
| 2 | Ground BOX | 1 | - |
| 3 | Rotator | 1 | - |
| 4 | Gitzo tripod with head | 1 | - |
| 5 | GCS battery | 2 | - |
| 6 | Panasonic FZ-G2 tablet | 2 | - |
| 7 | Panasonic FZ-G2 tablet battery | 2 | - |
| 8 | MARS antenna 23dBi | 1 | - |
| 9 | Power cable with ODU connector | 2 | 3m |
| 10 | Ethernet cable | 1 | 15m |
| 11 | Antenna cable with N-type connector | 2 | 0.25m |
| 12 | LAN cable with ODU connector | 2 | 3m |

**Table 1.7: Spare parts and service equipment package**

| # | Component | Qty. | Comment |
| --- | --- | --- | --- |
| 1 | Panasonic FZ-G2 Tablet battery charging station | 1 | - |
| 2 | GCS and UAV battery charger | 1 | - |
| 3 | Spare attachment bolts | 30 | - |
| 4 | Propeller blades | 2 | - |
| 5 | Propeller assembly | 1 | - |
| 6 | Set of tools | 1 | - |
| 7 | Panasonic FZ-G2 tablet spare batteries | 2 | - |

**Table 1.8: Transportation and storage cases**

| # | Component | Qty. | Comment |
| --- | --- | --- | --- |
| 1 | Case for Tactical backpack Avenger 5 UAV | 1 | - |
| 2 | Case for Tactical backpack GCS | 1 | - |
| 3 | Case for Spare parts and service equipment | 1 | - |

# 2 Overview

The Swarm C2 system consists of three main components:

**Application**
the operator software, running as a web application on one or more tablets. It provides the map view, mission planning, flight controls, and payload interface.

**Ground Station**
the ground-based system deployed in the field. It interfaces with operator devices, UAVs, radio equipment, and external services, and acts as the central hub for data routing, video streaming, storage, and coordination.

**UAV**
the unmanned aerial vehicle that receives commands, transmits live telemetry, and streams payload data back to the ground station.

[Figure 2.1: Swarm C2 Setup]

The application operates in one of two modes depending on whether the operator device has a connection to the ground station:

**Operation mode**
the operator device is connected to the ground station. Full application capabilities are available.

**Standalone mode**
the ground station is not reachable (ground station not deployed, powered off, or outside network range). A subset of application functions is available locally on the device.

## 2.1 Access and Installation

Swarm C2 is an application installed on the operator device. It runs in a browser and can be accessed from any device connected to the ground station network. Once installed, it works locally on the device -- no active connection is required to launch it.

**NOTE:** Swarm C2 comes pre-installed on the tablets supplied with the ground station. Google Chrome is the recommended browser.

## 2.2 Standalone Mode

In standalone mode the application works entirely on the device. You can plan missions, set the ground station position, and adjust preferences. Controls that require the ground station are unavailable until you return to operation mode. When the connection is restored, changes made are synced automatically.

## 2.3 Operation Mode

Operation mode is active when the ground station is connected and you are signed in. It covers two levels of access depending on what is connected:

**Ground station configuration**
with only the ground station available, you can configure radio and antenna settings, network connectivity, and external system integrations.

**UAV operations**
once a UAV connects to the ground station, live telemetry, commanding, and flight controls become available.

All connected operator devices share the same state, kept in sync through the ground station.

# 3 Interface

The GCS tablet comes with Swarm C2 software pre-installed. No additional setup is required. Simply launch the software to begin.

After launch, the main window is displayed. By default, Swarm C2 opens in Payload layout.

[Figure 3.1: Payload layout main window]

The main window contains the primary controls and information required during operation.

The following interface elements are visible in the main window:

1. **Main menu** – Provides access to configuration, navigation, and other Swarm C2 functions.
2. **Flight panel** – Displays the main flight controls and current UAV state.
3. **Instrument panel** – Displays live telemetry data from the UAV and provides access to related actions.
4. **GCS panel** – Displays ground control station battery information and provides access to GCS-related functions.
5. **Virtual joystick panel** – Touchscreen interface used for payload control or manual UAV control, depending on the selected layout.
6. **Screen mode panel** – Switches the main screen between map view and camera view.
7. **Pinned functions panel** – Displays functions pinned for quick access.
8. **Map position panel** – Provides shortcuts for centering the map on key positions.
9. **Zoom controls panel** – Provides controls for zooming the map in and out.
10. **Map scale** – Shows the scale of the current map zoom level.
11. **Video/Map panel** – Displays the map or live payload view, depending on the selected screen mode.
12. **Payload control panel** – Displays controls for the current UAV payload.
13. **Munition control panel** – Displays ESAD and engagement state and provides controls for both.

Detailed descriptions of these interface elements are provided in the following sections.

## 3.1 Main Menu

The Main menu provides access to configuration, navigation, and other Swarm C2 functions.

It includes the following sections:

1. **Display settings** – Used to configure pilot/operator layout and map-related settings.
2. **General settings** – Used to configure general application settings.
3. **Configuration** – Used to configure connectivity and integration settings.
4. **Advanced configuration** – Used for advanced system setup, such as radio binding.
5. **Navigation** – Provides shortcuts to available Swarm C2 functions that can be pinned to the main window.
6. **Version** – Displays the current Swarm C2 application version.

[Figure 3.2: Main menu]

### 3.1.1 Display Settings

The Display settings section is used to configure layout and map display options.

It includes the following options:

1. **Use Offline Maps** – Enables the use of locally stored maps.
2. **Toggle Fullscreen** – Enables fullscreen mode.
3. **Map View** – Controls which map layers are displayed:
   a. **All** – Displays all available layers.
   b. **Local** – Displays local operational elements such as UAV icons, points of interest, and Five Ws.
   c. **Tasking** – Displays map drawings and overlays related to current mission planning or execution, such as waypoints, paths, and targets.
   d. **Permanent** – Displays permanent or semi-static overlays such as CFF, Guided Loiter zones, and antenna line-of-sight lines.
   e. **Geofence** – Displays all configured geofences that define UAV flight boundaries.
   f. **Zoom controls** – Show or hide map zoom controls, allows the user to zoom map in or out for example using a pen.
4. **Layout** – Selects which predefined layout is used:
   a. **Payload** – Layout optimized for payload controls.
   b. **Pilot** – Layout optimized for aircraft controls.
5. **Advanced** – Enables advanced options.

[Figure 3.3: Display settings]

### 3.1.2 General Settings

The General settings section is used to configure general application settings and perform system actions.

It includes the following options:

1. **Coordinate format** – Selects how coordinates are displayed in the application.
2. **Map Service** – Checks whether the application can access the map service.
3. **Upload map** – Uploads a map for offline use in MBTiles format.
4. **Clear App Data** – Clears all application data and settings.
5. **Logout** – Logs out the current user from the application.

[Figure 3.4: General settings]

### 3.1.3 Configuration

The Configuration section is used to configure connectivity and integration settings.

It includes the following options:

1. **Tech support remote access** – Enables or disables secure remote access for technical support sessions.
2. **VPN setup** – Configures and monitors VPN connectivity for secure network access.
3. **Wi-Fi** – Configures the Wi-Fi module for internet access and displays connection status.
4. **TAK credentials** – Configures TAK integration settings, credentials, and connection status.
5. **Video Stream Setup** – Configures video stream connection settings and output behavior.
6. **Training mode** – Enables or disables the GPS plane icon for training/simulation purposes. The icon is hidden while Training Mode is active.

### 3.1.4 Advanced Configuration

The Advanced configuration section is used for advanced system setup tasks.

It includes the following options:

1. **Bind radios** – Links the UAV radio with the GCS radio to enable secure communication between radios.

## 3.2 Main Window Panels

The following panels are visible in the main window.

### 3.2.1 Flight Panel

The Flight panel displays the main flight controls and current UAV state.

[Figure 3.5: Flight panel]

It includes the following elements:

**Flight Command**
Used to arm or engage the UAV, depending on the current state.

**Flight Mode**
Displays the current flight mode and allows selecting another mode from the dropdown list. The list of available flight modes depends on system configuration and UAV state.

### 3.2.2 Instrument Panel

The Instrument panel displays live telemetry data from the UAV and provides access to related actions. The three-dot button at the end of the panel opens the UAV side panel.

Below the Instrument panel, an additional bar shows Munition Control and pinned telemetry fields selected in the telemetry view.

[Figure 3.6: Instrument Panel]

### 3.2.3 GCS Panel

The GCS panel displays ground control station battery information and provides access to GCS-related functions. Selecting this panel opens the GCS view.

### 3.2.4 Virtual Joystick Panel

The Virtual joystick panel is a touchscreen interface used for payload control or manual UAV control, depending on the selected layout.

| PayloadJoystick | PilotJoystick |
| --- | --- |

### 3.2.5 Screen Mode Panel

The Screen mode panel is used to switch the main screen between map view and camera view.

### 3.2.6 Pinned Functions Panel

[Figure 3.7: Pinned functions]

The Pinned functions panel displays shortcuts to selected Swarm C2 functions pinned from the Main menu. Pinned functions appear in the main window for quicker access during operation.

The following functions can be pinned to this panel:

**Ruler** – Measures distance between points.
**Planning** – Opens the mission planning menu.
**Artillery Correction** – Opens the interface for artillery correction using payload live video feed.
**Mark Location** – Marks a location on the map using input coordinates.

### 3.2.7 Map Position Panel

The Map position panel provides shortcuts for centering the map on key positions.

It includes the following controls:

**Camera View** – Centers the map on the camera viewpoint.
**Ground Station** – Centers the map on the ground station position.
**Plane** – Centers the map on the plane position.
**My Location** – Centers the map on the operator's current position.

### 3.2.8 Map Scale

The Map scale shows the scale of the current map zoom level.

### 3.2.9 Video/Map Panel

The Video/Map panel displays the map or live payload view, depending on the selected screen mode. The video window can be resized by dragging its top-right corner.

### 3.2.10 Payload Control Panel

The Payload control panel displays controls for the current UAV payload.

## 3.3 Main Window Layouts

The Swarm C2 main window can be configured in two layouts: Payload layout and Pilot layout.

### 3.3.1 Payload Layout

[Figure 3.8: Payload layout main window]

The Payload layout is optimized for payload operation and observation tasks. In this layout, the Virtual joystick panel is used for payload control.

### 3.3.2 Pilot Layout

[Figure 3.9: Pilot layout main window]

The Pilot layout is optimized for piloting and flight control.

In this layout:

**Virtual Horizon/Compass panel**
Displays the current UAV heading and virtual horizon.

**Virtual joystick panel**
In Cruise mode, the joystick is shown in white and is used to control vehicle heading and altitude.

## 3.4 Map Controls

Main map view has multiple functions for safe and efficient operation of UDS UAVs. This includes direct vehicle and payload controls, as well as multiple map-related functions and markers.

Map can be manipulated with both touch and mouse controls:

**Pan the map**
Press and drag a finger or mouse across the screen.

**Zoom the map**
Pinch the screen using two fingers, use the scroll wheel while hovering over the desired area, or use the + and − buttons in the zoom panel.

**Open function menu**
Tap over a desired area with mouse or finger.

**Zoom Controls**
Use + and − buttons when Zoom controls are enabled through App Menu.

### 3.4.1 Symbols

The following symbols appear on the map to indicate key objects during operation.

**Plane** – marks the current UAV position on the map.
**Home position** – marks the UAV home / RTL location on the map. The user is allowed to change it during flight.
**Marker** – marks the point selected on the map.
**POI** – marks the location of a Point of Interest (POI).
**Antenna** – marks the antenna location on the map.

### 3.4.2 Map View Layers

Different map layers can be configured to be displayed on the main map view. To configure them:

1. open main menu panel.
2. go to display settings.
3. press on checkmark boxes for which layers you want to be shown.

### 3.4.3 Function Menu

When pressing anywhere on the map, a marker will be placed and a function menu will appear displaying all available functions which require coordinates to function. Main functions include:

**Center Map** – centers map to clicked coordinates
**Add Five W** – adds a 5W report to the map.
**Add POI** – adds point of interest marker on map
**Call For Fire** – generates a CFF request on selected coordinates and copies formatted string to clipboard
**Set Home Position** – sets the selected point as the UAV's default RTL destination while the UAV is flying.
**Observe** – points the camera payload towards the selected coordinates and maintains continuous track.

[Figure 3.10: Function menu]

**Loiter Here** – set new loiter in this position.
**I'm Here** – sets the UAV's location to this point when GNSS is unavailable.
**I'm Looking Here** – When clicked, it sends the current coordinates to the UAV, prompting it to recalculate its position in GNSS-disabled environments based on camera zoom and other factors
**Edit POI/5W** – Ability to edit/delete POI or 5W

**NOTE:** Coordinates are in a format specified from the general settings tab.

# 4 Authentication

This chapter describes how operators sign in to Swarm C2 when using the payload operator application with the ground control station, how sessions end, and how the mandatory first-time password change works when accounts still use the factory default password.

Green circle in top right corner indicates whether Ground Station is connected.

[Figure 4.1: Logged Out Overview]

## 4.1 When sign-in is required

After Swarm C2 has launched and the tablet has connected to the ground station, the main map and interface are available, but server-backed user data and preferences are only loaded after a successful sign-in.

If the ground station link is up and you are not signed in, a notice appears top of the page with a Login control. Use that control to open the sign-in dialog.

**NOTE:** If the ground station is not connected, this sign-in notice does not appear. Establish the radio link first, then sign in.

## 4.2 Signing in

The application distinguishes two built-in operator identities, identified by callsign:

- **Payload** – Payload operator layout and functions.
- **Pilot** – Pilot operator layout and functions.

[Figure 4.2: Login Pop-up window]

**NOTE:** These are not separate accounts you create in the tablet; they are fixed roles the server recognises. Your organisation sets the password for each callsign on the ground-station service.

### 4.2.1 Login dialog

1. Use the horizontal toggle to select payload or pilot according to the role you are using for this session.
2. Enter the password for that callsign.
3. Choose Submit to authenticate.

Use the Eye button to hide or show the password.

You may close the dialog with the close control in the corner of the sign-in window. That returns you to the map without signing in; server-backed personal settings remain unavailable until you sign in successfully.

### 4.2.2 After a successful login

On success, the application stores authentication in the browser session, loads your user profile and preferences, and returns you to the normal main window workflow.

### 4.2.3 Sign-in errors

The application surfaces two common problems:

- **Invalid username or password** – The call sign or password does not match what the server expects. Check caps lock, the selected role (payload/pilot), and the password provided by your administrator.
- **Ground station unavailable** – The client could not reach the authentication service (for example, network outage). Resolve connectivity, then try again.

## 4.3 Changing the factory default password

For a new or freshly initialised system, each built-in callsign may still use the factory default password configured on the ground-station service (deployment-specific; not documented here). Swarm C2 does not allow continued use of that default once it recognises it: the first successful check of the default password does not complete a normal login.

Instead, the application switches to the set new password screen. You must choose a strong password before you can use the software in the usual way.

[Figure 4.3: Password Reset]

**IMPORTANT:** Complete this step promptly. The server only accepts the password-change request for a short time after it prompted you (on the order of a few minutes). If that window expires, sign in again with the default password to obtain a new change-password opportunity.

### 4.3.1 Set new password form

The form shows the callsign for the role you just authenticated; it is fixed for this step so it matches the server's expectation.

Enter the new password twice. The password must satisfy the strength rules used by the application, including at minimum:

- At least 8 characters.
- At least one uppercase letter.
- At least one lowercase letter.
- At least one digit.
- At least one special character from the supported set (for example `!@#$%^&*(),.?":{}|<>`).

Submit the form when the fields are valid. On success, you are returned to the login dialog; sign in again with the new password to start your session.

**IMPORTANT:** If the server rejects the change (for example, the short-lived authorisation from the previous step has expired), you will be sent back to login with an appropriate message. Use the default password once more if you still need to perform the initial change, or use your new password if the change already succeeded.

## 4.4 Signing out

To end the session and clear authentication from the tablet, use Main menu → General settings → Logout (see the Interface chapter). Logging out clears local session data associated with the application on that device; sign in again when you need server-backed settings.

# 5 UAV Status and Settings

UAV Panel provides connected UAV detailed telemetry and log information as well as parameter and sensors control. It is accessed in two ways:

1. by clicking on three dots in Instrument panel on the top of the screen
2. by clicking on three dots on the target UAV in UAV panel

The UAV Panel header contains:

1. **ID.** Vehicle Identification tag. It is saved locally for each UAV.
2. **UAV Type.** Currently selected UAV type.
3. **Pencil.** Button for changing identification tag name.
4. **Cross.** Panel close button

[Figure 5.1: UAV Panel header]

To rename the UAV tag press the pencil button and new tag input will appear. By pressing the check button new provided identifier will be saved locally.

UAV panel provides four main tabs:

1. **Telemetry.** Provides all available UAV telemetry data.
2. **Logs.** A list of all system messages with timestamp and severity level.
3. **Safety.** Safety parameters configuration.
4. **Utilities.** Sensor calibration and additional UAV actions.

## 5.1 Telemetry

Telemetry panel provides drone current telemetry data. Each parameter is provided with icon and value and can be pinned on the main window using the pin button.

**Altitude MSL.** Drone altitude above Mean Sea Level (MSL), in meters.
**Air Speed.** Speed of the drone is relative to the surrounding air, in meters per second.
**Ground Speed.** Horizontal speed of the drone over the ground, in meters per second.
**Volts.** Current total pack battery voltage.
**Amps.** Instantaneous current draw from the battery, in amperes (A).
**Wind.** Estimated wind speed (in meters per second) and direction affecting the drone.
**GPS Count.** Number of GNSS satellites currently being tracked.
**Distance to return.** Horizontal distance from the drone to the defined return point, in kilometers.
**ESC temperature.** Temperature of the Electronic Speed Controller, in degrees Celsius.
**Motor temperature.** Temperature of the motor, in degrees Celsius.
**Signal strength.** Quality of the control/telemetry link between the drone and ground station, shown as RSSI signal and noise levels.
**Flight time.** Duration of the current flight since takeoff.

## 5.2 Logs

A list of all system messages with timestamp and severity level. Messages are shown since the selected UAV was connected to Swarm C2.

There are three levels of severity:

**Info**
Normal system messages that describe regular operations or state changes. No action is required; these are for monitoring and traceability.

**Warning**
Indicates a potential issue or degraded condition that may require attention but does not immediately affect flight safety or system operation.

**Critical**
Serious fault or unsafe condition that can affect flight safety or core system functions. Requires immediate attention and may need emergency action.

[Figure 5.2: System log messages]

## 5.3 Safety

Safety defines how the aircraft behaves in failsafe and emergency situations (RTL behavior, link/GPS failsafes, mission handling) to keep operations predictable and safe. When the Safety Parameters panel is opened, current UAV parameters are loaded. After making changes, press Save to write the updated parameters back to the UAV.

### 5.3.1 Return To Launch (RTL)

[Figure 5.3: RTL configuration]

**Return at current altitude**
When RTL is triggered, the drone flies back home at its current altitude and then follows the configured landing sequence.

**Return at specified altitude**
When RTL is triggered, the drone first climbs/descends to the RTL Altitude and then flies back to home at that altitude.

**RTL Altitude**
Preset altitude the drone will use during RTL when Specified Altitude is selected.

**RTL Action**

1. **Disable** – RTL will not be triggered.
2. **Fly HOME then land.** – On RTL, the drone flies to home point or rally point and loiters unlimited.
3. **Go directly to landing sequence.** On RTL, the drone skips flying to home and immediately enters the configured landing sequence.
4. **Only For Go Around.** On RTL, starts a go-around procedure.

Rally points planned in the mission may be used as alternate RTL destinations when they are nearer than the home or return point and within configured range limits. See Rally Points.

### 5.3.2 Failsafe Triggers

[Figure 5.4: Failsafe action triggers]

**GCS Failsafe**
Enables or disables failsafe actions when the connection to the Ground Control Station is lost

**GCS Failsafe timeout**
Time period (in seconds) the GCS link must be lost before the GCS failsafe is triggered.

**Disarm ESAD on GCS timeout**
When enabled, disarms ESAD if no GCS ping is received for the configured timeout while the vehicle is armed.

**ESAD GCS timeout**
Time period (in seconds) without a GCS ping before ESAD is disarmed. Set to 0 to disable.

### 5.3.3 GPS

**Automatic drift calculation**
Enables automatic estimation of GPS position drift to improve position-hold and navigation accuracy.

**GPS Failsafe**
Enables or disables failsafe actions when GPS quality is lost or becomes unreliable.

**GPS Failsafe timeout**
Time period (in seconds) that GPS must be in a failed/poor state before the GPS failsafe is triggered.

[Figure 5.5: GPS safety configuration]

### 5.3.4 Mission Options

**Delete mission on reboot**
When enabled, the stored mission is cleared automatically each time the flight controller reboots.

[Figure 5.6: Delete mission on reboot]

### 5.3.5 Logging

**Log Enable**
Turns on board flight data logging on or off

[Figure 5.7: Log enable]

### 5.3.6 Safety Actions

**Clear Autopilot Logs**
Deletes all stored autopilot log data from the flight controller. Use to free space or remove old logs; this action cannot be undone.

**Remove UAV**
Drops this aircraft from the ground station's active list until it shows up again with new telemetry. Use it when aircraft state is stale – and you want to reset it.

**Power off ESAD**
Cut the power supply off for ESAD.

**NOTE:** If this button is pressed while the plane is airborne, there is no way to recover the ESAD.

## 5.4 Utilities

### 5.4.1 Compass Calibration

When flying for the first time in a new location, vehicle may return a compass inconsistent error. To fix this, simply calibrate compass using built-in Swarm C2 functionality

[Figure 5.8: Compass calibration menu]

To calibrate compass:

1. Select vehicle that needs to be calibrated.
2. Go to Utilities menu.
3. Pick up vehicle and move to a clear area.
   **CAUTION:** Make sure there are no large magnetic objects near the UAV when doing compass calibration, like buildings, cars, power poles, as calibration may fail.
   **NOTE:** It is recommended to remove any electronic devices from the person that is doing the calibration.
4. Start compass calibration.
5. Rotate the vehicle through all its axes. Rotate the vehicle steadily, making 1-3 turns throughout each axis.
6. Repeat rotations on a random axis until the progress bar is complete.
7. Reboot the vehicle.

[Figure 5.9: Compass calibration rotation axes]

8. Repeat calibration until both compasses are calibrated in the green zone.

**CAUTION:** If an error occurs during calibration or the bar stops moving, reboot the vehicle and try again.

### 5.4.2 Simple Compass Calibration

This is a simplified compass calibration procedure. It is recommended to use the full compass calibration procedure for best results. This compass calibration should only be used if the full compass calibration procedure is not available or cannot be performed.

[Figure 5.10: Compass calibration menu]

To calibrate compass:

1. Select vehicle that needs to be calibrated.
2. Go to Utilities menu.
3. Place the vehicle on a steady surface.
4. Click Start Compass Calibration

[Figure 5.11: Compass calibration menu]

5. Use another compass to get exact vehicle's heading (Relative to TRUE NORTH)
6. Enter the direction and press Start Compass Calibration to begin

**CAUTION:** Make sure there are no large magnetic objects near the UAV when doing compass calibration, like buildings, cars, power poles, as compass may produce an incorrect value.

**CAUTION:** Be extremely careful to ensure the compass is oriented correctly with respect to the vehicle's heading.

### 5.4.3 Reboot Commands

Reboot commands are used after certain actions that specifically request the UAV or Gimbal to be rebooted.

**Reboot Vehicle**
Autopilot reboot command is used after certain actions that specifically request the UAV to be rebooted, like configuring parameters that change functionality, after finishing sensor calibration, or some fault is detected on startup. Reboot command is never used during flight and this function is always disabled after the vehicle is armed.

**Reboot Gimbal**
This command power-cycles the payload module. It is used after configuring payload functions that specifically request for it to be rebooted, or can be used during flight if a fault is detected.

# 6 Mission Planning

Swarm C2 software supports mission planning functionality to automate UAV control during operations. This includes automatic takeoff and landing sequences, mission waypoints, and safety-related functionality such as geofences, rally points, and return points.

Planning functionality can be opened from the main menu or pinned to the main window.

[Figure 6.1: Open mission planning]

## 6.1 Start Screen

When the mission planner opens, the map is centered on the current UAV location, if one is available. Leaving the planner returns to the default map view and refreshes the mission currently stored on the connected UAV.

The start screen provides the main planning actions:

1. **New Mission** creates a new empty mission draft.
2. **Edit Mission** opens the currently assigned mission for editing. If the UAV has no mission uploaded, this button is hidden.
3. **Saved Missions** opens missions stored on the current device. A mission can be saved for later use and not yet uploaded to UAV.
4. **Geofences** opens the geofence planning view.
5. **Sync Mission Plan** fetches the mission currently stored on the connected UAV.

[Figure 6.2: Mission planning menu]

**WARNING:** When a UAV connects to the ground station, Swarm C2 fetches its configuration. If mission-planning configuration is not available for the supported UAV types, mission-planning actions are disabled.

## 6.2 Sync Mission Plan

When the UAV first connects to the GCS and is detected by Swarm C2, the software automatically syncs any pre-existing mission plan from the UAV, if available. Rally points stored on the UAV are included in this sync.

If changes are made to the UAV mission plan externally or through a second tablet, the system will automatically re-sync the mission plan, but the mission can also be manually synced at any time using Sync Mission Plan.

To sync a mission manually:

1. Open the mission planner.
2. Press Sync Mission Plan.

## 6.3 Mission Workflow

The mission planner follows a step-based workflow:

1. Start screen.
2. Vehicle type selection.
3. Mission path editing.
4. Mission upload.

### 6.3.1 Vehicle Type Selection

When entering the planning window, the software automatically checks which type of UAV is being configured and selects the appropriate mission planning presets.

Currently, Swarm C2 supports:

1. Forecaster ISTAR UAV platform.
2. Avenger 5 Loitering Munition.

When creating a new mission, the user must choose a UAV type before planning can continue. If only one UAV type is available in the current configuration, that type is selected automatically and the planner proceeds directly to the mission path step.

[Figure 6.3: Mission type]

If a mission plan is being preconfigured for a different type of UAV, or if nothing is currently connected to Swarm C2 software, the vehicle type can be configured as follows:

1. Open the mission planner.
2. Press New Mission.
3. Select the mission type from the available options.

### 6.3.2 Mission Plan Structure

A mission plan consists of three main flight stages:

1. Takeoff.
2. Waypoints.
3. Return Point.

Each UAV must have a valid mission plan uploaded before flight. A saveable plan must include a takeoff, at least one mission waypoint, and a return point.

Takeoff is a fully automatic sequence in which the UAV climbs to a specified altitude and maintains the heading set during arming. All mission plans must contain a valid takeoff waypoint at the beginning of the mission.

To set a takeoff waypoint:

1. Select the Takeoff item in the planning menu.
2. Press on the map where you want the takeoff to begin.
3. Configure the takeoff parameters as appropriate.

[Figure 6.4: Mission planning]

### 6.3.3 Mission Path Editing

The mission path screen is divided into four expandable groups:

1. Rally Points
2. Takeoff
3. Waypoints
4. Return Point

The planner also shows:

1. Total mission length.
2. Furthest point distance.
3. A waypoint altitude summary on the map when the mission contains items.

Users can activate one of the groups and then click on the map to place that type of mission item.

Mission map interaction works as follows:

1. Clicking an existing mission item activates it for editing.
2. Clicking a midpoint between existing items inserts a new regular waypoint at that position.
3. Clicking on the map while a group is active creates a new mission item of that type.
4. Only one takeoff item is allowed. If a takeoff already exists, the next takeoff placement becomes a regular waypoint.
5. Only one return point is allowed. If a return point already exists, the next placement will move it to the new location.

After a takeoff point is placed in a new mission, the planner automatically switches the active placement mode to regular waypoints.

When an existing mission item is selected, its parameter editor opens in the planner panel. The available parameters depend on the selected item type.

### 6.3.4 Rally Points

Rally points are optional alternate safe locations that can be uploaded with a mission plan. They are stored separately from mission waypoints and are not flown during normal AUTO mission execution. Instead, the autopilot may use them during RTL or other failsafe recovery when a rally point is nearer than the home or return point and within configured range limits.

Use rally points when the default home or return location is unsuitable for recovery, but a nearer clear area -- such as an alternate field or open ground behind terrain -- provides a safer hold or landing option.

**NOTE:** Rally points are optional. A mission can be saved and uploaded without any rally points.

[Figure 6.5: Rally points on the mission map]

**Adding Rally Points**

To add rally points to a mission:

1. Open the mission path editor.
2. Expand Rally Points and activate the group for placement.
3. Click on the map at each desired rally location. Multiple rally points are allowed.
4. Configure the altitude for each rally point as required.

When a rally point is placed, its default altitude is taken from the most recently placed mission item, or from the UAV default cruise altitude if no prior item is available.

**Editing and Removing Rally Points**

To change an existing rally point:

1. Click the rally point marker on the map, or select it from the Rally Points list.
2. Set Altitude in the parameter panel. Rally points do not expose waypoint type, loiter radius, or other mission-waypoint parameters.
3. Drag the marker on the map to reposition the rally point.
4. Delete a rally point using the delete control shown when the item is active.

[Figure 6.6: Rally Points list in the mission planner]

**Map Display**

Rally points appear on the map separately from the mission path:

1. Green markers labeled R1, R2, and so on.
2. A loiter circle around each rally point at the configured rally radius.

The default rally loiter radius for Avenger missions is 300m.

When a UAV is connected, the displayed circle radius follows the vehicle RTL loiter radius loaded from the aircraft.

Rally points are excluded from the mission path line, total mission length, and furthest-point distance. When the mission contains items, the altitude summary chart shows rally points as separate green markers from the main mission path.

**Upload and Sync**

Rally points are saved with the mission on the local device and uploaded to the UAV together with the mission waypoints. If a mission with no rally points is uploaded, any rally points previously stored on the UAV are cleared.

During Sync Mission Plan, rally points currently stored on the connected UAV are fetched and displayed in the planner along with the rest of the mission.

**Operational Behavior**

During RTL, the autopilot may divert to the nearest rally point instead of the home or return point when that rally point is closer and within configured range limits. Rally recovery behavior also depends on the RTL Action and related settings configured in the UAV Safety panel. See Return To Launch (RTL) and RTL Mode for more information.

### 6.3.5 Editable Parameters

The mission path editor currently exposes the following parameters:

**Altitude**
defines the commanded altitude for the selected mission item. This is available for takeoff, regular waypoint, and rally point items.

**Type**
changes a regular waypoint between supported waypoint behaviors:

1. Waypoint is a standard transit point.
2. Loiter unlimited keeps the UAV circling the point until a later mission action changes it (requires user interaction).
3. Loiter turns keeps the UAV circling the point for a defined number of turns.
4. Loiter to altitude keeps the UAV circling while climbing or descending to the required altitude.

**Exit Loiter from**
controls how the UAV leaves a loiter pattern:

1. Center leaves the orbit by passing through the center of the loiter circle.
2. Tangent leaves the orbit tangentially from the loiter circle.

**Leave Loiter at**
defines how the UAV continues after loitering:

1. Direction of next Waypoint exits the loiter in the direction of the next mission item.
2. Any Direction allows exit based on the current direction of travel.

**Loiter Radius**
sets the size of the loiter orbit in meters.

**Turns**
sets how many circles are flown for Loiter turns waypoint.

**Loiter Clockwise**
changes the orbit direction for loiter items. Clockwise or Counter-Clockwise

Some mission values are still taken from UAV configuration defaults rather than edited directly in the planner. Examples include default cruise speed, default loiter radius or takeoff pitch.

## 6.4 Saving and Reusing Missions

### 6.4.1 Saving Missions

The mission path screen allows the user to:

1. Set or edit the mission name.
2. Save the mission to the local device.
3. Delete a stored mission from the local device.
4. Continue to the upload step.

Mission names are limited to 24 characters in the planner.

### 6.4.2 Saved Missions

Saved missions are grouped by UAV type. Selecting a saved mission loads it into the planner, draws it on the map, and centers the map on the first mission item.

[Figure 6.7: Saved missions]

## 6.5 Mission Validation

Before a mission can be saved or uploaded, the planner validates it. A valid mission must have:

1. A selected UAV type.
2. A mission name.
3. A takeoff item.
4. A return point.
5. At least one mission waypoint.

In addition:

1. All mission items must have coordinates and altitude.
2. Minimum altitude for waypoints is 50m.
3. Loiter Turns waypoints must include the number of turns.
4. Loiter waypoint radius must not be lower than the configured default loiter radius for that UAV type.

If validation fails, the planner displays the relevant error messages and the mission cannot be saved or uploaded.

## 6.6 Mission Upload

During upload, the planner shows connected UAVs that match the selected mission type.

The currently active UAV is selected automatically if it matches the mission type and is connected. Otherwise, the first connected eligible UAV is selected automatically.

To upload a mission:

1. Open the Upload step from the mission path screen.
2. Select a connected UAV of the same mission type.
3. Use the confirmation slider to upload the mission.

The upload includes rally points defined in the mission, if any. Each rally point must have valid coordinates and altitude before upload can succeed.

**WARNING:** If no connected UAV of the correct type is available, the mission cannot be uploaded at that moment. In that case, save the mission in the previous step and upload it later when a matching UAV is connected.

[Figure 6.8: Upload mission]

## 6.7 Geofence Planning

Geofence planning is opened from the mission planner start screen by selecting Geofences.

The current geofence workflow supports:

1. One or more polygon geofence groups.
2. Per-group inclusion or exclusion behavior.

Geofence edits are managed separately from the normal mission waypoint workflow. The current planner UI exposes polygon geofences.

[Figure 6.9: Geofence inclusion and exclusion zones]

### 6.7.1 Polygon Geofences

Polygon geofences are organized into groups. Each group is drawn on the map and listed in the planner panel.

To create a new polygon group:

1. Open the Polygon section.
2. Press the + button for a new group.
3. Click on the map where the new geofence should be created.

When a new polygon group is created, the planner generates an initial four-point polygon around the selected map position.

To edit a polygon group:

1. Expand the required group in the list.
2. Use the group type control to toggle between Exclusion and Inclusion zones.
   1. Exclusion zones define areas the UAV must not enter. Entering an exclusion zone is treated as a geofence breach.
   2. Inclusion zones define the permitted operating area. Leaving an inclusion zone is treated as a geofence breach.
3. Press the + button inside the active group to add another point, then click on the map to place it.
4. Drag the polygon handles on the map to reposition existing points.
5. Delete individual points or remove the entire group if required.

Different fill patterns are used on the map to distinguish inclusion and exclusion zones.

### 6.7.2 Uploading Geofences

After editing is complete:

1. Press Upload.
2. Use the confirmation slider to send the geofence data to the active UAV.

# 7 Operation

This chapter describes the standard workflow from pre-flight inspection through arming and launch. Use the in-application Pre-flight Checklist as the main confirmation tool to successfully arm and launch the UAV.

## 7.1 Connecting to the Ground Station

Once the ground control station is prepared and catapult is assembled, connect the system as follows:

1. Power and position the UAV in the launch area.
2. Launch Swarm C2 on the GCS tablet.
3. Wait for the software to detect the UAV, establish telemetry.
4. Confirm that the correct UAV is selected and that telemetry values are updating in the main window.

**NOTE:** This process can take up to 2 minutes. If connection takes longer, verify the UAV power state and radio link.

**NOTE:** For best radio performance, keep the UAV at least 10 meters away from the radio module while on the ground.

## 7.2 Pre-Flight Checklist

[Figure 7.1: Pre-flight Checklist overview]

Before arming, complete the Pre-flight Checklist. The checklist combines automatically evaluated status checks with manually confirmed operator steps.

**NOTE:** The Slide To Arm control becomes available only after all required checklist items are complete.

### 7.2.1 Opening Pre-Flight Checklist

To open pre-flight checklist, click Preflight in top actions dialog

### 7.2.2 Checklist Behaviour

The Pre-flight Checklist behaves as follows:

1. The checklist opens in a pop-up window and requests the current checklist state for the connected UAV. Verification changes, overrides, flags, and resets are synchronized for the active session.
2. When the checklist is incomplete, the first incomplete group opens automatically. Only one group is expanded at a time. When the currently open group becomes complete, it collapses automatically and the next incomplete group opens.
3. Group headers indicate their current state. A group can show incomplete, warning, error, or complete status depending on the result of its checklist items.
4. Automatic checklist items are re-evaluated continuously while the UAV is connected, not armed, and not flying. These items show the automatic-check indicator and can change state without operator input.
5. Manual checklist items use checkboxes.
6. If any Pre-Arm checks fail, the Arming indicator will show Not Ready, when pressing the Arm button, will open a log which shows which systems are failing the Pre-Arm check.

[Figure 7.2: Preflight warnings and errors]

**CAUTION:** The pre-flight checklist may become incomplete or display an error even after successful completion if any items begin to fail afterward. If any of the items become invalid even after the checklist is complete, the program will disable Slide to Arm button.

### 7.2.3 Checklist Structure

The current Avenger 5 pre-flight checklist is divided into six main groups.

Quick navigation:

1. Catapult
2. Mission & parameters
3. Preparation & mounting
4. System checks
5. Video Checks
6. Warhead and Safety

**Catapult**

This group covers the physical preparation of the catapult launch system.

1. **Assemble catapult rail** makes sure that the catapult rail is assembled and secured to the ground properly.
2. **Carriage Safety pin set** confirms that the carriage is in its initial position, secured with a safety lock pin.
3. **Attach pulling rope** makes sure that the pulling rope is attached to the carriage and tensioned properly.
4. **Compressor valve closed** confirms that the main reservoir outlet valve is in the closed position.
5. **Pressure hose connected** confirms that the pressure hose connecting main valve outlet and the launch inlet is secured, clamps are locked and safety pins installed properly.
6. **Compressor ON** confirms that the compressor battery has been inserted and the pressurization process has begun.
7. **Pressure at 13-14 bar** confirms that the determined pressure for safely launching the UAV has been reached.
8. **Plane secured on catapult** confirms that the UAV has been positioned into the launch carriage.

[Figure 7.3: Catapult]

**Mission & Parameters**

This group confirms that the mission and ground-station-related flight settings are ready.

1. **Mission plan** confirms that a valid mission plan is available for the UAV. Helper button: Mission opens mission planning. If a mission is already loaded but the UAV is not in auto mission mode, the helper button changes to Set mode auto.
2. **RTL configured** confirms that the Return-to-Launch behavior has been configured.
3. **Rotator position & direction set** confirms that the antenna rotator position and pointing direction have been set and calibrated. Helper button: Set opens the ground-station control screen.
4. **Rotator in manual mode** confirms that the rotator is in manual mode. Helper button: Set Manual is shown when the rotator is in automatic tracking mode. The button sets the rotator mode to Manual.
5. **Antenna omni mode** confirms that the antenna is set to omnidirectional mode. Helper button: Switch is shown when the antenna is not currently in omni mode and changes it to omnidirectional.
6. **Radio power set** confirms whether Groundstation radio is turned on and power is set to 2W

[Figure 7.4: Mission & parameters]

**Preparation & Mounting**

This group covers the physical preparation of the aircraft before launch.

1. **Stabilizers attached** confirms that the stabilizers are installed.
2. **Wings unfolded** confirms that the wings have been unfolded.
3. **Wing and stabilizer bolts tightened** confirms that the wing and stabilizer bolts are tightened.
4. **Check Propeller** inspect the propeller for any looseness or play, and tighten the screws if necessary.
5. **Servo maximum deflection checked** confirms that servo movement has been checked through full travel. Helper button: Test runs the servo wiggle action. The operator should visually confirm that all servos are moving correctly after pressing the helper button.
6. **Check autostabilization** the operator must visually inspect whether all servos traveled full cycle.

[Figure 7.5: Preparation & mounting]

**System Checks**

This group checks aircraft health, sensor readiness, battery state, and navigation readiness.

1. **Sensors** is the parent item for the automatic sensor-health checks. Helper buttons: Show Logs or Hide Logs open or hide the sensor-error view, and Override appears when blocking sensor faults must be manually accepted.
2. **Battery voltage** checks that battery voltage is within the allowed pre-flight range. A fully charged battery should read approximately 49V to 50V.
3. **Pitot** includes two checks:
   - **Pitot airspeed below 3m/s** -- when the aircraft is stationary and the air around the pitot tube is calm, the indicated airspeed should remain below 3m/s.
   - **Pitot airspeed above 10m/s** -- the operator should blow gently and indirectly into the pitot tube. During this check, the indicated airspeed should rise above 10m/s.
4. **GNSS** is the parent item for GNSS-related pre-flight checks. Helper button: No GNSS Takeoff switches the workflow to a no-GNSS launch procedure. When that mode is active, the button changes to GNSS Takeoff. Child checks:
   - **Disable GNSS** confirms that GNSS is disabled. Helper button: Disable; that action disables GPS. The item is automatically checked.
   - **Plane position set** confirms that the aircraft position has been set by the operator.

[Figure 7.6: System checks]

**Video Checks**

This group verifies that the payload and camera system are ready for operation.

1. **Video Mode STOW** confirms that the video system can be set to STOW mode. Helper button: Set STOW.
2. **Video Track works** confirms that video tracking functions correctly. Clicking the video camera tracks the selected point.
3. **Video Mode GRR** confirms that the video system can be set to GRR mode. Helper button: Set GRR.
4. **RGB/IR Video Works** confirms that switching between RGB and IR video works. Helper button: Toggle Camera.
5. **IR Camera NUC works** confirms that an IR camera NUC can be performed. Helper button: Perform NUC.

[Figure 7.7: Video checks]

**Warhead and Safety**

This group verifies that the warhead and other safety checks are ready for operation.

1. **ESAD Powered** confirms that ESAD has been powered on and is ready.
2. **Removed ESAD Safety Pin** checks whether ESAD has started and is operational.
3. **Compressor Valve Open** manual check to ensure compressor valve has been opened.
4. **Remove Carriage Safety Pin** manual check to ensure catapult safety pin has been removed.

[Figure 7.8: Warhead and Safety]

## 7.3 Arming and Launching

When the Pre-flight Checklist is complete and no critical faults are found, the UAV is ready to be Armed.

To arm the UAV:

1. Open the checklist from the arm control in the flight toolbar if it is not already open.
2. Slide the Slide To Arm button within the pre-flight checklist panel.
3. Confirm that the UAV status in the UAV actions toolbar changes to Armed before proceeding with launch.

[Figure 7.9: Pre-flight complete and ready to arm]

**NOTE:** If arming is rejected, review the Pre-Arm Errors Found dialog or the flight logs, correct the reported issue, and repeat the arming procedure.

### 7.3.1 Launch procedure

Steps for launching the UAV:

1. Move the reservoir outlet valve to the Open position.
2. Remove the safety lock pin from the carriage.
3. Clear the catapult and launch area from any personnel.
4. Press and hold the catapult trigger button untill the UAV has left the catapult.

# 8 Controlling the UAV

Swarm C2 software offers various functions, which are essential for safe and effective flight using Unmanned Defense Systems UAV's. These functions include different flight modes, which are based on the currently selected platform type, controlling flight patterns directly from the main map view, as well as additional functions for direct speed and altitude adjustments.

## 8.1 Flight Modes

The Avenger 5 platform has 5 directly selectable flight modes from the dropdown menu:

1. **AUTO** – UAV flies the uploaded automatic mission.
2. **CRUISE** – Vehicle maintains current heading, altitude and cruise airspeed.
3. **LOITER** – Aircraft circles around the current position that the vehicle was when entering this mode at predefined radius.
4. **RTL** – UAV returns to the RETURN point.
5. **MANUAL** – UAV control surfaces follow direct RC input without autopilot stabilization.

**NOTE:** MANUAL mode is only available when Advanced is enabled in the Display menu. See Display Settings.

To enter the desired flight mode:

1. Press flight mode button within the flight panel.
2. Select desired flight mode from the dropdown.
3. Slide to confirm.

**NOTE:** GUIDED mode is not directly selectable from the dropdown menu. This mode is entered when the UAV is controlled directly from map view using standard flight patterns.

### 8.1.1 Auto Mode

In AUTO mode, UAV follows the uploaded mission plan waypoints or mission commands sequentially, based on the mission item number.

When flying towards the next mission item, vehicle will automatically control its direction and altitude, while maintaining Cruise airspeed unless specified otherwise by the operator. Vehicle will always choose the most direct path towards the next mission item and will set its desired climb or descent rate so that the target altitude is reached at the target location. Waypoints can be completed regardless of current altitude, even if the target altitude has not yet been reached.

**NOTE:** If UAV is flying towards Loiter to Altitude mission item, vehicle will only complete this item when both target position and altitude is reached.

[Figure 8.1: Changing flight mode]

The mission can be paused at any point by simply changing the flight mode, setting a new flight pattern from the map function menu, or dragging an existing flight pattern already present on the map. To resume the mission from the last waypoint, change the mode back into AUTO.

**NOTE:** If there is no mission plan present, vehicle will not allow to enter AUTO mode, and will default to RTL.

The mission plan is always visualized on the map for the currently selected aircraft, and can have different statuses depending on the progress of the mission:

**Takeoff/Home point**
It's always marked as the first point in the mission and is automatically updated to the latest GNSS position before Arming the vehicle. This point is the default return point for RTL

**Completed mission item**
Marks mission items that have already been completed or skipped by the operator.

**Target mission item**
Marks the mission item that is currently being executed. When re-entering AUTO mode, vehicle will continue executing the mission from this point.

**Incomplete mission item**
These items have not been reached or executed, and remain pending in the mission sequence.

### 8.1.2 Cruise Mode

In CRUISE mode, UAV is maneuvered with the use of a joystick, and when no joystick input is present, maintains its current heading, altitude and Cruise airspeed. The joystick controls are not direct control surface inputs, but demands for climb rate and turn rate, so there is no risk of running the vehicle out of control due to sharp maneuvers.

**NOTE:** The virtual joystick is only visible in the Pilot layout, and when UAV is in CRUISE mode, at the bottom right of the main map view.

The joystick has standard axis for plane control:

- **UP** – Decrease altitude.
- **DOWN** – Increase altitude.
- **LEFT** – Turn left.
- **RIGHT** – Turn right.

[Figure 8.2: Pilot joystick control axis]

**CAUTION:** Use caution when flying low to the ground in CRUISE mode, as vehicle controls altitude like in other modes, and takes some time to respond to joystick altitude inputs.

### 8.1.3 Loiter Mode

In LOITER mode, the UAV circles around the position where it was when the mode was activated, while maintaining its current altitude and Cruise airspeed.

The loiter direction is always set clockwise, and the radius of the circle is based on the platform that is currently being used:

- Avenger 5 - 300m

### 8.1.4 RTL Mode

In RTL (Return-to-Launch) mode, the UAV will return to its home location (usually set as the location the UAV was Armed) and loiter there indefinitely, or execute alternate instructions as configured inside the vehicle's Safety menu. If rally points are defined in the uploaded mission plan, the autopilot may divert to the nearest rally point instead when it is closer and within range. See Rally Points.

For Avenger 5 loitering munition platform, home location is set as the Return Point.

Depending on the operational environment, different RTL behavior for altitude control or actions may be required for safe UAV operation where loss of radio link is expected:

1. Altitude control:
   - **Return at Current Altitude** - The UAV flies back to its home location at its current altitude when entering RTL mode.
   - **Return at Specified Altitude** - The UAV flies back to its home location, while also climbing/descending to the configured RTL Altitude.
2. RTL Action:
   - **Disable** - RTL functionality will not be triggered after communication is lost. Vehicle will proceed with the automission or continue executing the last command.
   - **Fly HOME then Land** - Vehicle will return to HOME point first, then proceed with the automatic landing sequence. While flying towards HOME point, vehicle will be in RTL mode and maintain configured altitude control behavior.
   - **Go Directly to landing sequence** - Vehicle will fly straight towards the automatic landing sequence in AUTO mode, gradually descending towards landing altitude.
   - **Only For Go Around** - Vehicle will return to HOME point and then enter a standard loiter pattern at configured RTL altitude.

**CAUTION:** Disabling RTL functionality significantly increases the risk of losing and damaging the UAV, especially when flying in CRUISE or GUIDED modes.

### 8.1.5 Manual Mode

In MANUAL mode, the autopilot passes pilot stick inputs from the RC link directly to the control surfaces. The vehicle does not stabilize heading, altitude, or airspeed.

Unlike CRUISE mode, Swarm C2 does not provide on-screen joystick or gamepad flight control in MANUAL mode. Use the aircraft RC transmitter for direct control.

**CAUTION:** MANUAL mode is intended for experienced operators only. Loss of RC link in MANUAL mode triggers standard RC failsafe behavior configured in the vehicle Safety menu.

### 8.1.6 Guided Mode

When selecting Loiter Here map functionality, a pattern will appear on the map, which allows for quick and easy navigation towards a desired location, without the use of a mission plan.

To set a new loiter pattern on the map, or change the existing pattern's flight altitude:

1. Tap on the map, at the desired pattern location.
2. Select Loiter Here from the context menu.
3. Adjust location and dimensions by dragging the appropriate icons on the displayed flight pattern on the map.
4. Adjust pattern flight altitude using the altitude slider or input buttons.
5. Slide to confirm.

[Figure 8.3: Set new loiter pattern]

**NOTE:** After a flight pattern has been set, its position and flight radius can be changed by dragging the icons found on the displayed flight pattern on the map. When the loiter pattern is updated by dragging one of the pattern icons on the map, the UAV will immediately return to GUIDED mode if currently flying in other modes, and start navigating towards the new pattern.

### 8.1.7 Attack Mode

This mode is entered when operator decides to engage a tracked target through the video feed. When UAV is in ATTACK mode, it will guide itself automatically towards the tracked target, while removing any control constraints for attitude or airspeed present in other modes.

To enter ATTACK mode:

1. Press ENGAGE button within the flight panel.
2. Slide to confirm.

**NOTE:** To enter ATTACK mode, a valid track needs to be set and the warhead must be in the ARMED state.

## 8.2 Additional Vehicle Commands

In addition to the main UAV controls, additional commands for controlling flight altitude and airspeed are available in AUTO, GUIDED and LOITER modes. These commands temporarily override the current target airspeed and/or altitude, and will return back to the previous value after:

- Loiter pattern is updated on the map.
- UAV reaches a waypoint while executing an automatic mission plan.
- Vehicle enters an automatic landing sequence.
- Vehicle changes modes.

**CAUTION:** Make sure to plan for altitude or airspeed changes in advance, as changing altitude frequently or flying at high airspeeds severely increases power consumption and will reduce maximum flight time.

### 8.2.1 Change Altitude

To change current UAV target altitude:

1. Tap the altitude telemetry box on the instrument panel.
2. Use the dropdown panel to select target altitude.
3. Press confirm.

**NOTE:** When the target altitude is set through this panel, UAV will try to reach it as fast as possible, at the maximum available ascent/descent rate.

### 8.2.2 Change Airspeed

To change current UAV target airspeed:

1. Tap the aircraft speed telemetry box on the instrument panel.
2. Use the dropdown panel to select target airspeed.
3. Press confirm.

**NOTE:** When UAV enters RTL mode, if the current target airspeed is set above cruise speed, UAV will maintain that speed until the vehicle leaves RTL mode.

[Figure 8.4: Change altitude panel]

[Figure 8.5: Change airspeed panel]

# 9 Map Operations

## 9.1 Five Whiskey Report

Swarm C2 software allows the user to add, edit or remove 5W reports from the map, which can greatly increase situational awareness when utilizing external tactical awareness software like SitaWare or ATAK.

**NOTE:** All reports from Swarm C2 software are automatically synced, if connected to external tactical awareness software.

To add a report to the map:

1. Press on the map.
2. Select Five W.
3. Complete the fields so the report carries 5W (who, what, when, where, why) information for the map and any linked tactical clients:
   **Unit** – Unit function or type (for example infantry or reconnaissance). This sets the symbol on the map.
   **Standard Identity** – Whether the contact is friendly, hostile, neutral, or unknown.
   **Dimension** – Operating environment (for example ground, air, or sea).
   **Status** – Whether the unit is present at the location or anticipated.
   **Team Size** – Echelon (for example squad, platoon, or company), or unknown.
   **Movement** – Stationary or direction of movement.
   **Identified Unit** – Name, call sign, or designation of the specific force (required).
   **Comment** – Optional remarks or context.
   Where are the coordinates of your map press; When is applied automatically when you submit.
4. Press Mark unit.

[Figure 9.1: Five Whiskey report]

### 9.1.1 Edit Report

To move an existing 5W report:

1. Press and hold on the 5W icon on the map.
2. Drag towards and release over a desired location.
3. Slide to confirm.

To delete or perform a BDA on an existing 5W report:

1. Press on the 5W icon you want to edit or perform BDA.
2. Select Edit Five W/BDA from the function menu.
   a. Press delete to remove 5W report from the map.
   b. Add appropriate information and press Submit BDA.

[Figure 9.2: Edit Five W/BDA]

## 9.2 Call For Fire

This feature allows the user to send a CFF request message to external tactical awareness software, like SitaWare or ATAK.

To send a CFF request:

1. Press on desired coordinates on the map.
2. Select Call For Fire Request from the function menu.
3. Fill out the required information.
4. Slide to confirm.

[Figure 9.3: Call For Fire Request]

## 9.3 Calculate Distance between 2 Points

To calculate linear distance between two points:

1. Press on Ruler icon
2. Ruler mode will be enabled
3. Press on the map where you want to calculate distance from
4. Press on the map where you want to calculate distance to
5. You can press and drag any point to move it to the desired location
6. Total distance is shown in top center

[Figure 9.4: Total distance]

## 9.4 Points of Interest

Points of interest are a separate layer of markers which help operators use supported UAVs efficiently. These markers are stored locally and are separate from 5W reports and mission plans.

To add a new POI marker:

1. Press on desired coordinates on the map.
2. Select Add Point of Interest from the function menu.

To edit POI marker:

1. Press on a POI you want to edit.
2. Select Edit Point of Interest from the function menu.
3. Select POI type and desired options.
4. Press confirm.

[Figure 9.5: POI markers]

# 10 Radio Controls

[Figure 10.1: Rotator Control Interface]

GCS control panel features a Rotator Control Interface, which is opened by pressing the GCS button, and features both radio configuration, and rotator controls:

**Rotator control interface button**
Opens the Ground Control view

**Current radio frequency**
Shows currently selected UAV's Uplink/Downlink frequencies. If no vehicle is connected, then it shows only GCS frequency.

**Antenna toggle**
Switch between omni-directional and directional antennas, that GCS will be using for communication.

**Ground Radio power control**
Set currently selected GCS power output. With Enable/Disable ground transmitter radio output.

**Drone Radio power control**
Set currently selected vehicle power output.

**Set rotator location**
Sets GCS rotator location on the map. Swarm C2 allows multiple ways of setting rotator location:

**NOTE:** When rotator is placed on the map, it is possible to drag rotator icon on the map to fine-tune its location.

**Rotator calibration**
Recalibrates rotator direction to:

**Manual rotator control**
Sets rotator direction to a specified heading.

**Fine rotator control**
moves rotator by 0.5° towards a selected direction.

**Auto Follow toggle**
Enables/Disables auto follow mode.

## 10.1 Set antenna location

Use one of the location buttons to set the antenna location used for tracking and alignment.

**Set To Coordinates**
sets antenna location to specified LAT/LON or MGRS coordinates

**Set On Map**
sets antenna location to current map view's screen center.

**Set To UAV Location**
sets antenna location to currently selected UAV location.

**Set To My Location**
sets antenna location to current computer's location, if available.

## 10.2 Antenna Rotator Map calibration

Aligns the antenna direction on the map only. The antenna does not rotate physically.

**Calibrate By UAV**
calibrates rotator position to last UAV position.

**Calibrate**
calibrates rotator position towards a specified map location.

Before flight, set the rotator position on the map and calibrate its heading to achieve the best radio communication performance.

### 10.2.1 Pre-flight Rotator map calibration procedure

1. Set the rotator position using one of the available functions to achieve the highest possible accuracy.
2. Physically set the rotator direction:
   - Toward a point of interest visible on the map.
   - Toward a specific heading.
   - Toward north.
   **NOTE:** When the rotator location is set, the initial rotator heading is north.
3. Use Calibrate On Map to align the software direction with the physical rotator heading set in the previous step.

**CAUTION:** When using Auto Follow mode, make sure the vehicle is not loitering around the rotator location. Multiple rotations increase the risk of tangling or damaging GCS cables.

**CAUTION:** If multiple UAVs are connected at the same time, rotator Auto Follow tracks the currently selected UAV.

## 10.3 Antenna In-Flight calibration

This calibration applies a physical rotator movement, so the antenna rotates to the corrected heading. Use Fine Tune during flight, when the UAV is airborne and Auto Follow is active, to refine antenna pointing.

### 10.3.1 In-flight fine tune calibration procedure

While Auto Follow mode is enabled, use Fine Tuning mode to adjust the rotator manually. In Fine Tuning mode make small heading corrections and use the RSSI value as guidance.

[Figure 10.2: Rotator Fine Tune]

### 10.3.2 Rotator direction indicators

When changing rotator direction manually, or when using Auto Follow mode, the main map view shows:

1. **True Direction** – directly measured by the rotation mechanism inside the GCS rotator module.
2. **Desired direction** – software-defined target rotator heading.

[Figure 10.3: Rotator visualization]

**CAUTION:** When flying with disabled GNSS for navigation and Auto Follow enabled, the rotator follows the navigational position even if a valid GNSS position is present and shown on the map with a yellow aircraft icon.

[Figure 10.4: Rotator Auto Follow without GNSS]

# 11 Payload Controls

Camera payload is controlled directly from the main window by using the Payload control panel, which can be found at the bottom left edge of the screen, as well as touch functionality from the map or video feed.

[Figure 11.1: Payload control panel]

Payload control panel includes the most used payload controls:

**Menu**
Payload configuration menu

**Zoom**
Controls the zoom level of the video stream. Four buttons on the payload bar: 20× and 1× jump to high and unity zoom + and − step zoom in and out.

**Multitrack**
Payload capability for maintaining and managing multiple tracked objects (if available on current payload build).

**EO/IR camera switch**
Switches between EO (Daylight) and IR (Thermal/night) camera video stream.

**Record**
Starts/stops recording of the video stream. Video is saved to the payload SD card.

**Take a photo**
Takes a high-quality photo and saves it to the payload SD card.

**Expand video window**
Drag across the screen to resize the camera view box larger or smaller.

## 11.1 Camera View

The main layout shows the live EO or IR video from the payload.

[Figure 11.2: Camera]

The information layer on top of the feed includes:

**Compass Heading**
Scale aligned with camera yaw so you can read direction against the horizon.

**Recording**
Shows when the feed is being recorded

**Camera Mode**
Active camera mode

**Tracker Frame**
The on-video box that shows what the current tracker is following.

**Plane position**
Coordinate readouts in MGRS, altitude above sea level (ASL), and above ground (AGL).

**Target position**
Target coordinate readouts in MGRS.

**Ground Station Range**
Distance to Ground Station

**Elevation angle**
How far above or below the horizon the camera is looking: the pitch of the line of sight.

**Field of View**
How wide an area the camera captures

**Battery level**
Remaining charge from aircraft or payload telemetry.

**Slant range**
Straight-line distance from the aircraft to the point you are looking at.

**Satellite count**
How many GNSS satellites are in use for the position fix.

**Scale bar**
A labeled line segment whose length matches a ground distance at the current view and geometry.

**Expand**
Control at the top right of the video; drag it to resize the camera view

## 11.2 Payload configuration

Open Menu on the payload control panel to reach the camera configuration menu. From there you can extend or retract the gimbal, set camera orientation, choose how EO and IR are displayed, and adjust IR image options.

[Figure 11.3: Camera configuration menu]

**NUC**
Recalibrates IR camera to adjust for current temperature.

**NOTE:** NUC should be used right after takeoff or when changing altitude to adjust for temperature differences.

### 11.2.1 Camera mode

[Figure 11.4: Camera Modes]

**STOW**
Points and fixes camera directly forward downward.

**NADIR**
Points and fixes camera directly below the UAV.

**PTC**
Stabilizes view on map coordinates when selecting them from the map. To use this, tap or press the map and select Observe from the function menu.

**OBS**
Camera view follows the platform's motion.

**NOTE:** Joystick control is not possible when in OBS mode. Make sure to switch out of OBS mode to continue using the joystick.

**GRR**
Is controlled by moving the joystick and stabilizes view on map coordinates when not moving the joystick.

### 11.2.2 Camera Display

**Normal**
Shows a single full-frame video feed from the active sensor (EO or IR).

**Picture in Picture**
Shows the primary sensor fullscreen with the other sensor in a smaller inset window, so both views are visible at once.

**Side by Side**
Splits the video area and shows EO and IR streams next to each other at the same time.

**Blended**
Fuses EO and IR imagery into one combined view (payload-dependent), for a single stream that blends visible and thermal detail.

### 11.2.3 IR Color Mode

[Figure 11.5: IR color modes]

**Grayscale**
Renders the IR image in shades of gray (typical thermal view).

**Color**
Applies a false-color palette to the IR image to emphasize temperature differences.

### 11.2.4 IR Polarity

**White Hot**
Warmer objects appear brighter (light) against a darker background.

**Black Hot**
Warmer objects appear darker against a brighter background.

## 11.3 Camera Control

You can control the camera in three ways: on the live video, on the map, or with a joystick (on-screen or USB controller). Camera mode defines how the payload interprets those inputs.

### 11.3.1 Live video

Tap or click an object in the stream to point the gimbal at it and keep it centered. When multitrack is enabled, that applies to the active tracker selected in the multitrack sidebar (see Multitrack below).

### 11.3.2 Map

When in OBS mode you can press on map and select Observe from the menu

**Observe** – Points the camera payload toward the selected coordinates and maintains continuous track.

### 11.3.3 Joystick (gimbal)

**CAUTION:** To use the on-screen joystick for gimbal control, select Payload layout. In Pilot layout, the same control is used for manual aircraft control in Cruise mode, not for the gimbal.

**Virtual joystick**
In Payload layout, the virtual joystick panel drives gimbal pan (left/right) and tilt (up/down). Touch or press on the joystick, then drag; releasing recenters the control and stops motion.

**USB controller (optional)**
When a compatible USB game controller is connected, Main menu shows Joystick. Open Joystick Keys Mapping and turn on Enable/Disable Joystick. You can bind buttons: for each listed action (camera modes, zoom, track, photo, recording, gimbal open/close, and similar), select the bind control and press the controller button you want to use; use the delete control beside that row to clear a button binding. Axis Left and Axis Right are assigned separately to Gimbal or UAV Control (defaults: left Gimbal, right UAV Control).

## 11.4 Multitrack

Multitrack lets the payload maintain several simultaneous point tracks when the aircraft and payload build support it (see Multitrack on the payload control panel above).

[Figure 11.6: Multitrack]

**Opening the menu**
Tap the track icon on the payload control bar to open or close the multitrack sidebar.

**Active tracker**
Assign a tracker slot (0–4) to individual objects on screen.

**Primary tracker**
Set which tracker slot (0–4) the payload treats as the primary tracked object.

[Figure 11.7: Payload Multitrack]

### 11.4.1 Example: assigning and promoting a tracker

To assign an object to slot 0 and set it as the primary tracker:

1. Set the active tracker to slot 0, then tap the desired object on the video stream. The number 0 appears over the tapped point, confirming the assignment.
2. Set the primary tracker to slot 0. The camera will begin following the object assigned to that slot.

# 12 Target Engagement

Avenger 5 Loitering munition platform features a fully automatic guidance system capable of engaging both stationary and moving targets, which are tracked by the gimballed EO/IR camera sensor.

[Figure 12.1: engagement and warhead controls]

Interface elements for engagement and warhead control can be found in the Main window:

1. **Engage** – Initiates automatic guidance towards the tracked target.
2. **Warhead Safety** – Includes controls for operating the ESAD.
3. **Engagement Profiles** – Switches the engagement profile which the UAV flies during terminal guidance.
4. **Abort Engaging** – Initiates an automatic wave-off sequence away from the target.

## 12.1 Warhead Safety

The Electronic Safe and Arm Device (ESAD) is the principal safety device that prevents accidental warhead detonation and requires a proper sequence of events and certain conditions to be met before the warhead can be armed.

Functionally the device has 6 states, which are always visible in the Main window:

- **INACTIVE** - Device is powered off.
- **SAFE** - Device is powered on, but the safety pin is still in place.
- **ARM STAGE 1** - Safety pin is removed.
- **ARM STAGE 2** - Device is airborne and within a safe distance from launch point.
- **ARMED** - Device is armed and ready. This state is initiated by pressing a button in SC2 software.
- **FIRED** - Device has been detonated by proximity sensor trigger or impact.

The operator is allowed to ARM the warhead when all of the described conditions are met:

1. Device is powered and no faults are detected.
2. Safety pin is removed.
3. UAV has successfully completed a takeoff.
4. UAV is currently in flight.

After all of the conditions are met, the operator can ARM or DISARM the warhead:

1. Press Warhead Safety status icon.
2. Press ARM/DISARM.
3. Slide to confirm.

The user is also allowed to self-destruct the device by following the steps below:

1. Press and hold SELF DESTRUCT for 5 seconds.
2. Slide to confirm.

The user is also allowed to Abort the mission by following the steps below:

1. Press and hold ABORT button for 5 seconds.
2. Slide to confirm.

**NOTE:** After aborting the mission, there is no way to turn the device back on.

[Figure 12.2: arming the warhead]

**NOTE:** If the UAV is no longer flying and the ESAD is NOT ARMED, the device will return back to SAFE mode, re-enabling all safety checks and discharging the initiator.

## 12.2 Engagement Profiles

Avenger 5 has two operator selectable engagement profiles which change the trajectory flown by the UAV during the terminal guidance phase:

**CAUTION:** Due to more demanding flight profile, the engagement envelope is highly reduced when engaging moving targets from the front or sides.

**Shallow** – the UAV engages the target at a shallow trajectory, gradually increasing or decreasing the approach angle until the UAV is ~15° above the tracked target. This mode allows for the target to be hit at a shallow angle, or when low noise signature is required during the terminal phase of the engagement.

**CAUTION:** Take note of any terrain features or obstacles when using Shallow engagement profile as it may result in a collision or a loss of a valid track.

**CAUTION:** If initiating the engagement from a steeper angle than 15°, make sure that maximum dive airspeed is not exceeded.

**Direct** – the default mode, where the aircraft flies the most direct path towards the target, without any additional trajectory constraints. This mode has the widest engagement envelope and has the highest probability to hit the target from the front or side, but due to not having any control over its flight trajectory, the impact angle is purely dependent on the positioning of the UAV at the start of the engagement.

Currently selected mode icon is displayed in the Main window. To change the engagement profile:

1. Press Engagement Profile status icon.
2. Select the desired engagement profile.
3. Slide to confirm.

**CAUTION:** When UAV enters Attack mode, changing the engagement profile is no longer possible. If a different engagement profile is necessary, abort the attack and reengage with a new profile.

[Figure 12.3: changing engagement profile]

## 12.3 Engagement

For the loitering munition to have the highest success rate it is important to assure that:

- GCS Failsafe timeout is set long enough, to prevent the UAV from entering RTL during the critical engagement phase.
- Warhead is ARMED.
- Target is tracked using the Daylight (EO) camera sensor.
- Target has a valid track for 2-5 seconds to allow for the targeting system to acquire the best possible estimates.
- Elevation towards the target is no more than 15° when starting the engagement.
- There are no environmental objects that will obstruct the target during the engagement phase.

**CAUTION:** Operator is responsible for assuring that all of these conditions are met before proceeding with target engagement.

**WARNING:** During the engagement, the UAV MUST NOT exceed 55m/s airspeed. If this airspeed is exceeded, the gimbal MAY FAIL to point towards the tracked target, and will result in missing the target. If this airspeed is exceeded, immediately ABORT the engagement and re-engage from a shallower angle.

[Figure 12.4: engagement angle]

To start the engagement:

1. Verify that the abovementioned conditions are met.
2. Press Engage button.
3. Slide to confirm.

When UAV enters ATTACK mode, it will acquire the target that is actively being tracked and turn towards the predicted lead angle required to hit the target. After matching the heading, the engagement controller will take over and the UAV will fly towards the tracked target, while compensating for target motion, wind, or manually moving the active track.

If the track is lost, the UAV will fly in dead-reckoning mode, based on the last known target elevation and heading.

**CAUTION:** The tracker does not have active object detection or dead-reckoning, which would re-track the target by itself if it was lost due to low light conditions or being obstructed by another object or environment. Operator must manually re-track or abort the engagement if the tracker loses the target.

[Figure 12.5: tracker behavior]

## 12.4 Engaging Abort

When UAV engages a target in ATTACK mode, a slider bar will appear at the bottom of the main view screen with the message Abort Engaging.

To abort engagement, simply slide the Abort Engaging bar to the right.

When abort is initiated:

1. UAV will lock its current heading and immediately initiate a climb towards Takeoff altitude.
2. After reaching the Takeoff Altitude UAV will enter GUIDED mode and start a standard loiter around the abort location at Abort Engaging altitude.
3. If no radio link is present, UAV will enter RTL and start flying towards the Return Point.

**WARNING:** If Attack abort was initiated after the estimated time for safe abort has expired. The UAV would still wave-off from the target, but has a high probability of crashing into nearby objects or terrain.

# 13 Operation Scenarios

## 13.1 GNSS Denied Operation

When operating in a GNSS denied environment, Swarm C2 software supports required tools to operate all UDS UAV systems in such an environment.

**CAUTION:** GNSS denied operation requires elevated workload from both Payload Operator and Pilot and poses additional risk of losing the UAV. Read the UAV and GCS manuals carefully and familiarize with vehicle behavior, available functionality and best practices, before UDS UAVs in GNSS denied environment.

### 13.1.1 Takeoff Without GNSS

If no GNSS is available on the ground, UAV requires to manually enter its initial position and wind estimate before takeoff.

**CAUTION:** Wind estimate will always default to 0m/s, and if no value is entered, vehicle may experience very large drift from its true position. Make sure to enter wind speed and direction to your best knowledge before takeoff to minimize risk of losing the UAV.

### 13.1.2 UAV Location Correction in GNSS Denied Environments

When operating in GNSS-denied environments, if camera and vehicle locations on the map differ heavily from what is seen by the payload--but the UAV's or landmark's actual location is known to the operator--you can manually correct its position on the map using the I'm Here, or I'm Looking Here functionality.

Correct the position as follows:

1. Tap a point on the map that's supposed to be the correct UAV's location.
2. Tap "I'm Here" or "I'm Looking Here", depending on what the selected point represents.
3. Slide to confirm.
4. After confirmation, the UAV's position on the map will be updated, the flight path will automatically adjust, and wind speed and direction estimates will be recalculated to ensure accurate navigation to the next waypoint.

**NOTE:** The I'm Here button is only available when the UAV is not using GNSS for navigation.

### 13.1.3 GNSS Disabling in Spoofing Conditions

**NOTE:** Disabling GNSS is only recommended when signs of spoofing are observed.

**CAUTION:** Disabling GNSS during normal flight conditions reduces flight accuracy and may result in UAV damage or harm to nearby areas.

If spoofing is suspected and the UAV begins deviating from its planned flight path, you can disable the GNSS system as follows:

1. On the Flight Toolbar, tap on the GNSS information icon.
2. In the GPS Status window, tap Disable GNSS.

[Figure 13.1: Disable GNSS]

3. Once disabled, GNSS icon will turn red. This indicates that the UAV is now operating on inertial navigation only.

**WARNING:** When flying without GNSS make sure to regularly update vehicle position using known landmarks using I'm Here and I'm Looking Here functionality, as inertial navigation will continually drift from true position without GNSS.

**CAUTION:** If radio communication is lost while GNSS is disabled, the system will automatically re-enable GNSS after a certain amount of time, specified by GPS Failsafe Timeout parameter configured from flight safety options menu.

4. To enable the GNSS system back, tap the Enable GNSS button in the GNSS information window. Once GNSS is re-enabled, the warning message will disappear, and the UAV will start using GNSS for navigation if available.

**CAUTION:** If GNSS was disabled during flight, it will remain disabled unless a radio GNSS failsafe is triggered. Make sure to re-enable it before entering a safe area to avoid the risk of losing the UAV.

# 14 Terminology Glossary

This glossary defines common terms and abbreviations used throughout the Swarm C2 manual.

## 14.1 Core System Terms

| Term | Description |
| --- | --- |
| UDS | Unmanned Defense Systems; manufacturer of the UAV platforms supported by Swarm C2. |
| Swarm C2 | Ground control software used to operate supported UDS UAV systems. |
| GCS | Ground Control Station; operator station used to control UAVs, monitor telemetry, and manage mission execution. |
| UAV | Unmanned Aerial Vehicle; aircraft controlled either autonomously through mission plans or manually by operators. |
| Forecaster | UDS fixed-wing ISTAR UAV platform |
| Avenger | UDS Loitering Munition platform |
| Payload | Mission equipment carried by the UAV, typically EO/IR cameras and related control systems. |
| GCS Operator | Operator responsible for flight setup, mission control, and in-flight UAV operation from Swarm C2. |
| Payload Operator | Operator responsible for camera/payload use, observation, and target-related actions. |
| Launch Assistant | Crew member responsible for safe physical launch and post-landing handling tasks. |

## 14.2 Navigation and Positioning

| Term | Description |
| --- | --- |
| GNSS | Global Navigation Satellite System; satellite-based positioning used for navigation (for example GPS/Galileo). |
| GNSS-denied | Operational condition where GNSS is unavailable, unreliable, jammed, or intentionally disabled. |
| MSL | Mean Sea Level; altitude reference measured relative to average sea level. |
| AGL | Above Ground Level; altitude measured relative to the terrain directly below the aircraft, distinct from MSL. |
| MGRS | Military Grid Reference System; grid-based coordinate format used for tactical location reporting. |
| Geofence | Configured geographic boundary that constrains or governs UAV flight behavior. |
| Rally point | Predefined alternate safe location uploaded with the mission plan; the autopilot may use it during RTL instead of the home or return point when it is nearer and within configured limits. |
| POI | Point of Interest; user-created map marker used for reference during planning or execution. |

## 14.3 Flight Modes and Behaviors

| Term | Description |
| --- | --- |
| AUTO | Automatic mission execution mode using uploaded waypoints and mission logic. |
| CRUISE | Stabilized flight mode optimized for direct heading/altitude style operator control. |
| LOITER | Mode/behavior where UAV circles or holds around a selected point. |
| GUIDED | Map-commanded flight mode activated when the operator issues a Loiter Here or map-pattern command; not selectable directly from the Flight Mode dropdown. |
| RTL | Return To Launch; failsafe or commanded behavior to return toward launch/home according to configured safety options. |
| Home point | The recorded launch/takeoff location that the UAV navigates toward during RTL. |
| Go-around | Landing abort behavior where UAV exits landing and repositions for another landing attempt. |
| Deep Stall | Landing technique where the UAV transitions to a near-vertical descent to land in a confined area; the basis for the Quick Deep Stall profile. |
| Quick Deep Stall | Landing profile variation that transitions to deep-stall landing from a specific approach geometry. |

## 14.4 Payload and Video Terms

| Term | Description |
| --- | --- |
| EO | Electro-Optical; daylight/visible-spectrum camera feed. |
| IR | Infrared; thermal camera feed used for low-visibility or heat-based observation. |
| FOV | Field of View; angular extent of the camera's visible scene, displayed in the payload HUD overlay. |
| NUC | Non-Uniformity Correction; thermal camera recalibration to compensate for temperature-related sensor drift. |
| STOW | Camera/gimbal retracted position; used during takeoff, landing, and when the payload is not in use. |
| NADIR | Camera mode where the gimbal points straight down toward the ground. |
| OBS | Camera mode where the view follows the aircraft platform's motion (body-referenced). |
| PTC | Stabilizes the camera on map coordinates after you select a map point and choose Observe from the function menu. |
| GRR | Payload camera mode where joystick movement controls the view, then stabilizes on map coordinates when joystick input stops. |
| Multitrack | Payload capability for maintaining and managing multiple tracked objects (if available on current payload build). |

## 14.5 Reporting and Tactical Map Functions

| Term | Description |
| --- | --- |
| 5W | Five W report; structured tactical report marker used on the map for shared situational awareness. |
| BDA | Battle Damage Assessment; post-strike/effects assessment update attached to a tactical report. |
| CFF | Call For Fire; formatted fire-support request generated from selected map coordinates. |
| Set Home Position | Function to set the selected map point as the UAV's default RTL destination. |
| "I'm Here" | Function to correct UAV map position in GNSS-denied operation using known true location. |
| "I'm Looking Here" | Function to correct navigation estimate based on known viewed point and payload geometry. |

## 14.6 Connectivity and Integration

| Term | Description |
| --- | --- |
| TAK | Team Awareness Kit; tactical situational awareness ecosystem used for shared map data and collaboration. |
| ATAK | Android Team Awareness Kit; Android client in the TAK ecosystem. |
| SitaWare | External tactical awareness software that can exchange operational data with Swarm C2. |
| Uplink | Radio link from the GCS to the UAV; carries commands and control data. |
| Downlink | Radio link from the UAV to the GCS; carries telemetry and video data. |
| RSSI | Received Signal Strength Indicator; measure of radio link signal strength used for link quality monitoring. |
| MBTiles | Offline map tile file format; loaded via General Settings to enable map display without network access. |

## 14.7 Hardware and Safety Terms

| Term | Description |
| --- | --- |
| RBF pin | Remove Before Flight; safety pin used in pre/post-flight handling procedures. |
| Rotator | Directional antenna positioning mechanism used to improve radio link performance. |
| Auto Follow (Rotator) | Rotator mode that automatically points toward the currently selected UAV. |
