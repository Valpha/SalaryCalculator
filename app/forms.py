from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired


class GraphForm(FlaskForm):
    salary = IntegerField('每年积蓄（万元）', validators=[DataRequired()])
    span = IntegerField('理财年份', validators=[DataRequired()])
    rate = FloatField('年化率', validators=[DataRequired()])
    deposit = IntegerField('已有积蓄（万元）')
    submit = SubmitField('Submit')
