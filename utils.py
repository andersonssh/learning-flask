from models import Pessoas, Usuarios

def insere_pessoas():
    pessoa = Pessoas(nome='Luks', idade='29')
    pessoa.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Joaozao').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Joaozao').first()
    pessoa.idade = 21
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Joaozao")
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuario = Usuarios.query.all()
    print(usuario)

if __name__ == '__main__':
    #insere_usuario('joaozao', '321')
    #insere_pessoas()
    #exclui_pessoa()
    #altera_pessoa()
    #consulta_pessoas()
    consulta_todos_usuarios()