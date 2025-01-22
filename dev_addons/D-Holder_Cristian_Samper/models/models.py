#-*- coding: utf-8 -*.

from odoo import models, fields, api


class modelo1(models.Model):
   _name = 'D-Holder.modelo1'
   -description= 'D-Holder.modelo1'

   name = fields.Char()
#   value = fields.Integer()
#   value2 = fields.Float(compute="_value_pc", store=True)
#   description = field.Text()
#
#   @api.depends('value')
#    def _value_pc(self):
#       for record in self:
#          record.value2=float(record.value)/100