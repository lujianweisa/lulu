from odoo import api, fields, models

class TrainingLesson(models.Model):
_name = 'pscloud.training.lesson'
_description = "课程信息"
name = fields.Char(string='名称')
teacher_id = fields.Many2one('res.partner', string='老师', domain=[('is_teacher', '=', True)])
student_ids = fields.Many2many('res.partner', string='学生', domain=[('is_student', '=', True)], readonly=True)
start_date = fields.Date(string='开始时间')
end_date = fields.Date(string='结束时间')
seat_qty = fields.Integer(string='座位数')
subject_id = fields.Many2one('pscloud.training.subject', string='科目')
    