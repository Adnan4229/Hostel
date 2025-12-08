from odoo import models, fields, api

class HostelCategory(models.Model):
    _name= 'hostel.category'
    _description ='as per hostel category'
    parent_id = fields.Many2one(
        'hostel.hostel',
        string='Parent Category',
        ondelete='restrict',
        index=True)
    parent_path = fields.Char(index=True)
    # child_ids = fields.One2many('hostel.category', 'parent_id',
    #                             string='Child Categories')