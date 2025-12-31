# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import os
import frappe
from frappe import _, get_app_path, scrub
from frappe.core.doctype.data_import.data_import import export_json


@frappe.whitelist()
def bulk_export_fixtures(server_script_names=None, client_script_names=None, custom_html_block_names=None):
	"""Bulk export Server Scripts, Client Scripts, and Custom HTML Blocks using export_json (fixtures method).
	Works like the "Export to Module" button in form view, but for multiple records.
	Each record must have a module defined. If module is not defined, export stops with error message.

	Args:
		server_script_names: List of Server Script names to export (optional)
		client_script_names: List of Client Script names to export (optional)
		custom_html_block_names: List of Custom HTML Block names to export (optional)
	"""

	try:
		if not frappe.conf.developer_mode:
			frappe.throw(
				_("Only allowed to export fixtures in developer mode"))

		# Parse JSON if passed as string
		if isinstance(server_script_names, str):
			server_script_names = frappe.parse_json(server_script_names)
		if isinstance(client_script_names, str):
			client_script_names = frappe.parse_json(client_script_names)
		if isinstance(custom_html_block_names, str):
			custom_html_block_names = frappe.parse_json(custom_html_block_names)

		# Get server scripts - either selected ones or all visible
		if server_script_names:
			all_server_scripts = frappe.get_all(
				"Server Script",
				filters={"name": ["in", server_script_names]},
				fields=["name", "module"],
				order_by="name"
			)
		else:
			all_server_scripts = []

		# Get client scripts - either selected ones or all visible
		if client_script_names:
			all_client_scripts = frappe.get_all(
				"Client Script",
				filters={"name": ["in", client_script_names]},
				fields=["name", "module"],
				order_by="name"
			)
		else:
			all_client_scripts = []

		# Get custom html blocks - either selected ones or all visible
		if custom_html_block_names:
			all_custom_html_blocks = frappe.get_all(
				"Custom HTML Block",
				filters={"name": ["in", custom_html_block_names]},
				fields=["name", "module"],
				order_by="name"
			)
		else:
			all_custom_html_blocks = []

		# If no names provided, get all records
		if not server_script_names and not client_script_names and not custom_html_block_names:
			all_server_scripts = frappe.get_all(
				"Server Script",
				fields=["name", "module"],
				order_by="name"
			)
			all_client_scripts = frappe.get_all(
				"Client Script",
				fields=["name", "module"],
				order_by="name"
			)
			all_custom_html_blocks = frappe.get_all(
				"Custom HTML Block",
				fields=["name", "module"],
				order_by="name"
			)

		# Initialize exported files list
		all_exported_files = []

		# Group Server Scripts by module
		server_scripts_by_module = {}
		for script in all_server_scripts:
			module = script.get("module")
			if not module:
				frappe.throw(
					"{0} Module Not defined".format(script.get("name")))
			if module not in server_scripts_by_module:
				server_scripts_by_module[module] = []
			server_scripts_by_module[module].append(script.get("name"))

		# Export Server Scripts grouped by module
		for module, script_names in server_scripts_by_module.items():
			try:
				module_doc = frappe.get_doc("Module Def", module)
				app_name = module_doc.app_name
				if not app_name:
					frappe.throw(
						_("Could not determine app name for module: {0}").format(module))

				fixtures_path = get_app_path(app_name, "fixtures")
				if not os.path.exists(fixtures_path):
					os.makedirs(fixtures_path)

				file_path = os.path.join(
					fixtures_path, scrub("Server Script") + ".json")
				export_json(
					"Server Script",
					file_path,
					filters={"name": ["in", script_names]},
					order_by="idx asc, creation asc",
				)
				if file_path not in all_exported_files:
					all_exported_files.append(file_path)
			except Exception as e:
				frappe.log_error(
					"[fixtures.py] method: bulk_export_fixtures - Server Script Module: {0}".format(
						module
					),
					"Bulk Export Fixtures",
				)
				raise

		# Group Client Scripts by module
		client_scripts_by_module = {}
		for script in all_client_scripts:
			module = script.get("module")
			if not module:
				frappe.throw(
					"{0} Module Not defined".format(script.get("name")))
			if module not in client_scripts_by_module:
				client_scripts_by_module[module] = []
			client_scripts_by_module[module].append(script.get("name"))

		# Export Client Scripts grouped by module
		for module, script_names in client_scripts_by_module.items():
			try:
				module_doc = frappe.get_doc("Module Def", module)
				app_name = module_doc.app_name
				if not app_name:
					frappe.throw(
						_("Could not determine app name for module: {0}").format(module))

				fixtures_path = get_app_path(app_name, "fixtures")
				if not os.path.exists(fixtures_path):
					os.makedirs(fixtures_path)

				file_path = os.path.join(
					fixtures_path, scrub("Client Script") + ".json")
				export_json(
					"Client Script",
					file_path,
					filters={"name": ["in", script_names]},
					order_by="idx asc, creation asc",
				)
				if file_path not in all_exported_files:
					all_exported_files.append(file_path)
			except Exception as e:
				frappe.log_error(
					"[fixtures.py] method: bulk_export_fixtures - Client Script Module: {0}".format(
						module
					),
					"Bulk Export Fixtures",
				)
				raise

		# Group Custom HTML Blocks by module
		custom_html_blocks_by_module = {}
		for block in all_custom_html_blocks:
			module = block.get("module")
			if not module:
				frappe.throw(
					"{0} Module Not defined".format(block.get("name")))
			if module not in custom_html_blocks_by_module:
				custom_html_blocks_by_module[module] = []
			custom_html_blocks_by_module[module].append(block.get("name"))

		# Export Custom HTML Blocks grouped by module
		for module, block_names in custom_html_blocks_by_module.items():
			try:
				module_doc = frappe.get_doc("Module Def", module)
				app_name = module_doc.app_name
				if not app_name:
					frappe.throw(
						_("Could not determine app name for module: {0}").format(module))

				fixtures_path = get_app_path(app_name, "fixtures")
				if not os.path.exists(fixtures_path):
					os.makedirs(fixtures_path)

				file_path = os.path.join(
					fixtures_path, scrub("Custom HTML Block") + ".json")
				export_json(
					"Custom HTML Block",
					file_path,
					filters={"name": ["in", block_names]},
					order_by="idx asc, creation asc",
				)
				if file_path not in all_exported_files:
					all_exported_files.append(file_path)
			except Exception as e:
				frappe.log_error(
					"[fixtures.py] method: bulk_export_fixtures - Custom HTML Block Module: {0}".format(
						module
					),
					"Bulk Export Fixtures",
				)
				raise

		return {
			"exported_files": all_exported_files
		}

	except Exception as e:
		frappe.log_error(
			"[fixtures.py] method: bulk_export_fixtures",
			"Bulk Export Fixtures",
		)
		frappe.throw(_("Error during bulk export fixtures"))

