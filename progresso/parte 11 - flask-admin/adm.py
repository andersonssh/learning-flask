from models import User, Task, Profile
from app import db
from wtforms.fields import PasswordField
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash
from flask_login import current_user
from flask import redirect

class UserView(ModelView):
    #abrir edicao em popup
    edit_modal = True
    # abrir criar em popup envez de abrir uma pagina
    # create_modal = True
    #editar diretamente na coluna da pagina de adm!!!!!!!!!!!!
    column_editable_list = ['name', 'email', 'profile']

    # restringir edicoes somente a
    form_edit_rules = ['name', 'email', 'tasks', 'profile']

    #itens que podem ser pesquisados!
    column_searchable_list = ['email', 'name']

    # configuracoes extras para os campos do formulario
    form_extra_fields = {
        #passando label pelo parametro
        #a chave referencia o label tambem referencia o label
        'password': PasswordField('Password')
    }
    #objetos a serem excluido da coluna
    column_exclude_list = ['password']

    column_list = ['name', 'email', 'profile']

    #aplica filtros
    column_filters = ['name', 'profile']

    #colocando modelo inline (objeto inline)
    inline_models = [Profile]


    def on_model_change(self, form, model, is_created):
        #executa somente se o campo for editado durante a criacao
        if is_created:
            model.password = generate_password_hash(form.password.data)

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect('/login.html')
def init_app(admin):
    admin.add_view(UserView(User, db.session))
    admin.add_view(ModelView(Task, db.session))