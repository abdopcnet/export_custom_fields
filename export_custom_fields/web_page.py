# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import os
import frappe
from frappe import _, get_app_path, scrub
from frappe.core.doctype.data_import.data_import import export_json


@frappe.whitelist()
def export_web_pages_by_module(module):
	"""Export Web Pages for the specified module to fixtures folder, with special handling for Web Page Block child table."""

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

	# Export Web Pages to fixtures folder
	try:
		# Export Web Pages with their child tables (Web Page Block)
		export_json(
			"Web Page",
			os.path.join(fixtures_path, scrub("Web Page") + ".json"),
			filters={"module": module},
			order_by="idx asc, creation asc",
		)

		# Export Web Page Block child table records separately for better organization
		# Get all Web Pages in this module
		web_pages = frappe.get_all("Web Page", filters={"module": module}, fields=["name"])
		web_page_names = [wp.name for wp in web_pages]

		if web_page_names:
			# Export Web Page Block records for these Web Pages
			export_json(
				"Web Page Block",
				os.path.join(fixtures_path, scrub("Web Page Block") + ".json"),
				filters={"parent": ("in", web_page_names), "parenttype": "Web Page"},
				order_by="idx asc, creation asc",
			)

		frappe.msgprint(_("Web Pages for module <b>{0}</b> exported to fixtures successfully").format(module))
		return {"app": app_name, "module": module}
	except Exception as e:
		frappe.log_error(f"[web_page.py] method: export_web_pages_by_module", "Web Page Export")
		frappe.throw(_("Error exporting Web Pages: {0}").format(str(e)))

