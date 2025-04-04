# leer_archivo_demo1_v2.py

# Abrir el archivo
nombre_archivo = "salida.txt"
archivo = open(nombre_archivo, "r")

# Leer la primera línea del archivo
linea = archivo.readline()

# Desplegar la línea
print("La primera línea del archivo es ")
print(linea)

# Cerrar el archivo
archivo.close()
