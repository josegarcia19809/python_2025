# escribir_archivo_pedir_amigos.py
# El programa primero nos debe pedir cuántos
# amigos tenemos. Según el número de amigos que
# le hayamos dado, nos pedirá los datos.
# Escribirá dichos nombres en un archivo de texto

amigos = int(input("Cuántos amigos tienes? "))

with open("mis_amigos.txt", "w") as salida_archivo:
    for i in range(amigos):
        nombre = input(f"Dame nombre amigo #{i + 1}: ")
        salida_archivo.write(f"{nombre}\n")

print("Archivo guardado")
