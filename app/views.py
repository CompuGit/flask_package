from flask_admin.contrib.sqla import ModelView
from flask_admin.form import rules
from wtforms import PasswordField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash

class UserView(ModelView):
    column_searchable_list = ('username', 'email')
    column_filters = ('username', 'email')
    can_create = True
    can_edit = True
    can_delete = True
    #can_export = True

    form_extra_fields = {
        'password_hash': PasswordField('Password', validators=[DataRequired()])
    }

    form_rules = (
        rules.Field('username'),
        rules.Field('email'),
        rules.Field('password_hash'),
        rules.Field('is_admin')
    )

    def on_model_change(self, form, model, is_created):
        if form.password_hash.data:
            model.password_hash = generate_password_hash(form.password_hash.data)

