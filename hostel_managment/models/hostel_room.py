from odoo import models, fields, api

class HostelRoom(models.Model):
    _name="hostel.room"
    _description="its about rooms realated in a hostel"

    hostel_id = fields.Many2one("hostel.hostel", "hostel", help="Name of hostel")
    currency_id = fields.Many2one('res.currency', string='Currency')
    rent_amount = fields.Monetary('Rent Amount', help="Enter rent amount per month")
    room_no= fields.Integer(string="Room No")



    # <database level pr check kranaga ka ya jo value arahi dublicate tu nhi and then error dega agr dublicate hu>
    _sql_constraints=[
        ("room_no_unique", "unique(room_no)",
         "Room number must be unique")]




    # <python level pr check karanga and then respond us instead of database level>
    @api.constrains("rent_amount")
    def _check_rent_amount(self):
        if self.rent_amount < 0:
          raise ValidationError(_("Rent Amount Per Month should not be a negative value!"))