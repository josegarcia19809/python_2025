# El set comprehension en Python es una forma concisa y eficiente de crear conjuntos (set) usando
# una sintaxis similar a la de las listas por comprensión (list comprehension),
# pero con llaves {} en lugar de corchetes [].

# Sintaxis:

# {expresión for variable in iterable if condición}

# Creando un conjunto de valores al cuadrado de los valores 0 a 9
cuadrados = {x ** 2 for x in range(10)}
print(cuadrados)

print("-" * 100)

# Creando un conjunto de letras en mayusculas de la palabra "hello"
print({char.upper() for char in "hello"})
print("-" * 100)

# Se define una variable texto con la cadena "Buenos dias".
#
# print({letra for letra in texto if letra in "aeiou"})
# Se crea un set comprehension que:
#
# Itera sobre cada letra de texto.
# Filtra solo las letras que están en "aeiou" (las vocales minúsculas).
# Las agrega a un conjunto {} para eliminar duplicados.
# Se imprime el conjunto resultante.

texto = "Buenos dias"
print({letra for letra in texto if letra in "aeiou"})

# Este código verifica si el número de vocales únicas en texto es igual a 5 y devuelve True o False.
print(len({letra for letra in texto if letra in "aeiou"}) == 5)
