// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// MIT License. See license.txt

frappe.provide('frappe.customize_form');

// Frontend logging: console.log('[custom_field.js] method: function_name')

frappe.ui.form.on('Custom Field', {
	refresh: function (frm) {
		if (frappe.boot.developer_mode) {
			// Export Customizations button
			if (frm.doc.dt && frm.doc.module && frm.doc.is_system_generated === 0) {
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
									doctype: 'Custom Field',
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

console.log('[custom_field.js] method: form_settings');
