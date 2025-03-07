n = 6
A: list[int] = []

# Llenar el vector
print("Ingrese los elementos del vector")
for i in range(n):
    elemento = int(input("Dame elemento: "))
    A.append(elemento)

t = int(input("Dame elemento a buscar: "))

i = 0
while (A[i] != t) and (i < n - 1):
    i = i + 1

if A[i] == t:
    print(f"El número deseado está presente y ocupa el lugar {i}")
else:
    print(f"{t} no existe en el vector")
