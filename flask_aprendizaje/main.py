from flask import Flask, redirect, url_for, render_template, request, flash, \
    get_flashed_messages

import json
import os

app = Flask(__name__)
app.secret_key = "mi_clave_secreta_segura"


# 4. Herencia de plantillas
# http://127.0.0.1:5000
# @app.route("/")
# def index():
#     return render_template("index.html")



# Ruta GET: muestra el formulario
@app.route("/alta", methods=["GET"])
def mostrar_formulario():
    return render_template("alta.html")


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
        "mensaje": mensaje
    }

    datos.append(nuevo_usuario)

    with open("usuarios.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

    flash("Usuario registrado exitosamente.")
    return redirect("/usuarios")


@app.route("/usuarios")
def ver_usuarios():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as archivo:
            datos = json.load(archivo)
    else:
        datos = []

    return render_template("usuarios.html", datos=datos)


@app.route("/eliminar/<int:id>")
def eliminar_usuario(id):
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as archivo:
            datos = json.load(archivo)

        datos = [u for u in datos if u["id"] != id]

        with open("usuarios.json", "w") as archivo:
            json.dump(datos, archivo, indent=4)

        flash("Usuario eliminado.")

    return redirect("/usuarios")

@app.route("/editar/<int:id>", methods=["GET"])
def mostrar_edicion(id):
    if not os.path.exists("usuarios.json"):
        return redirect("/usuarios")

    with open("usuarios.json", "r") as archivo:
        datos = json.load(archivo)

    usuario = next((u for u in datos if u["id"] == id), None)

    if usuario is None:
        flash("Usuario no encontrado.")
        return redirect("/usuarios")

    return render_template("editar.html", usuario=usuario)


@app.route("/actualizar/<int:id>", methods=["POST"])
def actualizar_usuario(id):
    if not os.path.exists("usuarios.json"):
        return redirect("/usuarios")

    with open("usuarios.json", "r") as archivo:
        datos = json.load(archivo)

    usuario = next((u for u in datos if u["id"] == id), None)

    if usuario:
        usuario["nombre"] = request.form["nombre"]
        usuario["correo"] = request.form["correo"]
        usuario["mensaje"] = request.form["mensaje"]

        with open("usuarios.json", "w") as archivo:
            json.dump(datos, archivo, indent=4)

        flash("Usuario actualizado.")
    else:
        flash("Usuario no encontrado.")

    return redirect("/usuarios")

@app.route("/detalle/<int:id>")
def detalle_usuario(id):
    if not os.path.exists("usuarios.json"):
        return redirect("/usuarios")

    with open("usuarios.json", "r") as archivo:
        datos = json.load(archivo)

    usuario = next((u for u in datos if u["id"] == id), None)

    if usuario is None:
        flash("Usuario no encontrado.")
        return redirect("/usuarios")

    return render_template("detalle.html", usuario=usuario)


if __name__ == "__main__":
    app.run()
