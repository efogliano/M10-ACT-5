from odoo import models, fields
class zoo_especie(models.Model):
    _name = 'zoo.especie'
    perill = fields.Char('Perill')
    nomVulgar = fields.Char('Nom Vulgar')
    nomCientific = fields.Char('Nom cientific')
    familia = fields.Char('Familia')

    animal_ids = fields.One2many('zoo.animal', 'especie_id', string='Animals')