# Copyright (c) 2022, veerabala and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
#email validation
#from email_validator import validate_email, EmailNotValidError
from frappe.utils import comma_and, get_link_to_form, has_gravatar, validate_email_address
import re
class Visitors(Document):
		
	#for fill the fullname form first and last name
	def validate(self):
		#self.fullname_validation()
		self.email_validation()
		self.pincode_validation()
		self.before_insert()


#   def fullname_validation(self):
	#		if self.f_name:
	#			self.full_name = " ".join([self.f_name,self.l_name])
	def before_insert(self):
			if self.f_name:
				self.full_name = " ".join([self.f_name,self.l_name])
	       

	def email_validation(self):
		if self.email:
				validate_email_address(self.email, throw=True)#if its true it pass invalid email message
		else:
			pass
			
	def pincode_validation(self):
		
		self.pinstring = str(self.pincode)
		
		regex = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$"

	# ^ represents the starting of the number.
    # [1-9]{1} represents the starting digit in the pin code ranging from 1 to 9.
    # [0-9]{2} represents the next two digits in the pin code ranging from 0 to 9.
    # \\s{0, 1} represents the white space in the pin code that can occur once or never.
    # [0-9]{3} represents the last three digits in the pin code ranging from 0 to 9.
    # $ represents the ending of the number.

		self.pattern=re.compile(regex)

		if (self.pinstring==" "):
			frappe.throw('Pincode is Empty')#this show error message if condition is not met
		self.m_pattern=re.match(self.pattern,self.pinstring)

		if self.m_pattern is None:
			frappe.throw('Invalid Pincode')
		else:
			self.pincode=self.pincode
