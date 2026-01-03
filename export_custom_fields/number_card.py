# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import frappe
from frappe import _
from frappe.modules.export_file import export_to_files


@frappe.whitelist()
def export_number_cards_by_module(module):
	"""Export Number Cards for the specified module using the same method as on_update (export_to_files)."""

	if not frappe.conf.developer_mode:
		frappe.throw(_("Only allowed to export customizations in developer mode"))

	# Get all Number Cards in this module that are standard (same condition as on_update)
	number_cards = frappe.get_all(
		"Number Card",
		filters={"module": module, "is_standard": 1},
		fields=["name"],
	)

	if not number_cards:
		frappe.msgprint(_("No standard Number Cards found in module <b>{0}</b>").format(module))
		return {"app": None, "module": module, "count": 0}

	# Build record_list using the same format as on_update
	record_list = [["Number Card", card.name] for card in number_cards]

	# Export using the same method as on_update: export_to_files(record_list=[["Number Card", self.name]], record_module=self.module)
	try:
		export_to_files(record_list=record_list, record_module=module)
		frappe.msgprint(_("Exported <b>{0}</b> Number Card(s) for module <b>{1}</b>").format(len(number_cards), module))
		return {"module": module, "count": len(number_cards)}
	except Exception as e:
		frappe.log_error(f"Error exporting Number Cards for module {module}: {str(e)}")
		frappe.throw(_("Error exporting Number Cards: {0}").format(str(e)))

