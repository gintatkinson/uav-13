// GENERATED CODE - DO NOT MODIFY BY HAND
import 'package:app_flutter/models/instance_record.dart';

/// Strongly-typed zero-allocation view projection over an InstanceRecord.
extension type const WarheadView(InstanceRecord _record) implements InstanceRecord {
  String get componentName => _record.getPropertyString('component_name') ?? 'Modular warhead with HE, HEAT and thermobaric options';
  String get interfaceItem => _record.getPropertyString('interface_item') ?? 'ESAD payload cable; 1.5 mm HEX screw terminals; mounting brackets and retaining rings';
  int get mass => _record.getPropertyInt('mass') ?? 5;
  String get partNumber => _record.getPropertyString('part_number') ?? 'UDS 5 kg warhead';
  String get power => _record.getPropertyString('power') ?? 'Not stated';
}

