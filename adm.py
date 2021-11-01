from models import User
from app import db
from flask_admin.contrib.sqla import ModelView

def init_app(admin):
    admin.add_view(ModelView(User, db.session))
