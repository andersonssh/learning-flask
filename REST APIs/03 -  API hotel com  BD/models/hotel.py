from sqlalchemy_ import bd

class HotelModel(bd.Model):
    __tablename__ = 'hoteis'
    hotel_id = bd.Column(bd.String, primary_key=True)
    nome = bd.Column(bd.String(80))
    estrelas = bd.Column(bd.Float(precision=1))
    diaria = bd.Column(bd.Float(precision=2))
    cidade = bd.Column(bd.String(40))


    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade
        }

    @classmethod
    def encontra_hotel(cls, hotel_id):
        hotel = cls.query.get(hotel_id)
        if hotel:
            return hotel
        return None

    def save_hotel(self):
        bd.session.add(self)
        bd.session.commit()

    def update_hotel(self, hotel_id, nome, estrelas, diaria, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade =cidade

        self.save_hotel()

    def delete_hotel(self):
        bd.session.delete(self)
        bd.session.commit()


class UserModel(bd.Model):
    __tablename__ = 'usuarios'
    user_id = bd.Column(bd.Integer, primary_key=True)
    login = bd.Column(bd.String(40))
    senha = bd.Column(bd.String(40))

    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def json(self):
        return {
            'user_id': self.user_id,
            'login': self.login,
        }

    @classmethod
    def encontra_hotel(cls, user_id):
        user = cls.query.get(user_id)
        if user:
            return user
        return None

    def save_user(self):
        bd.session.add(self)
        bd.session.commit()

    def update_user(self, login, senha):
        self.login = login
        self.senha = senha

        self.save_user()

    def delete_user(self):
        bd.session.delete(self)
        bd.session.commit()