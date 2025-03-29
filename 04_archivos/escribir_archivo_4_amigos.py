# escribir_archivo_4_amigos.py
# Cómo le harían para que aparezcan 4 lineas
# en un archivo que se llame amigos4.txt, donde
# cada línea contenga el nombre de alguno de sus
# amigos

with open("amigos4.txt", "w") as archivo_salida:
    archivo_salida.write("Rox\n")
    archivo_salida.write("Mary\n")
    archivo_salida.write("Isaac\n")
    archivo_salida.write("Carolina\n")
    
print("Datos amigos guardados")
