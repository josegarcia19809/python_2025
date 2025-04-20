import json

# Paso 1: Leer la colección existente (si el archivo existe)
try:
    with open("lista_mascotas.json", "r") as archivo:
        mascotas = json.load(archivo)
except FileNotFoundError:
    mascotas = []  # Si no existe, empezamos con una lista vacía

# Paso 2: Crear una nueva mascota
nueva_mascota = {
    "nombre": "Rocky",
    "tipo": "Tortuga",
    "edad": 10
}

# Paso 3: Agregar la nueva mascota a la lista
mascotas.append(nueva_mascota)

# Paso 4: Guardar la lista actualizada en el archivo JSON
with open("lista_mascotas.json", "w") as archivo:
    json.dump(mascotas, archivo, indent=4)

# Confirmación
print("Mascota agregada correctamente.")