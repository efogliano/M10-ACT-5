from odoo import models, fields
class zoo_zoo(models.Model):
    _name = 'zoo.zoo'
    grandaria = fields.Integer('Grandaria')
    nom = fields.Char('Nom')
    ciutat = fields.Char('Ciutat')
    pais = fields.Char('Pais')

    animal_ids = fields.One2many('zoo.animal', 'zoo_id', string='Animals')