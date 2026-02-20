import os
os.system("cls")

class SmartDelivery:
    def __init__(self):
        self.rutas = {
            "Marbella": 10,
            "Torices": 15,
            "Bicentenario": 30
        }

        self.tarifas = {
            "Marbella": 10000,
            "Torices": 25000,
            "Bicentenario": 70000
        }

        self.reporte = {
            "Luis": "Centro",
            "Daniel": "Bicentenario",
            "Andres": "Marbella",
            "Pedro": "Todos"
        }

        self.pedidos = []

    def registro_de_pedidos(self, nombre, direccion, telefono, **kwargs):
        pedido = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono
        }

        pedido.update(kwargs)
        self.pedidos.append(pedido)

        return pedido