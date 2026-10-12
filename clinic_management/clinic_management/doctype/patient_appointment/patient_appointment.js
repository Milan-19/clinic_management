// Copyright (c) 2026, dev and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Patient Appointment", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on("Patient Appointment", {
	refresh(frm) {
		// Add custom action button for active appointments
		if (frm.doc.status === "Scheduled" && !frm.is_new()) {
			frm.add_custom_button(
				__("Mark Completed"),
				function () {
					frm.set_value("status", "Completed");
					frm.save().then(() => {
						frappe.show_alert({
							message: __("Appointment marked as Completed"),
							indicator: "green",
						});
					});
				},
				__("Status"),
			);
		}
	},
	doctor(frm) {
		// Fetch doctor fee on selection  if available
		if (frm.doc.doctor) {
			frappe.db.get_value("Doctor", frm.doc.doctor, "consultation_fee").then((r) => {
				if (r.message && r.message.consultation_fee) {
					frm.set_value("consultation_fee", r.message.consultation_fee);
				}
			});
		}
	},
});
