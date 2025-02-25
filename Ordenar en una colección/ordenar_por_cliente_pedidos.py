class PedidoOnline:
    def __init__(self, numero_pedido, nombre_cliente, fecha_pedido, estado_pedido):
        self.numero_pedido = numero_pedido
        self.nombre_cliente = nombre_cliente
        self.fecha_pedido = fecha_pedido
        self.estado_pedido = estado_pedido

    def __str__(self):
        return f"Pedido #{self.numero_pedido} - Cliente: {self.nombre_cliente} - Fecha: {self.fecha_pedido} - Estado: {self.estado_pedido}"

# Crear una lista de pedidos
pedidos = [
    PedidoOnline(1, "Carlos Gómez", "2025-01-20", "Enviado"),
    PedidoOnline(2, "Ana López", "2025-01-21", "Pendiente"),
    PedidoOnline(3, "Beatriz Pérez", "2025-01-19", "Entregado")
]

# Ordenar los pedidos por nombre del cliente
pedidos_ordenados = sorted(pedidos, key=lambda pedido_: pedido_.nombre_cliente)

# Mostrar los pedidos ordenados
for pedido in pedidos_ordenados:
    print(pedido)
