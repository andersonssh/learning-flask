from flask import Flask, redirect, render_template, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ap.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bnc = SQLAlchemy(app)
log_manager = LoginManager(app)

@log_manager.user_loader
def usuario_atual(id_usuario):
    return Usuario.query.get(id_usuario)


class Usuario(bnc.Model, UserMixin):
    __tablename__='usuarios'
    id = bnc.Column(bnc.Integer, primary_key=True)
    nome = bnc.Column(bnc.String(84), nullable=False)
    usuario = bnc.Column(bnc.String(84), nullable=False, unique=True)
    senha = bnc.Column(bnc.String(255), nullable=False)
    perfil = bnc.relationship('Perfil', backref='Usuario', uselist=False)

    def __str__(self):
        return self.nome




class Perfil(bnc.Model):
    __tablename__='perfis'
    id = bnc.Column(bnc.Integer, primary_key=True)
    foto = bnc.Column(bnc.Unicode(124), nullable=False)
    id_usuario = bnc.Column(bnc.Integer, bnc.ForeignKey('usuarios.id'))

    def __str__(self):
        return self.id

@app.route('/')
def index():
    usuarios = Usuario.query.all()
    return render_template('index.html', usuarios=usuarios)

@app.route('/user/<int:id>')
@login_required
def zona_usuario(id):
    user_by_id = Usuario.query.get(id)
    return render_template('usuario.html', user=user_by_id)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        user = Usuario()
        #.form['xxxx'] pega o atributo name do html
        user.nome = request.form['name']
        user.usuario = request.form['usuario']
        user.senha = generate_password_hash(request.form['password'])

        bnc.session.add(user)
        bnc.session.commit()

        return redirect(url_for('index'))

    return render_template('registro.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['password']
        user = Usuario.query.filter_by(usuario=usuario).first()
        erros = {}
        if not user:
            flash('Usuario inválido')
            return redirect(url_for('login'))

        if not check_password_hash(user.senha, senha):
            flash('Senha inválida')
            return redirect(url_for('login'))

        login_user(user)
        return redirect(url_for('index'))

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')