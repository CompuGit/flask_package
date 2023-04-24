from app import *
from app.models import User
from app.forms import LoginForm

@login_manager.user_loader
def load_user(id_):
    return User.query.filter_by(id=int(id_)).first()

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter(
                db.or_(User.username==form.username_or_email.data,
                       User.email==form.username_or_email.data)).first()
        
            remember = form.remember_me.data

        if user is not None:
            if user.check_password(form.password.data):
                login_user(user, remember=remember)
                return redirect(url_for('index'))
            else:
                flash('Invalid Password.')
        else:
            flash('Invalid Username/Email.')
    
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))