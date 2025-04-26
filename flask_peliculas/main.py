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


# http://127.0.0.1:5000/rating
@app.route("/rating")
def verificar_rating():
    titulo = "The avengers"
    rating = 9
    return render_template("rating.html", titulo=titulo, rating=rating)


# http://127.0.0.1:5000/peliculas
@app.route("/peliculas")
def mostrar_peliculas():
    peliculas = ["Avatar", "Spiderman: No Way Home", "The Batman", "The Lion King"]
    return render_template("peliculas.html", peliculas=peliculas)


if __name__ == "__main__":
    app.run()
