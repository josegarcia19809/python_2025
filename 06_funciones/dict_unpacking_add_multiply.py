def add_and_multiply_numbers(a, b, c, **kwargs):
    print(a + b * c)
    print("OTHER STUFF...")
    print(kwargs)


data = dict(a=1, b=2, c=3, d=55, name="Tony")
add_and_multiply_numbers(**data)

# El código define una función add_and_multiply_numbers que recibe tres parámetros
# obligatorios (a, b, c) y cualquier número adicional de argumentos clave-valor (**kwargs).
#
# Explicación:

# Definición de la función:
# a, b, y c son argumentos requeridos.
# Se imprime el resultado de a + (b * c).
# Se imprime "OTHER STUFF..." como mensaje adicional.
# Se imprime kwargs, que contiene los argumentos adicionales no utilizados en los
# parámetros requeridos.


# Uso de un diccionario para pasar argumentos:
#
# Se crea el diccionario data = dict(a=1, b=2, c=3, d=55, name="Tony").
# Se llama a add_and_multiply_numbers(**data), lo que desglosa el diccionario en
# argumentos clave-valor.
# a=1, b=2, c=3 se asignan a sus respectivos parámetros.
# d=55 y name="Tony" quedan en kwargs porque la función no tiene parámetros para ellos.
# Salida esperada:
# 7
# OTHER STUFF...
# {'d': 55, 'name': 'Tony'}
# (El resultado 7 proviene de 1 + (2 * 3)).
