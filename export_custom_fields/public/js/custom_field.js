// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// MIT License. See license.txt

frappe.provide("frappe.customize_form");

frappe.ui.form.on("Custom Field", {
	refresh: function (frm) {
		if (frappe.boot.developer_mode && frm.doc.module) {
			// Export to Module button
			frm
				.add_custom_button(
					__("📦 Export to Module"),
					function () {
						frappe.call({
							method: "export_custom_fields.customize_form.export_custom_fields_by_module",
							args: {
								module: frm.doc.module,
								sync_on_migrate: 1,
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
					}
				)
				.addClass("btn-danger");
		}
	},
});

