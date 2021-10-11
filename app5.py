from datetime import timedelta
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bancodedados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), nullable=False)
    username = db.Column(db.String(90), unique=True, nullable=False)
    profile = db.relationship('Profile', backref='User', uselist=False)

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(500), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

#methods post e get
#o metodo post funciona quando tem um arquivo json sendo recebido do cliente
#o metodo get funciona quando os parametros sao passados pela url
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
        #off para desativar o remember
        #remember deve ser True ou False
        try:
            #tentando atribuir verdadeiro atraves de str
            remember = request.form['remember']
        except KeyError as e:
            #atribuindo
            remember = False

        #first() resolve o erro 'BaseQuery' object has no attribute 'is_active'
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

    return render_template('login.html', time_conect=time_conect)

@app.route('/user/<int:id>')
@login_required
def user(id):
    user = User.query.get(id)
    return render_template('user.html', user=user)

#esta funcao é usada a cada requisicao do usuario
@login_manager.user_loader
def carrega_usuario(id_user):
    # apos o usuario ser carregado e autenticado esta funcao torna-se necessaria
    # para mapear o usuario na rede
    print('Logando como ', id_user)
    return User.query.get(id_user)

@app.route('/logout')
def logout():
    #quando chamada já recebe o usuario atual por conta da funcao
    #login_manager.user_loader que é chamda sempre que o usuario faz uma
    #requisicao
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')