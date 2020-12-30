from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, SubmitField
from wtforms.validators import DataRequired

class InfoForm(FlaskForm):
    latitude = FloatField('Latitude', validators=[DataRequired()])
    longtitude = FloatField('Longtitude', validators=[DataRequired()])
    phonenumber = StringField('phonenumber', validators=[DataRequired()])
    submit = SubmitField('Sign In')
