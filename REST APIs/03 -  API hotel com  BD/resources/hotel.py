from flask_restful import Resource, reqparse
from models.hotel import HotelModel

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
    atributos = reqparse.RequestParser()
    # pegar apenas os argumentos definidos abaixo
    atributos.add_argument('nome', required=True, help='O nome nao pode ser vazio!')
    atributos.add_argument('estrelas', type=float)
    atributos.add_argument('diaria', type=float)
    atributos.add_argument('cidade')

    # acessa com: **Hotel.atributos.parse_args()

    def get(self, hotel_id):
        hotel = HotelModel.encontra_hotel(hotel_id)

        if hotel:
            return hotel.json()

        return {'message': 'Hotel not found'}, 404

    def post(self, hotel_id):
        if HotelModel.encontra_hotel(hotel_id):
            return {"message": f"Hotel id '{hotel_id}' já existe."}, 400


        dados = {'hotel_id': hotel_id, **Hotel.atributos.parse_args()}
        #as chaves serao passadas para o construtor noformato (nome='xxx'....)
        hotel = HotelModel(**dados)
        hotel.save_hotel()

        return hotel.json(), 200


    def put(self, hotel_id):
        dados = {'hotel_id': hotel_id, **Hotel.atributos.parse_args()}
        hotel_encontrado = HotelModel.encontra_hotel(hotel_id)
        # hotel encontrado
        if hotel_encontrado:
            # atualiza hotel
            hotel_encontrado.update_hotel(**dados)
            return hotel_encontrado.json(), 200

        hotel = HotelModel(**dados)
        hotel.save_hotel()
        return hotel.json(), 201 # hotel criado

    def delete(self, hotel_id):
        hotel = HotelModel.encontra_hotel(hotel_id)
        if hotel:
            hotel.delete_hotel()
            return {'message': 'hotel deletado!'}
        return {'message': 'hotel não encontrado!'}

