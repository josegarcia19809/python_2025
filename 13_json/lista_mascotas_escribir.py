import json

# Lista de mascotas (cada una es un diccionario)
mascotas = [
    {"nombre": "Firulais", "tipo": "Perro", "edad": 4},
    {"nombre": "Mishi", "tipo": "Gato", "edad": 2},
    {"nombre": "Luna", "tipo": "Conejo", "edad": 1}
]

# Guardamos la colección en un archivo JSON
with open("lista_mascotas.json", "w") as archivo:
    json.dump(mascotas, archivo, indent=4)