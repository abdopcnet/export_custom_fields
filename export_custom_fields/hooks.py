app_name = "export_custom_fields"
app_title = "Export Custom Fields"
app_publisher = "abdopcnet"
app_description = "Export Custom Fields"
app_email = "abdopcnet@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "export_custom_fields",
# 		"logo": "/assets/export_custom_fields/logo.png",
# 		"title": "Export Custom Fields",
# 		"route": "/export_custom_fields",
# 		"has_permission": "export_custom_fields.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/export_custom_fields/css/export_custom_fields.css"
# app_include_js = "/assets/export_custom_fields/js/export_custom_fields.js"

# include js, css files in header of web template
# web_include_css = "/assets/export_custom_fields/css/export_custom_fields.css"
# web_include_js = "/assets/export_custom_fields/js/export_custom_fields.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "export_custom_fields/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}

# Add JS files to Customize Form, Server Script, Client Script, Custom Field and Property Setter doctypes
doctype_js = {
    "Customize Form": "public/js/customize_form.js",
    "Server Script": "public/js/server_script.js",
    "Client Script": "public/js/client_script.js",
    "Custom Field": "public/js/custom_field.js",
    "Property Setter": "public/js/property_setter.js",
    "Custom HTML Block": "public/js/custom_html_block.js"
}

doctype_list_js = {
    "Custom Field": "public/js/custom_field_list.js",
    "Property Setter": "public/js/property_setter_list.js",
    "Server Script": "public/js/server_script_list.js",
    "Client Script": "public/js/client_script_list.js",
    "Custom HTML Block": "public/js/custom_html_block_list.js"
}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "export_custom_fields/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "export_custom_fields.utils.jinja_methods",
# 	"filters": "export_custom_fields.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "export_custom_fields.install.before_install"
# after_install = "export_custom_fields.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "export_custom_fields.uninstall.before_uninstall"
# after_uninstall = "export_custom_fields.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "export_custom_fields.utils.before_app_install"
# after_app_install = "export_custom_fields.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "export_custom_fields.utils.before_app_uninstall"
# after_app_uninstall = "export_custom_fields.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "export_custom_fields.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"export_custom_fields.tasks.all"
# 	],
# 	"daily": [
# 		"export_custom_fields.tasks.daily"
# 	],
# 	"hourly": [
# 		"export_custom_fields.tasks.hourly"
# 	],
# 	"weekly": [
# 		"export_custom_fields.tasks.weekly"
# 	],
# 	"monthly": [
# 		"export_custom_fields.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "export_custom_fields.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "export_custom_fields.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "export_custom_fields.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["export_custom_fields.utils.before_request"]
# after_request = ["export_custom_fields.utils.after_request"]

# Job Events
# ----------
# before_job = ["export_custom_fields.utils.before_job"]
# after_job = ["export_custom_fields.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"export_custom_fields.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
