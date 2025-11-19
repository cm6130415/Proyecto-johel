from flask import Flask, request, redirect, render_template
import json

app = Flask(__name__)

def cargar_usuarios():
    try:
        with open("usuarios.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    correo = request.form.get("correo")
    contraseña = request.form.get("contraseña")

    usuarios = cargar_usuarios()

    for u in usuarios:
        if u["correo"] == correo and u["contraseña"] == contraseña:
            return redirect("/inicio")

    return "<h3>Usuario o contraseña incorrectos</h3>"

@app.route("/inicio")
def inicio():
    return render_template("inicio.html")

if __name__ == "__main__":
    app.run(debug=True)



