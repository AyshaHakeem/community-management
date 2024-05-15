# Copyright (c) 2023, D-codE and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class EventParticipant(Document):
    pass
	# def on_update(self):
	# 	if frappe.db.exists('Learner', self.learner_email):
	# 		learner = frappe.get_doc("Learner", self.learner_email)
	# 		existing_event = [event.event for event in learner.my_events]

	# 		if not self.event_id in existing_event:
	# 			learner_event=learner.append("my_events")
	# 			learner_event.event= self.event_id
	# 		learner.save(ignore_permissions = True)
