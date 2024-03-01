// Copyright (c) 2024, Innogenio and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Program Users", {
//     onload: function(frm) {
//         frm.call({
//             doc: frm.doc,
//             method: 'get_program_user_roles',
//             callback: function(response) {
//                 var options = response.message;
//                 frm.set_df_property('role', 'options', options);
//             }
//         });
//     }
// });

frappe.ui.form.on('Program Users', {
    refresh(frm) {
        frm.set_query('role', function() {
            return {
                filters: [
                    
                    ['Role', 'name', 'in', ['Helper', 'Coordinator', 'Administrator']]
                ]
            };
        });
    }
});