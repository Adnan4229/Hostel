from odoo import models, fields, api

class HostelRoom(models.Model):
    _name="hostel.room"
    _description="its about rooms realated in a hostel"

    hostel_id = fields.Many2one("hostel.hostel", "hostel", help="Name of hostel")
    currency_id = fields.Many2one('res.currency', string='Currency')
    rent_amount = fields.Monetary('Rent Amount', help="Enter rent amount per month")