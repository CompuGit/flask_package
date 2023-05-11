import os

SECRET_KEY = os.environ.get('SECRET_KEY')
API_KEY = os.environ.get('API_KEY')

UPLOAD_FOLDER = os.path.abspath(os.getcwd())+'/app/uploads'