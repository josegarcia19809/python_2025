import csv

from pelicula import Pelicula

peliculas = []


def leer_archivo_csv():
    with open("imdb.csv", mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for linea in lector:
            pelicula = Pelicula(
                int(linea["id"]),
                linea["nombre"],
                linea["genero"],
                int(linea["año"]),
                linea["calificacion_imdb"],
            )
            peliculas.append(pelicula)


def imprimir_lista_peliculas():
    print("Peliculas")
    print(f"{'id':>7} {'nombre':>50} {'género':>15} {'Año':>6} {'Calificación':>10}")
    print("-" * 60)
    for pelicula in peliculas:
        print(pelicula)


def filtrado_por_genero(genero):
    print(f"Peliculas del género {genero}")
    print(f"{'id':>7} {'nombre':>50} {'género':>15} {'Año':>6} {'Calificación':>10}")
    print("-" * 60)
    for pelicula in peliculas:
        if pelicula.genero == genero:
            print(pelicula)


# Quiero ver todas las peliculas de action que estén dentro de los años 2012 y 2013
def peliculas_action_2000_2001():
    print(f"Peliculas del género action")
    print(f"{'id':>7} {'nombre':>50} {'género':>15} {'Año':>6} {'Calificación':>10}")
    print("-" * 60)
    for pelicula in peliculas:
        if pelicula.genero == "action" and 2012 <= pelicula.anio <= 2013:
            print(pelicula)


def main():
    leer_archivo_csv()
    imprimir_lista_peliculas()
    print("-"*100)
    filtrado_por_genero("horror")
    print("-" * 100)
    peliculas_action_2000_2001()


if __name__ == "__main__":
    main()
