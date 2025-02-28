from gasto import Gasto


class Planificador:
    def __init__(self, presupuesto_inicial: float):
        self.presupuesto = presupuesto_inicial
        self.lista_gastos = []

    def total_gastos(self) -> float:
        total = 0
        for gasto in self.lista_gastos:
            total += gasto.get_cantidad()

        return total

    def obtener_presupuesto_inicial(self) -> float:
        return self.presupuesto

    def agregar_gasto(self, gasto: Gasto):
        self.lista_gastos.append(gasto)

    def mostrar_gastos(self):
        print("Lista de gastos")
        for gasto in self.lista_gastos:
            print(gasto.mostrar_info())

    def obtener_presupuesto_disponible(self) -> float:
        total_gastado = self.total_gastos()
        presupuesto_inicial = self.obtener_presupuesto_inicial()
        disponible = presupuesto_inicial - total_gastado
        return disponible
        # return self.obtener_presupuesto_inicial() - self.total_gastos()

    def obtener_porcentaje_gastado(self) -> float:
        porcentaje = self.total_gastos() * 100 / self.obtener_presupuesto_inicial()
        return porcentaje

    def alcanza_el_dinero(self, cantidad_a_gastar) -> bool:
        return self.obtener_presupuesto_disponible() - cantidad_a_gastar >= 0
