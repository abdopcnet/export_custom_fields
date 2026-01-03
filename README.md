# Export Custom Fields

![Version](https://img.shields.io/badge/version-2.1.2026-blue)

A comprehensive Frappe app for exporting customizations to JSON files for version control and deployment management.

## Features Preview

### 🎯 Module-Based Export System

Export customizations organized by module, making it easy to manage and deploy changes across different modules.

#### Supported DocTypes

1. **Custom Fields & Property Setters**

    - Export to: `{app}/{module}/custom/{doctype}.json`
    - Includes custom fields, property setters, and DocType links
    - Supports `sync_on_migrate` flag for automatic migration

2. **Server Scripts**

    - Export to: `{app}/fixtures/Server Script.json`
    - Filters by module
    - Ordered by index and creation date

3. **Client Scripts**

    - Export to: `{app}/fixtures/Client Script.json`
    - Filters by module
    - Ordered by index and creation date

4. **Custom HTML Blocks**

    - Export to: `{app}/fixtures/Custom HTML Block.json`
    - Single block export with module selection
    - Supports `sync_on_migrate` flag

5. **Web Pages**

    - Export to: `{app}/fixtures/Web Page.json`
    - Special handling for Web Page Block child table
    - Exports parent Web Pages and related child records separately

6. **Pages** ⭐ NEW

    - Export to: `{app}/fixtures/Page.json`
    - Filters by module
    - Ordered by index and creation date

7. **Reports** ⭐ NEW

    - Export to: `{app}/fixtures/Report.json`
    - Filters by module
    - Ordered by index and creation date

8. **Dashboards** ⭐ NEW

    - Export to: `{app}/fixtures/Dashboard.json`
    - Filters by module
    - Ordered by index and creation date

9. **Dashboard Charts** ⭐ NEW

    - Export to: `{app}/fixtures/Dashboard Chart.json`
    - Filters by module
    - Ordered by index and creation date

10. **Form Tours** ⭐ NEW

    - Export to: `{app}/fixtures/Form Tour.json`
    - Filters by module
    - Ordered by index and creation date

11. **Number Cards** ⭐ NEW

    - Export to: `{app}/fixtures/Number Card.json`
    - Filters by module
    - Ordered by index and creation date

12. **Workspaces** ⭐ NEW

    - Export to: `{app}/fixtures/Workspace.json`
    - Filters by module
    - Ordered by index and creation date

13. **Notifications** ⭐ NEW

    - Export to: `{app}/fixtures/Notification.json`
    - Filters by module
    - Ordered by index and creation date

14. **Print Formats** ⭐ NEW

    - Export to: `{app}/fixtures/Print Format.json`
    - Filters by module
    - Ordered by index and creation date

15. **Web Forms** ⭐ NEW

    - Export to: `{app}/fixtures/Web Form.json`
    - Filters by module
    - Ordered by index and creation date

16. **Web Templates** ⭐ NEW

    - Export to: `{app}/fixtures/Web Template.json`
    - Filters by module
    - Ordered by index and creation date

17. **Website Themes** ⭐ NEW
    - Export to: `{app}/fixtures/Website Theme.json`
    - Filters by module
    - Ordered by index and creation date

### 📦 Bulk Export Operations

#### Bulk Custom Fields & Property Setters Export

-   Export multiple custom fields and property setters at once
-   Groups by (module, doctype) combinations
-   Handles records without modules gracefully
-   Auto-cleans invalid doctype references

#### Bulk Fixtures Export

-   Export multiple Server Scripts, Client Scripts, and Custom HTML Blocks
-   Groups by module automatically
-   Validates module assignment before export

### 🔧 Module Management

#### Set Module Functionality

-   Bulk set module for multiple records
-   Supports: Custom Field, Property Setter, Server Script, Client Script, Custom HTML Block, Web Page, Page, Report, Dashboard, Dashboard Chart, Form Tour, Number Card, Workspace, Notification, Print Format, Web Form, Web Template, Website Theme
-   Validates module existence before assignment
-   Updates records in batch with transaction support

### 🎨 User Interface Features

#### Form View Buttons

-   **Export to Module** button (red) - Appears when module is set
-   **Set Module** button (green) - Always available for existing records
-   Buttons only visible in Developer Mode
-   One-click export from any supported DocType form

#### List View Actions

-   Bulk export buttons in list views
-   Select multiple records and export together
-   Module validation before export
-   Progress feedback and error handling

### 📁 Export Locations

#### Custom Files

```
{app}/{module}/custom/{doctype}.json
```

-   Custom Fields
-   Property Setters
-   DocType Links

#### Fixtures Files

```
{app}/fixtures/{doctype}.json
```

-   Server Script
-   Client Script
-   Custom HTML Block
-   Web Page
-   Web Page Block (child table)
-   Page
-   Report
-   Dashboard
-   Dashboard Chart
-   Form Tour
-   Number Card
-   Workspace
-   Notification
-   Print Format
-   Web Form
-   Web Template
-   Website Theme

### 🔒 Security & Validation

-   **Developer Mode Required**: All export operations require developer mode
-   **Module Validation**: Ensures module exists before export
-   **Error Handling**: Comprehensive error logging and user feedback
-   **Transaction Safety**: Database operations wrapped in transactions

### 📊 Export Features

#### Custom Fields Export

-   Groups by DocType automatically
-   Includes custom fields, property setters, and links
-   Supports `sync_on_migrate` flag
-   Excludes system-generated fields

#### Scripts Export

-   Filters by module
-   Maintains order (idx, creation)
-   Exports complete script definitions
-   Includes all script metadata

#### Web Page Export

-   Exports Web Page documents
-   Separately exports Web Page Block child records
-   Maintains parent-child relationships
-   Preserves all page content and settings

### 🚀 Workflow Integration

-   Seamless integration with Frappe's customization system
-   Compatible with standard export/import workflows
-   Supports version control systems (Git, etc.)
-   Ready for deployment pipelines

### 📝 Logging & Debugging

-   Comprehensive error logging
-   Method-level logging for debugging
-   Error messages with context
-   Logs stored in Error Log DocType

## Installation

```bash
bench get-app export_custom_fields
bench --site [site_name] install-app export_custom_fields
```

## Usage

### Single Record Export

1. Open any supported DocType (Custom Field, Server Script, etc.)
2. Set the `module` field if not already set
3. Click **"Export to Module"** button
4. Files are exported to the appropriate location

### Bulk Export

1. Go to list view of supported DocType
2. Select multiple records
3. Click bulk export button
4. Records are grouped and exported by module

### Set Module

1. Open any supported DocType
2. Click **"Set Module"** button
3. Select module from dropdown
4. Module is assigned to the record

## Requirements

-   Frappe Framework
-   Developer Mode enabled
-   Module Def records configured

## License

MIT

## Author

abdopcnet
