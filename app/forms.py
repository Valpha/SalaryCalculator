from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired

class GraphForm(FlaskForm):
    para1 = IntegerField('salary', validators=[DataRequired()])
    para2 = IntegerField('span', validators=[DataRequired()])
    para3 = FloatField('rate', validators=[DataRequired()])
    submit = SubmitField('Submit')