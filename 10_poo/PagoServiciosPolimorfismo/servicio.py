class Servicio:
    def __init__(self, nombre: str):
        self._nombre = nombre

    def __str__(self):
        return f"Servicio: {self._nombre}"

    def calcular_pago(self) -> float:
        return 0.0


class ServicioElectricidad(Servicio):
    def __init__(self, nombre: str, consumo_kwh: float, tarifa_kwh: float):
        super().__init__(nombre)
        self._consumo_kwh = consumo_kwh
        self._tarifa_kwh = tarifa_kwh

    def calcular_pago(self) -> float:
        return self._consumo_kwh * self._tarifa_kwh

    def __str__(self):
        return (f"{super().__str__()}, consumo: {self._consumo_kwh} kWh, "
                f"tarifa: {self._tarifa_kwh} $/kWh, "
                f"pago: ${self.calcular_pago():.2f}")


class ServicioAgua(Servicio):
    def __init__(self, nombre: str, consumo_m3: float, tarifa_m3: float):
        super().__init__(nombre)
        self._consumo_m3 = consumo_m3
        self._tarifa_m3 = tarifa_m3

    def calcular_pago(self) -> float:
        return self._consumo_m3 * self._tarifa_m3

    def __str__(self):
        return (f"{super().__str__()}, consumo: {self._consumo_m3} m³, "
                f"tarifa: {self._tarifa_m3} $/m³, "
                f"pago: ${self.calcular_pago():.2f}")


class ServicioGas(Servicio):
    def __init__(self, nombre: str, consumo_litros: float, tarifa_litro: float):
        super().__init__(nombre)
        self._consumo_litros = consumo_litros
        self._tarifa_litro = tarifa_litro

    def calcular_pago(self) -> float:
        return self._consumo_litros * self._tarifa_litro

    def __str__(self):
        return (f"{super().__str__()}, consumo: {self._consumo_litros} litros, "
                f"tarifa: {self._tarifa_litro} $/litro, "
                f"pago: ${self.calcular_pago():.2f}")
