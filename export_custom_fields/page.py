# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import os
import frappe
from frappe import _
from frappe.modules.utils import export_module_json


@frappe.whitelist()
def export_pages_by_module(module):
	"""Export Pages for the specified module using the same method as on_update (export_module_json)."""

	if not frappe.conf.developer_mode:
		frappe.throw(_("Only allowed to export customizations in developer mode"))

	# Get all Pages in this module that are standard (same condition as on_update)
	pages = frappe.get_all(
		"Page",
		filters={"module": module, "standard": "Yes"},
		fields=["name"],
	)

	if not pages:
		frappe.msgprint(_("No standard Pages found in module <b>{0}</b>").format(module))
		return {"app": None, "module": module, "count": 0}

	# Export each Page using the same method as on_update
	exported_count = 0
	for page in pages:
		try:
			doc = frappe.get_doc("Page", page.name)
			# Use same method as on_update: export_module_json(self, self.standard == "Yes", self.module)
			path = export_module_json(doc, doc.standard == "Yes", doc.module)
			if path:
				# Also create .js file (same as on_update does)
				if not os.path.exists(path + ".js"):
					with open(path + ".js", "w") as f:
						f.write(
							f"""frappe.pages['{doc.name}'].on_page_load = function(wrapper) {{
	var page = frappe.ui.make_app_page({{
		parent: wrapper,
		title: '{doc.title}',
		single_column: true
	}});
}}"""
						)
				exported_count += 1
		except Exception as e:
			frappe.log_error(f"Error exporting Page {page.name}: {str(e)}")

	frappe.msgprint(_("Exported <b>{0}</b> Page(s) for module <b>{1}</b>").format(exported_count, module))
	return {"module": module, "count": exported_count}

