// Copyright (c) 2022, veerabala and contributors
// For license information, please see license.txt
/* eslint-disable */
import DataTable from "frappe-datatable"

import getSampleData from "./data.js";


const el = document.getElementById("app");


const { columns, data } = getSampleData();


window.datatable = new DataTable(el, {

  columns,

  data,

  checkboxColumn: true,

  inlineFilters: true

  // layout: "fluid"

});




// frappe.query_reports["Library Membership"] = {
	
	
	
// };


