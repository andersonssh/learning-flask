from flask import Flask, render_template
from flask_mail import Mail, Message
config = {
    'MAIL_SERVER':'smtp.ethereal.email',
    'MAIL_PORT': 587,
    'MAIL_USE_TLS': True,
    'MAIL_DEBUG': True,
    'MAIL_USERNAME': 'shaniya.kirlin84@ethereal.email',
    'MAIL_PASSWORD': 'ESjHKSRN6za9SC5jHb',
    'MAIL_DEFAULT_SENDER': 'Andsu <loko@andsu.com.br>'
}

app = Flask(__name__)
#setando objeto de configuracao para o app de flask
app.config.update(config)
mail = Mail(app)
@app.route('/sendmail')
def sendmail():
    msg = Message(subject='Bem-Vindo(a)',
                  sender=app.config['MAIL_DEFAULT_SENDER'],
                  recipients=['black2018list123@gmail.com'],
                  #body='Ola! esta e uma mensagem automatica!',
                  html=render_template('welcome.html', name="JUAUMZAUM"))
    mail.send(msg)
    return 'e-mail enviado com sucesso!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
