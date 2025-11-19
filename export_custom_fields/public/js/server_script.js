// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// MIT License. See license.txt

frappe.provide("frappe.customize_form");

frappe.ui.form.on("Server Script", {
	refresh: function (frm) {
		if (frappe.boot.developer_mode && frm.doc.module) {
			// Export Server Scripts button
			frm
				.add_custom_button(
					__("📦 Export to Module"),
					function () {
						frappe.call({
							method: "export_custom_fields.server_script.export_server_scripts_by_module",
							args: {
								module: frm.doc.module,
							},
							callback: function (r) {
								if (!r.exc) {
									frappe.show_alert({
										message: __("Server Scripts exported successfully"),
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

