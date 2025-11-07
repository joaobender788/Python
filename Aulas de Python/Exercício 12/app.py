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
    curso = request.form['curso']
    email = request.form['email']
# Enviando os dados para o template resultado.html
    return render_template('resultado.html', nome=nome, idade=idade, cidade=cidade)

if __name__ == '__main__':
    app.run(debug=True)
