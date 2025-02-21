from cancion import Cancion
from catalogo import Catalogo


def imprimir_linea():
    print("-" * 80)


def menu() -> int:
    imprimir_linea()
    print("Operaciones sobre canciones")
    print("1. Añadir una canción")
    print("2. Mostrar lista de canciones")
    print("3. Buscar canción")
    print("4. Salir")
    return int(input("Elige tu opción: "))


def pedir_datos_cancion(catalogo: Catalogo):
    clave = int(input("Dame la clave de la canción: "))
    nombre_cancion = input("Dame el nombre de la canción: ")
    nombre_cantante = input("Dame el nombre del cantante: ")
    genero = input("Dame el género: ")
    album = input("Dame el nombre del álbum: ")
    precio = float(input("Dame precio: "))

    nueva_cancion = Cancion(
        clave, nombre_cancion, nombre_cantante, genero, album, precio
    )

    catalogo.insertar_cancion(nueva_cancion)


def buscar_cancion(catalogo: Catalogo):
    clave = int(input("Dame clave de la canción: "))
    cancion_encontrada = catalogo.buscar_por_clave(clave)
    if cancion_encontrada is None:
        print("Canción no encontrada")
    else:
        imprimir_cancion(cancion_encontrada)


def imprimir_cancion(cancion: Cancion):
    imprimir_linea()
    print("Datos de la canción")
    print(f"Nombre: {cancion.nombre_cancion}")
    print(f"Cantante: {cancion.nombre_cantante}")
    print(f"Género: {cancion.genero}")
    print(f"Álbum: {cancion.album}")
    print(f"Precio: {cancion.precio}")


def ver_catalogo(catalogo: Catalogo):
    encabezado = (
        f"{'Clave':<8}|"
        f"{'Nombre canción':<30}|"
        f"{'Artista':<30}|"
        f"{'Precio':>8}"
    )
    imprimir_linea()
    print(encabezado)
    imprimir_linea()

    for cancion in catalogo.obtener_lista_canciones():
        registro = (
            f"{cancion.clave:<8}|"
            f"{cancion.nombre_cancion:<30}|"
            f"{cancion.nombre_cantante:<30}|"
            f"${cancion.precio:<8.2f}"
        )
        print(registro)


def main():
    catalogo = Catalogo()
    ver_catalogo(catalogo)

    while True:
        opcion = menu()
        if opcion == 1:
            imprimir_linea()
            pedir_datos_cancion(catalogo)
            ver_catalogo(catalogo)
        elif opcion == 2:
            ver_catalogo(catalogo)
        elif opcion == 3:
            buscar_cancion(catalogo)
        elif opcion == 4:
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
