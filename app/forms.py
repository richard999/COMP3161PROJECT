from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, InputRequired
from wtforms.widgets import TextArea



class ContactForm(FlaskForm):
    firstname = StringField('firstname', validators=[DataRequired()])
    lastname = StringField('lastname', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    address = StringField('address', validators =[DataRequired()])