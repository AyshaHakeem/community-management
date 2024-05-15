import frappe
from frappe import get_doc, get_all, delete_doc, start_transaction, commit, rollback

import random

def on_target():
    return frappe.session.user

def on_user_signup(doc, method):
    pass