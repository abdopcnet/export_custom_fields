# File Structure

```
export_custom_fields/
├── hooks.py
├── customize_form.py
├── server_script.py
├── client_script.py
├── custom_html_block.py
├── fixtures.py
├── export_custom_fields/
│   ├── custom/
│   │   ├── custom_field.json
│   │   ├── property_setter.json
│   │   ├── server_script.json
│   │   └── client_script.json
│   └── config/
└── public/
    └── js/
        ├── customize_form.js
        ├── custom_field.js
        ├── custom_field_list.js
        ├── property_setter.js
        ├── server_script.js
        ├── client_script.js
        └── custom_html_block.js
```

## Key Files

- `hooks.py` - App hooks (doctype_js, doctype_list_js)
- `customize_form.py` - Custom Fields & Property Setters export
- `server_script.py` - Server Script export
- `client_script.py` - Client Script export
- `custom_html_block.py` - Custom HTML Block export
- `fixtures.py` - Bulk fixtures export
