from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo import _
from datetime import timedelta

class HostelRoom(models.Model):
    _name = "hostel.room"
    _description = "Rooms related in a hostel"

    student_ids = fields.One2many('hostel.student', 'room_id', string="Students")
    hostel_id = fields.Many2one("hostel.hostel", "hostel", help="Name of hostel")
    currency_id = fields.Many2one('res.currency', string='Currency')
    rent_amount = fields.Monetary('Rent Amount', help="Enter rent amount per month")
    room_no = fields.Integer(string="Room No")
    admission_date = fields.Date("Admission Date", help="Date of Admission in Hostel")
    discharge_date = fields.Date("Discharge Date", help="Date on which student discharged")
    duration = fields.Integer("Duration", compute="_compute_check_duration",
                              inverse="_inverse_duration", help="Enter duration of living" ,store="true")
    state = fields.Selection([
        ('draft', 'Unavailable'),
        ('available', 'Available'),
        ('closed', 'Closed')],
        'State', default="draft")

    @api.depends("admission_date","discharge_date")
    def _compute_check_duration(self):
        for rec in self:
            if rec.admission_date and rec.discharge_date:
                rec.duration = (rec.discharge_date - rec.admission_date).days

    def _inverse_duration(self):
        for stu in self:
            if stu.discharge_date and stu.admission_date:
                duration = (stu.discharge_date - stu.admission_date).days
                if duration != stu.duration:
                    stu.discharge_date = stu.admission_date + timedelta(days=stu.duration)

    student_per_room = fields.Integer("Student Per Room", required=True, help="Students allocated per room")
    availability = fields.Float(compute="_compute_check_availability", string="Availability",
                                help="Room availability in hostel")

    _sql_constraints = [
        ("room_no_unique", "unique(room_no)", "Room number must be unique")
    ]

    @api.constrains("rent_amount")
    def _check_rent_amount(self):
        for rec in self:
            if rec.rent_amount < 0:
                raise ValidationError(_("Rent Amount Per Month should not be a negative value!"))

    @api.depends("student_per_room", "student_ids")
    def _compute_check_availability(self):
        for rec in self:
            rec.availability = rec.student_per_room - len(rec.student_ids)
