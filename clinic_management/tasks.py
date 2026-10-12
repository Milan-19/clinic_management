import frappe

def auto_close_past_appointments():
    """Mark past appointments as Completed automatically."""
    today = frappe.utils.today()
    frappe.db.sql(""" UPDATE `tabPatient Appointment` SET status = 'Completed' WHERE appointment_date < %s AND status = 'Scheduled' """, (today,))
    frappe.db.commit()