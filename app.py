from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    #passando configuracoes
    app.config.from_object(Config)

    #passando controlador do sqlalchemy para app
    db.init_app(app)

    #area adm
    import adm
    admin = Admin(app, name='Andssu trol', template_mode='bootstrap4')
    adm.init_app(admin)

    return app

if __name__ == '__main__':
    create_app().run(debug=True, host='0.0.0.0')