import json

# Creamos un diccionario que representa una mascota
mascota = {
    "nombre": "Firulais",
    "tipo": "Perro",
    "edad": 4
}

# Convertimos el diccionario a JSON
mascota_json = json.dumps(mascota, indent=4)

# Mostramos el JSON
print(mascota_json)

# Guardamos el JSON en un archivo
with open("mascota.json", "w") as archivo:
    json.dump(mascota, archivo, indent=4)