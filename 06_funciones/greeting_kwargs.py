def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"] == "special":
        return "You get a special greeting David"
    elif "David" in kwargs:
        return f"{kwargs['David']} David"

    return "Not sure who this is..."


print(special_greeting(David="hello"))
print(special_greeting(David="special"))
print(special_greeting(Carolina="hello"))
print(special_greeting(Carolina="special", David="special"))


# **kwargs es un parámetro especial en Python que permite pasar un número variable de
# argumentos con nombre (clave-valor) a una función. Se usa cuando no se sabe de antemano
# cuántos argumentos nombrados se recibirán.
#
# Explicación:
# **kwargs captura los argumentos nombrados como un diccionario (dict).
# Se puede iterar sobre kwargs.items() para acceder a las claves y valores.
# 📌 Diferencia con *args:
#
# *args → Recibe argumentos posicionales como una tupla.
# **kwargs → Recibe argumentos nombrados como un diccionario.
