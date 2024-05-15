import frappe
import ast
from frappe import get_doc

@frappe.whitelist(allow_guest=True)
def event_registration(event, email, full_name, mobile_no):
    if frappe.db.exists("Event Registration", {"event": event, "email": email}):
        return frappe.msgprint(
            msg='You are already registered',
            title='Notification'
        )
    else:
        registration = get_doc({
            "doctype": "Event Registration",
            "event":  event,
            "email": email,
            "full_name": full_name,
            "mobile_no": mobile_no
        })

        registration.save(ignore_permissions = True)
        # frappe.msgprint(
        #     msg='Thank you for registering!',
        #     title='Success'
        # )

        # frappe.local.response['type'] = 'redirect'
        # frappe.local.response['location'] = '/upcoming-events'

@frappe.whitelist(allow_guest=True)
def submit_feedback(event, learner, question, response):

    feedback = get_doc({
        "doctype": "Feedback Submission",
        "event": event,
        "learner": learner,
        "question": question,
        "user_response": response
    })

    feedback.insert(ignore_permissions = True).save()
    # frappe.db.commit()
    frappe.msgprint(
        msg='Thank you for your feedback!',
        title='Success'
    )

@frappe.whitelist(allow_guest=True)
def submit_assignment(event, learner, question, response):

    assignment = get_doc({
        "doctype": "Assignment Submission",
        "event": event,
        "learner": learner,
        "question": question,
        "user_response": response
    })

    assignment.insert(ignore_permissions = True).save()
    # frappe.db.commit()
    frappe.msgprint(
        msg='Your assignment has been submitted.',
        title='Success'
    )

@frappe.whitelist(allow_guest=True)
def part(event, registrants, participants, skilledParticipants):
    registrations = ast.literal_eval(registrants)
    participant = ast.literal_eval(participants)
    skilled_participants = ast.literal_eval(skilledParticipants)

    try:
    # Loop through the selected emails and edit/create records in 'Event Participant' doctype
        for email in registrations:
            event_participant = get_doc('Event Registration', {'event': event, 'email': email}).name
            if email in participant:
                edit_doc(event_participant, 1)
            else:
                edit_doc(event_participant, 0)

            if email in skilled_participants:
                edit_skill(event_participant, 1)
            else:
                edit_skill(event_participant, 0)

        return ('Success')


    except Exception as e:
        frappe.throw(('An error occurred while editing/creating event participants. Please try again or contact support.'))

@frappe.whitelist(allow_guest=True)
def edit_doc(docname, field_value):
    doc = get_doc('Event Registration', docname)
    doc.reload()
    doc.is_participant = field_value
    doc.save(ignore_permissions=True)
    frappe.db.commit()

@frappe.whitelist(allow_guest=True)
def edit_skill(docname, field_value):
    doc = get_doc('Event Registration', docname)
    doc.reload()
    doc.add_skill = field_value
    doc.save(ignore_permissions=True)
    frappe.db.commit()


