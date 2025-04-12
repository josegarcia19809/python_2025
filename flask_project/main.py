from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def index():
    # http://127.0.0.1:5000
    return render_template("index.html")


@app.route("/informacion")
def informacion():
    return "<h1>Página de información</h1>"


@app.route("/contacto")
def contacto():
    # http://127.0.0.1:5000/contacto
    return "<h1>Mi nombre es José Luis García</h1>"


@app.route("/lenguajes-de-programacion")
def lenguajes():
    # http://127.0.0.1:5000/lenguajes-de-programacion
    return """
    <h1>Lenguajes de programación</h1>
    <p>Python</p>
    <p>Java</p>
    <p>JavaScript</p>
    <p>C++</p>
    <p>C#</p>
    """


@app.route("/recibir-nombre/<nombre>")
def recibir_nombre(nombre):
    # http://127.0.0.1:5000/recibir-nombre/luis
    return f"""
        <h1>Página de información</h1>
        <h3>Bienvenido {nombre}</h3>
    """


@app.route("/mostrar-calificacion/<nombre>/<promedio>")
def mostrar_calificacion(nombre, promedio):
    # http://127.0.0.1:5000/mostrar-calificacion/José/9.0
    return f"""
        <h1>Página de información</h1>
        <h3>Datos del alumno</h3>
        <h4>Bienvenido {nombre}</h4>
        <p>Tu promedio es {promedio}</p>
    """


@app.route("/mostrar-precio-producto/<string:producto>/<float:precio>")
def mostrar_precio_producto(producto, precio):
    # http://127.0.0.1:5000/mostrar-precio-producto/Coca%20Cola/15.00
    return f"""
        <h1>Página de información</h1>
        <h3>Datos del producto {producto}</h3>
        <p>Precio ${precio:,.2f}</p>
    """


@app.route("/mostrar-tipo-vehiculo")
@app.route("/mostrar-tipo-vehiculo/<tipo>")
def mostrar_tipo_vehiculo(tipo=None):
    # http://127.0.0.1:5000/mostrar-tipo-vehiculo
    # http://127.0.0.1:5000/mostrar-tipo-vehiculo/motocicleta
    texto = ""
    if tipo is not None:
        texto = f"Tipo de vehiculo {tipo}"
    return f"""
        <h1>Página de información</h1>
        <p>Datos del vehiculo</p>
        {texto}
    """


@app.route("/mostrar-contacto")
def mostrar_contacto():
    # http://127.0.0.1:5000/mostrar-contacto
    return redirect(url_for("contacto"))  # Poner el nombre de la función de la ruta


@app.route("/tarjeta")
def tarjeta():
    # http://127.0.0.1:5000/tarjeta
    return render_template("tarjeta.html")


if __name__ == "__main__":
    app.run()
