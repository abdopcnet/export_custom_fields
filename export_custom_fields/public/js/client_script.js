// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// MIT License. See license.txt

frappe.provide("frappe.customize_form");

frappe.ui.form.on("Client Script", {
	refresh: function (frm) {
		if (frappe.boot.developer_mode && frm.doc.module) {
			// Client Script button
			frm
				.add_custom_button(
					__("📦 Export to Module"),
					function () {
						if (!frm.doc.module) {
							frappe.msgprint(__("Please select a module first"));
							return;
						}
						frappe.call({
							method: "export_custom_fields.client_script.export_client_scripts_by_module",
							args: {
								module: frm.doc.module,
							},
							callback: function (r) {
								if (!r.exc) {
									frappe.show_alert({
										message: __("Client Scripts exported successfully"),
										indicator: "green",
									});
								}
							},
						});
					}
				)
				.addClass("btn-danger");
		}
	},
});

