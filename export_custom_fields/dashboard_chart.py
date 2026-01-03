# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import frappe
from frappe import _
from frappe.modules.export_file import export_to_files


@frappe.whitelist()
def export_dashboard_charts_by_module(module):
	"""Export Dashboard Charts for the specified module using the same method as on_update (export_to_files)."""

	if not frappe.conf.developer_mode:
		frappe.throw(_("Only allowed to export customizations in developer mode"))

	# Get all Dashboard Charts in this module that are standard (same condition as on_update)
	dashboard_charts = frappe.get_all(
		"Dashboard Chart",
		filters={"module": module, "is_standard": 1},
		fields=["name"],
	)

	if not dashboard_charts:
		frappe.msgprint(_("No standard Dashboard Charts found in module <b>{0}</b>").format(module))
		return {"app": None, "module": module, "count": 0}

	# Build record_list using the same format as on_update
	record_list = [["Dashboard Chart", chart.name] for chart in dashboard_charts]

	# Export using the same method as on_update: export_to_files(record_list=[["Dashboard Chart", self.name]], record_module=self.module)
	try:
		export_to_files(record_list=record_list, record_module=module)
		frappe.msgprint(_("Exported <b>{0}</b> Dashboard Chart(s) for module <b>{1}</b>").format(len(dashboard_charts), module))
		return {"module": module, "count": len(dashboard_charts)}
	except Exception as e:
		frappe.log_error(f"Error exporting Dashboard Charts for module {module}: {str(e)}")
		frappe.throw(_("Error exporting Dashboard Charts: {0}").format(str(e)))

