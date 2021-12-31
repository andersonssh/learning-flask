from sqlalchemy_ import bd

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
    def encontra_usuario(cls, user_id):
        user = cls.query.get(user_id)
        if user:
            return user
        return None

    @classmethod
    def encontra_usuario_por_login(cls, login):
        user = cls.query.filter_by(login=login).first()
        return user if user else None

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