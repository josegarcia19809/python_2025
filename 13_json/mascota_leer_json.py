import json

# Leemos el archivo JSON y lo convertimos a un diccionario
with open("mascota.json", "r") as archivo:
    datos_mascota = json.load(archivo)

# Mostramos los datos
print(datos_mascota)

# Accedemos a campos específicos
print("Nombre:", datos_mascota["nombre"])
print("Tipo:", datos_mascota["tipo"])
print("Edad:", datos_mascota["edad"])