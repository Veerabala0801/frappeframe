# Copyright (c) 2022, veerabala and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class LibraryMembership(Document):
	#check before submitting the document
	def before_submit(self):
		exists = frappe.db.exists(
			"Library Membership",
			{
				"library_memberss":self.library_memberss,
				"docstatus":DocStatus.submitted(),
				#check membership end date is later than membership start state
				"to_date":(">",self.from_date),
			},
		)
		if exists:
			frappe.throw("there is an active membership for this member")
		loan_period = frappe.db.get_single_value("Library Settings", "loan_period")
		self.to_date = frappe.utils.add_days(self.from_date, loan_period or 30)