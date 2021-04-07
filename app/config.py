import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    UPLOAD_FOLDER = './uploads'

dbconfig = { 
    'host': os.environ.get('MYSQL_HOST') or 'localhost',
    'user' : os.environ.get('MYSQL_USER') or 'root',
    'password' : os.environ.get('MYSQL_PASSWORD') or  '',
    'db' : os.environ.get('MYSQL_DB') or 'meal_planner'
}

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False