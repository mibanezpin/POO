class Producto:
    def inicio(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
    
    def get_codigo(self):
        return self.codigo
    
    def set_codigo(self, codigo):
        self.codigo = codigo
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_precio(self):
        return self.precio
    
    def set_precio(self, precio):
        self.precio = precio
    
    def calcular_total(self, unidades):
        return self.precio * unidades

class Pedido:
    def __init__(self):
        self.productos = []
        self.cantidades = []
    
    def agregar_producto(self, producto, cantidad):
        self.productos.append(producto)
        self.cantidades.append(cantidad)
    
    def total_pedido(self):
        return sum(prod.calcular_total(cant) for prod, cant in zip(self.productos, self.cantidades))
    
    def mostrar_productos(self):
        for prod, cant in zip(self.productos, self.cantidades):
            print(f"{prod.get_nombre()} - {cant} unidades - {prod.calcular_total(cant)}€")

producto1 = Producto(101, "ordenador", 1200)
producto2 = Producto(102, "raton", 25)

pedido = Pedido()
pedido.agregar_producto(producto1, 2)
pedido.agregar_producto(producto2, 5)

print("Productos en el pedido:")
pedido.mostrar_productos()
print(f"El total del pedido son {pedido.total_pedido()}€")