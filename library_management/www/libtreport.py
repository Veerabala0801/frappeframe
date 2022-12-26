import frappe 

def get_context(context):
    items = frappe.db.sql(""" SELECT article,full_name,type FROM `tabLibrary Transaction`;""",as_dict=True)
    context.items = items
    return context


@frappe.whitelist()
def add_user(first_name,email,paid):
    user = frappe.get_doc({
        "doctype":"library_member",
        "first_name":first_name,
        "email":email,
        "paid":paid
        }
    )