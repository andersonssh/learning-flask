from flask_restful import Resource
import json
from flask import request

skills = ['Python', 'Java', 'PHP']

class Habilidades(Resource):
    def get(self, id):
        return skills[id]
    def put(self, id):
        skills[id] = json.loads(request.data)
        return {'status': 'sucesso'}
    def delete(self, id):
        return {'status': 'sucesso'}

class ListaHabilidades(Resource):
    def get(self):
        return skills
    def post(self):
        skills.append(json.loads(request.data))
        return {'status': 'sucesso', 'message': 'habilidade cadastrada'}