# Export Custom Fields - Workflow

## Export Workflow Diagram

```
User Action
    │
    ├─> Open Custom Field Form
    │   └─> Click "📦 Export to Module"
    │       └─> Select Module
    │           └─> export_custom_fields_by_module()
    │               └─> Export to: {app}/{module}/custom/{doctype}.json
    │
    ├─> Open Property Setter Form
    │   └─> Click "📦 Export to Module"
    │       └─> Select Module
    │           └─> export_custom_fields_by_module()
    │               └─> Export to: {app}/{module}/custom/{doctype}.json
    │
    ├─> Open Customize Form
    │   ├─> Click "📦 Export to Module" (Custom App)
    │   │   └─> export_custom_fields_by_module()
    │   │       └─> Export to: {app}/{module}/custom/{doctype}.json
    │   │
    │   └─> Click "Export Customizations" (Core Frappe)
    │       └─> frappe.modules.utils.export_customizations()
    │           └─> Export to: {app}/{module}/custom/{doctype}.json
    │
    ├─> Open Server Script Form
    │   └─> Click "📦 Export to Module"
    │       └─> export_server_scripts_by_module()
    │           └─> Export to: {app}/fixtures/server_script.json
    │
    ├─> Open Client Script Form
    │   └─> Click "📦 Export to Module"
    │       └─> export_client_scripts_by_module()
    │           └─> Export to: {app}/fixtures/client_script.json
    │
    └─> Open Custom HTML Block Form
        └─> Click "📦 Export to Module"
            └─> Select Module
                └─> export_custom_html_blocks_by_module()
                    └─> Export to: {app}/fixtures/custom_html_block.json
```

## Command-Line Workflow

```
bench --site [site] export-fixtures --app [app]
    │
    └─> frappe.utils.fixtures.export_fixtures()
        └─> Reads hooks.py fixtures
            └─> Export to: {app}/fixtures/{doctype}.json
```

## Common Workflow Steps

1. **Developer Mode Check** - All exports require developer_mode enabled
2. **Module Selection** - User selects target module (except fixtures export)
3. **Data Collection** - System collects customization data from database
4. **File Creation** - Creates/updates JSON files in appropriate locations
5. **User Notification** - Shows success message with file paths
