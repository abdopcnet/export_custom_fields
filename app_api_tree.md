# API Tree

## Whitelisted API Methods

All methods are decorated with `@frappe.whitelist()` and require developer mode.

---

## export_custom_fields.customize_form

### `has_custom_fields_in_module(module)`

-   **Description**: Check if module has custom fields (is_system_generated=0)
-   **Parameters**:
    -   `module` (str): Module name
-   **Returns**: `bool` - True if module has custom fields
-   **Usage**: Validation before export

### `export_custom_fields_by_module(module, sync_on_migrate=True)`

-   **Description**: Export Custom Fields and Property Setters for the specified module to JSON files
-   **Parameters**:
    -   `module` (str): Module name
    -   `sync_on_migrate` (bool, optional): Whether to sync on migrate (default: True)
-   **Returns**: `list` - List of exported file paths
-   **Export Location**: `{app}/{module}/custom/{doctype}.json`
-   **Exports**:
    -   Custom Fields
    -   Property Setters
    -   DocType Links (custom only)
-   **Grouping**: By DocType

### `bulk_export_customizations(sync_on_migrate=True, custom_field_names=None, property_setter_names=None)`

-   **Description**: Bulk export multiple Custom Fields and Property Setters
-   **Parameters**:
    -   `sync_on_migrate` (bool, optional): Whether to sync on migrate (default: True)
    -   `custom_field_names` (list, optional): List of Custom Field names to export
    -   `property_setter_names` (list, optional): List of Property Setter names to export
-   **Returns**: `dict` - `{"exported_files": [list of file paths]}`
-   **Behavior**:
    -   Groups by (module, doctype) combinations
    -   Skips records without modules (logs error)
    -   Handles invalid doctypes (unsets module, logs error)
    -   Uses `frappe.modules.utils.export_customizations`

### `bulk_set_module(doctype, names, module)`

-   **Description**: Update module for multiple records
-   **Parameters**:
    -   `doctype` (str): DocType name ('Custom Field', 'Property Setter', 'Server Script', 'Client Script', 'Custom HTML Block', 'Web Page')
    -   `names` (list): List of document names to update
    -   `module` (str): Module name to set
-   **Returns**: `dict` - `{"updated_count": int, "message": str}`
-   **Validation**:
    -   Validates module exists
    -   Validates doctype is supported
    -   Transaction-safe (commits after all updates)

---

## export_custom_fields.server_script

### `export_server_scripts_by_module(module)`

-   **Description**: Export Server Scripts for the specified module to fixtures folder
-   **Parameters**:
    -   `module` (str): Module name
-   **Returns**: `dict` - `{"app": str, "module": str}`
-   **Export Location**: `{app}/fixtures/Server Script.json`
-   **Filters**: `{"module": module}`
-   **Order**: `idx asc, creation asc`

### `export_fixtures_by_module(module)`

-   **Description**: Export all fixtures for the app that contains the specified module
-   **Parameters**:
    -   `module` (str): Module name
-   **Returns**: `dict` - `{"app": str, "module": str}`
-   **Uses**: `frappe.utils.fixtures.export_fixtures`
-   **Exports**: All fixtures for the app

---

## export_custom_fields.client_script

### `export_client_scripts_by_module(module)`

-   **Description**: Export Client Scripts for the specified module to fixtures folder
-   **Parameters**:
    -   `module` (str): Module name
-   **Returns**: `dict` - `{"app": str, "module": str}`
-   **Export Location**: `{app}/fixtures/Client Script.json`
-   **Filters**: `{"module": module}`
-   **Order**: `idx asc, creation asc`

---

## export_custom_fields.custom_html_block

### `export_custom_html_blocks_by_module(name, module, sync_on_migrate=True)`

-   **Description**: Export a single Custom HTML Block to fixtures folder
-   **Parameters**:
    -   `name` (str): Custom HTML Block name (required)
    -   `module` (str): Module name
    -   `sync_on_migrate` (bool, optional): Whether to sync on migrate (default: True)
-   **Returns**: `dict` - `{"app": str, "module": str, "name": str}`
-   **Export Location**: `{app}/fixtures/Custom HTML Block.json`
-   **Export Type**: Single document export (by name)

---

## export_custom_fields.fixtures

### `bulk_export_fixtures(server_script_names=None, client_script_names=None, custom_html_block_names=None)`

-   **Description**: Bulk export Server Scripts, Client Scripts, and Custom HTML Blocks
-   **Parameters**:
    -   `server_script_names` (list, optional): List of Server Script names
    -   `client_script_names` (list, optional): List of Client Script names
    -   `custom_html_block_names` (list, optional): List of Custom HTML Block names
-   **Returns**: `dict` - `{"exported_files": [list of file paths]}`
-   **Behavior**:
    -   Groups by module automatically
    -   Validates module exists for each record
    -   Throws error if module not defined
    -   Exports to separate files per module
-   **Export Locations**:
    -   `{app}/fixtures/Server Script.json`
    -   `{app}/fixtures/Client Script.json`
    -   `{app}/fixtures/Custom HTML Block.json`

---

## export_custom_fields.web_page ⭐ NEW

### `export_web_pages_by_module(module)`

-   **Description**: Export Web Pages for the specified module with special handling for Web Page Block child table
-   **Parameters**:
    -   `module` (str): Module name
-   **Returns**: `dict` - `{"app": str, "module": str}`
-   **Export Locations**:
    -   `{app}/fixtures/Web Page.json` - Parent Web Pages
    -   `{app}/fixtures/Web Page Block.json` - Child table records
-   **Filters**:
    -   Web Page: `{"module": module}`
    -   Web Page Block: `{"parent": ["in", web_page_names], "parenttype": "Web Page"}`
-   **Order**: `idx asc, creation asc`
-   **Special Features**:
    -   Exports parent Web Pages first
    -   Separately exports Web Page Block child records
    -   Maintains parent-child relationships

---

## API Method Summary

### Export Methods by DocType

| DocType           | Method                                  | Export Location                         |
| ----------------- | --------------------------------------- | --------------------------------------- |
| Custom Field      | `export_custom_fields_by_module()`      | `{app}/{module}/custom/{doctype}.json`  |
| Property Setter   | `export_custom_fields_by_module()`      | `{app}/{module}/custom/{doctype}.json`  |
| Server Script     | `export_server_scripts_by_module()`     | `{app}/fixtures/Server Script.json`     |
| Client Script     | `export_client_scripts_by_module()`     | `{app}/fixtures/Client Script.json`     |
| Custom HTML Block | `export_custom_html_blocks_by_module()` | `{app}/fixtures/Custom HTML Block.json` |
| Web Page          | `export_web_pages_by_module()`          | `{app}/fixtures/Web Page.json`          |
| Web Page Block    | `export_web_pages_by_module()`          | `{app}/fixtures/Web Page Block.json`    |

### Bulk Export Methods

| Method                         | DocTypes Supported                              |
| ------------------------------ | ----------------------------------------------- |
| `bulk_export_customizations()` | Custom Field, Property Setter                   |
| `bulk_export_fixtures()`       | Server Script, Client Script, Custom HTML Block |

### Utility Methods

| Method                          | Purpose                  |
| ------------------------------- | ------------------------ |
| `has_custom_fields_in_module()` | Validation check         |
| `bulk_set_module()`             | Module assignment        |
| `export_fixtures_by_module()`   | Full app fixtures export |

---

## Error Handling

All methods:

-   Require `frappe.conf.developer_mode` to be enabled
-   Validate module existence before export
-   Log errors using `frappe.log_error()`
-   Throw user-friendly error messages
-   Use transaction-safe database operations

## Common Patterns

### Module Resolution

```python
module_doc = frappe.get_doc("Module Def", module)
app_name = module_doc.app_name
```

### Export JSON Pattern

```python
export_json(
    doctype,
    file_path,
    filters={"module": module},
    order_by="idx asc, creation asc"
)
```

### File Path Creation

```python
fixtures_path = get_app_path(app_name, "fixtures")
if not os.path.exists(fixtures_path):
    os.makedirs(fixtures_path)
```

## JavaScript API Calls

### Form View Export

```javascript
frappe.call({
	method: 'export_custom_fields.{module}.export_{doctype}_by_module',
	args: { module: frm.doc.module },
	callback: function (r) {
		/* handle response */
	},
});
```

### Bulk Set Module

```javascript
frappe.call({
	method: 'export_custom_fields.customize_form.bulk_set_module',
	args: {
		doctype: 'DocType Name',
		names: [name1, name2],
		module: 'Module Name',
	},
});
```
