from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def index():
    mensaje_bienvenida = "Bienvenido a su sitio de películas"
    titulo = "The Avengers"
    genero = "Action"
    anio_estreno = 2012
    rating = 8.1
    vigente = True
    fecha_resenia = "25 de abril de 2025"

    return render_template("index.html", mensaje=mensaje_bienvenida,
                           titulo=titulo,
                           genero=genero,
                           anio_estreno=anio_estreno,
                           rating=rating,
                           vigente=vigente,
                           fecha_resenia=fecha_resenia)


if __name__ == "__main__":
    app.run()
