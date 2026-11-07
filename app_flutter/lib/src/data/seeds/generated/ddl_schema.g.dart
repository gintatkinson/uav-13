// GENERATED CODE - DO NOT MODIFY BY HAND
import 'package:sqflite_common_ffi/sqflite_ffi.dart';
const int kDeapSchemaHash = 0x594A54B3E334EFBC;
Future<void> applyCanonicalDeapDdl(DatabaseExecutor txn) async {
    await txn.execute('''
      CREATE TABLE IF NOT EXISTS type_definitions (type_name TEXT PRIMARY KEY, display_name TEXT NOT NULL, icon_symbol TEXT NOT NULL)
    ''');
    await txn.execute('''
      CREATE TABLE IF NOT EXISTS type_attributes (id INTEGER PRIMARY KEY AUTOINCREMENT, type_name TEXT NOT NULL REFERENCES type_definitions(type_name) ON DELETE CASCADE, key TEXT NOT NULL, label TEXT NOT NULL, field_type TEXT NOT NULL, section_label TEXT, section_order INTEGER DEFAULT 0, is_required INTEGER DEFAULT 0, min_value REAL, max_value REAL, regex_pattern TEXT, enum_options TEXT, enum_display_names TEXT, default_value TEXT, input_formatters TEXT, UNIQUE(type_name, key))
    ''');
    await txn.execute('''
      CREATE TABLE IF NOT EXISTS type_relations (id INTEGER PRIMARY KEY AUTOINCREMENT, parent_type TEXT NOT NULL REFERENCES type_definitions(type_name) ON DELETE CASCADE, relation_name TEXT NOT NULL, child_type TEXT NOT NULL REFERENCES type_definitions(type_name) ON DELETE CASCADE, display_label TEXT NOT NULL)
    ''');
    await txn.execute('''
      CREATE TABLE IF NOT EXISTS instances (id TEXT PRIMARY KEY, type_name TEXT NOT NULL REFERENCES type_definitions(type_name) ON DELETE RESTRICT, label TEXT NOT NULL, parent_id TEXT REFERENCES instances(id) ON DELETE SET NULL, created_at INTEGER NOT NULL, updated_at INTEGER NOT NULL)
    ''');
    await txn.execute('''
      CREATE TABLE IF NOT EXISTS properties (id INTEGER PRIMARY KEY AUTOINCREMENT, instance_id TEXT NOT NULL REFERENCES instances(id) ON DELETE CASCADE, key TEXT NOT NULL, value_text TEXT, value_num REAL, value_type TEXT NOT NULL, UNIQUE(instance_id, key))
    ''');
    await txn.execute('''
      CREATE INDEX IF NOT EXISTS idx_properties_lookup ON properties(instance_id, key)
    ''');
    await txn.execute('''
      CREATE INDEX IF NOT EXISTS idx_instances_type ON instances(type_name)
    ''');
    await txn.execute('''
      CREATE INDEX IF NOT EXISTS idx_instances_parent ON instances(parent_id)
    ''');
}
