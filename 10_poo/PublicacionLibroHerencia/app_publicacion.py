from publicacion import Publicacion, LibroBiblioteca


def imprimir_linea():
    print()
    print("-" * 100)


def prueba_libro_biblioteca():
    libro1 = LibroBiblioteca("Cien años de soledad", "Gabriel García Márquez",
                             "9781234567890", 12)
    libro2 = LibroBiblioteca("El Quijote", "Miguel de Cervantes",
                             "9789834567890", 8)
    libro3 = LibroBiblioteca("La sombra del viento", "Carlos Ruiz",
                             "97834567890", 20)

    print(libro1)
    imprimir_linea()
    print(libro2)
    imprimir_linea()
    print(libro3)
    imprimir_linea()
    
    print("Solo titulos de libros*****************")
    print(libro1.get_titulo())
    print(libro2.get_titulo())
    print(libro3.get_titulo())


def main():
    prueba_libro_biblioteca()


if __name__ == '__main__':
    main()
