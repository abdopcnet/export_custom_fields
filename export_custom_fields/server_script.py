# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import os
import frappe
from frappe import _, get_app_path, scrub
from frappe.core.doctype.data_import.data_import import export_json
from frappe.utils.fixtures import export_fixtures


@frappe.whitelist()
def export_server_scripts_by_module(module):
    """Export Server Scripts for the specified module to fixtures folder, similar to export_fixtures."""
    
    if not frappe.conf.developer_mode:
        frappe.throw(_("Only allowed to export customizations in developer mode"))
    
    # Get app_name from module
    module_doc = frappe.get_doc("Module Def", module)
    app_name = module_doc.app_name
    
    if not app_name:
        frappe.throw(_("Could not determine app name for module: {0}").format(module))
    
    # Create fixtures folder if it doesn't exist
    fixtures_path = get_app_path(app_name, "fixtures")
    if not os.path.exists(fixtures_path):
        os.makedirs(fixtures_path)
    
    # Export Server Scripts to fixtures folder
    try:
        export_json(
            "Server Script",
            os.path.join(fixtures_path, scrub("Server Script") + ".json"),
            filters={"module": module},
            order_by="idx asc, creation asc",
        )
        frappe.msgprint(_("Server Scripts for module <b>{0}</b> exported to fixtures successfully").format(module))
        return {"app": app_name, "module": module}
    except Exception as e:
        frappe.log_error(f"Error exporting Server Scripts for module {module}: {str(e)}")
        frappe.throw(_("Error exporting Server Scripts: {0}").format(str(e)))


@frappe.whitelist()
def export_fixtures_by_module(module):
    """Export fixtures for the app that contains the specified module."""
    
    if not frappe.conf.developer_mode:
        frappe.throw(_("Only allowed to export fixtures in developer mode"))
    
    # Get app_name from module
    module_doc = frappe.get_doc("Module Def", module)
    app_name = module_doc.app_name
    
    if not app_name:
        frappe.throw(_("Could not determine app name for module: {0}").format(module))
    
    # Export fixtures for the app
    try:
        export_fixtures(app=app_name)
        frappe.msgprint(_("Fixtures for app <b>{0}</b> exported successfully").format(app_name))
        return {"app": app_name, "module": module}
    except Exception as e:
        frappe.log_error(f"Error exporting fixtures for app {app_name}: {str(e)}")
        frappe.throw(_("Error exporting fixtures: {0}").format(str(e)))

