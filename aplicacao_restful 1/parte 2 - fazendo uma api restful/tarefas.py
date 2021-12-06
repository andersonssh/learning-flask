#exercicio de tarefas

from flask import Flask, request, jsonify
import json

app = Flask(__name__)

tasks = [
    {
     'responsavel': 'BOT',
     'tarefa': 'Manuntenção nos servidores',
     'status': 'incompleto',
     }
]
@app.route('/tarefas/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def tarefas(id):
    #retorna erro caso o id nao corresponda a nenhuma tarefa
    if id >= len(tasks):
        return jsonify({'status': 'fracasso', 'mensagem': 'o id inserido nao corresponde a nenhuma tarefa'})
    else:
        if request.method == 'GET':
            response = tasks[id]
            return jsonify(response)
        elif request.method == 'PUT':
            #modificar status
            try:
                dados = json.loads(request.data)

                if dados['status'] == 'completo' or dados['status'] == 'incompleto':
                    tasks[id]['status'] = dados['status']
                    response = {'status': 'sucesso', 'mensagem': 'status modificado!'}
                else:
                    response = {'status': 'fracasso', 'mensagem': 'os unicos valores de status que podem ser adicionados sao "completo" ou "incompleto"'}
            except KeyError:
                response = {'status': 'fracasso', 'mensagem': 'o json deve conter "status": "completo" ou "incompleto"'}

            return jsonify(response)

        elif request.method == 'DELETE':
            tasks.pop(id)
            return jsonify({'status': 'sucesso', 'mensagem': 'tarefa deletada'})

#retorna lista de tarefas e adiciona novas tarefas
@app.route('/tarefas', methods=['POST', 'GET'])
def lista_tarefas():
    if request.method == 'POST':
        dados = json.loads(request.data)
        #adicionando id automaticamente de acordo com o tamanho da lista
        tasks.append(dados)
        return jsonify({'status': 'sucesso', 'mensagem': 'a tarefa foi adicionada'})
    elif request.method == 'GET':
        return jsonify(tasks)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
