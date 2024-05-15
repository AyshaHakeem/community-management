import frappe

def send_registration_email(doc, method):
    
    learner = frappe.get_doc("Learner", doc.learner)
    email = doc.email
    subject = "Welcome to the event!"
    message = "Dear learner, thank you for registering for the event."
    
    frappe.sendmail(recipients=email, subject=subject, message=message)

