import frappe
import datetime

no_cache = 1
no_sitemap = 1

from de_tinkerhub.de_tinkerhub.utils import (
	get_restriction_details
)

def get_context(context):

    user_roles = frappe.get_roles()
    if 'Event Admin' in user_roles:
        context.event_admin = True
    else:
        context.event_admin = False

    context.show_sidebar = 1

    cur_user = frappe.session.user

    if cur_user=="Guest":
        frappe.throw( ("You have to login as a member access this page"), frappe.PermissionError)
    else:
        # participated events
        learner = frappe.get_doc("Learner", cur_user)
        events = [event.event for event in learner.my_events]

        context.past_events = frappe.db.get_list('Event Custom',
                                    filters={
                                        'name': ['in', events]
                                    },
                                    fields=['name','title', 'starting_date'])
        # registered events
        registered_event_ids = frappe.db.get_all(
            'Event Registration',
            filters={
                'email': cur_user
            },
            fields=['event'],
            as_list=True 
        )

        today = datetime.date.today()
        event_ids = [event[0] for event in registered_event_ids]

        context.restriction = get_restriction_details()

        context.registered_events = frappe.db.get_list('Event Custom',
                                    filters={
                                        'name': ['in', event_ids],
                                        'starting_date':  [">=", today],
                                        'status': ['!=', 'Completed']
                                    },
                                    fields=['name','title', 'starting_date'])
        
    return context

