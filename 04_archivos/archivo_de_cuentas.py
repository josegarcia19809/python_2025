# archivo_de_cuentas.py

# El siguiente programa crea un archivo que guarda datos de cuentas bancarias

with open("cuentas.txt", mode="w") as cuentas:
    cuentas.write("100 Carolina 24.98\n")
    cuentas.write("200 José 345.90\n")
    cuentas.write("300 Luis 0.0\n")
    cuentas.write("400 Rogelio -42.16\n")
    cuentas.write("500 Rox 224.62\n")
