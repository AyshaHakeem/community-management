import frappe

def send_event_update_email(doc, method):
    event_name = doc.name
    registrations = frappe.get_all(
        "Event Registration",
        filters={"event": event_name},
        fields=["email"]
    )
    subject = "Event Update: {}".format(event_name)
    message = "Dear learner, the event '{}' has been updated.".format(event_name)
    
    for registration in registrations:
        if frappe.db.exists('Learner', registration.email):
            learner = frappe.get_doc("Learner", registration.email)
            email = learner.email
            # frappe.sendmail(recipients=email, subject=subject, message=message)
