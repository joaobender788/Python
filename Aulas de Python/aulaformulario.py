from flask import Flask, request, render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("form.html")
@app.route("/resultado", methods=["POST"])
def resultado():
    nome = request.form["nome"]
    return f"Olá, {nome}! Formulário enviado com sucesso!"
if __name__ == "__main__":
    app.run(debug=True)
