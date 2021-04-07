"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db, login_manager
from .forms import ContactForm
from .loginform import LoginForm
from flask import render_template, request, redirect, url_for, flash
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import ContactForm
#from app.models import UserProfile
from werkzeug.security import check_password_hash


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Our Recipe Planner")
@app.route('/search/')
def search():
    return render_template('search.html')

@app.route('/AddRecipe/')
def addRecipe():
    return render_template('addRecipe.html')
@app.route('/recipe')
def viewRecipe():
    return render_template('viewRecipe.html')



@app.route('/login/',methods=["GET", "POST"])
def login():
        if current_user.is_authenticated:
            return redirect(url_for('dashboard'))
        lform = LoginForm()
        if request.method == "POST" and form.validate_on_submit():
            email = lform.username.data
            password = lform.password.data
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM User WHERE email= %s AND password = %s', (email, password,))
            user = cursor.fetchone()






@app.route('/logout/')
def logout():
    render_template('logout.html')
    
@app.route('/signup/')
def signUp():
    cform = ContactForm()
    if request.method == 'POST' and form.validate_on_submit():
        if cform.validate_on_submit():
            firstname = cform.name.data
            lastname = cform.name.data
            email = cform.email.data
            password = cform.password.data
            address = cform.password.data

            
            flash("Sign up Complete !", "Successful")
            return redirect(url_for('login'))
   
        flash_errors(cform)
    return render_template('sign_up.html', contact=cform)


@app.route('/newMealPlan/')
def createMealPlan():
    return render_template('newMealPlan')



###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404




if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
