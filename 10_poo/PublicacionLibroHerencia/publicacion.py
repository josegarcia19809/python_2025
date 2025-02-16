class Publicacion:
    def __init__(self, titulo: str, autor: str):
        self._titulo = titulo
        self._autor = autor

    def get_titulo(self) -> str:
        return self._titulo

    def get_autor(self) -> str:
        return self._autor

    def set_titulo(self, titulo: str) -> None:
        self._titulo = titulo

    def set_autor(self, autor: str) -> None:
        self._autor = autor

    def __str__(self) -> str:
        return f"Título: {self._titulo}\nAutor: {self._autor}"


class LibroBiblioteca(Publicacion):
    def __init__(self, titulo: str, autor: str, isbn: str, cantidad_disponible: int):
        super().__init__(titulo, autor)
        self._isbn = isbn
        self._cantidad_disponible = cantidad_disponible

    def get_isbn(self) -> str:
        return self._isbn

    def get_cantidad_disponible(self) -> int:
        return self._cantidad_disponible

    def set_cantidad_disponible(self, cantidad_disponible: int) -> None:
        self._cantidad_disponible = cantidad_disponible

    def set_isbn(self, isbn: str) -> None:
        self._isbn = isbn

    def __str__(self) -> str:
        return (f"{super().__str__()}\nISBN: {self._isbn}\n"
                f"Cantidad disponible: {self._cantidad_disponible}")
