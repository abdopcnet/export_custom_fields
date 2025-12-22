# Export Custom Fields - File Structure

```
export_custom_fields/
├── export_custom_fields/
│   ├── __init__.py
│   ├── hooks.py                    # App configuration, doctype_js hooks
│   ├── customize_form.py           # Export Custom Fields/Property Setters by module
│   ├── server_script.py            # Export Server Scripts and fixtures by module
│   ├── client_script.py            # Export Client Scripts by module
│   ├── custom_html_block.py        # Export Custom HTML Blocks by module
│   ├── public/
│   │   └── js/
│   │       ├── customize_form.js  # Customize Form UI extension
│   │       ├── custom_field.js     # Custom Field UI extension
│   │       ├── property_setter.js  # Property Setter UI extension
│   │       ├── server_script.js    # Server Script UI extension
│   │       ├── client_script.js    # Client Script UI extension
│   │       └── custom_html_block.js # Custom HTML Block UI extension
│   ├── config/
│   ├── templates/
│   ├── modules.txt
│   └── patches.txt
├── README.md
├── app_api_tree.md
├── app_file_structure.md
├── app_workflow.md
├── app_plan.md
└── AGENTS.md
```

## Key Files

### Server-Side (Python)

-   `customize_form.py` - Main export logic for Custom Fields and Property Setters
-   `server_script.py` - Export Server Scripts and fixtures
-   `client_script.py` - Export Client Scripts
-   `custom_html_block.py` - Export Custom HTML Blocks

### Client-Side (JavaScript)

-   `public/js/*.js` - UI extensions that add export buttons to forms

### Configuration

-   `hooks.py` - Registers JavaScript files for doctypes via `doctype_js`

## Export Locations

### Custom Fields & Property Setters

```
{app_name}/{module_name}/custom/{doctype_name}.json
```

### Scripts & Blocks

```
{app_name}/fixtures/{doctype_name}.json
```
