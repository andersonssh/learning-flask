from flask import Blueprint

bk = Blueprint('book', __name__)

from . import views
