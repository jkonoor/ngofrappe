# Copyright (c) 2024, Innogenio and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class CentreUsers(Document):
    def before_insert(self):
        # This method will be called when the custom form is submitted
        self.create_or_update_user()
        # self.assign_roles_to_user()
        # self.link_user_to_centre()

    def create_or_update_user(self):
        email = self.email  # Assuming 'email' is a field in your custom form
        first_name = (
            self.first_name
        )  # Assuming 'first_name' is a field in your custom form
        last_name = (
            self.last_name
        )  # Assuming 'last_name' is a field in your custom form
        password = self.password
        role = self.role
        if not frappe.db.exists("User", email):
            # Create a new user if it does not exist
            user = frappe.new_doc("User")
            user.email = email
            user.name = email
            user.first_name = first_name
            user.last_name = last_name
            user.new_password = password
            user.enabled = 1
            user.append("roles", {"role": role})

            user.insert()

        else:
            # Update existing user
            user = frappe.get_doc("User", email)
            user.first_name = first_name
            user.last_name = last_name
            user.new_password = password
            user.save()

        frappe.db.commit()  # Ensure changes are committed to the database

    def assign_roles_to_user(self):
        email = self.email

        user = frappe.get_doc("User", email)

        # Clear existing roles
        user.roles = []
        user.append("roles", {"role": role})

        user.save()
        frappe.db.commit()

    def link_user_to_centre(self):
        email = self.email
        centre = self.centre  # Assuming 'centre' is a field in your custom form

        # Assuming there's a Centre Doctype and you want to store the link in User Properties
        frappe.db.set_value("User", email, "centre", centre)
        frappe.db.commit()
