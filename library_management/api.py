import frappe

class libapi():
    pass

@frappe.whitelist( allow_guest = True )
def insert_user(first_name,email):
    
    user = frappe.get_doc({
        "doctype":"User",
        "first_name":first_name,
        "email":email,
        "new_password":"Frappe@123",
        "roles": [{"role": "System Manager"},{"role": "Blogger"},{"role": "Loan Manager"}],
        "block_modules":[{"module":"Contacts"},{"module":"Core"},{"module":"Email"},{"module": "Desk"},{"module": "Accounts"}] 
        
        })


    user.insert(ignore_permissions=True)    
    frappe.db.commit()
   
    return f"The data for {first_name} inserted"

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
def user_module(module_profile_name,module):
    roles= frappe.get_doc({
        "doctype":"Module Profile",
        "module_profile_name":"module_profile_name",
        # "block_modules":"module"
        })
    roles.insert(ignore_permissions=True)
    frappe.db.commit()
    return "success"






