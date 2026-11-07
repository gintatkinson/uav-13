// GENERATED CODE - DO NOT MODIFY BY HAND
import 'package:app_flutter/models/instance_record.dart';

/// Strongly-typed zero-allocation view projection over an InstanceRecord.
extension type const RadioModuleDtcView(InstanceRecord _record) implements InstanceRecord {
  String get componentName => _record.getPropertyString('component_name') ?? 'Command and control radio transceiver';
  String get interfaceItem => _record.getPropertyString('interface_item') ?? 'ETH; serial from autopilot; 12 V radio power; two RF antenna feeds';
  String get mass => _record.getPropertyString('mass') ?? 'Not stated';
  String get partNumber => _record.getPropertyString('part_number') ?? 'DTC 4.4-5 GHz';
  String get power => _record.getPropertyString('power') ?? 'Not stated';
}

