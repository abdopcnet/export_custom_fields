// Frontend logging: console.log('[property_setter_list.js] method: function_name')

frappe.listview_settings['Property Setter'] = {
	onload: function (listview) {
		if (frappe.boot.developer_mode) {
			// Bulk Export Fixture button - always visible
			listview.page.add_button(
				__('Bulk Export Fixture'),
				function () {
					let selected = listview.get_checked_items();
					if (!selected || selected.length === 0) {
						frappe.msgprint({
							message: __('Please select records to export.'),
							indicator: 'orange',
						});
						return;
					}

					// Check if all selected items have module and same module
					let modules = [];
					let hasNoModule = false;
					for (let item of selected) {
						if (!item.module) {
							hasNoModule = true;
							break;
						}
						if (modules.indexOf(item.module) === -1) {
							modules.push(item.module);
						}
					}

					// Show error if any record doesn't have module
					if (hasNoModule) {
						frappe.throw(__('Set Module First Before Exporting'));
						return;
					}

					// Show error if records belong to different modules
					if (modules.length > 1) {
						frappe.throw(
							__(
								'Selected records belong to different modules. Please select records with the same module.',
							),
						);
						return;
					}

					if (modules.length === 0) {
						frappe.throw(__('Set Module First Before Exporting'));
						return;
					}

					// Export Property Setter only
					frappe.call({
						method: 'export_custom_fields.customize_form.bulk_export_fixtures_for_module',
						args: {
							module: modules[0],
							doctype: 'Property Setter',
						},
						freeze: true,
						freeze_message: __('Exporting fixtures...'),
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
