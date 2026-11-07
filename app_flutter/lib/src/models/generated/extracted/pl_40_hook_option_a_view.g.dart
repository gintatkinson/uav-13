// GENERATED CODE - DO NOT MODIFY BY HAND
import 'package:app_flutter/models/instance_record.dart';

/// Strongly-typed zero-allocation view projection over an InstanceRecord.
extension type const Pl40HookOptionAView(InstanceRecord _record) implements InstanceRecord {
  String get componentName => _record.getPropertyString('component_name') ?? 'Front and rear hook brackets, Aluminum 6061-T6';
  String get interfaceItem => _record.getPropertyString('interface_item') ?? 'Carriage support levers';
  double get mass => _record.getPropertyDouble('mass') ?? 0.004;

  /// Validates SysML inv constraint for mass
  bool validateMass() {
    final v = mass;
    return v >= 0.0 && v <= 1000000.0;
  }
  String get partNumber => _record.getPropertyString('part_number') ?? 'Not stated';
  String get power => _record.getPropertyString('power') ?? 'Not stated';
}

