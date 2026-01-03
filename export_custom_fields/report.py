# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import frappe
from frappe import _
from frappe.modules.export_file import export_to_files


@frappe.whitelist()
def export_reports_by_module(module):
	"""Export Reports for the specified module using the same method as on_update (export_doc -> export_to_files)."""

	if not frappe.conf.developer_mode:
		frappe.throw(_("Only allowed to export customizations in developer mode"))

	# Get all Reports in this module that are standard (same condition as export_doc)
	reports = frappe.get_all(
		"Report",
		filters={"module": module, "is_standard": "Yes"},
		fields=["name"],
	)

	if not reports:
		frappe.msgprint(_("No standard Reports found in module <b>{0}</b>").format(module))
		return {"app": None, "module": module, "count": 0}

	# Build record_list using the same format as export_doc: export_to_files(record_list=[["Report", self.name]], record_module=self.module, create_init=True)
	record_list = [["Report", report.name] for report in reports]

	# Export using the same method as export_doc: export_to_files(record_list=[["Report", self.name]], record_module=self.module, create_init=True)
	try:
		export_to_files(record_list=record_list, record_module=module, create_init=True)
		# Also create report.py files (same as export_doc does)
		for report in reports:
			try:
				doc = frappe.get_doc("Report", report.name)
				doc.create_report_py()
			except Exception as e:
				frappe.log_error(f"Error creating report.py for {report.name}: {str(e)}")
		frappe.msgprint(_("Exported <b>{0}</b> Report(s) for module <b>{1}</b>").format(len(reports), module))
		return {"module": module, "count": len(reports)}
	except Exception as e:
		frappe.log_error(f"Error exporting Reports for module {module}: {str(e)}")
		frappe.throw(_("Error exporting Reports: {0}").format(str(e)))

