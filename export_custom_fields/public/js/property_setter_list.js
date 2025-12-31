// Frontend logging: console.log('[property_setter_list.js] method: function_name')

frappe.listview_settings['Property Setter'] = {
	onload: function (listview) {
		if (frappe.boot.developer_mode) {
			// Bulk Export button
			listview.page.add_button(
				__('Bulk Export Customizations'),
				function () {
					let selected = listview.get_checked_items(true);
					if (!selected || selected.length === 0) {
						frappe.msgprint({
							message: __('Please select records to export.'),
							indicator: 'orange',
						});
						return;
					}

					frappe.call({
						method: 'export_custom_fields.customize_form.bulk_export_customizations',
						args: {
							property_setter_names: selected,
						},
						freeze: true,
						freeze_message: __('Exporting customizations...'),
						callback: function (r) {
							if (!r.exc && r.message) {
								let count = r.message.exported_files
									? r.message.exported_files.length
									: 0;
								frappe.msgprint({
									message: __(
										'Bulk export completed successfully! {0} files exported.',
									).replace('{0}', count),
									indicator: 'green',
								});
							}
						},
					});
				},
				{ btn_class: 'btn-danger' },
			);

			// Set Module button
			listview.page.add_button(
				__('Set Module'),
				function () {
					let selected_names = listview.get_checked_items(true);
					if (!selected_names || selected_names.length === 0) {
						frappe.msgprint({
							message: __('Please select records to update.'),
							indicator: 'orange',
						});
						return;
					}

					frappe.prompt(
						[
							{
								fieldtype: 'Link',
								fieldname: 'module',
								options: 'Module Def',
								label: __('Select Module'),
								reqd: 1,
							},
						],
						function (data) {
							frappe.call({
								method: 'export_custom_fields.customize_form.bulk_set_module',
								args: {
									doctype: 'Property Setter',
									names: selected_names,
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
										listview.refresh();
									}
								},
							});
						},
						__('Select Module'),
					);
				},
				{ btn_class: 'btn-success' },
			);
		}
	},
};

console.log('[property_setter_list.js] method: listview_settings');
