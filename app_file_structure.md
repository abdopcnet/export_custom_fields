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
│   ├── web_page.py                    # Web Page export
│   ├── page.py                        # Page export (NEW)
│   ├── report.py                      # Report export (NEW)
│   ├── dashboard.py                   # Dashboard export (NEW)
│   ├── dashboard_chart.py             # Dashboard Chart export (NEW)
│   ├── form_tour.py                   # Form Tour export (NEW)
│   ├── number_card.py                 # Number Card export (NEW)
│   ├── workspace.py                   # Workspace export (NEW)
│   ├── notification.py                # Notification export (NEW)
│   ├── print_format.py                # Print Format export (NEW)
│   ├── web_form.py                    # Web Form export (NEW)
│   ├── web_template.py                # Web Template export (NEW)
│   ├── website_theme.py               # Website Theme export (NEW)
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
│           ├── web_page.js            # Web Page form script
│           ├── page.js                # Page form script (NEW)
│           ├── report.js              # Report form script (NEW)
│           ├── dashboard.js           # Dashboard form script (NEW)
│           ├── dashboard_chart.js     # Dashboard Chart form script (NEW)
│           ├── form_tour.js           # Form Tour form script (NEW)
│           ├── number_card.js         # Number Card form script (NEW)
│           ├── workspace.js           # Workspace form script (NEW)
│           ├── notification.js        # Notification form script (NEW)
│           ├── print_format.js        # Print Format form script (NEW)
│           ├── web_form.js            # Web Form form script (NEW)
│           ├── web_template.js        # Web Template form script (NEW)
│           └── website_theme.js       # Website Theme form script (NEW)
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
-   **Supported DocTypes**: Customize Form, Server Script, Client Script, Custom Field, Property Setter, Custom HTML Block, Web Page, Page, Report, Dashboard, Dashboard Chart, Form Tour, Number Card, Workspace, Notification, Print Format, Web Form, Web Template, Website Theme

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

#### `web_page.py`

-   **Purpose**: Export Web Pages with special child table handling
-   **Key Functions**:
    -   `export_web_pages_by_module()`: Export Web Pages and Web Page Blocks by module
-   **Export Location**:
    -   `{app}/fixtures/Web Page.json`
    -   `{app}/fixtures/Web Page Block.json`

#### `page.py` ⭐ NEW

-   **Purpose**: Export Pages
-   **Key Functions**:
    -   `export_pages_by_module()`: Export Pages by module
-   **Export Location**: `{app}/fixtures/Page.json`

#### `report.py` ⭐ NEW

-   **Purpose**: Export Reports
-   **Key Functions**:
    -   `export_reports_by_module()`: Export Reports by module
-   **Export Location**: `{app}/fixtures/Report.json`

#### `dashboard.py` ⭐ NEW

-   **Purpose**: Export Dashboards
-   **Key Functions**:
    -   `export_dashboards_by_module()`: Export Dashboards by module
-   **Export Location**: `{app}/fixtures/Dashboard.json`

#### `dashboard_chart.py` ⭐ NEW

-   **Purpose**: Export Dashboard Charts
-   **Key Functions**:
    -   `export_dashboard_charts_by_module()`: Export Dashboard Charts by module
-   **Export Location**: `{app}/fixtures/Dashboard Chart.json`

#### `form_tour.py` ⭐ NEW

-   **Purpose**: Export Form Tours
-   **Key Functions**:
    -   `export_form_tours_by_module()`: Export Form Tours by module
-   **Export Location**: `{app}/fixtures/Form Tour.json`

#### `number_card.py` ⭐ NEW

-   **Purpose**: Export Number Cards
-   **Key Functions**:
    -   `export_number_cards_by_module()`: Export Number Cards by module
-   **Export Location**: `{app}/fixtures/Number Card.json`

#### `workspace.py` ⭐ NEW

-   **Purpose**: Export Workspaces
-   **Key Functions**:
    -   `export_workspaces_by_module()`: Export Workspaces by module
-   **Export Location**: `{app}/fixtures/Workspace.json`

#### `notification.py` ⭐ NEW

-   **Purpose**: Export Notifications
-   **Key Functions**:
    -   `export_notifications_by_module()`: Export Notifications by module
-   **Export Location**: `{app}/fixtures/Notification.json`

#### `print_format.py` ⭐ NEW

-   **Purpose**: Export Print Formats
-   **Key Functions**:
    -   `export_print_formats_by_module()`: Export Print Formats by module
-   **Export Location**: `{app}/fixtures/Print Format.json`

#### `web_form.py` ⭐ NEW

-   **Purpose**: Export Web Forms
-   **Key Functions**:
    -   `export_web_forms_by_module()`: Export Web Forms by module
-   **Export Location**: `{app}/fixtures/Web Form.json`

#### `web_template.py` ⭐ NEW

-   **Purpose**: Export Web Templates
-   **Key Functions**:
    -   `export_web_templates_by_module()`: Export Web Templates by module
-   **Export Location**: `{app}/fixtures/Web Template.json`

#### `website_theme.py` ⭐ NEW

-   **Purpose**: Export Website Themes
-   **Key Functions**:
    -   `export_website_themes_by_module()`: Export Website Themes by module
-   **Export Location**: `{app}/fixtures/Website Theme.json`

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
