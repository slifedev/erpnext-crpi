import frappe


def get_context(context):

    context.route = frappe.local.request.path
