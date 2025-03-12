# ordenamiento_pedidos_group_by.py
from lista_pedidos import pedidos
from itertools import groupby


def imprimir_linea():
    print("-" * 100)


# Ordenar los pedidos por estado del pedido
print("2.- Ordenar por estado del pedido")
pedidos_ordenados_por_estado = sorted(pedidos, key=lambda pedido: pedido.estado_pedido)

for pedido_estado in pedidos_ordenados_por_estado:
    print(pedido_estado)

imprimir_linea()
# Agrupar por estado
grupos = groupby(pedidos_ordenados_por_estado, key=lambda pedido:pedido.estado_pedido)

for estado, grupo in grupos:
    print(f"Estado: {estado}")
    for pedido_g in grupo:
        print(f"  - {pedido_g.nombre_cliente} {pedido_g.fecha_pedido}")
    print("-" * 30)

imprimir_linea()


