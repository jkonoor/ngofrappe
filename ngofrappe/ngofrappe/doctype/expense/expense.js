// Copyright (c) 2024, Innogenio and contributors
// For license information, please see license.txt

frappe.ui.form.on("Expense", {
	refresh(frm) {
        let btn = frm.add_custom_button(__('Validate Expense'), function(){
			// Perform desired action such as routing to a new form or fetching etc.
		}); 

        btn.css({'background-color': '#3498db', 'color': '#ffffff'});

	},
});
