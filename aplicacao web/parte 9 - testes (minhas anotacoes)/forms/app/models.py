from . import db, login_manager
from flask_login import UserMixin

books_in_users = db.Table('books_users',
                          db.Column('user_id',
                                    db.Integer,
                                    db.ForeignKey('users.id'),
                                    nullable=False),
                          db.Column('book_id',
                                    db.Integer,
                                    db.ForeignKey('books.id'),
                                    nullable=False)
                          )

@login_manager.user_loader
def current_user(user_id):
    print('id user atual [ {} ]'.format(user_id))
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(84), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True, index=True)
    password = db.Column(db.String(255), nullable=False)
    #o primeiro parametro de relationship é a classe para onde quer apontar
    profile = db.relationship('Profile', backref='user', uselist=False)
    books = db.relationship('Book', secondary=books_in_users, lazy=True,
                            backref=db.backref('users'))
    def __str__(self):
        return self.name

class Profile(db.Model):
    __tablename__ = "profiles"
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.Unicode(124), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))


    def __str__(self):
        return self.name

class Book(db.Model):
    __tablename__='books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    #user_id = db.Column(db.Integer, db.ForeignKey('users.id'))