from odoo import models
from datetime import datetime

class HostelXlsxReport(models.AbstractModel):
    _name = 'report.hostel_managment.hostel_xlsx_report'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, records):

        date_from = data.get('date_from')
        date_to = data.get('date_to')

        sheet = workbook.add_worksheet("Hostel Report")

        header = workbook.add_format({'bold': True, 'bg_color': '#CCCCCC', 'border': 1})
        text = workbook.add_format({'border': 1})

        # Title
        sheet.merge_range(0, 0, 0, 5, "Hostel Filter Report", header)
        sheet.merge_range(1, 0, 1, 5, f"From: {date_from}  To: {date_to}", text)

        # Filter hostel by create_date
        domain = []
        if date_from:
            domain.append(('create_date', '>=', date_from))
        if date_to:
            domain.append(('create_date', '<=', date_to))

        hostels = self.env['hostel.hostel'].search(domain)

        # Header row
        headers = ['Name', 'Code', 'City', 'Phone', 'Email', 'Create Date']
        for col, h in enumerate(headers):
            sheet.write(3, col, h, header)

        row = 4
        for h in hostels:
            sheet.write(row, 0, h.name or '', text)
            sheet.write(row, 1, h.hostel_code or '', text)
            sheet.write(row, 2, h.city or '', text)
            sheet.write(row, 3, h.phone or '', text)
            sheet.write(row, 4, h.email or '', text)
            sheet.write(row, 5, h.create_date.strftime('%Y-%m-%d'), text)
            row += 1
