class Pelicula:
    def __init__(
        self, idx: int, nombre: str, genero: str, anio: int, calificacion_imdb: float
    ):
        self.id = idx
        self.nombre = nombre
        self.genero = genero
        self.anio = anio
        self.calificacion_imdb = calificacion_imdb

    def __str__(self):
        nombre = self.nombre if len(self.nombre) < 45 else self.nombre[:45] + '...'
        return (
            f"{self.id:>7}"
            f"{nombre:>50} "
            f"{self.genero:>15} "
            f"{self.anio:>6} "
            f"{self.calificacion_imdb:>10}"
        )
