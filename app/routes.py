from app import *


@app.route('/')
@login_required
def index():
	return render_template('index.html')

@app.route('/favicon')
def favicon():
	return send_from_directory(app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon')
