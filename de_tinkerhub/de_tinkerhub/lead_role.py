import frappe
from frappe import get_doc

def on_lead_role(self, method):
    user_id = self.name

    if not frappe.db.exists( "Learner", {"email": user_id}):
        learner = get_doc({
            "doctype": "Learner",
            "user": user_id,
            "email": user_id,
            "is_published": 1
        })
        learner.insert(ignore_permissions=True)
        # add learner role
        doc = frappe.get_doc(
			{
				"doctype": "Has Role",
				"parent": user_id,
				"role": 'Learner',
				"parenttype": "User",
				"parentfield": "roles",
			}
		)
        doc.save(ignore_permissions=True)

    # check for campus lead role
    old_doc = self.get_doc_before_save()

    if old_doc:

        if old_doc.roles != self.roles :
            roles = frappe.get_all(
                'Has Role',
                filters={'parent': self.name},
                fields=['role']
            )
            cur_roles = [item['role'] for item in roles]
            college = frappe.db.get_value('Learner', self.name, 'college')
            if 'Campus Lead' in cur_roles and not frappe.db.exists('User Permission', {'user': self.name, 'allow': 'College', 'for_value': college}):
                if college:
                    permission = get_doc({
                        'doctype': 'User Permission',
                        'user': self.name, 
                        'allow': 'College', 
                        'for_value': college
                    })
                    permission.insert(ignore_permissions=True)
                    frappe.db.delete("User Permission", {
                        'user': self.name, 
                        'allow': 'Learner', 
                        'for_value': self.name
                    })
                    frappe.db.commit()
                        
                else:
                    frappe.db.delete("User Permission", {
                        'user': self.name, 
                        'allow': 'College', 
                        'for_value': college
                    })
                    if not frappe.db.exists( "User Permission", { "user": user_id, "allow": 'Learner', "for_value": self.email}):
                        permission = get_doc({
                            'doctype': 'User Permission',
                            'user': self.name, 
                            'allow': 'Learner', 
                            'for_value': self.name
                        })
                        permission.insert(ignore_permissions=True)
                    frappe.db.commit()

                    
            

