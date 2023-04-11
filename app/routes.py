from app import *
from app.models import *

@app.route('/api_key')
def api_key():
      return f'API_KEY = { app.config.get("API_KEY") }'

@app.route('/')
def index():
	return render_template('index.html')

@app.errorhandler(404) 
def invalid_route(e): 
    return jsonify({'errorCode' : 404, 'message' : 'Route not found'})