from flask_restful import Resource, reqparse
from models.usuario import UserModel


class User(Resource):
    def get(self, hotel_id):
        usuario = UserModel.encontra_usuario(hotel_id)

        if usuario:
            return usuario.json()

        return {'message': 'User not found'}, 404

    def delete(self, user_id):
        usuario = UserModel.encontra_usuario(user_id)
        if usuario:
            try:
                usuario.delete_usuario()
            except:
                return {'message': 'Ocorreu um erro interno ao tentar deletar dados'}, 500
            return {'message': 'usuario deletado!'}
        return {'message': 'usuario não encontrado!'}
