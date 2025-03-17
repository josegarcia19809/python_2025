def factorial(n):  # Obtiene el factorial de n
    if n < 1: return 1  # Es 1 para cualquier número < 1
    return n * factorial(n - 1)  # Multiplica por el factorial anterior


def main():
    print("Calculando algunos factoriales...")
    print(f"Factorial de 5: {factorial(5)}")
    print(f"Factorial de 8: {factorial(8)}")
    print(f"Factorial de 1: {factorial(1)}")
    print(f"Factorial de 0: {factorial(0)}")
    print(f"Factorial de 20: {factorial(20)}")


if __name__ == "__main__":
    main()
