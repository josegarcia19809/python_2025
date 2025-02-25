def sum_all_values(*args):
    total = 0
    for value in args:
        total += value
    print(total)


nums = (1, 2, 3, 4, 5) # tupla
sum_all_values(*nums)

numbers = [10, 2, 3, 4, 5] # lista
sum_all_values(*numbers)


# El código define una función sum_all_values que recibe un número variable de argumentos
# (*args) y calcula la suma de todos ellos. Luego, imprime el resultado.

# Llamadas a la función:
# Se define una tupla nums = (1, 2, 3, 4, 5), y se pasa con *nums, lo que desglosa
# los valores como argumentos individuales.
# Se define una lista numbers = [10, 2, 3, 4, 5], y se pasa con *numbers,
# logrando el mismo efecto.