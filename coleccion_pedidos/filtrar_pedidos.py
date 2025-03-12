# filtrar_pedidos.py

from lista_pedidos import pedidos


def imprimir_linea():
    print("-" * 100)


# Mostrar solo los pedidos que han sido enviados
pedidos_enviados = list(filter(
    lambda pedido: pedido.estado_pedido == "Enviado", pedidos))

print("Pedidos enviados")
for pedido_enviado in pedidos_enviados:
    print(pedido_enviado)

imprimir_linea()

# Mostrar solo los pedidos que están pendientes
pedidos_pendientes = list(filter(
    lambda pedido: pedido.estado_pedido == "Pendiente", pedidos))

print("Pedidos pendientes")
for pedido_pendiente in pedidos_pendientes:
    print(pedido_pendiente)

imprimir_linea()

# Mostrar solo los pedidos que han sido entregados
pedidos_entregados = list(filter(
    lambda pedido: pedido.estado_pedido == "Entregado", pedidos))

print("Pedidos entregados")
for pedido_entregado in pedidos_entregados:
    print(pedido_entregado)

imprimir_linea()

# Mostrar solamente el nombre de los clientes con estado "Entregado"
print("Clientes con pedidos 'Entregado'")
clientes_entregados = list(
    map(lambda pedido: pedido.nombre_cliente,
        filter(lambda pedido: pedido.estado_pedido == "Entregado", pedidos))
)

for nombre_cliente in clientes_entregados:
    print(nombre_cliente)

imprimir_linea()
# Contar cuántos pedidos están en Pendiente
pendientes = sum(map(
    lambda pedido: pedido.estado_pedido == "Pendiente", pedidos))
print(f"Pedidos pendientes: {pendientes}")
