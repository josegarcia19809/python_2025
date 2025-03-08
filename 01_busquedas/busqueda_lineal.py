# Programa de búsqueda secuencial de un valor en una lista

def buscar(valor_a_buscar: int, lista_numeros: list[int]) -> int:
    for i in range(0, len(lista_numeros)):
        if lista_numeros[i] == valor_a_buscar:
            return i

    return -1


def main():
    print("Búsqueda secuencial")
    edades: list[int] = [23, 57, 87, 12, 60, 45, 11, 15, 99, 65, 2, 43]
    numero_a_buscar = int(input("Dame número a buscar: "))

    indice: int = buscar(numero_a_buscar, edades)
    if indice == -1:
        print("No se encontró")
    else:
        print(f"Se encontró en la posición {indice}")


if __name__ == "__main__":
    main()
    print("-"*100)
