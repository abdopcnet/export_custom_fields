# Workflow

## Export Custom Fields / Property Setters

```
User Opens Customize Form / Custom Field / Property Setter
    ↓
Click "📦 Export to Module" Button
    ↓
Validate Developer Mode
    ↓
Get Module from Document
    ↓
Fetch All Custom Fields & Property Setters for Module
    ↓
Group by DocType
    ↓
Export to: {app}/{module}/custom/{doctype}.json
    ↓
Set sync_on_migrate if enabled
    ↓
Show Success Message
```

## Export Server / Client Scripts

```
User Opens Server Script / Client Script Form
    ↓
Click "📦 Export to Module" Button
    ↓
Validate Developer Mode
    ↓
Get Module from Document
    ↓
Get App Name from Module
    ↓
Create fixtures folder (if not exists)
    ↓
Export Scripts to: {app}/fixtures/{doctype}.json
    ↓
Filter by module, order by idx/creation
    ↓
Show Success Message
```

## Export Custom HTML Block

```
User Opens Custom HTML Block Form
    ↓
Click "📦 Export to Module" Button
    ↓
Prompt for Module Selection
    ↓
Validate Developer Mode
    ↓
Get App Name from Module
    ↓
Create fixtures folder (if not exists)
    ↓
Export Block to: {app}/fixtures/custom_html_block.json
    ↓
Show Success Message
```

## Bulk Export Workflow

```
User Selects Multiple Records in List View
    ↓
Click Bulk Export Button
    ↓
Validate Developer Mode
    ↓
Group Records by (module, doctype)
    ↓
For Each (module, doctype) Combination:
    ├─ Export using frappe.modules.utils.export_customizations
    └─ Track exported files
    ↓
Show Summary (exported files count)
```
