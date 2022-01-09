from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from resources.usuario import User, UserRegister, UserLogin, UserLogout
from flask_jwt_extended import JWTManager
from BLACKLIST import BLACKLIST

app = Flask(__name__)
api = Api(app)
jwt = JWTManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev'
app.config['JWT_BLACKLIST_ENABLED'] = True

@app.before_first_request
def cria_banco():
    bd.create_all()

# retorna objeto de usuario acessivel pelo jwt
# com current_user
from models.usuario import UserModel
@jwt.user_lookup_loader
def user(cabecalho_jwt, dados_jwt):
    identidade = dados_jwt['sub']
    return UserModel.query.get(identidade)

# VERIFICA SE UM TOKEN ESTA NA BLACKLIST
@jwt.token_in_blocklist_loader
def verifica_blacklist(jwt_header, jwt_payload):
    print(jwt_payload['jti'] in BLACKLIST)
    return jwt_payload['jti'] in BLACKLIST


@jwt.revoked_token_loader
def token_de_acesso_invalido(jwt_header, jwt_payload):
    print('token invalidado')
    return {'message': 'voce ja fez logout'}, 401


api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(UserRegister, '/cadastro')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')

if __name__ == '__main__':
    from sqlalchemy_ import bd
    bd.init_app(app)
    app.run(debug=True)
