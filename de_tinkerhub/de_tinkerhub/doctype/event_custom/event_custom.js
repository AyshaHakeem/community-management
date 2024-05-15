// Copyright (c) 2023, D-codE and contributors
// For license information, please see license.txt

frappe.ui.form.on('Event Custom', {
	// refresh: function(frm) {

	// } 
	starting_date: frm =>{
		frm.set_value("ending_date", frm.doc.starting_date)
		frm.refresh_field("ending_date")	
	}
});

