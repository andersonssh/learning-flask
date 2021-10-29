from .authbp import auth as auth_blueprint
from .book import bk as book_blueprint
from .user import user as user_blueprint

def init_app(app):
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(book_blueprint)
    app.register_blueprint(user_blueprint)