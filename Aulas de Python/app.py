from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/user/<nome>")
def user(nome):
    return render_template("usuario.html", nome=nome)
if __name__ == "__main__":
    app.run(debug=True)