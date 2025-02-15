dictionary = {
    "gato": "chat",
    "perro": "chien",
    "caballo": "cheval"
}

# Imprimir valor del elemento "perro".
print(dictionary["perro"])

print()

# El siguiente ciclo recorre un diccionario e imprime cada clave junto con su valor asociado
# en el formato clave -> valor.
for key in dictionary.keys():
    print(key, "->", dictionary[key])

print()

# O se puede utilizar una tupla para conseguir los elementos de un diccionario
for spanish, french in sorted(dictionary.items()):
    print(spanish, "->", french)

print()

# Modificar un valor de un diccionario
dictionary["gato"] = "Miau"
print(dictionary)
