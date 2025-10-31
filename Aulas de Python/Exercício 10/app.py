from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    nome = request.form['nome']
    idade = request.form['idade']
    cidade = request.form['cidade']
    email = request.form['email']
    telefone = request.form['telefone']
    return f"<h2>Olá {nome}, você tem {idade} anos e mora em {cidade}! Seu e-mail é {email} e seu telefone é {telefone}.</h2>"
if __name__ == '__main__':
    app.run(debug=True)