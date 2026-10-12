import frappe

def get_appointment_conditions(user):
    if not user:
        user = frappe.session.user
        # System Manager can see all appointments
        if "System Manager" in frappe.get_roles(user):
            return "" # Find Doctor linked to this User
        doctor = frappe.db.get_value("Doctor", {"user_id": user}, "name")
        if doctor:
            return f"`tabPatient Appointment`.doctor = '{doctor}'"
        # Non-doctors see nothing by default
        return "`tabPatient Appointment`.name IS NULL"