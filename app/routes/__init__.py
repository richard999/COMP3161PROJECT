from flask import redirect, url_for, send_from_directory
from app import app

"""import blueprints (routes) for different sections of the system"""
from .updatedb_routes import update_db
from .querydb_routes import query_db
from .user_routes import user


app.register_blueprint(update_db, url_prefix="/update_db")
app.register_blueprint(query_db, url_prefix="/query_db")
app.register_blueprint(user, url_prefix="/user")


@app.route('/')
def index():
     return redirect(url_for('user.home'))
     #return redirect(url_for('user.index'))

