# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import frappe
import os
from frappe import _, scrub
from frappe.core.doctype.data_import.data_import import export_json


@frappe.whitelist()
def has_custom_fields_in_module(module):
    """Check if there are custom fields (is_system_generated=0) in the specified module"""
    custom_fields_count = frappe.db.count(
        "Custom Field",
        filters={"module": module, "is_system_generated": 0}
    )
    return custom_fields_count > 0


@frappe.whitelist()
def bulk_export_fixtures_for_module(module, doctype):
    """Export Custom Fields or Property Setters for the specified module.
    Exports to [app]/fixtures/ directory.

    Args:
        module: Module name to export fixtures for
        doctype: DocType to export ("Custom Field" or "Property Setter")
    """

    try:
        if not frappe.conf.developer_mode:
            frappe.throw(
                _("Only allowed to export fixtures in developer mode"))

        if not module:
            frappe.throw(_("Module is required"))

        if not doctype:
            frappe.throw(_("DocType is required"))

        # Validate module exists
        if not frappe.db.exists("Module Def", module):
            frappe.throw(_("Module '{0}' does not exist").format(module))

        # Validate doctype
        if doctype not in ["Custom Field", "Property Setter"]:
            frappe.throw(_("Invalid doctype. Must be 'Custom Field' or 'Property Setter'"))

        # Get module doc to determine app name
        module_doc = frappe.get_doc("Module Def", module)
        app_name = module_doc.app_name
        if not app_name:
            frappe.throw(_("Could not determine app name for module: {0}").format(module))

        # Get app path
        app_path = frappe.get_app_path(app_name)
        fixtures_path = os.path.join(app_path, "fixtures")
        if not os.path.exists(fixtures_path):
            os.makedirs(fixtures_path)

        # Determine file path based on doctype
        if doctype == "Custom Field":
            file_path = os.path.join(fixtures_path, "custom_field.json")
        else:  # Property Setter
            file_path = os.path.join(fixtures_path, "property_setter.json")

        # Export the specified doctype
        export_json(
            doctype,
            file_path,
            filters={"module": module},
            order_by="idx asc, creation asc",
        )

        return {
            "module": module,
            "app": app_name,
            "doctype": doctype,
            "exported_files": [file_path]
        }

    except Exception as e:
        frappe.log_error(
            "[customize_form.py] method: bulk_export_fixtures_for_module",
            "Bulk Export Fixtures",
        )
        frappe.throw(_("Error during bulk export fixtures: {0}").format(str(e)))


@frappe.whitelist()
def bulk_export_fixtures_for_modules(modules):
    """Export Custom Fields and Property Setters for multiple modules.
    Exports each module to its app's fixtures/ directory.

    Args:
        modules: List of module names to export fixtures for
    """

    try:
        if not frappe.conf.developer_mode:
            frappe.throw(
                _("Only allowed to export fixtures in developer mode"))

        if not modules:
            frappe.throw(_("Modules are required"))

        # Parse JSON if passed as string
        if isinstance(modules, str):
            modules = frappe.parse_json(modules)

        if not isinstance(modules, list):
            frappe.throw(_("Modules must be a list"))

        all_exported_files = []
        exported_modules = []

        # Export each module separately
        for module in modules:
            try:
                result = bulk_export_fixtures_for_module(module)
                if result and result.get("exported_files"):
                    all_exported_files.extend(result.get("exported_files", []))
                    exported_modules.append(module)
            except Exception as e:
                frappe.log_error(
                    "[customize_form.py] method: bulk_export_fixtures_for_modules - Module: {0}".format(
                        module),
                    "Bulk Export Fixtures",
                )
                # Continue with other modules even if one fails
                continue

        if exported_modules:
            frappe.msgprint(_("Fixtures for modules <b>{0}</b> exported successfully").format(
                ", ".join(exported_modules)
            ))
        else:
            frappe.throw(_("No fixtures exported. Please check errors in Error Log."))

        return {
            "modules": exported_modules,
            "exported_files": all_exported_files
        }

    except Exception as e:
        frappe.log_error(
            "[customize_form.py] method: bulk_export_fixtures_for_modules",
            "Bulk Export Fixtures",
        )
        frappe.throw(_("Error during bulk export fixtures: {0}").format(str(e)))


@frappe.whitelist()
def bulk_set_module(doctype, names, module):
    """Update module for multiple records (Custom Field, Property Setter, Server Script, or Client Script).

    Args:
        doctype: DocType name ('Custom Field', 'Property Setter', 'Server Script', or 'Client Script')
        names: List of document names to update
        module: Module name to set
    """
    try:
        if not frappe.conf.developer_mode:
            frappe.throw(
                _("Only allowed to update module in developer mode"))

        if doctype not in ['Custom Field', 'Property Setter', 'Server Script', 'Client Script', 'Custom HTML Block']:
            frappe.throw(
                _("Invalid doctype. Must be 'Custom Field', 'Property Setter', 'Server Script', 'Client Script', or 'Custom HTML Block'"))

        if not names:
            frappe.throw(_("No records selected"))

        if not module:
            frappe.throw(_("Module is required"))

        # Parse JSON if passed as string
        if isinstance(names, str):
            names = frappe.parse_json(names)

        # Validate module exists
        if not frappe.db.exists("Module Def", module):
            frappe.throw(_("Module '{0}' does not exist").format(module))

        # Update module for each record
        updated_count = 0
        for name in names:
            try:
                frappe.db.set_value(doctype, name, "module", module)
                updated_count += 1
            except Exception as e:
                frappe.log_error(
                    "[customize_form.py] method: bulk_set_module - Record: {0}".format(
                        name),
                    "Bulk Set Module",
                )
                raise

        frappe.db.commit()

        return {
            "updated_count": updated_count,
            "message": _("{0} records updated successfully").format(updated_count)
        }

    except Exception as e:
        frappe.log_error(
            "[customize_form.py] method: bulk_set_module",
            "Bulk Set Module",
        )
        frappe.throw(_("Error updating module"))
