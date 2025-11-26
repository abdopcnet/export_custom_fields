// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// MIT License. See license.txt

frappe.ui.form.on('Custom HTML Block', {
	setup_export(frm) {
		if (frappe.boot.developer_mode && frm.doc.name) {
			// Export to Module button
			frm.add_custom_button(__('📦 Export to Module'), function () {
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
	},

	refresh: function (frm) {
		frm.events.setup_export(frm);
	},
});
