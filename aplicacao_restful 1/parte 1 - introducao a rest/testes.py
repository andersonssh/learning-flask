import requests

#enviando requisicao GET
response = requests.get('http://127.0.0.1:5000/soma')
#os dados de requests podem ser recebidos diretamente em json
dados = response.json()

print('Mostrando resposta da requisicao GET')
print(dados)

response = requests.post('http://127.0.0.1:5000/soma', json={'valores': [10, 20, 30]})

print('Mostrando resposta da requisicao POST em texto')
print(response.text)
print('Mostrando resposta da requisicao POST em formato json')
print(response.json())


