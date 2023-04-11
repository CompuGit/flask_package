from flask import Flask, request, make_response, session, url_for, jsonify, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os
 
db_file = os.path.abspath(os.getcwd())+"/project.db"


app = Flask(__name__)
app.config.from_pyfile('settings.py')

app.config['MEDIA_FOLDER'] = os.path.join(app.root_path, 'media')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+db_file
db = SQLAlchemy(app)


@app.route('/api_key')
def api_key():
      return f'API_KEY = { app.config.get("API_KEY") }'

@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(
        app.config['MEDIA_FOLDER'],
        filename,
        as_attachment=True
    )

from app import routes
