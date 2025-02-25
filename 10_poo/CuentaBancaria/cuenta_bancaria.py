class CuentaBancaria:
    def __init__(self, titular: str, numero_cuenta: str, saldo: float, tipo_cuenta: str):
        """Constructor para inicializar los campos de la clase"""
        self.__titular = titular
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo
        self.__tipo_cuenta = tipo_cuenta

    # Métodos de acceso (getters)
    def get_titular(self) -> str:
        return self.__titular

    def get_numero_cuenta(self) -> str:
        return self.__numero_cuenta

    def get_saldo(self) -> float:
        return self.__saldo

    def get_tipo_cuenta(self) -> str:
        return self.__tipo_cuenta

    # Métodos mutadores (setters)
    def set_titular(self, titular: str):
        self.__titular = titular

    def set_numero_cuenta(self, numero_cuenta: str):
        self.__numero_cuenta = numero_cuenta

    def set_saldo(self, saldo: float):
        self.__saldo = saldo

    def set_tipo_cuenta(self, tipo_cuenta: str):
        self.__tipo_cuenta = tipo_cuenta

    # Método para mostrar la información de la cuenta
    def mostrar_informacion(self) -> str:
        return (f"Cuenta Bancaria:\n"
                f"Titular: {self.__titular}\n"
                f"Número de Cuenta: {self.__numero_cuenta}\n"
                f"Saldo: ${self.__saldo:.2f}\n"
                f"Tipo de Cuenta: {self.__tipo_cuenta}")
