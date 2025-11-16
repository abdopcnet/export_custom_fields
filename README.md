# Export Custom Fields

![Version](https://img.shields.io/badge/version-16.11.2025-blue)


A Frappe application that provides functionality to export custom fields and property setters from the database to JSON files for version control and deployment purposes.

## What it does

This application allows developers to export custom fields and property setters that have been created through the Frappe Customize Form interface. It exports these customizations to JSON files in the module's `custom` directory, following the same structure and format as Frappe's built-in customization export system.

## Features

- **Module-based Export**: Export custom fields and property setters for specific modules
- **Developer Mode Only**: Only works when developer mode is enabled for security
- **JSON Format**: Exports data in the same JSON format used by Frappe's customization system
- **Sync on Migrate**: Option to enable automatic synchronization during migrations
- **UI Integration**: Adds an "Export Custom Fields" button to the Customize Form interface

## How to use

1. **Enable Developer Mode**: Make sure developer mode is enabled in your Frappe installation
2. **Navigate to Customize Form**: Go to any form and click on "Customize" 
3. **Export Custom Fields**: Click the "Export Custom Fields" button that appears
4. **Select Module**: Choose the module you want to export customizations from
5. **Configure Options**: 
   - Select the target module
   - Choose whether to sync on migrate (recommended: enabled)
6. **Export**: The custom fields and property setters will be exported to JSON files in the module's `custom` directory

## Output

The application creates JSON files in the following structure:
```
{module_name}/custom/{doctype_name}.json
```

Each JSON file contains:
- Custom fields for the doctype
- Property setters for the doctype  
- Custom permissions (if any)
- Sync on migrate configuration

## Use Cases

- **Version Control**: Track custom field changes in Git
- **Deployment**: Deploy customizations across different environments
- **Backup**: Backup custom field configurations
- **Development Workflow**: Share customizations between team members

## Requirements

- Frappe Framework (v15+)
- Developer mode enabled
- Appropriate permissions to access Customize Form

## License

MIT License