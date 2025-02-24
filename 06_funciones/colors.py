def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")


fav_colors(Carolina="blue", Pepe="red", Rox="green")
print("-" * 100)
fav_colors(Maria="yellow")


# El código define una función llamada fav_colors que recibe un número variable de
# argumentos con nombre (**kwargs) y luego imprime el color favorito de cada persona.
#
# **kwargs permite recibir cualquier cantidad de argumentos nombrados.
# kwargs.items() devuelve pares clave-valor (persona-color).
# Se usa un for para recorrer estos pares e imprimir un mensaje formateado.