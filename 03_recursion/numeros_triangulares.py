def numero_triangular(n: int) -> int:
    """Obtener el número triangular enésimo de forma recursiva"""
    if n < 1:
        return 0
    return n + numero_triangular(n - 1)


def main():
    print(f"Número triangular de 6: {numero_triangular(6)}")
    print(f"Número triangular de 100: {numero_triangular(100)}")
    print(f"Número triangular de 200: {numero_triangular(200)}")
    print(f"Número triangular de 500: {numero_triangular(500)}")


if __name__ == '__main__':
    main()
