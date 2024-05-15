frappe.ready(() => {
	$(".btn-save-quiz").click((e) => {
		validate_mandatory();
		save_quiz({
			quiz_title: $("#quiz-title").val()
		});
	});

	$(".question-row").click((e) => {
		edit_question(e);
	});

	$(".btn-add-question").click((e) => {
		show_question_modal();
	});
});

const show_question_modal = (values = {}) => {
	let fields = get_question_fields(values);
	this.question_dialog = new frappe.ui.Dialog({
		title: __("Add Question"),
		fields: fields,
		primary_action: (data) => {
			if (values) data.name = values.name;
			save_question(data);
		},
	});

	question_dialog.show();
};

const get_question_fields = (values = {}) => {
	let dialog_fields = [
		{
			fieldtype: "Small Text",
			fieldname: "question",
			label: __("Question"),
			reqd: 1,
			default: values.question || "",
		},
		{
			fieldtype: "Select",
			fieldname: "type",
			label: __("Type"),
			options: ["Choices", "User Input", "Multiple Answers"],
			default: values.type || "Choices",
		},
	];
	Array.from({ length: 4 }, (x, i) => {
		num = i + 1;

		dialog_fields.push({
			fieldtype: "Section Break",
			fieldname: `section_break_${num}`,
		});

		let option = {
			fieldtype: "Small Text",
			fieldname: `option_${num}`,
			label: __("Option") + ` ${num}`,
			depends_on: "eval:doc.type=='Choices'",
			default: values[`option_${num}`] || "",
		};

		if (num <= 2) option.mandatory_depends_on = "eval:doc.type=='Choices'";

		dialog_fields.push(option);

		possibility = {
			fieldtype: "Small Text",
			fieldname: `user_input_${num}`,
			label: __("Possible Answer") + ` ${num}`,
			depends_on: "eval:doc.type=='User Input'",
			default: values[`user_input_${num}`] || "",
		};

		// if (num == 1)
		// 	possibility.mandatory_depends_on = "eval:doc.type=='User Input'";

		// dialog_fields.push(possibility);

		multi_answer = {
			fieldtype:"Small Text",
			fieldname:`multi_answer_${num}`,
			label:__("Option ") + `${num}`,
			depends_on: "eval:doc.type=='Multiple Answers'",
			default: values[`multi_answer_${num}`] || "",
		}
		if (num <= 2) 
			multi_answer.mandatory_depends_on = "eval:doc.type=='Multiple Answers'";
		
		dialog_fields.push(multi_answer)
		
	});
	return dialog_fields;
};

const save_quiz = (values) => {
	frappe.call({
		method: "de_tinkerhub.de_tinkerhub.doctype.registration_question.registration_question.save_quiz",
		args: {
			title: values.quiz_title,
			event: $("#quiz-form").data("event") || "",
			quiz: $("#quiz-form").data("name") || "",
		},
		callback: (data) => {
			frappe.show_alert({
				message: __("Saved"),
				indicator: "green",
			});
			setTimeout(() => {
				window.location.href = `/registration-quiz?event=${$("#quiz-form").data("event")}`;
			}, 2000);
		},
	});
};

const validate_mandatory = () => {
	if (!$("#quiz-title").val()) {
		frappe.show_alert({
			message: __("Title is mandatory"),
			indicator: "red",
		});
	}
};

const save_question = (values) => {
	frappe.call({
		method: "de_tinkerhub.de_tinkerhub.doctype.registration_question.registration_question.save_question",
		args: {
			quiz: $("#quiz-form").data("name") || "",
			values: values,
			index: $("#quiz-form").data("index") + 1,
		},
		callback: (data) => {
			if (data.message) this.question_dialog.hide();

			frappe.show_alert({
				message: __("Saved"),
				indicator: "green",
			});
			setTimeout(() => {
				window.location.reload();
			}, 1000);
		},
	});
};

const edit_question = (e) => {
	let question = $(e.currentTarget).data("question");
	frappe.call({
		method: "de_tinkerhub.de_tinkerhub.doctype.registration_question.registration_question.get_question_details",
		args: {
			question: question,
		},
		callback: (data) => {
			if (data.message) show_question_modal(data.message);
		},
	});
};