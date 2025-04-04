# crear_archivos_amigos.py

import os

os.system("clear")

nombre_archivo = "amigos4.txt"
archivo = open(nombre_archivo, "r")
for linea in archivo.readlines():
    if linea[-1] == "\n":
        linea = linea[:-1]
    nuevo_archivo = open(f"invitaciones_{linea.lower()}.txt", "w")
    nuevo_archivo.write(f"Hola {linea}\n")
    nuevo_archivo.write(f"Estás invitado(a) a mi fiesta de graduación")
    nuevo_archivo.close()
archivo.close()
