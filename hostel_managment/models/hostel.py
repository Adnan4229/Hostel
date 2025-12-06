from odoo import models, fields, api


class Hostel(models.Model):
    _name = 'hostel.hostel'
    _description = 'information about hostel'
    _order = 'name desc'
    name = fields.Char(string="hostel Name", required=True)
    hostel_code = fields.Char(string="Code", required="true")
    street = fields.Char('street')
    street2 = fields.Char('street2')
    zip = fields.Char('Zip', change_default=True)
    city = fields.Char('City')
    state_id = fields.Many2one("res.country.state", string="State")
    country_id = fields.Many2one('res.country', string="Country")
    phone = fields.Char('Phone', required="true")
    mobile = fields.Char('Mobile', required="true")
    email = fields.Char('Email', required="true")
    description = fields.Html('Description')


    hostel_floors = fields.Integer(string="Total Floors")
    image = fields.Binary('Hostel Image')
    active = fields.Boolean("Active", default=True,
                        help="Activate/Deactivate hostel record")
    type = fields.Selection([("male", "Boys"), ("female", "Girls"),
                         ("common", "Common")], "Type", help="Type of Hostel",
                        required=True, default="common")
    other_info = fields.Text("Other Information",
                         help="Enter more information")
    hostel_rating = fields.Float('Hostel Average Rating', digits=(14, 4))

    def report_xlsx(self):
        pass

