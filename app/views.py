"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash
from flask_wtf import Flaskform 
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


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
@app.route('/login/')
def login():
       error = None
    if request.method == 'POST':
    # this part need to change as we get the sql
        if request.form['username'] != app.config['ADMIN_USERNAME'] or request.form['password'] != app.config['ADMIN_PASSWORD']:
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True
            
            flash('You were logged in', 'success')
            return redirect(url_for('upload'))
    return render_template('login.html', error=error)
@app.route('/logout/')
def logout():
    render_template('logout.html')
    
@app.route('/signup/')
def signUp():
    return render_template('sign_up.html')

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

'''connect to mysql database'''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'meal_planner'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql.init_app(app)


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
