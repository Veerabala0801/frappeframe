# Copyright (c) 2022, veerabala and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.utils import validate_email_address

class LibraryMember(Document):

	def validate(self):
		self.before_save()
		self.email_validation()

	def before_save(self):
			if self.f_name:
				self.full_name = " ".join([self.f_name,self.l_name])

	def email_validation(self):
		if self.email:
				validate_email_address(self.email, throw=True)#if its true it pass invalid email message
		else:
			pass
