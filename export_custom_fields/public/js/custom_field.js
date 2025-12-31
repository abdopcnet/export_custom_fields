// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// MIT License. See license.txt

frappe.provide('frappe.customize_form');

frappe.ui.form.on('Custom Field', {
	refresh: function (frm) {
		if (
			frappe.boot.developer_mode &&
			frm.doc.dt &&
			frm.doc.module &&
			frm.doc.is_system_generated === 0
		) {
			frm.add_custom_button(__('Export Customizations'), function () {
				frappe.call({
					method: 'frappe.modules.utils.export_customizations',
					args: {
						doctype: frm.doc.dt,
						module: frm.doc.module,
						sync_on_migrate: 1,
						with_permissions: 0,
					},
				});
			}).addClass('btn-danger');
		}
	},
});
