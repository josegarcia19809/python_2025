def display_names(first, second):
    print(f"{first} says hello to {second}")


names = {"first": "José", "second": "María"}
display_names(**names)


# El código define una función display_names que recibe dos parámetros (first y second)
# y muestra un mensaje en el que first saluda a second.
#
# Explicación:
# Definición de la función:
#
# first y second son parámetros de la función.
# Se usa una f-string (f"{first} says hello to {second}") para imprimir el mensaje.

# Uso de un diccionario para pasar argumentos:
# Se crea el diccionario names = {"first": "José", "second": "María"}.
# Al llamar display_names(**names), el operador ** desglosa el diccionario en
# argumentos clave-valor, asignando "José" a first y "María" a second.
# Salida esperada:

# José says hello to María