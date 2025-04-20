import json

# Función para cargar las mascotas
def cargar_mascotas():
    try:
        with open("lista_mascotas.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

# Función para guardar las mascotas
def guardar_mascotas(mascotas):
    with open("lista_mascotas.json", "w") as archivo:
        json.dump(mascotas, archivo, indent=4)

# Función para mostrar la lista de mascotas
def mostrar_mascotas(mascotas):
    if not mascotas:
        print("No hay mascotas registradas.")
    else:
        for i, mascota in enumerate(mascotas):
            print(f"{i+1}. {mascota['nombre']} - {mascota['tipo']} - {mascota['edad']} años")

# Función para agregar una mascota
def agregar_mascota(mascotas):
    nombre = input("Nombre: ")
    tipo = input("Tipo: ")
    edad = int(input("Edad: "))
    mascotas.append({"nombre": nombre, "tipo": tipo, "edad": edad})
    print("Mascota agregada.")

# Función para editar una mascota
def editar_mascota(mascotas):
    nombre_buscar = input("Nombre de la mascota a editar: ")
    for mascota in mascotas:
        if mascota["nombre"].lower() == nombre_buscar.lower():
            print(f"Editando a {mascota['nombre']}")
            mascota["nombre"] = input(f"Nuevo nombre (actual: {mascota['nombre']}): ") or mascota["nombre"]
            mascota["tipo"] = input(f"Nuevo tipo (actual: {mascota['tipo']}): ") or mascota["tipo"]
            edad_nueva = input(f"Nueva edad (actual: {mascota['edad']}): ")
            if edad_nueva:
                mascota["edad"] = int(edad_nueva)
            print("Mascota actualizada.")
            return
    print("Mascota no encontrada.")

def eliminar_mascota(mascotas):
    nombre_buscar = input("Nombre de la mascota a eliminar: ")
    for i, mascota in enumerate(mascotas):
        if mascota["nombre"].lower() == nombre_buscar.lower():
            confirmacion = input(f"¿Estás seguro de eliminar a {mascota['nombre']}? (s/n): ")
            if confirmacion.lower() == "s":
                mascotas.pop(i)
                print("Mascota eliminada.")
            else:
                print("Eliminación cancelada.")
            return
    print("Mascota no encontrada.")

def buscar_por_tipo(mascotas):
    tipo_buscar = input("Tipo de mascota a buscar (ej. Perro): ").lower()
    encontrados = [m for m in mascotas if m["tipo"].lower() == tipo_buscar]
    if encontrados:
        print(f"\nMascotas tipo '{tipo_buscar}':")
        mostrar_mascotas(encontrados)
    else:
        print("No se encontraron mascotas de ese tipo.")

# Programa principal
mascotas = cargar_mascotas()

while True:
    print("\n--- Menú Mascotas ---")
    print("1. Ver mascotas")
    print("2. Agregar mascota")
    print("3. Editar mascota")
    print("4. Eliminar mascota")
    print("5. Buscar por tipo")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        mostrar_mascotas(mascotas)
    elif opcion == "2":
        agregar_mascota(mascotas)
        guardar_mascotas(mascotas)
    elif opcion == "3":
        editar_mascota(mascotas)
        guardar_mascotas(mascotas)
    elif opcion == "4":
        eliminar_mascota(mascotas)
        guardar_mascotas(mascotas)
    elif opcion == "5":
        buscar_por_tipo(mascotas)
    elif opcion == "6":
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")