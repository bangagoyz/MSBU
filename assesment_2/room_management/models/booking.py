from odoo import models, fields, api
from datetime import datetime

class RoomBooking(models.Model):
    _name = 'room.booking'
    _description = 'Room Booking'

    booking_number = fields.Char(string="Nomor Pemesanan", required=True, copy=False, readonly=True, default='New')
    room_id = fields.Many2one('room.booking.room', string="Ruangan", required=True)
    booking_name = fields.Char(string="Nama Pemesan", required=True)
    booking_date = fields.Datetime(string="Tanggal Pemesanan", required=True)
    booking_status = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing', 'On Going'),
        ('done', 'Done')
    ], string="Status Pemesanan", default='draft')
    booking_notes = fields.Text(string="Catatan Pemesanan")

    _sql_constraints = [
        ('booking_name_unique', 'unique(booking_name)', 'Nama Pemesanan tidak boleh sama.')
    ]

    @api.model
    def create(self, vals):
        if vals.get('booking_number', 'New') == 'New':
            vals['booking_number'] = self.env['ir.sequence'].next_by_code('room.booking')
        return super(RoomBooking, self).create(vals)

    @api.constrains('room_id', 'booking_date')
    def _check_booking_date(self):
        for record in self:
            if self.search_count([('room_id', '=', record.room_id.id), ('booking_date', '=', record.booking_date), ('id', '!=', record.id)]):
                raise ValidationError("Tidak boleh memesan ruangan dan tanggal pemesanan yang sama.")

    def action_ongoing(self):
        self.write({'booking_status': 'ongoing'})

    def action_done(self):
        self.write({'booking_status': 'done'})