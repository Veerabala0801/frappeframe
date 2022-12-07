// Copyright (c) 2022, veerabala and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Transaction', {
	
	refresh: function(frm) {
		frm.set_query("full_name", function() 
		{

			return {	filters: [	["Library Membership","payment", "in", ["PAID"]]	]	}
		
		});
	}
});
