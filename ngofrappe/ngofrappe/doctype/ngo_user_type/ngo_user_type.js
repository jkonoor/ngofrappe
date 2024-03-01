// Copyright (c) 2024, Innogenio and contributors
// For license information, please see license.txt

frappe.ui.form.on("NGO User Type", {
	refresh(frm) {
        if (!frm.is_new()) {
            frm.set_df_property('center', 'read_only', 1);
           
        }

	},
});
