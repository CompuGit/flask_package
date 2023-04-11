from flask import Flask, request, make_response, session, url_for, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os
 
db_file = os.path.abspath(os.getcwd())+"/project.db"


app = Flask(__name__)
app.config.from_pyfile('settings.py')

app.config['MEDIA_FOLDER'] = os.path.join(app.root_path, 'media')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+db_file
db = SQLAlchemy(app)



from app import routes
