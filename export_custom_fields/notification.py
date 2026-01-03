# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import os
import frappe
from frappe import _
from frappe.modules.utils import export_module_json

FORMATS = {"HTML": ".html", "Markdown": ".md", "Plain Text": ".txt"}


@frappe.whitelist()
def export_notifications_by_module(module):
	"""Export Notifications for the specified module using the same method as on_update (export_module_json)."""

	if not frappe.conf.developer_mode:
		frappe.throw(_("Only allowed to export customizations in developer mode"))

	# Get all Notifications in this module that are standard (same condition as on_update)
	notifications = frappe.get_all(
		"Notification",
		filters={"module": module, "is_standard": 1},
		fields=["name"],
	)

	if not notifications:
		frappe.msgprint(_("No standard Notifications found in module <b>{0}</b>").format(module))
		return {"app": None, "module": module, "count": 0}

	# Export each Notification using the same method as on_update: export_module_json(self, self.is_standard, self.module)
	exported_count = 0
	for notification in notifications:
		try:
			doc = frappe.get_doc("Notification", notification.name)
			# Use same method as on_update: export_module_json(self, self.is_standard, self.module)
			path = export_module_json(doc, doc.is_standard, doc.module)
			if path and doc.message:
				# Also create message file (same as on_update does)
				extension = FORMATS.get(doc.message_type, ".md")
				file_path = path + extension
				with open(file_path, "w") as f:
					f.write(doc.message)

				# py file (same as on_update does)
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
			frappe.log_error(f"Error exporting Notification {notification.name}: {str(e)}")

	frappe.msgprint(_("Exported <b>{0}</b> Notification(s) for module <b>{1}</b>").format(exported_count, module))
	return {"module": module, "count": exported_count}

