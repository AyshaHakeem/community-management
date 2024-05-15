# Copyright (c) 2023, D-codE and contributors
# For license information, please see license.txt
import json
import frappe
from frappe.utils import cstr
from frappe.model.document import Document

class RegistrationQuestion(Document):
	pass

@frappe.whitelist()
def save_quiz(
	title, event, quiz=None
):
	values = {
		"title": title,
		"event":event
	}

	if quiz:
		frappe.db.set_value("Registration Question", quiz, values)
		return quiz
	else:
		doc = frappe.new_doc("Registration Question")
		doc.update(values)
		doc.save(ignore_permissions=True)
		return {doc.name}
	
@frappe.whitelist()
def save_question(quiz, values, index):
	values = frappe._dict(json.loads(values))

	if values.get("name"):
		doc = frappe.get_doc("Event Question", values.get("name"))
	else:
		doc = frappe.new_doc("Event Question")

	doc.update(
		{
			"question": values["question"],
			"type": values["type"],
		}
	)

	if not values.get("name"):
		doc.update(
			{
				"parent": quiz,
				"parenttype": "Registration Question",
				"parentfield": "questions",
				"idx": index,
			}
		)

	for num in range(1, 5):
		if values.get(f"option_{num}"):
			doc.update(
				{
					f"option_{num}": values[f"option_{num}"],
					# f"is_correct_{num}": values[f"is_correct_{num}"],
				}
			)

		if values.get(f"user_input_{num}"):
			doc.update(
				{
					f"user_input_{num}": values[f"user_input_{num}"],
				}
			)

		if values.get(f"multi_answer_{num}"):
			doc.update(
				{
					f"multi_answer_{num}": values[f"multi_answer_{num}"],
				}
			)

		doc.save(ignore_permissions=True)

	return quiz

@frappe.whitelist()
def get_question_details(question):
	if frappe.db.exists("Event Question", question):
		fields = ["name", "question", "type"]
		for num in range(1, 5):
			fields.append(f"option_{cstr(num)}")
			fields.append(f"user_input_{cstr(num)}")
			fields.append(f"multi_answer_{cstr(num)}")

		return frappe.db.get_value("Event Question", question, fields, as_dict=1)
	return