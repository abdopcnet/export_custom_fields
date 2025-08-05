import frappe
import json
import os
from frappe import _, get_module_path, scrub

@frappe.whitelist()
def export_custom_fields_by_module(module, sync_on_migrate=False):
    """Export Custom Fields and Property Setters for the specified module to JSON files.
    This follows the same pattern as frappe.modules.utils.export_customizations"""
    
    if not frappe.conf.developer_mode:
        frappe.throw(_("Only allowed to export customizations in developer mode"))

    sync_on_migrate = frappe.utils.cint(sync_on_migrate)
    
    # Get custom fields for the specified module
    custom_fields = frappe.get_all(
        "Custom Field",
        filters={"module": module},
        fields="*",
        order_by="name"
    )
    
    if not custom_fields:
        frappe.msgprint(_("No custom fields found for module: {0}").format(module))
        return

    # Group custom fields by doctype
    doctype_fields = {}
    for field in custom_fields:
        doctype = field.get("dt")
        if doctype not in doctype_fields:
            doctype_fields[doctype] = []
        doctype_fields[doctype].append(field)

    # Create export folder if it doesn't exist
    folder_path = os.path.join(get_module_path(module), "custom")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    exported_files = []
    
    # Export each doctype separately (same as original)
    for doctype, fields in doctype_fields.items():
        # Get property setters for this doctype AND module
        property_setters = frappe.get_all(
            "Property Setter",
            filters=[
                ["doc_type", "=", doctype],
                ["module", "=", module]
            ],
            fields="*",
            order_by="name"
        )
        
        # Prepare data for export (same structure as original)
        custom = {
            "custom_fields": fields,
            "property_setters": property_setters,
            "custom_perms": [],
            "doctype": doctype,
            "sync_on_migrate": sync_on_migrate,
        }

        # Export to JSON file (same naming convention as original)
        filename = scrub(doctype) + ".json"
        file_path = os.path.join(folder_path, filename)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(frappe.as_json(custom, indent=2))
        
        exported_files.append(file_path)

    if exported_files:
        frappe.msgprint(_("Custom Fields for module <b>{0}</b> exported to:<br>{1}").format(
            module, "<br>".join(exported_files)
        ))
        return exported_files
