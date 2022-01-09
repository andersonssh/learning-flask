from flask_restful import Resource, reqparse
from models.usuario import UserModel
from flask_jwt_extended import create_access_token
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import jwt_required, get_jwt
from BLACKLIST import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('login', type=str, required=True, help='O campo login nao pode ficar em branco')
atributos.add_argument('senha', type=str, required=True, help='O campo senha nao pode ficar em branco')

class User(Resource):
    def get(self, user_id):
        usuario = UserModel.encontra_usuario(user_id)

        if usuario:
            return usuario.json()

        return {'message': 'User not found'}, 404

    @jwt_required()
    def delete(self, user_id):
        usuario = UserModel.encontra_usuario(user_id)
        if usuario:
            try:
                usuario.delete_user()
            except:
                return {'message': 'Ocorreu um erro interno ao tentar deletar dados'}, 500
            return {'message': 'usuario deletado!'}
        return {'message': 'usuario não encontrado!'}


class UserRegister(Resource):
    # /cadastro
    def post(self):
        dados = atributos.parse_args()

        if UserModel.encontra_usuario_por_login(dados['login']):
            return {'message': 'O usuario já existe'}, 400
        else:
            # salva usuario no bd
            ################## HASH não foi usado
            UserModel(**dados).save_user()
            return {'message': 'usuario criado'}, 200

class UserLogin(Resource):
    @classmethod
    def post(cls):
        dados = atributos.parse_args()

        user = UserModel.encontra_usuario_por_login(dados['login'])

        if user and safe_str_cmp(user.senha, dados['senha']):
            token_de_acesso = create_access_token(identity=user.user_id)
            return {'acess_token': token_de_acesso}, 200
        return {'message': 'Usuario ou senha incorreta.'}

class UserLogout(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti'] # identificador do token
        BLACKLIST.add(jti)
        return {'message': 'voce se deslogou'}, 200