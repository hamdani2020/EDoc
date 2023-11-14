from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField
from wtforms.validators import DataRequired



class UpdatePatient(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    number = StringField('Phone Number', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    prescription = StringField('Prescription Info', validators=[DataRequired()])
    submit = SubmitField()

class UpdateDoctor(FlaskForm):
    number = StringField('Phone Number', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField()

class AddDoctor(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    number = StringField('Phone Number', validators=[DataRequired()])
    address =  StringField('Address', validators=[DataRequired()])
    submit = SubmitField()


