// GENERATED CODE - DO NOT MODIFY BY HAND
import 'package:app_flutter/models/instance_record.dart';

/// Strongly-typed zero-allocation view projection over an InstanceRecord.
extension type const EsadDetonatorView(InstanceRecord _record) implements InstanceRecord {
  String get componentName => _record.getPropertyString('component_name') ?? 'LEEFI or EFI detonator';
  String get interfaceItem => _record.getPropertyString('interface_item') ?? 'ESAD J401 HV_OUT and HV_GND';
  String get mass => _record.getPropertyString('mass') ?? 'Not stated';
  String get partNumber => _record.getPropertyString('part_number') ?? 'Not stated';
  String get power => _record.getPropertyString('power') ?? 'Not stated';
}

