# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import os
import frappe
from frappe import _, get_app_path, scrub
from frappe.core.doctype.data_import.data_import import export_json


@frappe.whitelist()
def export_custom_html_blocks_by_module(name, module, sync_on_migrate=False):
	"""Export the current Custom HTML Block to fixtures folder of the app that contains the selected module."""
	
	if not frappe.conf.developer_mode:
		frappe.throw(_("Only allowed to export customizations in developer mode"))
	
	if not name:
		frappe.throw(_("Custom HTML Block name is required"))
	
	sync_on_migrate = frappe.utils.cint(sync_on_migrate)
	
	# Get app_name from module
	module_doc = frappe.get_doc("Module Def", module)
	app_name = module_doc.app_name
	
	if not app_name:
		frappe.throw(_("Could not determine app name for module: {0}").format(module))
	
	# Create fixtures folder if it doesn't exist
	fixtures_path = get_app_path(app_name, "fixtures")
	if not os.path.exists(fixtures_path):
		os.makedirs(fixtures_path)
	
	# Export the current Custom HTML Block to fixtures folder
	try:
		export_json(
			"Custom HTML Block",
			os.path.join(fixtures_path, scrub("Custom HTML Block") + ".json"),
			name=name,
			order_by="idx asc, creation asc",
		)
		frappe.msgprint(_("Custom HTML Block <b>{0}</b> exported to fixtures folder of app <b>{1}</b> (module: {2})").format(name, app_name, module))
		return {"app": app_name, "module": module, "name": name}
	except Exception as e:
		frappe.log_error(f"Error exporting Custom HTML Block {name} for module {module}: {str(e)}")
		frappe.throw(_("Error exporting Custom HTML Block: {0}").format(str(e)))

