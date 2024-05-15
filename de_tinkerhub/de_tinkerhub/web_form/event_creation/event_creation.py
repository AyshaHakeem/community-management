import frappe
def get_context(context):
	context.no_cache = 1
	return context

@frappe.whitelist()
def check_admin():
	cur_user = frappe.session.user
	user_roles = frappe.get_roles()
	
	if 'Event Admin' not in user_roles: 
		return False
	else:
		college = frappe.db.get_value('Learner', cur_user, 'college')
		if college:
	
			events = frappe.db.get_list('Event Custom',
						filters = {
							'host_college': college
						},
						fields=['name','title', 'starting_date']
					)
			list = [event.name for event in events]
		else:
			events = frappe.db.get_list('Event Custom',
						filters = {
							'owner': cur_user
						},
						fields=['name','title', 'starting_date'])
			list = [event.name for event in events]
		return list
		

	
	

# def check_admin():
# 	cur_user = frappe.session.user
# 	user_roles = frappe.get_roles()
	
# 	if 'Event Admin' not in user_roles: 
# 		return False
# 	else:
# 		college = frappe.db.get_value('Learner', cur_user, 'college')
# 		if college:
# 			admins = frappe.db.get_list('Learner',
# 								filters={
# 									'college': college
# 								},
# 								fields=['email'],
# 								as_list=True 
# 								)
# 			college_admins = [admin[0] for admin in admins ]
			
# 			events = frappe.db.get_list('TinkerHub Event',
# 						filters = {
# 							'owner': ['in', college_admins]
# 						},
# 						fields=['name','title', 'starting_date']
# 					)
# 			list = [event.name for event in events]
# 		else:
# 			events = frappe.db.get_list('TinkerHub Event',
# 						filters = {
# 							'owner': cur_user
# 						},
# 						fields=['name','title', 'starting_date'])
# 			list = [event.name for event in events]
# 		return list
		