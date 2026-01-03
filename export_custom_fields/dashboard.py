# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import frappe
from frappe import _
from frappe.modules.export_file import export_to_files


@frappe.whitelist()
def export_dashboards_by_module(module):
	"""Export Dashboards for the specified module using the same method as on_update (export_to_files)."""

	if not frappe.conf.developer_mode:
		frappe.throw(_("Only allowed to export customizations in developer mode"))

	# Get all Dashboards in this module that are standard (same condition as on_update)
	dashboards = frappe.get_all(
		"Dashboard",
		filters={"module": module, "is_standard": 1},
		fields=["name"],
	)

	if not dashboards:
		frappe.msgprint(_("No standard Dashboards found in module <b>{0}</b>").format(module))
		return {"app": None, "module": module, "count": 0}

	# Build record_list using the same format as on_update
	record_list = [["Dashboard", dashboard.name, f"{module} Dashboard"] for dashboard in dashboards]

	# Export using the same method as on_update: export_to_files(record_list=[["Dashboard", self.name, f"{self.module} Dashboard"]], record_module=self.module)
	try:
		export_to_files(record_list=record_list, record_module=module)
		frappe.msgprint(_("Exported <b>{0}</b> Dashboard(s) for module <b>{1}</b>").format(len(dashboards), module))
		return {"module": module, "count": len(dashboards)}
	except Exception as e:
		frappe.log_error(f"Error exporting Dashboards for module {module}: {str(e)}")
		frappe.throw(_("Error exporting Dashboards: {0}").format(str(e)))

