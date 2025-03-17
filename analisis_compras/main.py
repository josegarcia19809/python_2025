# main.py
from lista_compras import compras
from compra_comida import CompraComida

from itertools import groupby


def agrupar_por_ciudad():
    # Primero ordenamos por ciudad
    compras_ordenadas_por_ciudad = sorted(compras, key=lambda compra: compra.ciudad)

    # Y después agrupamos
    grupos_por_ciudad = groupby(compras_ordenadas_por_ciudad,
                                key=lambda compra: compra.ciudad)
    for ciudad, ciudades_en_grupo in grupos_por_ciudad:
        print(f"Ciudad: {ciudad}")
        for ciudad_elemento in ciudades_en_grupo:
            print(f"    - {ciudad_elemento.nombre} {ciudad_elemento.frecuencia}")
        imprimir_linea()


def agrupar_por_frecuencia():
    pass


def agrupar_por_genero():
    pass


def imprimir_linea():
    print("-" * 100)


def imprimir_tabla(lista_compras: list[CompraComida]):
    encabezado = (
        f"{'Nombre':<10}"
        f"{'Género':<12}"
        f"{'Ciudad':<14}"
        f"{'Frecuencia':<17}"
        f"{'Artículo':<10}"
        f"{'Gasto':>8}"
    )
    print(encabezado)
    imprimir_linea()
    for compra in lista_compras:
        print(compra)


def ordenar_datos():
    # Ordenar las compras por nombre del cliente
    imprimir_linea()
    compras_nombre = sorted(compras, key=lambda compra: compra.nombre)
    print("******************Ordenar por nombre del cliente")
    imprimir_tabla(compras_nombre)

    # Ordenar las compras por ciudad

    # Ordenar las compras por frecuencia


def main():
    imprimir_tabla(compras)
    imprimir_linea()
    ordenar_datos()
    imprimir_linea()
    agrupar_por_ciudad()


if __name__ == "__main__":
    main()
