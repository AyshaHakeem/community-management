# Copyright (c) 2023, D-codE and contributors
# For license information, please see license.txt

import frappe
import json
import ast
from frappe.model.document import Document


class EventRegistration(Document):
    
    def on_update(self):
        # Get the previous version of the document before the update
        learner = ''
        # Fetch existing skills and events of the learner
        if frappe.db.exists("Learner", self.email):
            learner = frappe.get_doc("Learner", self.email)
            existing_skills = [skill.skill for skill in learner.my_skills]
            existing_events = [event.event for event in learner.my_events]

            # Fetch skills from the event
            event = frappe.get_doc("Event Custom", self.event)
            event_skills = [skill.skill for skill in event.skills]
            
        
        old_doc = self.get_doc_before_save()
        if old_doc and learner:
            if old_doc.is_participant != self.is_participant:
                if self.is_participant:
                    if self.event not in existing_events:
                        learner.append('my_events', { 'event': self.event })
                else:
                    if self.event in existing_events:
                        for row in learner.my_events:
                            if row.event == self.event:
                                row.delete(ignore_permissions=True)

        # Handle changes in add_skill
            if old_doc.add_skill != self.add_skill:
                if self.add_skill:
                    for skill in event_skills:
                        if skill not in existing_skills:
                            learner.append('my_skills', { 'event': self.event, 'skill': skill })
                else:
                    for skill in event_skills:
                        for row in learner.my_skills:
                            if row.skill == skill:
                                row.delete(ignore_permissions=True)

        # Save the learner document and update skill_list
            learner.save(ignore_permissions=True)
            frappe.db.commit()
            learner.reload()
            learner_skills = [skill.skill for skill in learner.my_skills]
            skill_list = ', '.join(learner_skills)
            frappe.db.set_value("Learner", self.email, "skill_list", skill_list)  

            # Commit the changes to the database
            frappe.db.commit()
            

@frappe.whitelist(allow_guest=True)
def save_response(result, primary, event):
    prim =  ast.literal_eval(primary)
    result = json.loads(result)
    response = frappe.new_doc("Event Registration")

    response.event = event
    response.full_name = prim[0]
    response.email = prim[1]
    response.mobile_no = prim[2]
    for i in result:
        response.append('registration_quiz_answer',i)
    response.save(ignore_permissions=True)
    return response.name





    # def on_update(self):
    # 	existing_skills = []
    # 	old_doc = self.get_doc_before_save()
        
    # 	if frappe.db.exists("Learner", self.email):
    # 		learner = frappe.get_doc("Learner", self.email)
    # 		existing_skills = [skill.skill for skill in learner.my_skills]
    # 		existing_event = [event.event for event in learner.my_events]
    # 		#  skills from event
    # 		event = frappe.get_doc("TinkerHub Event", self.event)
    # 		event_skills = [skill.skill for skill in event.skills]

    # 	if old_doc.is_participant != self.is_participant:
    # 		if self.is_participant:
    # 			if not self.event in existing_event:
    # 				# learner.reload()
    # 				# learner_event=learner.append("my_events")
    # 				# learner_event.event= self.event
    # 				learner.append('my_events', { 'event': self.event})
    # 			# learner.save(ignore_permissions = True)
    # 		else:
    # 			if self.event in existing_event:
    # 				for row in learner.my_events:
    # 					if row.event == self.event:
    # 						# learner.reload() 
    # 						row.delete(ignore_permissions=True)
    # 	# learner.save(ignore_permissions = True)

    # 	if old_doc.add_skill != self.add_skill:
    # 		if self.add_skill:
    # 			for skill in event_skills:
    # 				if skill not in existing_skills:
    # 					# learner.reload()
    # 					learner.append('my_skills', { 'event': self.event ,'skill': skill})
    # 		else:
    # 			for skill in event_skills:
    # 				for row in learner.my_skills:
    # 					if row.skill == skill:
    # 						# learner.reload()
    # 						row.delete(ignore_permissions=True)
            
    # 		skills = frappe.get_all('My Skills', filters={'parent': learner }, fields=['skill'])
    # 		learner_skills = [skill['skill'] for skill in skills]
    # 		skill_list= ', '.join(learner_skills)
    # 		# learner.reload()
    # 		learner.save(ignore_permissions=True)
    # 		frappe.db.set_value("Learner", self.email, "skill_list", skill_list)  
        
    # 	frappe.db.commit()
            
    