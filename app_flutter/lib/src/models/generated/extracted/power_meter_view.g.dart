// GENERATED CODE - DO NOT MODIFY BY HAND
import 'package:app_flutter/models/instance_record.dart';

/// Strongly-typed zero-allocation view projection over an InstanceRecord.
extension type const PowerMeterView(InstanceRecord _record) implements InstanceRecord {
  String get componentName => _record.getPropertyString('component_name') ?? 'Voltage and current sensor with main power switch';
  String get interfaceItem => _record.getPropertyString('interface_item') ?? 'Battery power input; switched power to ESC; CAN 1; UAV RBF key';
  String get mass => _record.getPropertyString('mass') ?? 'Not stated';
  String get partNumber => _record.getPropertyString('part_number') ?? 'Not stated';
  String get power => _record.getPropertyString('power') ?? 'Not stated';
}

