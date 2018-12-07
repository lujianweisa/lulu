from odoo import api, fields, models

class TrainingSubject(models.Model):
_name='pscloud_training.models.subject'
_description='科目'
name=fields.Char(string='名称')
perseon_id=fields.Many2one('res_partner','负责人')
lesson_ids = fields.One2many('pscloud_training.models.lesson', 'subject_id', string='课程')
desc = fields.Text(string='描述')