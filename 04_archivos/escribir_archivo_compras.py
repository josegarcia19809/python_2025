# escribir_archivo_compras.py

nombre_archivo = input("Introduce el nombre del archivo: ")
num_articulos = int(input("Cantidad de artículos: "))

salida_archivo = open(nombre_archivo, "w")

for i in range(num_articulos):
    articulo = input(f"Dame artículo #{i + 1}: ")
    salida_archivo.write(f"{i + 1}.- {articulo}\n")

salida_archivo.close()
print("Datos almacenados")
