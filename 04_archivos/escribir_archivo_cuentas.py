# escribir_archivo_cuentas.py

import os
import sys

nombre_archivo = input("Dame nombre del archivo: ")
# Asegurarse de que el archivo no exista
if os.path.exists(nombre_archivo):
    print(f"El archivo {nombre_archivo} ya existe")
    sys.exit()

num_cuentas = int(input("Dame número de cuentas: "))
salida_archivo = open(nombre_archivo, "w")
for i in range(num_cuentas):
    print()
    no_cuenta = int(input(f"Número de cuenta #{i + 1}: "))
    nombre = input("Dame nombre del cliente: ")
    saldo = float(input("Dame saldo del cliente: "))
    salida_archivo.write(f"{no_cuenta} {nombre} {saldo}\n")

salida_archivo.close()
print("Datos guardados")
