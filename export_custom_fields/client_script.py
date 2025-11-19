# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import os
import frappe
from frappe import _, get_app_path, scrub
from frappe.core.doctype.data_import.data_import import export_json


@frappe.whitelist()
def export_client_scripts_by_module(module):
    """Export Client Scripts for the specified module to fixtures folder, similar to export_fixtures."""
    
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
    
    # Export Client Scripts to fixtures folder
    try:
        export_json(
            "Client Script",
            os.path.join(fixtures_path, scrub("Client Script") + ".json"),
            filters={"module": module},
            order_by="idx asc, creation asc",
        )
        frappe.msgprint(_("Client Scripts for module <b>{0}</b> exported to fixtures successfully").format(module))
        return {"app": app_name, "module": module}
    except Exception as e:
        frappe.log_error(f"Error exporting Client Scripts for module {module}: {str(e)}")
        frappe.throw(_("Error exporting Client Scripts: {0}").format(str(e)))

