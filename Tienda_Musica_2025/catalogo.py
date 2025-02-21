from cancion import Cancion
from archivo_canciones import datos_canciones


class Catalogo:
    def __init__(self):
        self.lista_canciones = self.cargar_canciones_desde_diccionario()

    def insertar_cancion(self, nueva_cancion: Cancion):
        self.lista_canciones.append(nueva_cancion)

    def obtener_lista_canciones(self):
        return self.lista_canciones

    def buscar_por_clave(self, clave: int):
        for cancion in self.lista_canciones:
            if cancion.clave == clave:
                return cancion
        return None

    def cargar_canciones_desde_diccionario(self):
        return [Cancion(**datos) for datos in datos_canciones]