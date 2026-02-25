import os
os.system("cls")

# SMART DELIVERY S.A.S

# REGISTRO DE PEDIDOS (POO + **kwargs)

class Pedido:
    def __init__(self, **kwargs):
        self.nombre = kwargs.get("nombre")
        self.direccion = kwargs.get("direccion")
        self.telefono = kwargs.get("telefono")
        self.zona = kwargs.get("zona") 
        self.tarifa = 0
        self.repartidor = ""

    def mostrar(self):
        print("\n===== INFORMACIÓN DEL ENVÍO =====")
        print("Cliente:", self.nombre)
        print("Dirección:", self.direccion)
        print("Teléfono:", self.telefono)
        print("Zona:", self.zona) 
        print("Tarifa:", self.tarifa)
        print("Repartidor:", self.repartidor)


# MOTOR DE RUTAS (*args)

class MotorRutas:
    def __init__(self):
        self.centro = "Centro"
        self.rutas = {
            "Marbella": 10,
            "Torices": 15,
            "Bicentenario": 30
        }

    def optimizar(self, *args):
        print("\n--- Rutas Disponibles ---")
        for zona in args:
            if zona in self.rutas:
                print(f"{self.centro} → {zona}: {self.rutas[zona]} km")


# CÁLCULO DINÁMICO (DESACOPLADO)

class CalculoTarifa:
    def __init__(self):
        self.tarifas_base = {
            "Marbella": 10000,
            "Torices": 25000,
            "Bicentenario": 70000
        }

    def calcular(self, pedido, zona):
        pedido.tarifa = self.tarifas_base.get(zona, 0)


# ASIGNACIÓN AUTOMÁTICA (**kwargs)

class Asignacion:
    def asignar(self, pedido, zona, **kwargs):
        mapa = kwargs.get("repartidores")
        if zona in mapa:
            pedido.repartidor = mapa[zona]
        else:
            pedido.repartidor = "No disponible"


# PROGRAMA PRINCIPAL

print("===== SMART DELIVERY S.A.S =====")

nombre = input("Ingrese nombre del cliente: ")
direccion = input("Ingrese dirección: ")
telefono = input("Ingrese teléfono: ")
zona = input("Seleccione zona (Marbella, Torices, Bicentenario): ")

pedido = Pedido(
    nombre=nombre,
    direccion=direccion,
    telefono=telefono,
    zona=zona
)

# Selección de zona (ya hace parte de rutas)
zona = input("Seleccione zona (Marbella, Torices, Bicentenario): ")

# Calcular tarifa
calculo = CalculoTarifa()
calculo.calcular(pedido, zona)

# Asignar repartidor usando **kwargs
asignador = Asignacion()
asignador.asignar(
    pedido,
    zona,
    repartidores={
        "Marbella": "Luis",
        "Torices": "Roy",
        "Bicentenario": "Pedro"
    }
)

# Mostrar resultado final
pedido.mostrar()