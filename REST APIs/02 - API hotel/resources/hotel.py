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
    argumentos = reqparse.RequestParser()
    # pegar apenas os argumentos definidos abaixo
    argumentos.add_argument('nome', required=True, help='O nome nao pode ser vazio!')
    argumentos.add_argument('estrelas', type=float)
    argumentos.add_argument('diaria', type=float)
    argumentos.add_argument('cidade')

    def encontrar_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel

        return None

    def get(self, hotel_id):
        hotel = Hotel.encontrar_hotel(hotel_id)

        if hotel:
            return hotel

        return {'message': 'Hotel not found'}, 404

    def post(self, hotel_id):
        dados = {'hotel_id': hotel_id, **Hotel.argumentos.parse_args()}
        hoteis.append(dados)
        return dados


    def put(self, hotel_id):
        hotel = Hotel.encontrar_hotel(hotel_id)
        novo_hotel = {'hotel_id': hotel_id, **Hotel.argumentos.parse_args()}
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200, 'OK'

        hoteis.append(novo_hotel)
        return novo_hotel, 201 # codigo para: created

    def delete(self, hotel_id):
        pass
