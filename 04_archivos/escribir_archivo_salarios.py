# escribir_archivo_salarios.py

# Pedir la cantidad de salarios
cantidad = int(input("Dame cantidad de salarios: "))

# Abrir el archivo
salida_archivo = open("salarios_lista.txt", "w")

# Escribir los salarios
for i in range(cantidad):
    salario = float(input("Dame salario: "))
    salida_archivo.write(f"{salario}\n")

# Cerrar el archivo
salida_archivo.close()
print("Lista de salarios guardada")
