class Cancion:
    def __init__(
        self,
        clave: int,
        nombre_cancion: str,
        nombre_cantante: str,
        genero: str,
        album: str,
        precio: float,
    ):
        self.clave = clave
        self.nombre_cancion = nombre_cancion
        self.nombre_cantante = nombre_cantante
        self.genero = genero
        self.album = album
        self.precio = precio
