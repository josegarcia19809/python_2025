from gasto import Gasto
from planificador import Planificador


def menu():
    print("Planificador de gastos")
    print("1.- Agregar gasto")
    print("2.- Mostrar gastos")
    print("3.- Salir")
    return int(input("Elige tu opción: "))


def ingresar_gasto(gastos):
    print("Dame nombre del gasto: ")
    nombre = input()

    mostrar_categorias()
    tipo = input()

    print("Dame cantidad gastada: ")
    cantidad = float(input())

    print("Dame fecha del gasto: ")
    fecha = input()

    nuevo_gasto = Gasto(nombre, tipo, cantidad, fecha)
    gastos.agregar_gasto(nuevo_gasto)


def mostrar_categorias():
    print("Categorias disponibles---")
    print("Ahorro")
    print("Comida")
    print("Casa")
    print("Gastos varios")
    print("Ocio")
    print("Salud")
    print("Suscripciones")
    print("Elige tu categoría: ")


def mostrar_gastos(gastos):
    gastos.mostrar_gastos()


def main():
    planificador_g = Planificador(1000)

    while True:
        opcion = menu()
        if opcion == 1:
            ingresar_gasto(planificador_g)
        elif opcion == 2:
            mostrar_gastos(planificador_g)
        elif opcion == 3:
            break


if __name__ == "__main__":
    main()
