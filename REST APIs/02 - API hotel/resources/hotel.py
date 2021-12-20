from flask_restful import Resource, reqparse

hoteis = [
    {
        'hotel_id': 'xx',
        'nome': 'Hotelzao 1',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'RJ'
    },{
        'hotel_id': 'yy',
        'nome': 'Hotelzao 3',
        'estrelas': 4.8,
        'diaria': 770.34,
        'cidade': 'SC'
    },{
        'hotel_id': 'zz',
        'nome': 'Hotelzao 3',
        'estrelas': 3.8,
        'diaria': 500.34,
        'cidade': 'SP'
    },
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis':hoteis}


class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel

        return {'message': 'Hotel not found'}, 404

    def post(self, hotel_id):
        argumentos = reqparse.RequestParser()
        # pegar apenas os argumentos definidos abaixo
        argumentos.add_argument('nome', required=True, help='O nome nao pode ser vazio!')
        argumentos.add_argument('estrelas', type=float)
        argumentos.add_argument('diaria', type=float)
        argumentos.add_argument('cidade')

        dados = {'hotel_id': hotel_id, **argumentos.parse_args()}
        hoteis.append(dados)
        return dados


    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass
