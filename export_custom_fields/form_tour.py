# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import frappe
from frappe import _
from frappe.modules.export_file import export_to_files


@frappe.whitelist()
def export_form_tours_by_module(module):
	"""Export Form Tours for the specified module using the same method as on_update (export_to_files)."""

	if not frappe.conf.developer_mode:
		frappe.throw(_("Only allowed to export customizations in developer mode"))

	# Get all Form Tours in this module that are standard (same condition as on_update)
	form_tours = frappe.get_all(
		"Form Tour",
		filters={"module": module, "is_standard": 1},
		fields=["name"],
	)

	if not form_tours:
		frappe.msgprint(_("No standard Form Tours found in module <b>{0}</b>").format(module))
		return {"app": None, "module": module, "count": 0}

	# Build record_list using the same format as on_update: export_to_files([["Form Tour", self.name]], self.module)
	record_list = [["Form Tour", tour.name] for tour in form_tours]

	# Export using the same method as on_update: export_to_files([["Form Tour", self.name]], self.module)
	try:
		export_to_files(record_list=record_list, record_module=module)
		frappe.msgprint(_("Exported <b>{0}</b> Form Tour(s) for module <b>{1}</b>").format(len(form_tours), module))
		return {"module": module, "count": len(form_tours)}
	except Exception as e:
		frappe.log_error(f"Error exporting Form Tours for module {module}: {str(e)}")
		frappe.throw(_("Error exporting Form Tours: {0}").format(str(e)))

