# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import os
import frappe
from frappe import _
from frappe.modules.utils import export_module_json


@frappe.whitelist()
def export_web_forms_by_module(module):
	"""Export Web Forms for the specified module using the same method as on_update (export_module_json)."""

	if not frappe.conf.developer_mode:
		frappe.throw(_("Only allowed to export customizations in developer mode"))

	# Get all Web Forms in this module that are standard (same condition as on_update)
	web_forms = frappe.get_all(
		"Web Form",
		filters={"module": module, "is_standard": 1},
		fields=["name"],
	)

	if not web_forms:
		frappe.msgprint(_("No standard Web Forms found in module <b>{0}</b>").format(module))
		return {"app": None, "module": module, "count": 0}

	# Export each Web Form using the same method as on_update
	exported_count = 0
	for web_form in web_forms:
		try:
			doc = frappe.get_doc("Web Form", web_form.name)
			# Use same method as on_update: export_module_json(self, self.is_standard, self.module)
			path = export_module_json(doc, doc.is_standard, doc.module)
			if path:
				# Also create .js file (same as on_update does)
				if not os.path.exists(path + ".js"):
					with open(path + ".js", "w") as f:
						f.write(
							"""frappe.ready(function() {
	// bind events here
})"""
						)

				# Also create .py file (same as on_update does)
				if not os.path.exists(path + ".py"):
					with open(path + ".py", "w") as f:
						f.write(
							"""import frappe

def get_context(context):
	# do your magic here
	pass
"""
						)
				exported_count += 1
		except Exception as e:
			frappe.log_error(f"Error exporting Web Form {web_form.name}: {str(e)}")

	frappe.msgprint(_("Exported <b>{0}</b> Web Form(s) for module <b>{1}</b>").format(exported_count, module))
	return {"module": module, "count": exported_count}

