# pedido_online.py

class PedidoOnline:
    def __init__(self, numero_pedido: int, nombre_cliente: str, fecha_pedido: str,
                 estado_pedido: str):
        self.numero_pedido = numero_pedido
        self.nombre_cliente = nombre_cliente
        self.fecha_pedido = fecha_pedido
        self.estado_pedido = estado_pedido

    def __str__(self) -> str:
        datos = (
            f"Pedido #{self.numero_pedido}"
            f" - Cliente: {self.nombre_cliente}"
            f" - Fecha: {self.fecha_pedido}"
            f" - Estado: {self.estado_pedido}"
        )
        return datos
