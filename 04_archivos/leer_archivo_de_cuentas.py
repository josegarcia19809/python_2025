# leer_archivo_de_cuentas.py
import os

os.system("clear")

with open("cuentas.txt", mode="r") as cuentas:
    print(f"{'Cuenta':<10}{'Nombre':<12}{'Balance':>10}")
    for registro in cuentas:
        cuenta, nombre, balance = registro.split()
        print(f"{cuenta:<10}{nombre:<12}{balance:>10}")
