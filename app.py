from flask import Flask, render_template, flash

app = Flask(__name__, template_folder='views')
app.config['SECRET_KEY'] = 'dev'

@app.route('/')
def index():
    user = {
        'name': 'marcos souza junior',
        'idade': 10000,
        'email': 'sousajunior@gmail.com'
    }
    #('.html', user = user) o primeiro user é como será chamado dentro do template, e o segundo é o objeto atual da funcao que será passado
    flash('Mensagem que vou enviar' )
    flash('massavelio')
    return render_template('index.html', user=user)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')