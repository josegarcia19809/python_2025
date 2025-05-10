from flask import (
    Flask,
    redirect,
    url_for,
    render_template,
    request,
    flash,
    get_flashed_messages,
)

import json
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# Ruta GET: muestra el formulario
# http://127.0.0.1:5000/alta
@app.route("/alta", methods=["GET"])
def mostrar_formulario():
    return render_template("alta.html")


# Ruta POST: recibe los datos del formulario
@app.route("/registrar", methods=["POST"])
def registrar_usuario():
    nombre = request.form["nombre"]
    correo = request.form["correo"]
    mensaje = request.form["mensaje"]

    datos = []
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as archivo:
            datos = json.load(archivo)

    nuevo_id = datos[-1]["id"] + 1 if datos else 1

    nuevo_usuario = {
        "id": nuevo_id,
        "nombre": nombre,
        "correo": correo,
        "mensaje": mensaje,
    }

    datos.append(nuevo_usuario)

    with open("usuarios.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

    return redirect("/usuarios")


@app.route("/usuarios")
def ver_usuarios():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as archivo:
            datos = json.load(archivo)
    else:
        datos = []

    return render_template("usuarios.html", datos=datos)


if __name__ == "__main__":
    app.run()
