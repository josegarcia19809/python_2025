# ocupacion_hotelera.py

# Este programa usa variables acumulativas para sacar totales

print("Ocupación hotelera")
print("¿Cuántos pisos hay en el hotel? ", end="")
pisos = int(input())

if pisos < 1:
    print("Número de pisos no válido")
    print("Ingrese nuevamente al programa")
    exit()

total_habitaciones = 0
total_ocupadas = 0

for i in range(1, pisos + 1):
    print()
    print(f"¿Cuántas habitaciones tiene el piso {i}? ", end="")
    habitaciones = int(input())
    total_habitaciones = total_habitaciones + habitaciones

    print("¿Cuántas habitaciones están ocupadas? ", end="")
    ocupadas = int(input())
    total_ocupadas += ocupadas

print()
porcentaje_ocupacion = (float(total_ocupadas) / float(total_habitaciones) * 100.0)
total_desocupadas = total_habitaciones - total_ocupadas

print(f"Total de habitaciones: {total_habitaciones}")
print(f"Total de habitaciones ocupadas: {total_ocupadas}")
print(f"Total de habitaciones desocupadas: {total_desocupadas}")
print(f"Porcentaje de ocupación: {porcentaje_ocupacion:.2f}%")
