// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// MIT License. See license.txt

frappe.provide('frappe.customize_form');

frappe.ui.form.on('Web Form', {
	refresh: function (frm) {
		if (frappe.boot.developer_mode) {
			// Export to Module button
			if (frm.doc.module) {
				frm.add_custom_button(__('Export to Module'), function () {
					if (!frm.doc.module) {
						frappe.msgprint(__('Please select a module first'));
						return;
					}
					frappe.call({
						method: 'export_custom_fields.web_form.export_web_forms_by_module',
						args: {
							module: frm.doc.module,
						},
						callback: function (r) {
							if (!r.exc) {
								frappe.show_alert({
									message: __('Web Forms exported successfully'),
									indicator: 'green',
								});
							}
						},
					});
				}).addClass('btn-danger');
			}

			// Set Module button
			if (frm.doc.name) {
				frm.add_custom_button(__('Set Module'), function () {
					frappe.prompt(
						[
							{
								fieldtype: 'Link',
								fieldname: 'module',
								options: 'Module Def',
								label: __('Select Module'),
								reqd: 1,
								default: frm.doc.module || '',
							},
						],
						function (data) {
							frappe.call({
								method: 'export_custom_fields.customize_form.bulk_set_module',
								args: {
									doctype: 'Web Form',
									names: [frm.doc.name],
									module: data.module,
								},
								freeze: true,
								freeze_message: __('Updating module...'),
								callback: function (r) {
									if (!r.exc) {
										frappe.show_alert({
											message: __('Module updated successfully.'),
											indicator: 'green',
										});
										frm.reload_doc();
									}
								},
							});
						},
						__('Select Module'),
					);
				}).addClass('btn-success');
			}
		}
	},
});
