from flask import Flask, request
from flask_restful import Resource, Api
import json
from skill import Habilidades, ListaHabilidades

app = Flask(__name__)
api = Api(app)

devs = [
    {
        'id': 1,
        'nome': 'joaozaum',

    }
]

class Dev(Resource):
    def get(self, id):
        try:
            response = devs[id]
        except IndexError:
            message = 'O desenvolvedor de ID {} não existe!'.format(id)
            response = {'status': 'erro', 'message': message}
        except Exception:
            message = 'erro desconhecido'
            response = {'status': 'erro', 'message': message}
        return response
        #com a lib restful nao necessita retornar como jsonify({dict}), ele já retorna formatado adequadamente
        #return {'nome': 'Juju'}
    def put(self, id):
        dados = json.loads(request.data)
        devs.append(dados)
        return {'status': 'ok', 'message': 'Dados alterados!'}
    def delete(self, id):
        try:
            devs.pop(id)
        except IndexError:
            response = {'status': 'erro', 'message': 'o id inserido nao corresponde a nenhum usuario'}
        else:
            response = {'status': 'sucesso', 'message': 'usuario apagado!'}

        return response

class ListaDevs(Resource):
    def get(self):
        return devs

    def post(self):
        dados = json.loads(request.data)
        dados['id'] = len(devs)
        devs.append(dados)
        return {'status': 'sucesso', 'message': 'usuario cadastrado!'}



api.add_resource(Dev, '/dev/<int:id>')
api.add_resource(ListaDevs, '/dev/')
api.add_resource(Habilidades, '/habilidades/<int:id>')
api.add_resource(ListaHabilidades, '/habilidades/')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')