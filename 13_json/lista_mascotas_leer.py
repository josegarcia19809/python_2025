import json
# Leer el archivo y cargar la lista de mascotas
with open("lista_mascotas.json", "r") as archivo:
    mascotas_cargadas = json.load(archivo)

# Mostramos cada mascota
for mascota in mascotas_cargadas:
    print(f"{mascota['nombre']} es un {mascota['tipo']} de {mascota['edad']} años")