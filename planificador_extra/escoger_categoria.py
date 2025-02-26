def mostrar_categorias():
    categorias = [
        "Ahorro",
        "Comida",
        "Casa",
        "Gastos varios",
        "Ocio",
        "Salud",
        "Suscripciones"
    ]

    while True:
        print("Categorías disponibles:")
        for i, categoria in enumerate(categorias, start=1):
            print(f"{i}. {categoria}")

        try:
            opcion = int(input("Elige el número de tu categoría: "))
            if 1 <= opcion <= len(categorias):
                return categorias[opcion - 1]  # Retorna el nombre de la categoría elegida
            else:
                print("⚠️ Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("⚠️ Entrada inválida. Ingresa un número válido.")


categoria_seleccionada = mostrar_categorias()
print(f"Has seleccionado: {categoria_seleccionada}")
