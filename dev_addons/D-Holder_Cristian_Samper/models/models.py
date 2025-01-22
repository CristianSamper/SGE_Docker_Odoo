#-*- coding: utf-8 -*.

from odoo import models, fields, api


class modelo1(models.Model):
   _name = 'D-Holder.modelo1'
   _description= 'D-Holder.modelo1'

   name = fields.Char()

class tree(models.tree):
   _name = 'D-Holder.tree'
   _description = 'D-Holder.tree'

class formPer(models.form):
   _name = 'D-Holder.formPer'
   _description = 'D-Holder.formPer'

   name=fields.char()
   race=fields.char()
   level=fields.integer()