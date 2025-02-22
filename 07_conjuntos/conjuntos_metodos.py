# conjunto con 10 frutas
frutas = {"manzana", "pera", "plátano", "uva", "naranja", "sandía", "kiwi", "fresa",
          "mango", "piña"}
print(frutas)
print("-" * 100)

# Agregando elementos
frutas.add("banana")
print(frutas)

frutas.add("banana") # Ya no lo va a agregar
print(frutas)
print("-" * 100)

# Eliminando elementos
frutas.remove("banana")
print(frutas)

# Si el elemento no existe, marcará un error
# frutas.remove("banana")

print("-" * 100)
frutas.discard("mango")
print(frutas)

frutas.discard("papaya") # no existe papaya, pero no marca error
print(frutas)

# Copiando un conjunto en otro
print("-" * 100)
mis_frutas = frutas.copy()
print(mis_frutas)

# Limpiar un conjunto
mis_frutas.clear()
print(mis_frutas)