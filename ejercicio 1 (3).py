class Producto:
    def inicio (self, codigo, nombre, precio):
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

producto = Producto(101, "ordenador", 1200)
unidades = 3
print(f"Total a pagar por {unidades} cantidad de {producto.get_nombre()} es {producto.calcular_total(unidades)}€")