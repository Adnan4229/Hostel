from odoo import models, fields

class HostelReportWizard(models.TransientModel):
    _name = 'hostel.report.wizard'
    _description = 'Wizard to Filter Hostel Records by Date'

    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)

    def print_xlsx_report(self):
        return self.env.ref('hostel_managment.hospital_xlsx_report').report_action(self, data={
            'start_date': self.start_date,
            'end_date': self.end_date,
        })
