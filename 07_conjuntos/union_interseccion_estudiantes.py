programacion = {"Ana", "Carlos", "Luis", "María", "Pedro"}
bases_datos = {"María", "Pedro", "Sofía", "David", "Carlos"}

# Nombres únicos (estudiantes de al menos un grupo)
todos_los_estudiantes = programacion | bases_datos
print(f"Estudiantes únicos: {todos_los_estudiantes}")

# Estudiantes en ambos grupos
en_ambos = programacion & bases_datos
print(f"Estudiantes en ambos grupos: {en_ambos}")
print("-" * 100)