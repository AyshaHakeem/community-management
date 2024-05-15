import frappe
from frappe import _
from frappe import get_doc 

no_cache = 1
no_sitemap = 1

def get_context(context):
    user_roles = frappe.get_roles()
    context.no_cache = 1
    # if frappe.session.user == "Guest":
    #     message = "Please login to access this page."
    #     raise frappe.PermissionError(_(message))
    
    context.duplication = False
    if frappe.db.exists("Learner", {"email":frappe.session.user}):
        if frappe.db.exists("Event Registration", {'email':frappe.session.user,
                                                   'event':frappe.form_dict["event"]}):
            context.duplication = True


    # if 'Learner' in user_roles:
    #     doc = get_doc('Event Registration', {'event': frappe.form_dict["event"], 
    #                                    'email': frappe.session.user})
    #     if doc.registration_quiz_answer:
    #         context.duplication = True
    #     else:
    #         context.duplication = False
        
    context.has_custom = False
    if frappe.form_dict.get("event"):
        # event = frappe.form_dict["event"]
        event = frappe.get_doc("Event Custom", frappe.form_dict["event"])
        rq = None
        if frappe.db.exists("Registration Question", {'event':frappe.form_dict["event"]}):
            context.has_custom = True
            rq = frappe.get_doc("Registration Question", {'event':frappe.form_dict["event"]})
            fields = ["name", "question", "type", "option_1", "option_2", "option_3", "option_4",
                    "multi_answer_1",  "multi_answer_2",  "multi_answer_3",  "multi_answer_4"]
            questions = frappe.db.get_list("Event Question", {'parent':rq.name}, fields, ignore_permissions=True, order_by="idx")

            context.show_question = True
            context.quiz = {
                "title": event.title,
                "name":rq.name,
                "event_name":frappe.form_dict["event"],
                "questions": questions or None
            }

        else:
            context.quiz = {}


    if frappe.session.user != "Guest":
        context.is_learner = True
        user = frappe.get_user().doc
        context.full_name = user.full_name
        context.email = user.email

    # context.full_name = full_name or ''
    # context.email = email or ''
    
    context.no_cache = 1
    return context