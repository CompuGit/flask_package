from flask import (
    Flask, request, make_response, 
    session, url_for, jsonify, 
    render_template, send_from_directory, 
    redirect, flash)

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user


#creating app in the project
app = Flask(__name__)


#app configurations
app.config.from_pyfile('settings.py')


#configuring database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)
app.app_context().push()

#creating login manager
login_manager = LoginManager(app)
login_manager.login_view='login'


#creating an api_key endpoint
@app.route('/api_key')
def api_key():
      return f'API_KEY = { app.config.get("API_KEY") }'


#default 404 handler
@app.errorhandler(404) 
def invalid_route(e): 
    return render_template('404.html'), 404


from app import routes
from app import auth
