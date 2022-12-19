import frappe 

def get_context(context):
    items = frappe.db.sql(""" SELECT article,full_name,type FROM `tabLibrary Transaction`;""",as_dict=True)
    context.items = items
    return context