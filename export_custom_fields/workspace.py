# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import frappe
from frappe import _
from frappe.modules.export_file import export_to_files


@frappe.whitelist()
def export_workspaces_by_module(module):
	"""Export Workspaces for the specified module using the same method as on_update (export_to_files)."""

	if not frappe.conf.developer_mode:
		frappe.throw(_("Only allowed to export customizations in developer mode"))

	# Get all Workspaces in this module that are public (same condition as on_update)
	workspaces = frappe.get_all(
		"Workspace",
		filters={"module": module, "public": 1},
		fields=["name"],
	)

	if not workspaces:
		frappe.msgprint(_("No public Workspaces found in module <b>{0}</b>").format(module))
		return {"app": None, "module": module, "count": 0}

	# Build record_list using the same format as on_update
	record_list = [["Workspace", workspace.name] for workspace in workspaces]

	# Export using the same method as on_update: export_to_files(record_list=[["Workspace", self.name]], record_module=self.module)
	try:
		export_to_files(record_list=record_list, record_module=module)
		frappe.msgprint(_("Exported <b>{0}</b> Workspace(s) for module <b>{1}</b>").format(len(workspaces), module))
		return {"module": module, "count": len(workspaces)}
	except Exception as e:
		frappe.log_error(f"Error exporting Workspaces for module {module}: {str(e)}")
		frappe.throw(_("Error exporting Workspaces: {0}").format(str(e)))

