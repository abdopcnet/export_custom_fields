# API Tree

## Whitelisted API Methods

### export_custom_fields.customize_form

- `has_custom_fields_in_module(module)`
  - Description: Check if module has custom fields
  - Returns: boolean

- `export_custom_fields_by_module(module, sync_on_migrate=True)`
  - Description: Export Custom Fields and Property Setters for module
  - Returns: List of exported file paths

- `bulk_export_customizations(sync_on_migrate=True, custom_field_names=None, property_setter_names=None)`
  - Description: Bulk export multiple custom fields/property setters
  - Returns: List of exported files

### export_custom_fields.server_script

- `export_server_scripts_by_module(module)`
  - Description: Export Server Scripts for module to fixtures
  - Returns: Dict with app and module info

- `export_fixtures_by_module(module)`
  - Description: Export all fixtures for app containing module
  - Returns: Dict with app and module info

### export_custom_fields.client_script

- `export_client_scripts_by_module(module)`
  - Description: Export Client Scripts for module to fixtures
  - Returns: Dict with app and module info

### export_custom_fields.custom_html_block

- `export_custom_html_blocks_by_module(name, module, sync_on_migrate=True)`
  - Description: Export Custom HTML Block to fixtures
  - Returns: Dict with app, module, and name info

### export_custom_fields.fixtures

- `bulk_export_fixtures(server_script_names=None, client_script_names=None, custom_html_block_names=None)`
  - Description: Bulk export fixtures
  - Returns: Export results
