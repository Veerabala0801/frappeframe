import frappe

class libapi():
    pass

@frappe.whitelist()
def insert_user(first_name,email):
    user = frappe.get_doc({
        "doctype":"User",
        "first_name":first_name,
        "email":email,
        "new_password":"Frappe@123",
        "role_profile_name":"RPQB",
        "user_type":"System User",
        "module_profile":"RPQB-Man"
        })
    user.insert(ignore_permissions=True)    
    frappe.db.commit()
   
    return f"The data for {first_name} inserted"
#thalapathi
# @frappe.whitelist()
# def user_role(module,role,url):
#    u_role = frappe.get_doc({"doctype":"User","module_profile":module,"role_profile_name":role,"redirect_url":url})
#    u_role.update(ignore_permissions=True)
#    frappe.db.commit()
#    return "Value Insterted"
#  user_ins = frappe.db.sql(""" update `tabUser` set  role_profile_name = {} ,redirect_url = {} where email = {}""".format(role,url,email))
#     user_ins.insert(ignore_permissions=True)
#     frappe.db.commit()
@frappe.whitelist()
def user_module(role):
    roles= frappe.get_doc({"doctype":"User","":role})
    roles.insert(ignore_permissions=True)
    frappe.db.commit()
    return "success"