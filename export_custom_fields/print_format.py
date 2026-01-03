# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import frappe
from frappe import _
from frappe.modules.utils import export_module_json


@frappe.whitelist()
def export_print_formats_by_module(module):
	"""Export Print Formats for the specified module using the same method as on_update (export_doc -> export_module_json)."""

	if not frappe.conf.developer_mode:
		frappe.throw(_("Only allowed to export customizations in developer mode"))

	# Get all Print Formats in this module that are standard (same condition as export_doc)
	print_formats = frappe.get_all(
		"Print Format",
		filters={"module": module, "standard": "Yes"},
		fields=["name"],
	)

	if not print_formats:
		frappe.msgprint(_("No standard Print Formats found in module <b>{0}</b>").format(module))
		return {"app": None, "module": module, "count": 0}

	# Export each Print Format using the same method as export_doc: export_module_json(self, self.standard == "Yes", self.module)
	exported_count = 0
	for print_format in print_formats:
		try:
			doc = frappe.get_doc("Print Format", print_format.name)
			# Use same method as export_doc: export_module_json(self, self.standard == "Yes", self.module)
			path = export_module_json(doc, doc.standard == "Yes", doc.module)
			if path:
				exported_count += 1
		except Exception as e:
			frappe.log_error(f"Error exporting Print Format {print_format.name}: {str(e)}")

	frappe.msgprint(_("Exported <b>{0}</b> Print Format(s) for module <b>{1}</b>").format(exported_count, module))
	return {"module": module, "count": exported_count}

