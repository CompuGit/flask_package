from app import *
from app.models import *

@app.route('/')
def index():
	return render_template('index.html')

@app.errorhandler(404) 
def invalid_route(e): 
    return jsonify({'errorCode' : 404, 'message' : 'Route not found'})