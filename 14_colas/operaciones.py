class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class Cola:
    def __init__(self, valor):
        nuevo_nodo = Nodo(valor)
        self.primero = nuevo_nodo
        self.ultimo = nuevo_nodo
        self.longitud = 1

    def imprimir_cola(self):
        temporal = self.primero
        while temporal is not None:
            print(temporal.valor)
            temporal = temporal.siguiente

    def encolar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
        self.longitud += 1
        return True

    def desencolar(self):
        if self.longitud == 0:
            return None
        temporal = self.primero
        if self.longitud == 1:
            self.primero = None
            self.ultimo = None
        else:
            self.primero = self.primero.siguiente
            temporal.siguiente = None
        self.longitud -= 1
        return temporal


# Se insertarán los siguientes elementos:
"""
1
2
3
4
5
"""

mi_cola = Cola(1)
mi_cola.encolar(2)
mi_cola.encolar(3)
mi_cola.encolar(4)
mi_cola.encolar(5)

# Ahora se estarán sacando
print(mi_cola.desencolar().valor)

print(mi_cola.desencolar().valor)

print(mi_cola.desencolar().valor)
print(mi_cola.desencolar().valor)
print(mi_cola.desencolar().valor)

"""
    SALIDA ESPERADA:
    ----------------
    1
    2
    None
"""
