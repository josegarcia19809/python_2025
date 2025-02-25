from cuenta_bancaria import CuentaBancaria

def main():
    # Prueba del programa
    cuenta = CuentaBancaria("María López", "123456789", 35000.75, "Ahorros")

    # Mostrar información inicial
    print(cuenta.mostrar_informacion())

    # Modificar algunos valores
    cuenta.set_saldo(40000.50)
    cuenta.set_tipo_cuenta("Corriente")

    # Mostrar información actualizada
    print("\nInformación actualizada:")
    print(cuenta.mostrar_informacion())


if __name__ == '__main__':
    main()
    print("-"*100)