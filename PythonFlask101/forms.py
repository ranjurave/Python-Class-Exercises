from flask import Flask
from wtforms import validators, ValidationError
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, RadioField, SelectField, SubmitField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    name = StringField(label='User Name: ', validators=[DataRequired()])
    gender = RadioField('Gender', choices=[('M', 'Male'),('F', 'Female'), ('O', 'Other'), ('D', 'Dont Specify')])
    address = TextAreaField('Address')
    email = StringField(label='email', validators=[DataRequired()])
    age = IntegerField('age')
    language = SelectField('Language', choices=[('cpp', 'C++'), ('python','Python'), ('csharp', 'C#')])
    submit = SubmitField('Submit')