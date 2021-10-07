from flask import Flask, render_template, flash
from datetime import datetime

#IMPORTANDO OS FILTROS!!
import filtro



#outra flag pra a classe Flask pode ser static_folder='nomedapasta' por padrao, é static
app = Flask(__name__, template_folder='views')
app.config['SECRET_KEY'] = 'dev'


#CADASTRANDO FILTROS NO FLASK
#a chave é o nome da funcao dentro do html e o valor é a funcao
app.jinja_env.filters['format_dat'] = filtro.formatar_data
app.jinja_env.filters['teste'] = filtro.teste
app.jinja_env.filters['f3'] = filtro.func3
@app.route('/')
def index():
    #('.html', user = user) o primeiro user é como será chamado dentro do template, e o segundo é o objeto atual da funcao que será passado
    #flash(msg, categoria)
    #flash(message="mesangem", category="categoriaquequiser")
    flash('Mensagem que vou enviar', 'warning' )
    flash('massavelio', 'danger')
    return render_template('index.html', users=users)

@app.route('/users')
def users():
    usuariosss = [{
        'nome': 'marcos souza junior',
        'idade': 10000,
        'email': 'sousajunior@gmail.com',
        'status': True,
        'since': datetime.utcnow()
    }, {
        'nome': 'mahria Joselina',
        'idade': 20002020,
        'email': 'joseina20000000 A.C @gmail.com',
        'status': False,
        'since': datetime.utcnow()
    }
    ]
    return render_template('users.html', users=usuariosss)

@app.route('/condicionaiss')
def condi():
    up = True
    st = 'este é um teste de mensagem.'
    return render_template('condicionais.html', user_page=up, texto=st)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')