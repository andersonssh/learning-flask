from app import db, login_manager
from flask_login import UserMixin
#esta funcao é usada a cada requisicao do usuario
@login_manager.user_loader
def carrega_usuario(id_user):
    # apos o usuario ser carregado e autenticado esta funcao torna-se necessaria
    # para mapear o usuario na rede
    print('Logando como ', id_user)
    return User.query.get(id_user)

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
