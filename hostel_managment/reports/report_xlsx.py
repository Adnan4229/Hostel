from odoo import models , fields
from datetime import datetime

class HostelXlsxReport(models.AbstractModel):
    _name = 'report.hostel_managment.hostel_xlsx_report'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, records):
        sheet = workbook.add_worksheet("Hostel Report")

        bold = workbook.add_format({'bold': True, 'font_color': 'black', 'bg_color': '#D3D3D3'})

        headers = ['name', 'hostel_code', 'street', 'street2','zip','city','state_id','country_id','phone','mobile','email','description']
        for col, header in enumerate(headers):
            sheet.write(0, col, header, bold)

        # Data
        row = 1
        for hostel in records:
            sheet.write(row, 0, hostel.name or '')
            sheet.write(row, 1, hostel.hostel_code or '')
            sheet.write(row, 2, hostel.street or 0)
            sheet.write(row, 3, hostel.street2 or 0)
            sheet.write(row, 4, hostel.zip or 0)
            sheet.write(row, 5, hostel.city or 0)
            sheet.write(row, 6, hostel.state_id.name or '')
            sheet.write(row, 7, hostel.country_id.name or '')
            sheet.write(row, 8, hostel.phone or 0)
            sheet.write(row, 9, hostel.mobile or 0)
            sheet.write(row, 10, hostel.email or 0)
            sheet.write(row, 11, hostel.description or 0)

            row += 1


