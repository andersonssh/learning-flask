from app.models import User
from app import db
from flask import render_template, redirect, url_for, request
from datetime import timedelta
from flask_login import login_user, logout_user, login_required

def init_app(app):
    @app.route('/')
    def index():
        users = User.query.all()
        return render_template('index.html', users=users)

    # methods post e get
    # o metodo post funciona quando tem um arquivo json sendo recebido do cliente
    # o metodo get funciona quando os parametros sao passados pela url
    @app.route('/register', methods=['POST', 'GET'])
    def register():
        if request.method == 'POST':
            print('detectado metodo POST')
            print('dicionario atual!')
            print(request.form)
            user = User()
            user.name = request.form['nameform']
            user.username = request.form['userform']
            print('senha: ', request.form['passform'])
            db.session.add(user)
            db.session.commit()

        return render_template('register.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        time_conect = 10
        if request.method == 'POST':
            print(request.form)
            username = request.form['userform']
            # caso a chave remember nao seja passada ele atribui o valor
            # off para desativar o remember
            # remember deve ser True ou False
            try:
                # tentando atribuir verdadeiro atraves de str
                remember = request.form['remember']
            except KeyError as e:
                # atribuindo
                remember = False

            # first() resolve o erro 'BaseQuery' object has no attribute 'is_active'
            user = User.query.filter_by(username=username).first()

            if not user:
                print('nao logado')
                return redirect(url_for('login'))

            # o usuario tera sua sessao salva pela duracao definida
            # serve para o caso de o usuario encerrar o browser, o mesmo n necessite
            # relogar! apos o prazo, se o browser for reiniciado a sessao é perdida
            # e é necessario fazer o login novamente
            login_user(user, remember=remember, duration=timedelta(seconds=time_conect))
            print('Logado com sucesso')
            return redirect(url_for('index'))

        return render_template('login.html', time_conect=time_conect)

    @app.route('/user/<int:id>')
    @login_required
    def user(id):
        user = User.query.get(id)
        return render_template('user.html', user=user)

    @app.route('/logout')
    def logout():
        # quando chamada já recebe o usuario atual por conta da funcao
        # login_manager.user_loader que é chamda sempre que o usuario faz uma
        # requisicao
        logout_user()
        return redirect(url_for('index'))