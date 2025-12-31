// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// MIT License. See license.txt

frappe.provide('frappe.customize_form');

// Frontend logging: console.log('[property_setter.js] method: function_name')

frappe.ui.form.on('Property Setter', {
	refresh: function (frm) {
		if (frappe.boot.developer_mode) {
			// Export Customizations button
			if (frm.doc.doc_type) {
				frm.add_custom_button(__('Export Customizations'), function () {
					frappe.prompt(
						[
							{
								fieldtype: 'Link',
								fieldname: 'module',
								options: 'Module Def',
								label: __('Module to Export'),
								reqd: 1,
								default: frm.doc.module || '',
							},
							{
								fieldtype: 'Check',
								fieldname: 'sync_on_migrate',
								label: __('Sync on Migrate'),
								default: 1,
							},
							{
								fieldtype: 'Check',
								fieldname: 'with_permissions',
								label: __('Export Custom Permissions'),
								description: __(
									'Exported permissions will be force-synced on every migrate overriding any other customization.',
								),
								default: 0,
							},
						],
						function (data) {
							frappe.call({
								method: 'frappe.modules.utils.export_customizations',
								args: {
									doctype: frm.doc.doc_type,
									module: data.module,
									sync_on_migrate: data.sync_on_migrate,
									with_permissions: data.with_permissions,
								},
							});
						},
						__('Select Module'),
					);
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
									doctype: 'Property Setter',
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

console.log('[property_setter.js] method: form_settings');
