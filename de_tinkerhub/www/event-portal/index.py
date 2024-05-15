import frappe
from frappe import get_doc
import urllib.parse
def get_context(context):

    user_roles = frappe.get_roles()
    if 'Event Admin' in user_roles:
        context.event_admin = True
    else:
        context.event_admin = False

    event_id = frappe.form_dict.name
    event  = get_doc('Event Custom', event_id)

    registrants = frappe.db.get_list(
        'Event Registration', 
        filters={
            'event': event_id
        },
        fields=['name', 'email', 'is_participant', 'add_skill'],
        order_by = 'is_participant DESC'
    )

    learner = []
    guests = []
    final_array = []
    

    if registrants:
        for submission in registrants:
            user_array = []
        # Access the child table field
            user_array = [submission.email, {}]

            # context.has_custom = True

            rq = frappe.db.get_value('Event Registration', {'event':frappe.form_dict.name, 'email': submission.email}, ['name'])
            fields = ["name", "question", "answer_1"]
            qa = frappe.db.get_list("Registration Quiz Answer", {'parent':rq}, fields, ignore_permissions=True, order_by="idx")
            
            # rows = submission.registration_quiz_answer

            # Loop through child table rows
            if qa:
                for q in qa:
                    question = q.question
                    # answer = urllib.parse.unquote(q.answer_1)
                    answer = q.answer_1
                    user_array[1][f'{question}'] = f'{answer}'
            final_array.append(user_array)

    context.qa = final_array
            
    
    parents = [parent.name for parent in registrants]

    context.child_table_data = frappe.db.get_all(
        'Registration Quiz Answer',
        filters={'parent': ['in', parents]},  
        fields=['question', 'answer_1'],  
        order_by='idx'  
    )
    if frappe.db.exists("Registration Question", {'event':frappe.form_dict.name}):
            # context.has_custom = True
            rq = frappe.get_doc("Registration Question", {'event':frappe.form_dict.name})
            fields = ["name", "question", "type"]
            context.questions = frappe.db.get_list("Event Question", {'parent':rq.name}, fields, ignore_permissions=True, order_by="idx")

    
    for registrant in  registrants:
        if frappe.db.exists('Learner', registrant.email):
            learner.append(registrant.email)
        else:
            guests.append(registrant.email)
    
    
    context.event = event
    context.registrants = registrants
    # context.learner = learner
    # context.guests = guests
    context.show_sidebar = 1
    context.no_cache = 1
    return context