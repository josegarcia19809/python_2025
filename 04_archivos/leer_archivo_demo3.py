# leer_archivo_demo3.py

import os

os.system("clear")

nombre_archivo = input("Dame el nombre del archivo: ")

# Asegurarse de que el archivo exista
if not os.path.exists(nombre_archivo):
    print("El archivo", nombre_archivo, "no existe")
    exit(0)

archivo = open(nombre_archivo, "r")

linea = archivo.readline()
print("La primera línea dice:")
print(linea)

archivo.close()
