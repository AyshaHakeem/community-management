# Copyright (c) 2023, D-codE and contributors
# For license information, please see license.txt

import frappe
from frappe import get_doc
from frappe.website.website_generator import WebsiteGenerator

class Learner(WebsiteGenerator):
	def autoname(self):
		self.name= self.user

	def validate(self):
		if not self.route:
			self.route = f'learner/{self.name}'

	def after_insert(self):
		if not frappe.db.exists( 
			"User Permission", 
			{ 
				"user": self.name, 
				"allow": 'Learner', 
				"for_value": self.name
			}):
			permission = get_doc({
                            'doctype': 'User Permission',
                            'user': self.name, 
                            'allow': 'Learner', 
                            'for_value': self.name
                        })
			permission.insert(ignore_permissions=True)
			frappe.db.commit()
	
	def get_context(self, context):
		if self.college:
			college = frappe.db.get_value('college', self.college, 'college_name')
			context.college= college
			return context

				
                        
        
