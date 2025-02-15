nombres = ('Carolina', "Rogelio", "Miriam", "Blanca")

for nombre in nombres:
    print(nombre)

print("-" * 100)
meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre",
         "noviembre", "diciembre")

for mes in meses:
    print(mes)

print("-" * 100)
for i in range(0, len(meses)):
    print(f"Mes {i + 1}: {meses[i]}")
