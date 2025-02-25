class Gasto:
    def __init__(self, nombre: str, tipo: str, cantidad: float, fecha: str):
        self._nombre = nombre
        self._tipo = tipo
        self._cantidad = cantidad
        self._fecha = fecha

    def get_nombre(self) -> str:
        return self._nombre

    def set_nombre(self, nombre: str) -> None:
        self._nombre = nombre

    def get_tipo(self) -> str:
        return self._tipo

    def set_tipo(self, tipo: str) -> None:
        self._tipo = tipo

    def get_cantidad(self) -> float:
        return self._cantidad

    def set_cantidad(self, cantidad: float) -> None:
        self._cantidad = cantidad

    def get_fecha(self) -> str:
        return self._fecha

    def set_fecha(self, fecha: str) -> None:
        self._fecha = fecha

    def mostrar_info(self) -> str:
        return f"Gasto: {self._nombre}, Tipo: {self._tipo}, Cantidad: {self._cantidad}, Fecha: {self._fecha}"
