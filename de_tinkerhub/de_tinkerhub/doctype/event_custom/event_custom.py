# Copyright (c) 2023, D-codE and contributors
# For license information, please see license.txt

import frappe 
from frappe.website.website_generator import WebsiteGenerator
from frappe.website.utils import cleanup_page_name
from frappe import get_doc
from datetime import datetime

class EventCustom(WebsiteGenerator):

	def after_insert(self):
		if frappe.db.get_value('Learner', self.owner, 'college'):
			
			college = frappe.db.get_value('Learner', self.owner, 'college')
			if not self.host_college:
				self.host_college = college

			try:
				event_reference = frappe.get_doc(
				{
					"doctype": "College Event Reference",
					"college_event": self.name,
					"parent": college,
					"parenttype": "College",
					"parentfield": "college_events"
				}
				)
				event_reference.save(ignore_permissions=True)
				frappe.db.commit()
				
			except Exception as e:
				frappe.throw(('An error occurred while adding college reference'))
		else:
			pass

	def validate(self):
		# web view route
		if not self.route:
			self.route = f"events/{self.name}"

	
	def get_context(self, context):
		context.has_custom = False
		user_roles = frappe.get_roles()
		cur_user = frappe.session.user
		participant = False
		registrant = False
		cur_event = self.name

		if 'Event Admin' in user_roles:
			context.event_admin = True
		else:
			context.event_admin = False

		if cur_user == 'Guest':
			is_admin = False
			is_learner = False
			is_guest = True
		elif cur_user == 'Administrator':
			is_admin = True
			is_learner = False
			is_guest = False
		elif 'Learner' in user_roles:
			is_admin = False
			is_learner = True
			is_guest = False

		if is_learner:
			if frappe.db.exists("Learner", cur_user):
				learner = frappe.get_doc("Learner", cur_user)
				user_events = [event.event for event in learner.my_events]
				if cur_event in user_events:
					participant = True
				if frappe.db.exists(
					'Event Registration', 
					{'event': f'{self.name}', 'email': cur_user}):
					registrant = True
			else:
				participant = False
				registrant: False
		
		if frappe.db.exists('Registration Question', {'event': self.name}):
			context.has_custom = True
		# doc = get_doc('Event Registration', {'event': frappe.form_dict["event"], 
        #                                'email': frappe.session.user})
		
		# if doc.
        
		
		
		# convert time to 12 hour format
		event_time = [self.starting_time, self.ending_time]
		# for index, time in enumerate(event_time):
		# 	if time:
		# 		time_obj = datetime.strptime(str(time), "%H:%M:%S")
		# 		context[f"event_time_{index}"]  = time_obj.strftime("%I:%M %p")

		context.participant = participant
		context.registrant = registrant
		context.is_guest = is_guest
		context.is_learner = is_learner
		context.is_admin = is_admin
		context.show_sidebar=1
		context.no_cache = 1

		return context


	
	# def on_update(self):

		# event_registrations = frappe.get_all("Event Registration", filters={"event": self.name})
		# for event_registration in event_registrations:
		# 	registration_doc = frappe.get_doc("Event Registration", event_registration.name)
		# 	existing_skills = [skill.skill for skill in registration_doc.skills_gained]
			
		# 	for skill in self.skills:
		# 		if skill.skill not in existing_skills:
		# 			registration_doc.append("skills_gained", {
		# 				"skill": skill.skill
		# 			})
		# 	registration_doc.save()


