import frappe

@frappe.whitelist(allow_guest=True)
def get_doctor_appointments(doctor, date):
    """Get all appointments for a doctor on a specific date."""
    return frappe.get_all(
        "Patient Appointment",
        fields=["name", "patient", "status", "consultation_fee"],
        filters={"doctor": doctor, "appointment_date": date}
    )