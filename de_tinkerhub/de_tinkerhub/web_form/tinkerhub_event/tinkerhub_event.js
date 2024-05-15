frappe.ready(function() {
	frappe.web_form.on('starting_date', ()=>{
		let date = frappe.web_form.get_value('starting_date');
		frappe.web_form.set_value('ending_date', date);
	});
})