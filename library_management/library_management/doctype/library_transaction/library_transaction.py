# Copyright (c) 2022, veerabala and contributors
# For license information, please see license.txt

# from re import template
import frappe
# import jinja2
from jinja2 import Environment,PackageLoader,select_autoescape
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class LibraryTransaction(Document):

	def validate(self):
		self.before_submit()
		self.validate_maximum_limit()
		self.validate_membership()
		# self.html_tabvalue()
	
	# def html_tabvalue(self):
	# 	env=jinja2.Environment()
	# 	data1 = frappe.db.sql(""" SELECT article,full_name,type FROM `tabLibrary Transaction`""")
	# 	data = list(data1)
	# 	template = env.get_template("article_report.html")
	# 	template.render(data)

	def before_submit(self):
		
		if self.type == "Issue":
			article = frappe.get_doc("Article",self.article)
			if article.stocks == 0:
					frappe.throw("out of stocks")		
			article.stocks -= 1
			article.save()
			if article.stocks == 0:
				article.status = "Issued"
				article.save()
					
		elif self.type == "Return":
			article=frappe.get_doc("Article",self.article)
			article.stocks += 1
			article.status = "Available"
			article.save()
	
	def validate_maximum_limit(self):	
			max_articles = frappe.db.get_single_value("Library Settings", "max_articles")
			count = frappe.db.count("Library Transaction",{"library_member":self.full_name,"type": "Issue",	 "docstatus": DocStatus.submitted()},)
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



