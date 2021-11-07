from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def current_user(user_id):
    return User.query.get(id=user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(85), nullable=False)
    #index melhora a perfomance em uma procura de usuario por email
    email = db.Column(db.String(85), nullable= False, unique=True, index=True)
    password = db.Column(db.String(255), nullable=False)
    #(tabela, com backref=use, a tabela users esta acessivel atraves da tabela tasks com tasks.users)
    tasks = db.relationship('Task', backref='user')
    profile = db.relationship('Profile', backref='user')

    def __repr__(self):
        return self.name

class Task(db.Model):
    __tablename__= 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(85), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return self.name


class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(20), nullable=False, unique=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)