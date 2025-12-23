# Export Custom Fields - API Structure

## Server-Side APIs (Python)

### export_custom_fields.customize_form

-   `export_custom_fields_by_module(module, sync_on_migrate=False)`
    -   Exports Custom Fields and Property Setters for a module
    -   Returns: List of exported file paths

### export_custom_fields.server_script

-   `export_server_scripts_by_module(module)`
    -   Exports Server Scripts for a module to fixtures folder
    -   Returns: Dict with app and module info
-   `export_fixtures_by_module(module)`
    -   Exports fixtures for the app containing the module
    -   Returns: Dict with app and module info

### export_custom_fields.client_script

-   `export_client_scripts_by_module(module)`
    -   Exports Client Scripts for a module to fixtures folder
    -   Returns: Dict with app and module info

### export_custom_fields.custom_html_block

-   `export_custom_html_blocks_by_module(name, module, sync_on_migrate=False)`
    -   Exports Custom HTML Block to fixtures folder
    -   Returns: Dict with app, module, and name info

## Client-Side Extensions (JavaScript)

### Customize Form

-   Adds "📦 Export to Module" button
-   Calls: `export_custom_fields.customize_form.export_custom_fields_by_module`

### Custom Field

-   Adds "📦 Export to Module" button
-   Calls: `export_custom_fields.customize_form.export_custom_fields_by_module`

### Property Setter

-   Adds "📦 Export to Module" button
-   Calls: `export_custom_fields.customize_form.export_custom_fields_by_module`

### Server Script

-   Adds "📦 Export to Module" button
-   Calls: `export_custom_fields.server_script.export_server_scripts_by_module`

### Client Script

-   Adds "📦 Export to Module" button
-   Calls: `export_custom_fields.client_script.export_client_scripts_by_module`

### Custom HTML Block

-   Adds "📦 Export to Module" button
-   Calls: `export_custom_fields.custom_html_block.export_custom_html_blocks_by_module`

## Core Frappe Functions Used

### frappe.modules.utils.export_customizations

-   Core Frappe function called by "Export Customizations" button in Customize Form
-   Exports Custom Fields, Property Setters, DocType Links for a doctype
-   Location: `/home/frappe/frappe-bench/apps/frappe/frappe/modules/utils.py`

### frappe.utils.fixtures.export_fixtures

-   Core Frappe function used by `bench export-fixtures` command
-   Exports fixtures defined in hooks.py to `[app]/fixtures` folder
-   Location: `/home/frappe/frappe-bench/apps/frappe/frappe/utils/fixtures.py`
-   Command: `bench --site [site] export-fixtures --app [app]`
