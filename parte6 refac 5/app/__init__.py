
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#antes, as 2 possuiam os parametros com a instancia Flask
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bancodedados.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)

    from app import routes
    routes.init_app(app)
    #retornando aplicativo criado!
    return app


if __name__ == '__main__':
    pass