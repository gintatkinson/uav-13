// GENERATED CODE - DO NOT MODIFY BY HAND
import 'package:app_flutter/models/instance_record.dart';

/// Strongly-typed zero-allocation view projection over an InstanceRecord.
extension type const RpiCm5004032View(InstanceRecord _record) implements InstanceRecord {
  String get componentName => _record.getPropertyString('component_name') ?? 'Raspberry Pi compute module for SC2 command and control interfacing';
  String get interfaceItem => _record.getPropertyString('interface_item') ?? 'ETH; serial to autopilot; RS-485 to ESAD; GPIO trigger to ESAD';
  String get mass => _record.getPropertyString('mass') ?? 'Not stated';
  String get partNumber => _record.getPropertyString('part_number') ?? 'CM5004032';
  String get power => _record.getPropertyString('power') ?? 'Not stated';
}

