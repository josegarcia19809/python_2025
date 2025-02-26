from gasto import Gasto


class Planificador:
    def __init__(self, presupuesto_inicial: float):
        self.presupuesto = presupuesto_inicial
        self.lista_gastos = []

    def total_gastos(self):
        pass

    def obtener_presupuesto_inicial(self):
        pass

    def agregar_gasto(self, gasto: Gasto):
        self.lista_gastos.append(gasto)

    def mostrar_gastos(self):
        print("Lista de gastos")
        for gasto in self.lista_gastos:
            print(gasto.mostrar_info())

    def obtener_presupuesto_disponible(self):
        pass
