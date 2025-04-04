# leer_archivo_4_amigos.py

import os

os.system("clear")

nombre_archivo = "amigos4.txt"
archivo = open(nombre_archivo, "r")
for linea in archivo.readlines():
    if linea[-1] == "\n":
        linea = linea[:-1]
    print(linea)
archivo.close()
