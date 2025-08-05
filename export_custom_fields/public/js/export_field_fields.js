// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// MIT License. See license.txt

frappe.provide("frappe.customize_form");

frappe.ui.form.on("Customize Form", {
	refresh: function (frm) {
		if (frappe.boot.developer_mode) {
			frm.add_custom_button(
				__("Export Custom Fields"),
				function () {
					frappe.prompt(
						[
							{
								fieldtype: "Link",
								fieldname: "module",
								options: "Module Def",
								label: __("Module to Export"),
								reqd: 1,
							},
							{
								fieldtype: "Check",
								fieldname: "sync_on_migrate",
								label: __("Sync on Migrate"),
								default: 1,
							},
						],
						function (data) {
							frappe.call({
								method: "export_custom_fields.api.export_custom_fields_by_module",
								args: {
									module: data.module,
									sync_on_migrate: data.sync_on_migrate,
								},
								callback: function (r) {
									if (!r.exc) {
										frappe.show_alert({
											message: __("Custom Fields exported successfully"),
											indicator: "green",
										});
									}
								},
							});
						},
						__("Select Module")
					);
				}
			);
		}
	},
});
