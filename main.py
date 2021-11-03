from flask import Flask, jsonify, request
import json
app = Flask(__name__)

@app.route('/teste/<int:id>')
def pessoa(id):
    return jsonify({'id': id , 'nome': 'Rafael', 'profissao': 'Desenvolvedor'})

# é possivel fazer como no exemplo abaixo, colocar um 2 parametros com o separador que quiser!!!!!!!!!!!!!!!!
@app.route('/soma/<int:valor1>somacom<int:valor2>')
def soma(valor1, valor2):
    return jsonify({'soma': valor1 + valor2})

@app.route('/soma', methods=['POST', 'PUT', 'GET'])
def somapost():
    # o exemplo abaixo retorna valores json com chaves diferentes somente para fim de testes
    if request.method == 'POST':
        dados = json.loads(request.data)
        return jsonify({'POST-soma': sum(dados['valores'])})
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        return jsonify({'PUT-soma': sum(dados['valores'])})
    elif request.method == 'GET':
        return jsonify({'GET-soma': 0})

if __name__ == '__main__':
    app.run(debug=True)