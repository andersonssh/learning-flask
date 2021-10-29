from flask import Flask,request, Response, redirect, url_for, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return 'contato inicial'

@app.route('/response')
def responserrrrr():
    return render_template('response.html')

@app.route('/posts')
@app.route('/posts/<int:id>')
def posts(id):
    titulo = request.args.get('titulo')
    data = dict(
        path=request.path,
        referrer=request.referrer,
        content_type=request.content_type,
        method=request.method,
        titulo=titulo,
        id= id if id else 0
    )
    return data

@app.route('/redirect')
def redirecionamento():
    #url_for pega o nome da funcao nao da rota.
    #quando app.route('/redirect') se vincula a funcao, esta funcao esta ligada aquela url
    #o url for cuida para que essa funcao seja acessada independente do caminho da rota
    return redirect(url_for('responserrrrr'))



if __name__ == '__main__':
    app.run(debug=True)