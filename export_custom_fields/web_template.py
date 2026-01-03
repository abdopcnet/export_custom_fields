# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import frappe
from frappe import _


@frappe.whitelist()
def export_web_templates_by_module(module):
	"""Export Web Templates for the specified module using the same method as before_save (export_to_files)."""

	if not frappe.conf.developer_mode:
		frappe.throw(_("Only allowed to export customizations in developer mode"))

	# Get all Web Templates in this module that are standard (same condition as before_save)
	web_templates = frappe.get_all(
		"Web Template",
		filters={"module": module, "standard": 1},
		fields=["name"],
	)

	if not web_templates:
		frappe.msgprint(_("No standard Web Templates found in module <b>{0}</b>").format(module))
		return {"app": None, "module": module, "count": 0}

	# Export each Web Template using the same method as before_save: self.export_to_files()
	exported_count = 0
	for web_template in web_templates:
		try:
			doc = frappe.get_doc("Web Template", web_template.name)
			# Use same method as before_save: self.export_to_files()
			doc.export_to_files()
			exported_count += 1
		except Exception as e:
			frappe.log_error(f"Error exporting Web Template {web_template.name}: {str(e)}")

	frappe.msgprint(_("Exported <b>{0}</b> Web Template(s) for module <b>{1}</b>").format(exported_count, module))
	return {"module": module, "count": exported_count}

