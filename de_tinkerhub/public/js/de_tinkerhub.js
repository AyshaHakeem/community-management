let show_form = () => {

    let fields = registration_fields()
    let question_dialog = new frappe.ui.Dialog({
        title: "Event Registration",
        fields: fields,
        primary_action: data => {
            event_registration(data)  
            question_dialog.hide()
        }
    });

    question_dialog.show();
};

let feedback_dialog = (question) => {

    let fields = [{
            label: question,
            fieldname: 'response',
            fieldtype: 'Small Text'
        }]
    let feedback_dialog = new frappe.ui.Dialog({
        title: "Event Feedback",
        fields: fields,
        primary_action: data => {
            submit_feedback(data, question)  
            feedback_dialog.hide()
        }
    });

    feedback_dialog.show();
};

let assignment_dialog = (question) => {

    let fields = [{
            label: question,
            fieldname: 'response',
            fieldtype: 'Data'
        }]
    let feedback_dialog = new frappe.ui.Dialog({
        title: "Assignment Submission",
        fields: fields,
        primary_action: data => {
            submit_assignment(data, question)  
            feedback_dialog.hide()
        }
    });

    feedback_dialog.show();
};

let event_registration = (data) => {
    let url = window.location.href,
        event = url.split('/')[4]
    frappe.call({
        method: 'de_tinkerhub.services.rest.event_registration',
        args: {
            'event': event,
            'email' : data.email,
            'full_name': data.full_name,
            'mobile_no': data.contact
        },
        callback: r => {
            
        }
    })
}

submit_assignment = (data, question) => {
    let url = window.location.href,
    event = url.split('/')[4]

    frappe.call({
    method: 'de_tinkerhub.services.rest.submit_assignment',
    args: {
        'event': event,
        'learner': frappe.session.user,
        'question': question,
        'response': data.response
    },
    callback: r => {
    }
})
}

submit_feedback = (data, question) => {
    let url = window.location.href,
    event = url.split('/')[4]

    frappe.call({
    method: 'de_tinkerhub.services.rest.submit_feedback',
    args: {
        'event': event,
        'learner': frappe.session.user,
        'question': question,
        'response': data.response
    },
    callback: r => {
    }
})
}

// dialog fields
const registration_fields = () => {
    let full_name, email
    if(frappe.session.user != "Guest"){
        full_name = frappe.full_name
        email = frappe.session.user
    }

	let dialog_fields = [
        {
            label: 'Full Name',
            fieldname: 'full_name',
            fieldtype: 'Data',
            reqd: 1,
            default: full_name || ""
        },
        {
            label: 'Email',
            fieldname: 'email',
            fieldtype: 'Data',
            reqd: 1,
            default: email || ""
        },
        {
            label: 'Contact Number',
            fieldname: 'contact',
            fieldtype: 'Data',
            reqd: 1
        }
    ]

    if (full_name && email) {
        dialog_fields[0].read_only = 1
        dialog_fields[1].read_only = 1
    }

	return dialog_fields;
};

const feedback_fields = (q) => {
    let url = window.location.href,
        event = url.split('/')[4]
	let dialog_fields = [
        {
            label: q,
            fieldname: 'response',
            fieldtype: 'Small Text'
        }
    ]
	return dialog_fields;
};