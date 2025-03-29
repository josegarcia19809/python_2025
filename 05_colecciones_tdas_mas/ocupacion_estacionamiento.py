# ocupacion_estacionamiento.py

# Programa que usará listas para guardar elementos y después sumarlos

print("Ocupación de un estacionamiento")

niveles = int(input("¿Cuántos niveles tiene el estacionamiento? "))

if niveles < 1:
    print("Número de niveles no válido")
    print("Vuelva a ejecutar el programa")
    exit()

espacios_por_nivel = []
espacios_ocupados_por_nivel = []

for i in range(niveles):
    print()
    print(f"Dime cuántos espacios tiene el nivel #{i + 1}: ", end="")
    espacios = int(input())
    espacios_por_nivel.append(espacios)

    print(f"Dime cuántos espacios hay ocupados: ", end="")
    ocupados = int(input())
    espacios_ocupados_por_nivel.append(ocupados)

print("-" * 100)
total_espacios = 0
for espacios in espacios_por_nivel:
    total_espacios += espacios

print(f"Total de espacios: {total_espacios}")

total_ocupados = sum(espacios_ocupados_por_nivel)
print(f"Total de espacios ocupados: {total_ocupados}")

total_disponibles = total_espacios - total_ocupados
print(f"Total de espacios disponibles: {total_disponibles}")

porcentaje_ocupacion = float(total_ocupados) / float(total_espacios) * 100.0
print(f"Porcentaje de ocupación: {porcentaje_ocupacion:.2f}%")
