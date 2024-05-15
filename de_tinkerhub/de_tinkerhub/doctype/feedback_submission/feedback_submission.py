# Copyright (c) 2023, D-codE and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class FeedbackSubmission(Document):
	pass


@frappe.whitelist(allow_guest=True)
def check(user):
	events = frappe.db.get_list('Event Custom',
						filters={
							'owner':  user
						},
						fields=['name'])