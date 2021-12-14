import pytest
from forms.app import create_app, db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    #sem ///nomedb siginifica que ira ser usado db em memoria
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
    app.config['SQLALCHEMY_TRCK_MODIFICATIONS'] = False
    app.config['WTF_CSRF_ENABLED'] = False

    context = app.app_context()
    context.push()

    db.create_all()

    yield app.test_client()

    db.session.remove()
    db.drop_all()

    context.pop()

#se a pagina usuario retorna o status code 200
def test_se_a_pagina_usuario_retorna_status_code_200(client):
    response = client.get('/')
    assert response.status_code == 200

def test_se_o_link_registrar_existe(client):
    response = client.get()
    #assert 'Registrar' in response.get_data(as_text=True)
    #ou
    assert b'Registrar' in response.data


def test_se_o_link_de_login_existe(client):
    response = client.get()

    assert b'Login' in response.data


def test_registrando_usuario(client):
    data = {
        'name': 'seila',
        'email': 'seila@gmail.com',
        'password': 'seila'
    }
    response = client.post('/register', data=data, follow_redirects=True)
    assert b'seila@gmail.com' in response.data

def test_logando_usuario(client):
    data = {
        'name': 'seila',
        'email': 'seila@gmail.com',
        'password': 'seila'
    }

    client.post('/register', data=data, follow_redirects=True)


    response = client.post('/login', data=data, follow_redirects=True)
    assert b'Sair' in response.data