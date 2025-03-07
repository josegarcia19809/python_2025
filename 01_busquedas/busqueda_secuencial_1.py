n: int = int(input("Dime cuántos elementos tiene la lista: "))
A: list[int] = []

# Llenar el vector
print("Ingrese los elementos del vector")
for i in range(n):
    elemento: int = int(input(f"Dame elemento {i}: "))
    A.append(elemento)

# Leer el elemento a buscar
t = int(input("Dame valor a buscar: "))

# Recorrido de la lista
for i in range(n):
    if A[i] == t:
        print(f"Elemento encontrado en la posición {i}")

# 6, 8, 10, 9, 7, 5 n=6
