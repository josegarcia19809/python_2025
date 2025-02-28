# Función regular
def square(num): return num * num


# Lambda equivalente, se guarda en una variable
square2 = lambda num: num * num

# Otra lambda
add = lambda a, b: a + b

# Ejecutando las lambdas
print(square(2))
print(add(2, 3))

# Nota que la función square tiene nombre, pero las lambda no
print(square.__name__)
print(square2.__name__)
print(add.__name__)

# 4
# 5
# square
# <lambda>
# <lambda>