import frappe
from frappe import _
from frappe.desk.doctype.dashboard_chart.dashboard_chart import get_result
from frappe.desk.doctype.notification_log.notification_log import make_notification_logs
from frappe.utils import (
	add_months,
	cint,
	cstr,
	flt,
	fmt_money,
	format_date,
	get_datetime,
	getdate,
)

from frappe.utils.dateutils import get_period

cur_user = frappe.session.user

def get_restriction_details():
	user = frappe.db.get_value(
		"Learner", frappe.session.user, "restrict_profile"
	)
	return user

def add_nav(context, title, href):
	"""Adds a breadcrumb to the navigation."""
	nav = context.setdefault("nav", [])
	nav.append({"title": title, "href": href})