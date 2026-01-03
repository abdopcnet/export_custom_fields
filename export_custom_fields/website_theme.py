# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import frappe
from frappe import _
from frappe.modules.export_file import export_to_files


@frappe.whitelist()
def export_website_themes_by_module(module):
	"""Export Website Themes for the specified module using the same method as on_update (export_doc -> export_to_files)."""

	if not frappe.conf.developer_mode:
		frappe.throw(_("Only allowed to export customizations in developer mode"))

	# Get all Website Themes in this module that are not custom (same condition as on_update)
	website_themes = frappe.get_all(
		"Website Theme",
		filters={"module": module, "custom": 0},
		fields=["name"],
	)

	if not website_themes:
		frappe.msgprint(_("No standard Website Themes found in module <b>{0}</b>").format(module))
		return {"app": None, "module": module, "count": 0}

	# Build record_list using the same format as export_doc: export_to_files(record_list=[["Website Theme", self.name]], create_init=True)
	record_list = [["Website Theme", theme.name] for theme in website_themes]

	# Export using the same method as export_doc: export_to_files(record_list=[["Website Theme", self.name]], create_init=True)
	try:
		export_to_files(record_list=record_list, create_init=True)
		frappe.msgprint(_("Exported <b>{0}</b> Website Theme(s) for module <b>{1}</b>").format(len(website_themes), module))
		return {"module": module, "count": len(website_themes)}
	except Exception as e:
		frappe.log_error(f"Error exporting Website Themes for module {module}: {str(e)}")
		frappe.throw(_("Error exporting Website Themes: {0}").format(str(e)))

