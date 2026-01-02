# Workflow Diagrams

## Overview

This document describes the complete workflow for all export operations in the Export Custom Fields app.

---

## 1. Custom Fields & Property Setters Export

### Single Record Export (Form View)

```
User Opens Customize Form / Custom Field / Property Setter Form
    ↓
Check Developer Mode
    ↓
Check if module field is set
    ↓
[If module exists]
    Show "Export to Module" Button (Red)
    ↓
User Clicks "Export to Module"
    ↓
Validate Developer Mode
    ↓
Get Module from Document
    ↓
Call: export_custom_fields_by_module(module)
    ↓
Fetch All Custom Fields for Module
    ↓
Fetch All Property Setters for Module
    ↓
Fetch DocType Links (custom only)
    ↓
Group by DocType
    ↓
For Each DocType:
    ├─ Prepare export data:
    │   ├─ custom_fields
    │   ├─ property_setters
    │   ├─ links
    │   └─ sync_on_migrate flag
    ↓
    Create folder: {app}/{module}/custom/
    ↓
    Export to: {app}/{module}/custom/{doctype}.json
    ↓
Show Success Message with file paths
```

### Bulk Export (List View)

```
User Opens Custom Field / Property Setter List View
    ↓
Select Multiple Records
    ↓
Click Bulk Export Button
    ↓
Validate Developer Mode
    ↓
Call: bulk_export_customizations()
    ↓
Get Selected Records
    ↓
Group by (module, doctype)
    ↓
For Each (module, doctype) Combination:
    ├─ Validate module exists
    ├─ Skip records without module (log error)
    ├─ Check if doctype exists
    │   ├─ [If not exists]
    │   │   ├─ Unset module for records
    │   │   ├─ Log error
    │   │   └─ Skip export
    │   └─ [If exists]
    │       └─ Call: frappe.modules.utils.export_customizations()
    ↓
Show Summary (exported files count)
```

### Set Module Workflow

```
User Opens Any Supported DocType Form
    ↓
Click "Set Module" Button (Green)
    ↓
Show Prompt Dialog
    ├─ Field: Module (Link to Module Def)
    └─ Default: Current module (if exists)
    ↓
User Selects Module
    ↓
Call: bulk_set_module(doctype, [name], module)
    ↓
Validate Developer Mode
    ↓
Validate Module Exists
    ↓
Update Document Module Field
    ↓
Commit Transaction
    ↓
Reload Document
    ↓
Show Success Message
```

---

## 2. Server Script Export

### Single Record Export

```
User Opens Server Script Form
    ↓
Check Developer Mode
    ↓
Check if module field is set
    ↓
[If module exists]
    Show "Export to Module" Button (Red)
    ↓
User Clicks "Export to Module"
    ↓
Validate Developer Mode
    ↓
Get Module from Document
    ↓
Call: export_server_scripts_by_module(module)
    ↓
Get Module Def Document
    ↓
Get App Name from Module
    ↓
Create fixtures folder: {app}/fixtures/
    ↓
Export to: {app}/fixtures/Server Script.json
    ├─ Filter: {"module": module}
    └─ Order: idx asc, creation asc
    ↓
Show Success Message
```

### Bulk Export

```
User Opens Server Script List View
    ↓
Select Multiple Records
    ↓
Click Bulk Export Button
    ↓
Validate Developer Mode
    ↓
Call: bulk_export_fixtures(server_script_names=[...])
    ↓
Get Selected Server Scripts
    ↓
Group by Module
    ↓
For Each Module:
    ├─ Validate module exists
    ├─ Get App Name
    ├─ Create fixtures folder
    └─ Export to: {app}/fixtures/Server Script.json
        └─ Filter: {"name": ["in", script_names]}
    ↓
Show Summary
```

---

## 3. Client Script Export

### Single Record Export

```
User Opens Client Script Form
    ↓
Check Developer Mode
    ↓
Check if module field is set
    ↓
[If module exists]
    Show "Export to Module" Button (Red)
    ↓
User Clicks "Export to Module"
    ↓
Validate Developer Mode
    ↓
Get Module from Document
    ↓
Call: export_client_scripts_by_module(module)
    ↓
Get Module Def Document
    ↓
Get App Name from Module
    ↓
Create fixtures folder: {app}/fixtures/
    ↓
Export to: {app}/fixtures/Client Script.json
    ├─ Filter: {"module": module}
    └─ Order: idx asc, creation asc
    ↓
Show Success Message
```

### Bulk Export

```
User Opens Client Script List View
    ↓
Select Multiple Records
    ↓
Click Bulk Export Button
    ↓
Validate Developer Mode
    ↓
Call: bulk_export_fixtures(client_script_names=[...])
    ↓
Get Selected Client Scripts
    ↓
Group by Module
    ↓
For Each Module:
    ├─ Validate module exists
    ├─ Get App Name
    ├─ Create fixtures folder
    └─ Export to: {app}/fixtures/Client Script.json
        └─ Filter: {"name": ["in", script_names]}
    ↓
Show Summary
```

---

## 4. Custom HTML Block Export

### Single Record Export

```
User Opens Custom HTML Block Form
    ↓
Check Developer Mode
    ↓
Click "Export to Module" Button
    ↓
Show Prompt Dialog
    ├─ Field: Module (Link to Module Def)
    └─ Field: Sync on Migrate (Check)
    ↓
User Selects Module
    ↓
Call: export_custom_html_blocks_by_module(name, module)
    ↓
Validate Developer Mode
    ↓
Get Module Def Document
    ↓
Get App Name from Module
    ↓
Create fixtures folder: {app}/fixtures/
    ↓
Export to: {app}/fixtures/Custom HTML Block.json
    ├─ Filter: {"name": name}
    └─ Order: idx asc, creation asc
    ↓
Show Success Message
```

### Bulk Export

```
User Opens Custom HTML Block List View
    ↓
Select Multiple Records
    ↓
Click Bulk Export Button
    ↓
Validate Developer Mode
    ↓
Call: bulk_export_fixtures(custom_html_block_names=[...])
    ↓
Get Selected Custom HTML Blocks
    ↓
Group by Module
    ↓
For Each Module:
    ├─ Validate module exists
    ├─ Get App Name
    ├─ Create fixtures folder
    └─ Export to: {app}/fixtures/Custom HTML Block.json
        └─ Filter: {"name": ["in", block_names]}
    ↓
Show Summary
```

---

## 5. Web Page Export ⭐ NEW

### Single Record Export

```
User Opens Web Page Form
    ↓
Check Developer Mode
    ↓
Check if module field is set
    ↓
[If module exists]
    Show "Export to Module" Button (Red)
    ↓
User Clicks "Export to Module"
    ↓
Validate Developer Mode
    ↓
Get Module from Document
    ↓
Call: export_web_pages_by_module(module)
    ↓
Get Module Def Document
    ↓
Get App Name from Module
    ↓
Create fixtures folder: {app}/fixtures/
    ↓
Export Web Pages:
    ├─ File: {app}/fixtures/Web Page.json
    ├─ Filter: {"module": module}
    └─ Order: idx asc, creation asc
    ↓
Get All Web Page Names in Module
    ↓
[If Web Pages exist]
    Export Web Page Blocks:
        ├─ File: {app}/fixtures/Web Page Block.json
        ├─ Filter: {"parent": ["in", web_page_names], "parenttype": "Web Page"}
        └─ Order: idx asc, creation asc
    ↓
Show Success Message
```

### Special Handling

```
Web Page Export Process:
    ↓
Step 1: Export Parent Web Pages
    ├─ Filter by module
    └─ Export to: Web Page.json
    ↓
Step 2: Get Web Page Names
    └─ Extract names from exported Web Pages
    ↓
Step 3: Export Child Web Page Blocks
    ├─ Filter by parent (Web Page names)
    ├─ Filter by parenttype ("Web Page")
    └─ Export to: Web Page Block.json
    ↓
Result: Two separate JSON files
    ├─ Web Page.json (parent records)
    └─ Web Page Block.json (child records)
```

---

## 6. Full App Fixtures Export

### Export All Fixtures

```
User Opens Server Script Form
    ↓
Click "Export Fixtures" Button (if available)
    ↓
Validate Developer Mode
    ↓
Get Module from Document
    ↓
Call: export_fixtures_by_module(module)
    ↓
Get Module Def Document
    ↓
Get App Name from Module
    ↓
Call: frappe.utils.fixtures.export_fixtures(app=app_name)
    ↓
Export All Fixtures for App
    ├─ Server Scripts
    ├─ Client Scripts
    ├─ Custom HTML Blocks
    └─ Other fixtures
    ↓
Show Success Message
```

---

## 7. Error Handling Workflow

### Validation Errors

```
Any Export Operation
    ↓
Check Developer Mode
    ├─ [Not Enabled]
    │   └─ Throw Error: "Only allowed in developer mode"
    └─ [Enabled]
        ↓
Check Module Exists
        ├─ [Not Exists]
        │   └─ Throw Error: "Module does not exist"
        └─ [Exists]
            ↓
Check App Name
            ├─ [Not Found]
            │   └─ Throw Error: "Could not determine app name"
            └─ [Found]
                ↓
Proceed with Export
```

### Export Errors

```
Export Operation
    ↓
Try Export
    ├─ [Success]
    │   └─ Show Success Message
    └─ [Error]
        ↓
Log Error
        ├─ Method: frappe.log_error()
        ├─ Message: "[file.py] method: function_name"
        └─ Tag: Error Category
        ↓
Throw User-Friendly Error
        └─ Message: "Error exporting {doctype}: {error}"
```

### Invalid Doctype Handling

```
Bulk Export Customizations
    ↓
For Each (module, doctype) Combination
    ↓
Try Export
    ├─ [Doctype Not Found]
    │   ├─ Unset module for all records referencing doctype
    │   ├─ Commit transaction
    │   ├─ Log error
    │   └─ Skip export (continue with next)
    └─ [Doctype Found]
        └─ Proceed with export
```

---

## 8. Module Assignment Workflow

### Bulk Set Module

```
User Selects Multiple Records in List View
    ↓
Click "Set Module" Button
    ↓
Show Prompt Dialog
    ├─ Field: Module (Link to Module Def)
    └─ Default: Empty or first record's module
    ↓
User Selects Module
    ↓
Call: bulk_set_module(doctype, names, module)
    ↓
Validate Developer Mode
    ↓
Validate Doctype Supported
    ├─ [Not Supported]
    │   └─ Throw Error: "Invalid doctype"
    └─ [Supported]
        ↓
Validate Module Exists
        ├─ [Not Exists]
        │   └─ Throw Error: "Module does not exist"
        └─ [Exists]
            ↓
For Each Record Name:
            ├─ Try Update Module
            │   ├─ [Success]
            │   │   └─ Increment counter
            │   └─ [Error]
            │       ├─ Log error
            │       └─ Throw error
            ↓
Commit Transaction
    ↓
Return Success
    ├─ updated_count
    └─ message
```

---

## Workflow Summary

### Export Types

1. **Custom Files Export** (`{app}/{module}/custom/`)
   - Custom Fields
   - Property Setters
   - DocType Links

2. **Fixtures Export** (`{app}/fixtures/`)
   - Server Scripts
   - Client Scripts
   - Custom HTML Blocks
   - Web Pages
   - Web Page Blocks

### Common Patterns

1. **Form View Pattern**:
   - Check developer mode
   - Check module field
   - Show export button
   - Validate and export

2. **List View Pattern**:
   - Select records
   - Group by module
   - Bulk export
   - Show summary

3. **Error Handling Pattern**:
   - Validate inputs
   - Try operation
   - Log errors
   - Show user feedback

### Key Decision Points

- **Module Check**: Export only if module is set
- **Developer Mode**: All operations require developer mode
- **Doctype Validation**: Skip invalid doctypes, log errors
- **Grouping**: Group by (module, doctype) for bulk operations
- **File Organization**: Separate custom files from fixtures
