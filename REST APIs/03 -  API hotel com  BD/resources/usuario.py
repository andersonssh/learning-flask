from flask_restful import Resource, reqparse
from models.usuario import UserModel


class User(Resource):
    def get(self, user_id):
        usuario = UserModel.encontra_usuario(user_id)

        if usuario:
            return usuario.json()

        return {'message': 'User not found'}, 404

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
        atributos = reqparse.RequestParser()
        atributos.add_argument('login', type=str, required=True, help='O campo login nao pode ficar em branco')
        atributos.add_argument('senha', type=str, required=True, help='O campo senha nao pode ficar em branco')

        dados = atributos.parse_args()

        if UserModel.encontra_usuario_por_login(dados['login']):
            return {'message': 'O usuario já existe'}, 400
        else:
            # salva usuario no bd
            ################## HASH não foi usado
            UserModel(**dados).save_user()
            return {'message': 'usuario criado'}, 200
