
import frappe
from frappe import _

@frappe.whitelist()
def create_course(title):
    try:
        if not title:
            frappe.throw(_("Title is required"))
            
        course = frappe.new_doc("LMS Course")
        course.title = title
        course.save()
        return course
    except Exception as e:
        frappe.log_error(f"Course Creation Failed: {str(e)}")
        raise e
