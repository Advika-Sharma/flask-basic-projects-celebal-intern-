from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators

class ContactForm(FlaskForm):
    name = StringField("Name Of Student", [validators.DataRequired("Please enter your name.")])
    Gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    Address = TextAreaField("Address")

    email = StringField("Email", [
        validators.DataRequired("Please enter your email address."),
        validators.Email("Please enter a valid email address.")
    ])

    Age = IntegerField("Age")
    language = SelectField('Languages', choices=[('cpp', 'C++'), ('py', 'Python')])
    submit = SubmitField("Send")

#python -m venv venv
#venv\Scripts\activate
#pip install flask flask-wtf
#pip install wtforms