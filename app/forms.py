from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Email

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class SignupForm(FlaskForm):
    fname = StringField('First Name', validators=[InputRequired()])
    lname = StringField('Last Name', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    rpassword = PasswordField('Reapeat Password', validators=[InputRequired()])

class AddtoKitchenForm(FlaskForm):
    quantity= StringField('Quantity', validators=[InputRequired()])
    unitmeasurement= StringField('unitmeasurement' validators=[InputRequired()])

class RecipeForm(FlaskForm):
    name = StringField('Recipe Name', validators=[InputRequired()])
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])
    
class SearchRecipeForm(FlaskForm):
    search = StringField('Search for recipe', validators=[InputRequired()])