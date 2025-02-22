def ensure_correct_info(*args):
    if "Jose" in args and "Garcia" in args:
        return "Welcome back, Jose!"
    return "Not sure who are you..."


print(ensure_correct_info("Jose", "Garcia", 23, True))
print(ensure_correct_info("Arturo", "Garcia", 23, True))

# El código define una función llamada ensure_correct_info, que verifica si los argumentos recibidos
# incluyen los valores "Jose" y "Garcia".
#
# La función utiliza *args, lo que le permite aceptar una cantidad variable de argumentos. Luego,
# dentro de la función, se evalúa si los valores "Jose" y "Garcia" están presentes en los
# argumentos recibidos.
#
# Si ambos nombres están en los argumentos, la función devuelve "Welcome back, Jose!".
# Si falta alguno de los nombres, devuelve "Not sure who are you...".
# Después de definir la función, se realizan dos llamadas:
#
# ensure_correct_info("Jose", "Garcia", 23, True): Como "Jose" y "Garcia" están presentes, devuelve
# "Welcome back, Jose!".
# ensure_correct_info("Arturo", "Garcia", 23, True): Falta "Jose", por lo que devuelve
# "Not sure who are you...".
# Esta función permite validar de manera flexible la identidad de un usuario en función de los
# datos proporcionados.
