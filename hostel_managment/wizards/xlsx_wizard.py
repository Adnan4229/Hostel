from odoo import models, fields, api
from datetime import datetime


class HostelReportWizard(models.TransientModel):
    _name = 'hostel.report.wizard'
    _description = 'Hostel XLSX Report Wizard'

    date_from = fields.Date("Start Date")
    date_to = fields.Date("End Date")

    def print_report(self):
        data = {
            'date_from': self.date_from.strftime('%Y-%m-%d'),
            'date_to': self.date_to.strftime('%Y-%m-%d')
        }
        return self.env.ref('hostel_managment.hostel_xlsx_report_action').report_action(self, data=data)
