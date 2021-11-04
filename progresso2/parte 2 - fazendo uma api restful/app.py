from flask import Flask, jsonify, request
import json
app = Flask(__name__)

devs = [
    {'nome': 'Rafael',
     'habilidades': ['Python', 'Flask'],
     },
    {'nome': 'Jusesao',
     'habilidades': ['Python', 'Django'],
     },
]

#retornna, altera ou deleta os dados de um dev pelo ID
@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def deselvolvedor(id):
    if request.method == 'GET':
        try:
            response = devs[id]
        except IndexError:
            response = {'status': 'fracasso', 'mensagem': 'O id inserido não existe!'}
        except Exception:
            response = {'status': 'fracasso', 'mensagem': 'Erro desconhecido. Procure o adm da API'}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        devs[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        try:
            devs.pop(id)
        except IndexError:
            return jsonify({'status': 'fracasso', 'mensagem': 'O registro informado não existe!'})
        else:
            return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluido com sucesso!'})

# lista todos os desevolvedores e permite registrar um novo dev
@app.route('/dev/', methods=['POST', 'GET'])
def lista_devs():
    if request.method == 'POST':
        dados = json.loads(request.data)
        devs.append(dados)
        return jsonify({'status': 'sucesso', 'mensagem': 'registro inserido! o id do usuario atual é {}'.format(len(devs) - 1)})
    elif request.method == 'GET':
        return jsonify(devs)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')