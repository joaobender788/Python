from flask import Flask, request, render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("form.html")
@app.route("/resultado", methods=["GET"])
def resultado():
    nome = request.form["nome"]
    idade = request.form["idade"]
    cidade = request.form["cidade"]
    return f"Olá, {nome}! você tem {idade} anos e mora em {cidade}."
if __name__ == "__main__":
    app.run(debug=True)
