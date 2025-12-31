# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import frappe
import os
from frappe import _, get_module_path, scrub


@frappe.whitelist()
def has_custom_fields_in_module(module):
    """Check if there are custom fields (is_system_generated=0) in the specified module"""
    custom_fields_count = frappe.db.count(
        "Custom Field",
        filters={"module": module, "is_system_generated": 0}
    )
    return custom_fields_count > 0


@frappe.whitelist()
def export_custom_fields_by_module(module, sync_on_migrate=False):
    """Export Custom Fields and Property Setters for the specified module to JSON files.
    This follows the same pattern as frappe.modules.utils.export_customizations"""

    if not frappe.conf.developer_mode:
        frappe.throw(
            _("Only allowed to export customizations in developer mode"))

    sync_on_migrate = frappe.utils.cint(sync_on_migrate)

    # Get custom fields for the specified module
    custom_fields = frappe.get_all(
        "Custom Field",
        filters={"module": module},
        fields="*",
        order_by="name"
    )

    # Get property setters for the specified module
    property_setters = frappe.get_all(
        "Property Setter",
        filters={"module": module},
        fields="*",
        order_by="name"
    )

    # Check if there are any customizations to export
    if not custom_fields and not property_setters:
        frappe.msgprint(
            _("No custom fields or property setters found for module: {0}").format(module))
        return

    # Group custom fields by doctype
    doctype_fields = {}
    for field in custom_fields:
        doctype = field.get("dt")
        if doctype not in doctype_fields:
            doctype_fields[doctype] = []
        doctype_fields[doctype].append(field)

    # Group property setters by doctype
    doctype_property_setters = {}
    for ps in property_setters:
        doctype = ps.get("doc_type")
        if doctype not in doctype_property_setters:
            doctype_property_setters[doctype] = []
        doctype_property_setters[doctype].append(ps)

    # Get DocType Links for doctypes in this module
    # Get all doctypes that have customizations first
    all_doctypes = set(doctype_fields.keys()) | set(
        doctype_property_setters.keys())

    # Get Custom DocType Links for these doctypes
    # Note: DocType Link doesn't have a module field, so we filter by custom=1
    # Custom links are typically from custom apps, but cannot be separated by module
    # System export gets ALL links (custom + standard), but for module-based export,
    # we only export custom links to avoid mixing standard links from core apps
    doctype_links = {}
    if all_doctypes:
        links = frappe.get_all(
            "DocType Link",
            fields="*",
            filters={"parent": ["in", list(all_doctypes)], "custom": 1},
            order_by="name"
        )
        for link in links:
            doctype = link.get("parent")
            if doctype not in doctype_links:
                doctype_links[doctype] = []
            doctype_links[doctype].append(link)

    # Create export folder if it doesn't exist
    folder_path = os.path.join(get_module_path(module), "custom")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    exported_files = []

    # Export each doctype separately (same as original)
    for doctype in all_doctypes:
        fields = doctype_fields.get(doctype, [])
        ps_list = doctype_property_setters.get(doctype, [])
        links_list = doctype_links.get(doctype, [])

        # Prepare data for export (same structure as system export)
        # Order matches frappe.modules.utils.export_customizations
        custom = {
            "custom_fields": fields,
            "custom_perms": [],
            "doctype": doctype,
            "links": links_list,
            "property_setters": ps_list,
            "sync_on_migrate": sync_on_migrate,
        }

        # Export to JSON file (same naming convention as original)
        filename = scrub(doctype) + ".json"
        file_path = os.path.join(folder_path, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(frappe.as_json(custom, indent=2))

        exported_files.append(file_path)

    if exported_files:
        frappe.msgprint(_("Custom Fields and Property Setters for module <b>{0}</b> exported to:<br>{1}").format(
            module, "<br>".join(exported_files)
        ))
        return exported_files
