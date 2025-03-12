# ordenamiento_pedidos.py
from lista_pedidos import pedidos


def imprimir_linea():
    print("-" * 100)


# Ordenar los pedidos por nombre del cliente
print("1.- Ordenar por nombre de cliente")
pedidos_ordenados_por_cliente = sorted(pedidos, key=lambda pedido: pedido.nombre_cliente)

for pedido_cliente in pedidos_ordenados_por_cliente:
    print(pedido_cliente)

imprimir_linea()

# Ordenar los pedidos por estado del pedido
print("2.- Ordenar por estado del pedido")
pedidos_ordenados_por_estado = sorted(pedidos, key=lambda pedido: pedido.estado_pedido)

for pedido_estado in pedidos_ordenados_por_estado:
    print(pedido_estado)

imprimir_linea()

# 3. Ordenar los pedidos por fecha de manera descendente
pedidos_ordenados_fecha_desc = sorted(pedidos, key=lambda pedido: pedido.fecha_pedido,
                                      reverse=True)

print("3. Pedidos ordenados por fecha (descendente)")
for pedido_fecha_desc in pedidos_ordenados_fecha_desc:
    print(pedido_fecha_desc)

imprimir_linea()
# 4. Uso de .lower en sorted
pedidos_ordenados_por_estado = sorted(pedidos,
                                      key=lambda pedido: pedido.estado_pedido.lower())

print("4. Ordenados por estado (No importa si son mayúsculas o minúsculas)")
for pedido_estado in pedidos_ordenados_por_estado:
    print(pedido_estado)

imprimir_linea()

# 5. Ordenar por estado y por nombre del cliente   
print("5. Ordenar por estado y por nombre")
pedidos_ordenados_estado_nombre = sorted(
    pedidos,
    key=lambda pedido: (pedido.estado_pedido,
                        pedido.nombre_cliente)
)

for pedido_estado_nombre in pedidos_ordenados_estado_nombre:
    print(pedido_estado_nombre)

imprimir_linea()
