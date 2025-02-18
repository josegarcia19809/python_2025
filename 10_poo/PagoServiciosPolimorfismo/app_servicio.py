from servicio import ServicioElectricidad, ServicioGas, ServicioAgua


def imprimir_linea():
    print("-" * 50)


def main():
    servicio_electricidad = ServicioElectricidad("Luz", 100, 0.13)
    servicio_gas = ServicioGas("Gas", 200, 0.07)
    servicio_agua = ServicioAgua("Agua", 100, 12)

    imprimir_linea()
    print(servicio_electricidad)
    print(servicio_agua)
    print(servicio_gas)
    imprimir_linea()


if __name__ == "__main__":
    main()
