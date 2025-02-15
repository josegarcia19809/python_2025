estudiantes_escuela = {}

while True:
    nombre = input("Ingresa el nombre del estudiante: ")
    if nombre == '':
        break

    calificacion = int(input("Ingresa la calificación del estudiante (0-10): "))
    if calificacion not in range(0, 11):
        break

    if nombre in estudiantes_escuela:
        estudiantes_escuela[nombre] += (calificacion,)
    else:
        estudiantes_escuela[nombre] = (calificacion,)

for nombre in sorted(estudiantes_escuela.keys()):
    suma = 0
    contador = 0
    for calificacion in estudiantes_escuela[nombre]:
        suma += calificacion
        contador += 1
    print(nombre, ":", suma / contador)
