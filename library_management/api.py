import frappe
class Libapi():
    pass
    # def allowed_module(self):
    #     if self.module_profile:
    #         module_profile = frappe.get_doc("Module Profile",self.module_profile)
    #         self.set("block_modules", [])
    #         for d in module_profile.get("block_modules"):
    #             self.append("block_modules", {"module":d.module})

    # def get_blocked_modules(self):
    #     return [d.module for d in self.block_modules] if self.block_modules else []
# @frappe.whitelist()
# def get_module_profile(modules):
# 	module_profile = frappe.get_doc("User", 
#                {
#                 "block_modules":
#                 [
#                 {"modules" : "Blogger"},
#                 {"modules" : "CRM"}
#                 ]
#                })
# 	return module_profile.get("block_modules")
  
@frappe.whitelist(allow_guest = True)
def insert_user(first_name,email):
    user = frappe.get_doc({
        "doctype":"User",
        "first_name":first_name,
        "email":email,
        "new_password":"Frappe@123",
        "roles":[
            {"role": "System Manager"},
            {"role": "Blogger"},
            {"role": "Loan Manager"}],
        "block_modules":[
              {"module": "Contacts"},
              {"module": "Core"},
              {"module": "Email"},
              {"module": "Desk"},
              {"module": "Event Streaming"},
              {"module": "Projects"},
              {"module": "Manufacturing"},
              {"module": "Utilities"},
              {"module": "Maintenance"},
              {"module": "Quality Management"},
              {"module": "Telephony"},
              {"module": "Subcontracting"},
              {"module": "Bulk Transaction"},
              {"module": "Communication"},
              {"module": "Regional"},
              {"module": "Assets"},
              {"module": "Stock"},
              {"module": "Selling"},
              {"module": "CRM"},
              {"module": "Payments"},
              {"module": "Social"},
              {"module": "Integrations"},
              {"module": "Custom"},
              {"module": "Website"},
              {"module": "Workflow"},
              {"module": "Geo"},
              {"module": "Automation"},
              {"module": "Payment Gateways"},
              {"module": "Buying"},
              {"module": "Setup"},
              {"module": "Support"},
              {"module": "Portal"},
              {"module": "ERPNext Integrations"},
              {"module": "Loan Management"},
              {"module": "E-commerce"},
              {"module": "Accounts"},
              {"module": "Printing"},           
              {"module": "Library Management"}, 
               ]
                })   
    user.insert(ignore_permissions=True)
    frappe.db.commit()
    return f"The data for {first_name} inserted"

@frappe.whitelist(allow_guest = True)
def del_module(email):
    mod = {"mail":email,
    "block_modules":[
        {"module":"Email"},
        {"module":"Core"}
        ]
        }
    for i in mod["mail"].values():
        for j in mod["block_modules"].values:
            frappe.db.sql(f""" delete  from `tabBlock Module` where module ={mod["module"].value} and parent = {mod["mail"].value};""")
            frappe.db.commit()
    return f"module for {email} is added"


























# @frappe.whitelist(allow_guest = True)
# def delete_module(email):
#     frappe.db.delete({
#         "doctype",
#         "parent":email,
#         "module":[
#               {"module": "Contacts"},
#               {"module": "Core"},
#               {"module": "Email"},
#                 ]
#                 })
#     # module.delete(ignore_permissions=True)
#     #frappe.db.sql(""" delete from `tabUser`  where email = {}""".format(email))
#     frappe.db.commit()
#     return "deleted"
#    u_role = frappe.get_doc({"doctype":"User","module_profile":module,"role_profile_name":role,"redirect_url":url})
#    u_role.update(ignore_permissions=True)
#    frappe.db.commit()
#    return "Value Insterted"
#  user_ins = frappe.db.sql(""" update `tabUser` set  role_profile_name = {} ,redirect_url = {} where email = {}""".format(role,url,email))
#     user_ins.insert(ignore_permissions=True)
#     frappe.db.commit()
# 
# @frappe.whitelist()
# def user_module(module_profile_name,module):
    # roles= frappe.get_doc({
        # "doctype":"Module Profile",
        # "module_profile_name":"module_profile_name",
        # "block_modules":"module"
        # })
    # roles.insert(ignore_permissions=True)
    # frappe.db.commit()
    # return "success"
# 
#    
# url = "http://localhost:8000/api/method/library_management.api.?name=&email=max@gmail.com"
# headers = {}
# payload = {"fields" : ["name","email","password","roles","block_modules"] }
# r = requests.get(url,headers=headers,payload =payload)

# data = r.json()
