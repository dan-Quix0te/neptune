from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import ValidationError, DataRequired


class ingestMediaForm(FlaskForm):
    name = StringField('Media Name', validators=[DataRequired()])
    path = FileField('Media Path', validators=[DataRequired()])
    submit = SubmitField('Probe')

