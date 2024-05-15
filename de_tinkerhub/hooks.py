from . import __version__ as app_version
app_name = "community_management"
app_title = "Community Management"
app_publisher = "Aysha"
app_description = "App For Event Management"
app_email = "ayshahakeem02@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/de_tinkerhub/css/de_tinkerhub.css"
# app_include_js = "/assets/de_tinkerhub/js/de_tinkerhub.js"

# include js, css files in header of web template
# web_include_css = "/assets/de_tinkerhub/css/de_tinkerhub.css"
web_include_css = "lms.bundle.css"
web_include_js = "/assets/de_tinkerhub/js/de_tinkerhub.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "de_tinkerhub/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

website_route_rules = [
    {'from':'/registration-quiz?event=<event>', 'to':'registration-quiz'},
    {'from':'/submit-reg-quiz?event=<event>', 'to':'submit-reg-quiz'}
]

website_redirects = [
    {"source": "/event-creation/list", "target": f"/event-creation/new"}
]

role_home_page = {
    "Learner": "/upcoming-events",
    "Campus Lead": "/app/events",
    # "Administrator": "desk"
}

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "de_tinkerhub.utils.jinja_methods",
#	"filters": "de_tinkerhub.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "de_tinkerhub.install.before_install"
# after_install = "de_tinkerhub.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "de_tinkerhub.uninstall.before_uninstall"
# after_uninstall = "de_tinkerhub.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "de_tinkerhub.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Event Registration": {
		"on_submit": "de_tinkerhub.de_tinkerhub.registration_email.send_registration_email"
	},
    "Event Custom":{
        "on_update":"de_tinkerhub.de_tinkerhub.event_update_email.send_event_update_email"
    },
    # "User":{
    #     "after_insert":"de_tinkerhub.de_tinkerhub.learner_creation.on_user_signup"
    # },
    "User":{
        "on_update":"de_tinkerhub.de_tinkerhub.lead_role.on_lead_role"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"de_tinkerhub.tasks.all"
#	],
#	"daily": [
#		"de_tinkerhub.tasks.daily"
#	],
#	"hourly": [
#		"de_tinkerhub.tasks.hourly"
#	],
#	"weekly": [
#		"de_tinkerhub.tasks.weekly"
#	],
#	"monthly": [
#		"de_tinkerhub.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "de_tinkerhub.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "de_tinkerhub.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "de_tinkerhub.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["de_tinkerhub.utils.before_request"]
# after_request = ["de_tinkerhub.utils.after_request"]

# Job Events
# ----------
# before_job = ["de_tinkerhub.utils.before_job"]
# after_job = ["de_tinkerhub.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"de_tinkerhub.auth.validate"
# ]

# portal_menu_items = [ 
#     {"title": "Upcoming Events", "route": "/upcoming-events", "role": "All"},
#     {"title": "My Events", "route": "/my-events", "role": "Learner"},
#     {"title": "My Profile", "route": "/learner-profile/new", "role": "Learner"},
#     {"title": "Public Profile", "route": f"/learner/{frappe.session.user}", "role": "Learner"},
#     {"title": "Event Admin", "route": "/admin-portal", "role": "Event Admin"},
#     {"title": "Create Event", "route": "/event-creation/new", "role": "Event Admin"}
# ]  

website_route_rules = [
    {"from_route": "/event-portal/<name>", "to_route": "event-portal"},
]

# permission_query_conditions = {
# 	"Feedback Submission": "frappe.desk.doctype.feedback_submission.feedback_submission.get_permission_query_conditions"
# }

fixtures = [
    "Custom DocPerm"
]

profile_mandatory_fields = [
	"full_name",
	"mobile_no",
	"college_student"
]