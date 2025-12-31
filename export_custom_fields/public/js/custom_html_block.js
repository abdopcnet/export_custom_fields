// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// MIT License. See license.txt

// Frontend logging: console.log('[custom_html_block.js] method: function_name')

frappe.ui.form.on('Custom HTML Block', {
	refresh: function (frm) {
		if (frappe.boot.developer_mode) {
			// Export to Module button
			if (frm.doc.name) {
				frm.add_custom_button(__('Export to Module'), function () {
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
					],
					function (data) {
						frappe.call({
							method: 'export_custom_fields.custom_html_block.export_custom_html_blocks_by_module',
							args: {
								name: frm.doc.name,
								module: data.module,
								sync_on_migrate: data.sync_on_migrate,
							},
							callback: function (r) {
								if (!r.exc) {
									frappe.show_alert({
										message: __('Custom HTML Block exported successfully'),
										indicator: 'green',
									});
								}
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
									doctype: 'Custom HTML Block',
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

console.log('[custom_html_block.js] method: form_settings');
