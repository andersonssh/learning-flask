from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from resources.usuario import User, UserRegister

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request
def cria_banco():
    bd.create_all()


api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(UserRegister, '/cadastro')

if __name__ == '__main__':
    from sqlalchemy_ import bd
    bd.init_app(app)
    app.run(debug=True)
