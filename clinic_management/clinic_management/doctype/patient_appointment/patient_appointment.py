# Copyright (c) 2026, dev and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PatientAppointment(Document):
	def validate(self):
		# Fall back to Clinic Settings default fee if consultation\_fee is not set
		if not self.consultation_fee:
			default_fee = frappe.db.get_single_value("Clinic Settings","default_consultation_fee") or 50
			self.consultation_fee = default_fee

	def on_submit(self):
		# Automatically mark appointment as Completed when submitted
		self.status = "Completed"
		self.db_set("status", "Completed")
