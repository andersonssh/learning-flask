from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

# USUARIOS = {
#     'joaozao': '123',
#     'juju': '321'
# }
#
# @auth.verify_password
# def verificacao(login, senha):
#     print('Validando usuario: ', USUARIOS.get(login) == senha)
#     if not (login, senha):
#         return False
#
#     return USUARIOS.get(login) == senha

@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()

class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'error',
                'message': 'pessoa nao encontrada'
            }
        return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        #veriricando chaves do dicionario
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'nome': pessoa.nome,
            'idade': pessoa.idade,
            'id': pessoa.id
        }
        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome)
        pessoa.delete()
        response = {
            'status': 'sucesso',
            'message': 'pessoa deletada!'
        }
        return response

class ListaPessoas(Resource):
    @auth.login_required
    def get(self):
        pessoa = Pessoas.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoa]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()

        return {'status': 'sucesso', 'message': 'usuario cadastrado'}

class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        print(atividades)
        return [{'atividade': i.nome, 'responsavel': i.pessoa.nome} for i in atividades]

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'status': 'sucesso',
            'message': 'atividade cadastrada para {}'.format(dados['pessoa'])
        }
        return response


api.add_resource(Pessoa, '/pessoa/<string:nome>')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(ListaAtividades, '/atividades/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')