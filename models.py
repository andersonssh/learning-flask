from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(85), nullable=False)
    #index melhora a perfomance em uma procura de usuario por email
    email = db.Column(db.String(85), nullable= False, unique=True, index=True)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return self.name

