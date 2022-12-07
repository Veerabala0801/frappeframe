# Copyright (c) 2022, veerabala and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class LibraryTransaction(Document):

	def validate(self):
		self.before_submit()
		self.validate_maximum_limit()
		self.validate_membership()
		self.available_stocks()
		
	def before_submit(self):
		
		if self.type == "Issue":  
			#self.validate_issue()
			article = frappe.get_doc("Article",self.article)
			if article.status == "Issued":
				frappe.throw("Article is issued to other mem")
			
			#set the article status to be Issued
			else:
				article.status = "Issued"
				article.save()
					
		elif self.type == "Return":
			#self.validate_return()
			article=frappe.get_doc("Article",self.article)
			article.status = "Available"
			article.save()
	
	def validate_maximum_limit(self):	
			max_articles = frappe.db.get_single_value("Library Settings", "max_articles")
			count = frappe.db.count(
			"Library Transaction",{"library_member":self.full_name,"type": "Issue", "docstatus": DocStatus.submitted()},)
			if count >= max_articles:
				frappe.throw("maximum limit reached for issuing article")
					# a member can have maximum 3 books
		
	def validate_membership(self):

		full_name = frappe.db.exists(			
			"Library Membership",
			{
				"full_name":self.full_name,
				"docstatus":DocStatus.submitted(),
				"from_date":("<",self.date),
				"to_date":(">",self.date),
			},
		)

		if full_name:
			frappe.throw("The member is not a valid member")

	      
            