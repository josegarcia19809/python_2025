# Clase base para empleados
class EmpleadoBase:
    def __init__(self, nombre, id_empleado, salario):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.salario = salario

    def calcular_salario(self):
        return self.salario

    def __str__(self):
        return f"Empleado: {self.nombre}, ID: {self.id_empleado}, Salario: {self.salario}"


# Subclase para empleados de tiempo completo
class EmpleadoTiempoCompleto(EmpleadoBase):
    def __init__(self, nombre, id_empleado, salario, beneficios):
        super().__init__(nombre, id_empleado, salario)
        self.beneficios = beneficios

    def __str__(self):
        return super().__str__() + f", Beneficios: {self.beneficios}"


# Subclase para empleados de medio tiempo
class EmpleadoMedioTiempo(EmpleadoBase):
    def __init__(self, nombre, id_empleado, tarifa_hora, horas_trabajadas):
        super().__init__(nombre, id_empleado, tarifa_hora * horas_trabajadas)
        self.tarifa_hora = tarifa_hora
        self.horas_trabajadas = horas_trabajadas

    def __str__(self):
        return super().__str__() + f", Horas trabajadas: {self.horas_trabajadas}, Tarifa por hora: {self.tarifa_hora}"


# Subclase para empleados contratistas
class EmpleadoContratista(EmpleadoBase):
    def __init__(self, nombre, id_empleado, tarifa_proyecto):
        super().__init__(nombre, id_empleado, tarifa_proyecto)
        self.tarifa_proyecto = tarifa_proyecto

    def __str__(self):
        return super().__str__() + f", Tarifa del proyecto: {self.tarifa_proyecto}"


# Lista dinámica de empleados
empleados = []

# Agregar diferentes tipos de empleados
empleados.append(EmpleadoTiempoCompleto("Alice", 1, 50000, "Seguro Médico"))
empleados.append(EmpleadoMedioTiempo("Bob", 2, 20, 25))
empleados.append(EmpleadoContratista("Charlie", 3, 3000))

# Visualizar los empleados
for empleado in empleados:
    print(empleado)

# Calcular el salario total de todos los empleados
salario_total = sum(empleado.calcular_salario() for empleado in empleados)
print(f"Salario total de todos los empleados: {salario_total}")
