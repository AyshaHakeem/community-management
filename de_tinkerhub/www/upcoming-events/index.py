import frappe
import datetime

no_cache = 1
no_sitemap = 1

from de_tinkerhub.de_tinkerhub.utils import (
	get_restriction_details,
    add_nav
)


def get_context(context):
    events = []

    user_roles = frappe.get_roles()
    if 'Event Admin' in user_roles:
        context.event_admin = True
    else:
        context.event_admin = False

    restriction = get_restriction_details()
    context.restriction = restriction

    events = frappe.db.sql(f"""
    SELECT te.name, te.starting_date, te.title, te.host_college, te.route
    FROM `tabEvent Custom` as te
    WHERE 
        starting_date >= CURDATE() AND
        status = 'Confirmed' AND
        is_published = 1 AND
        (public_event = 1 OR host_college IN (
            SELECT college FROM `tabLearner` WHERE name = '{frappe.session.user}'
        ));

    """, as_dict=True)



    # if query:
    #     events = frappe.db.get_list(
	# 		'Event Custom',
	# 		filters = {
	# 			'name': ['in', query]
	# 		},
	# 		fields = ['name','starting_date', 'title', 'host_college', 'route']
    # 	)

    context.events = events
    context.show_sidebar = 1
    context.no_cache = 1
    return context

