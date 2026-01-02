# File Structure

## Complete Application Structure

```
export_custom_fields/
├── export_custom_fields/
│   ├── __init__.py                    # App initialization
│   ├── hooks.py                        # Frappe hooks configuration
│   ├── modules.txt                     # Module definitions
│   ├── patches.txt                     # Database patches
│   │
│   ├── customize_form.py              # Custom Fields & Property Setters export
│   ├── server_script.py               # Server Script export
│   ├── client_script.py               # Client Script export
│   ├── custom_html_block.py           # Custom HTML Block export
│   ├── fixtures.py                    # Bulk fixtures export
│   ├── web_page.py                    # Web Page export (NEW)
│   │
│   ├── config/                        # Configuration files
│   │   └── __init__.py
│   │
│   ├── templates/                     # Jinja templates
│   │   ├── __init__.py
│   │   └── pages/
│   │       └── __init__.py
│   │
│   ├── export_custom_fields/          # Internal modules
│   │   └── __init__.py
│   │
│   └── public/                        # Public assets
│       └── js/                        # JavaScript files
│           ├── customize_form.js      # Customize Form form script
│           ├── custom_field.js      # Custom Field form script
│           ├── custom_field_list.js   # Custom Field list script
│           ├── property_setter.js    # Property Setter form script
│           ├── property_setter_list.js # Property Setter list script
│           ├── server_script.js       # Server Script form script
│           ├── server_script_list.js  # Server Script list script
│           ├── client_script.js      # Client Script form script
│           ├── client_script_list.js # Client Script list script
│           ├── custom_html_block.js  # Custom HTML Block form script
│           ├── custom_html_block_list.js # Custom HTML Block list script
│           └── web_page.js            # Web Page form script (NEW)
│
├── README.md                          # Main documentation
├── app_file_structure.md             # This file
├── app_api_tree.md                   # API documentation
├── app_workflow.md                   # Workflow diagrams
├── app_used_custom_fields.md         # Custom fields usage
├── license.txt                       # License file
└── pyproject.toml                    # Python project configuration
```

## Key Files Description

### Python Modules

#### `hooks.py`

-   **Purpose**: Frappe app hooks configuration
-   **Key Configurations**:
    -   `doctype_js`: Maps DocTypes to their JavaScript form scripts
    -   `doctype_list_js`: Maps DocTypes to their JavaScript list scripts
-   **Supported DocTypes**: Customize Form, Server Script, Client Script, Custom Field, Property Setter, Custom HTML Block, Web Page

#### `customize_form.py`

-   **Purpose**: Export Custom Fields and Property Setters
-   **Key Functions**:
    -   `has_custom_fields_in_module()`: Check if module has custom fields
    -   `export_custom_fields_by_module()`: Export by module
    -   `bulk_export_customizations()`: Bulk export multiple records
    -   `bulk_set_module()`: Set module for multiple records
-   **Export Location**: `{app}/{module}/custom/{doctype}.json`

#### `server_script.py`

-   **Purpose**: Export Server Scripts
-   **Key Functions**:
    -   `export_server_scripts_by_module()`: Export Server Scripts by module
    -   `export_fixtures_by_module()`: Export all fixtures for app
-   **Export Location**: `{app}/fixtures/Server Script.json`

#### `client_script.py`

-   **Purpose**: Export Client Scripts
-   **Key Functions**:
    -   `export_client_scripts_by_module()`: Export Client Scripts by module
-   **Export Location**: `{app}/fixtures/Client Script.json`

#### `custom_html_block.py`

-   **Purpose**: Export Custom HTML Blocks
-   **Key Functions**:
    -   `export_custom_html_blocks_by_module()`: Export single block by module
-   **Export Location**: `{app}/fixtures/Custom HTML Block.json`

#### `fixtures.py`

-   **Purpose**: Bulk export fixtures
-   **Key Functions**:
    -   `bulk_export_fixtures()`: Bulk export Server Scripts, Client Scripts, and Custom HTML Blocks
-   **Export Location**: `{app}/fixtures/{doctype}.json`

#### `web_page.py` ⭐ NEW

-   **Purpose**: Export Web Pages with special child table handling
-   **Key Functions**:
    -   `export_web_pages_by_module()`: Export Web Pages and Web Page Blocks by module
-   **Export Location**:
    -   `{app}/fixtures/Web Page.json`
    -   `{app}/fixtures/Web Page Block.json`

### JavaScript Files

#### Form Scripts (`*.js`)

-   **Location**: `public/js/`
-   **Purpose**: Add export buttons to form views
-   **Features**:
    -   "Export to Module" button (red, appears when module is set)
    -   "Set Module" button (green, always available)
    -   Developer mode validation
    -   Module validation
    -   Success/error feedback

#### List Scripts (`*_list.js`)

-   **Location**: `public/js/`
-   **Purpose**: Add bulk export functionality to list views
-   **Features**:
    -   Bulk export button
    -   Multi-select support
    -   Module validation
    -   Progress feedback

### File Organization

#### Export Locations

**Custom Files** (Custom Fields, Property Setters):

```
{app}/{module}/custom/{doctype}.json
```

**Fixtures Files** (Scripts, Blocks, Pages):

```
{app}/fixtures/{doctype}.json
```

#### Module Structure

Each module follows Frappe's standard structure:

-   Custom files in `{module}/custom/` folder
-   Fixtures in app-level `fixtures/` folder

## File Relationships

### Form View Flow

```
Form View (DocType)
    ↓
JavaScript (public/js/{doctype}.js)
    ↓
Python API (export_custom_fields/{module}.py)
    ↓
Export Function
    ↓
File System ({app}/{location}/{file}.json)
```

### List View Flow

```
List View (DocType)
    ↓
JavaScript (public/js/{doctype}_list.js)
    ↓
Python API (export_custom_fields/{module}.py)
    ↓
Bulk Export Function
    ↓
Multiple Files ({app}/{location}/{file}.json)
```

## Dependencies

### Frappe Core

-   `frappe.core.doctype.data_import.data_import.export_json`
-   `frappe.modules.utils.export_customizations`
-   `frappe.utils.fixtures.export_fixtures`

### Standard Libraries

-   `os`: File system operations
-   `json`: JSON handling (via Frappe)

## Configuration Files

### `hooks.py`

-   Defines which JavaScript files load for which DocTypes
-   Configures app-level hooks

### `modules.txt`

-   Lists app modules

### `patches.txt`

-   Database migration patches

### `pyproject.toml`

-   Python project metadata
-   Dependencies configuration
