import json

# Paso 1: Cargar la colección si existe, o iniciar vacía
try:
    with open("lista_mascotas.json", "r") as archivo:
        mascotas = json.load(archivo)
except FileNotFoundError:
    mascotas = []

# Paso 2: Pedir datos al usuario
nombre = input("Nombre de la mascota: ")
tipo = input("Tipo de mascota (ej. Perro, Gato): ")
edad = int(input("Edad de la mascota: "))

# Paso 3: Crear la nueva mascota y agregarla
nueva_mascota = {
    "nombre": nombre,
    "tipo": tipo,
    "edad": edad
}
mascotas.append(nueva_mascota)

# Paso 4: Guardar la colección actualizada
with open("lista_mascotas.json", "w") as archivo:
    json.dump(mascotas, archivo, indent=4)

# Confirmación
print(f"Mascota '{nombre}' agregada correctamente.")
