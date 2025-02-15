x = (1, 2, 3, 3, 3, 3, 1)

print(f"Cantidad de 1s: {x.count(1)}")  # 2
print(f"Cantidad de 3s: {x.count(3)}")  # 4
print("-" * 100)
# Retorna el indice donde se encuentra un elemento por primera vez
print(x.index(1))  # 0
# print(x.index(5)) # tuple.index(x): x not in tuple
print(x.index(3))  # 2
print("-" * 100)