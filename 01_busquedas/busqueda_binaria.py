# Programa de búsqueda binaria de un valor en una lista
def busqueda_binaria(valores: list[int], valor_a_buscar: int) -> int:
    bajo: int = 0
    alto: int = len(valores) - 1

    while bajo <= alto:
        mitad: int = (bajo + alto) // 2
        buscando: int = valores[mitad]

        if buscando == valor_a_buscar:
            return mitad
        elif buscando > valor_a_buscar:
            alto = mitad - 1
        else:
            bajo = mitad + 1

    return -1


def main():
    print("Búsqueda binaria")
    arreglo: list[int] = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    valor = int(input("Dame número a buscar: "))
    indice: int = busqueda_binaria(arreglo, valor)

    if indice != -1:
        print(f"El valor {valor} fue encontrado en la posición {indice}")
    else:
        print(f"El valor {valor} no fue encontrado en el arreglo")

    print("-" * 100)


if __name__ == "__main__":
    main()
