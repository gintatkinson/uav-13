// GENERATED CODE - DO NOT MODIFY BY HAND
import 'package:app_flutter/models/instance_record.dart';

/// Strongly-typed zero-allocation view projection over an InstanceRecord.
extension type const PropulsionView(InstanceRecord _record) implements InstanceRecord {
  String get componentName => _record.getPropertyString('component_name') ?? 'Propulsion subsystem boundary enclosing fuse, power meter, ESC and motor';
  String get interfaceItem => _record.getPropertyString('interface_item') ?? 'Battery main power; three-phase motor drive; ESC telemetry';
  String get mass => _record.getPropertyString('mass') ?? 'Not stated';
  String get partNumber => _record.getPropertyString('part_number') ?? 'Not stated';
  String get power => _record.getPropertyString('power') ?? 'Not stated';
}

