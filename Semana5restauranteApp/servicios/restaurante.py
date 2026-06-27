#  Importando las clases Producto y Cliente desde sus respectivos módulos

from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self, nombre_establecimiento: str):
        self.nombre_establecimiento = nombre_establecimiento
        # Uso de listas como estructuras de datos compuestos (Tipadas)
        self.lista_productos: list = []
        self.lista_clientes: list = []

    def registrar_producto(self, nuevo_producto: Producto):
        # Método para agregar objetos Producto a la lista
        self.lista_productos.append(nuevo_producto)

    def registrar_cliente(self, nuevo_cliente: Cliente):
        # Método para agregar objetos Cliente a la lista
        self.lista_clientes.append(nuevo_cliente)

    def mostrar_inventario_y_clientes(self):
        # Muestra la información organizada de forma estética en la consola
        print("\n" + "="*60)
        print(f"--- BIENVENIDO AL RESTAURANTE {self.nombre_establecimiento.upper()} ---")
        print("="*60)
        
        print("\nLista de Productos / Menu:")
        for producto in self.lista_productos:
            print(f"- {producto}")
        
        print("\nLista de Clientes:")
        for cliente in self.lista_clientes:
            print(f"- {cliente}")
        print("="*60 + "\n")