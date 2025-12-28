// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// MIT License. See license.txt

frappe.provide('frappe.customize_form');

frappe.ui.form.on('Customize Form', {
	refresh: function (frm) {
		if (frappe.boot.developer_mode && frm.doc.doc_type) {
			frm.add_custom_button(__('Export Customizations'), function () {
				frappe.prompt(
					[
						{
							fieldtype: 'Link',
							fieldname: 'module',
							options: 'Module Def',
							label: __('Module to Export'),
							reqd: 1,
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
	},
});
