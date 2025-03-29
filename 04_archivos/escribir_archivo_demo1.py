# escribir_archivo_demo1.py

with open("salida.txt", "w") as archivo_salida:
    # Escribir en el archivo
    archivo_salida.write("Hola, mundo!\n")
    
print("Datos grabados en el archivo")