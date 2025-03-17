# compra_comida.py

class CompraComida:
    def __init__(self, nombre: str, genero: str, ciudad: str, frecuencia: str,
                 articulo: str, gasto: float):
        self.nombre = nombre
        self.genero = genero
        self.ciudad = ciudad
        self.frecuencia = frecuencia
        self.articulo = articulo
        self.gasto = gasto

    def __str__(self):
        datos = (
            f"{self.nombre:<10}"
            f"{self.genero:<12}"
            f"{self.ciudad:<14}"
            f"{self.frecuencia:<17}"
            f"{self.articulo:<10}"
            f"{self.gasto:>8.2f}"
        )
        return datos
