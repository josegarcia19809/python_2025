# El siguiente código define una función llamada suma_todos_elementos, que permite sumar una cantidad
# variable de números enteros.
#
# La función utiliza el parámetro *args, lo que le permite recibir un número indeterminado de argumentos.
# Dentro de la función, se inicializa una variable total con un valor de 0. Luego, se recorre cada
# número recibido en args mediante un bucle for, sumándolo a total. Finalmente, la función retorna el
# valor acumulado de la suma.
#
# Después de definir la función, el código la ejecuta en dos ocasiones:
#
# Primero, con los números 4, 6, 8, 12 y 23, lo que devuelve 53.
# Luego, con los números 4 y 6, obteniendo como resultado 10.
# De esta forma, la función permite realizar la suma de cualquier cantidad de números sin necesidad de
# definir explícitamente cuántos argumentos recibirá.

def suma_todos_elementos(*args) -> int:
    total = 0
    for elemento in args:
        total += elemento
    return total


print(suma_todos_elementos(4, 6, 8, 12, 23))
print(suma_todos_elementos(4, 6))
