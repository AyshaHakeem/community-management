import frappe
from frappe.utils import cstr
from frappe import _

no_cache = 1
no_sitemap = 1

def get_context(context):
	context.no_cache = 1
	context.quiz = frappe._dict()
	rq = {}
	questions = []
	if frappe.db.exists("Registration Question", {'event':frappe.form_dict["event"]}):
		rq = frappe.get_doc("Registration Question", {'event':frappe.form_dict["event"]})
	event_doc = frappe.get_doc("Event Custom", frappe.form_dict["event"])
	rq_title = rq.get('title') or ""
	rq_name = rq.get('name') or ""
	rq_max_atpms = rq.get('max_attempts') or ""
	if frappe.db.exists("Event Question", {'parent':rq.get('name')}):
		questions = frappe.db.get_all("Event Question", {'parent':rq.get('name')}, ['name','question', 'type'], order_by="idx")
	context.quiz = {
		"title":rq_title, 
		"name":rq_name, 
		'max_attempts':rq_max_atpms,
		"event_title":event_doc.title,
		"event_name":event_doc.name,
		'questions': questions
	}