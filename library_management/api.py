import frappe
class Libapi():
    pass

@frappe.whitelist(allow_guest = True)
def insert_user(first_name,email,modules):
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
              {"module": "Library Management"}
               ]
                })   
    user.insert(ignore_permissions=True)
    frappe.db.commit()
    em=email
    m_filter = modules.split(',')
    for j in m_filter:
        frappe.db.sql(f"""delete from `tabBlock Module` where module = "{j}" and parent = "{em}";""")
        frappe.db.commit()
    return f"module for {email} is added"

