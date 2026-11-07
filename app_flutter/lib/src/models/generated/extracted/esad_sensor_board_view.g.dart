// GENERATED CODE - DO NOT MODIFY BY HAND
import 'package:app_flutter/models/instance_record.dart';

/// Strongly-typed zero-allocation view projection over an InstanceRecord.
extension type const EsadSensorBoardView(InstanceRecord _record) implements InstanceRecord {
  String get componentName => _record.getPropertyString('component_name') ?? 'Proximity and impact sensor board with UART, IRQ_L and 5 V interface';
  String get interfaceItem => _record.getPropertyString('interface_item') ?? 'J1 cable to ESAD J102; 5 V power; UART; IRQ_L trigger';
  String get mass => _record.getPropertyString('mass') ?? 'Not stated';
  String get partNumber => _record.getPropertyString('part_number') ?? 'Not stated';
  String get power => _record.getPropertyString('power') ?? 'Not stated';
}

