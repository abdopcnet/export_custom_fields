// Frontend logging: console.log('[property_setter_list.js] method: function_name')

frappe.listview_settings['Property Setter'] = {
	onload: function (listview) {
		if (frappe.boot.developer_mode) {
			listview.page
				.add_button(
					__('Bulk Export Customizations'),
					function () {
						// Get selected items, or all visible items if none selected
						let selected_names = listview.get_checked_items(true);
						if (!selected_names || selected_names.length === 0) {
							// If no items selected, use all visible items
							selected_names = listview.data.map((d) => d.name);
						}

						if (!selected_names || selected_names.length === 0) {
							frappe.msgprint({
								message: __('No records selected to export.'),
								indicator: 'orange',
							});
							return;
						}

						frappe.call({
							method: 'export_custom_fields.customize_form.bulk_export_customizations',
							args: {
								property_setter_names: selected_names,
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
					'add',
				)
				.addClass('btn-danger');
		}
	},
};

console.log('[property_setter_list.js] method: listview_settings');
