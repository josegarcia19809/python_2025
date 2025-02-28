from gasto import Gasto
from planificador import Planificador


def menu():
    print()
    print("-" * 100)
    print("Planificador de gastos")
    print("1.- Agregar gasto")
    print("2.- Mostrar gastos")
    print("3.- Mostrar presupuesto inicial, total de gastos y dinero disponible")
    print("4.- Resetear")
    print("5.- Salir")
    return int(input("Elige tu opción: "))


def mostrar_informacion_presupuesto(gastos):
    print("Mostrando información de su planificador")
    print(f"Presupuesto inicial: ${gastos.obtener_presupuesto_inicial():.2f}")
    print(f"Total de gastos: ${gastos.total_gastos():.2f}")
    print(f"Dinero disponible: ${gastos.obtener_presupuesto_disponible():.2f}")
    print(f"Porcentaje gastado: {gastos.obtener_porcentaje_gastado():.1f}%")


def ingresar_gasto(gastos):
    print("Dame nombre del gasto: ")
    nombre = input()

    tipo = mostrar_categorias()

    print("Dame cantidad a gastar: ")
    cantidad = float(input())
    if not gastos.alcanza_el_dinero(cantidad):
        print("No se alcanza a cubrir el gasto")
        return

    print("Dame fecha del gasto: ")
    fecha = input()

    nuevo_gasto = Gasto(nombre, tipo, cantidad, fecha)
    gastos.agregar_gasto(nuevo_gasto)


def mostrar_categorias() -> str:
    categorias = [
        "Ahorro", "Comida", "Casa", "Gastos varios", "Ocio",
        "Salud", "Suscripciones"
    ]

    print()
    print("-" * 50)
    print("Categorías disponibles")
    for i, categoria in enumerate(categorias, start=1):
        print(f"{i}. {categoria}")

    print("Elige el número de la categoría: ")
    categoria_elegida = int(input())
    # TODO: Corregir si el usuario elige una opción fuera del rango
    return categorias[categoria_elegida - 1]


def mostrar_gastos(gastos):
    gastos.mostrar_gastos()


def main():
    cantidad_inicial = float(input("Dame presupuesto inicial: "))
    planificador_g = Planificador(cantidad_inicial)

    while True:
        opcion = menu()
        if opcion == 1:
            ingresar_gasto(planificador_g)
        elif opcion == 2:
            mostrar_gastos(planificador_g)
        elif opcion == 3:
            mostrar_informacion_presupuesto(planificador_g)
        elif opcion == 4:
            pass
        elif opcion == 5:
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
