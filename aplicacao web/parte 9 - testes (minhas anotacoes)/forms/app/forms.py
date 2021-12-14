from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import Length, Email, DataRequired
from .models import Book

class LoginForm(FlaskForm):
    # a vantagem em colocar esses campos diretamente no html
    # e que eles podem ser configurados e modificados apartir desta classe
    email = EmailField('Email', validators=[
        Email()
    ])
    #validators necessita de 3 parametros, o 1: min de caracteres
    #2:max de caracteres 3: mensagem de erro que é armazenado em uma varaivel desta classe (errors)
    password = PasswordField('Senha', validators=[
        Length(3, 6, "O campo deve conter de 3 a 6 caracteres")
    ])
    remember = BooleanField('Permanecer Conectado')
    submit = SubmitField('Logar')

class RegisterForm(FlaskForm):
    name = StringField('Nome', validators=[
        DataRequired("O campo é obrigatório!")
    ])
    email = EmailField('Email', validators=[
        Email()
    ])
    password = PasswordField('Senha', validators=[
        Length(3, 6, "a senha deve ter entre 3 a 6 caracteres")
    ])
    submit = SubmitField('cadastrar')

class BookForm(FlaskForm):
    name = StringField('Nome do livro', validators=[
        DataRequired('O campo é obrigatorio (Mensagem de erro)')
    ])
    submit = SubmitField('Salvar')

class UserBookForm(FlaskForm):
    #book = SelectField('Livro', coerce=int,
     #                  choices=[
    #                            (1, 'seila velio n add'),
     #                           (2, 'teste')])
    book = SelectField('Livro')
    submit = SubmitField('Adicionar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #passando choices para Select field instanciado na var book
        self.book.choices = [
            #passando todos os livros e passando em lista de tuplas
            (book.id, book.name) for book in Book.query.all()
        ]
        print(self.book.choices)
