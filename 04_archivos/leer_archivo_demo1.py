# leer_archivo_demo1.py
import os

os.system("clear")
# Abrir el archivo
nombre_archivo = "salida.txt"
with open(nombre_archivo, "r") as archivo:
    # Leer la primera línea del archivo
    linea = archivo.readline()

    # Desplegar la línea
    print("La primera línea del archivo es: ")
    print(linea)
