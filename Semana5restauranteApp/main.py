# Importaciones entre modulos

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def main():
    # Instancia del servicio principal
    mi_restaurante = Restaurante("VACA & VACO")

    # --- VARIEDAD DE PLATOS (Comidas principales) ---
    plato1 = Producto("Lomo de Falda", 12.50, 15, False)
    plato2 = Producto("Pechuga de pollo", 8.00, 10, False)
    plato3 = Producto("Camarones", 6.50, 25, False)
    plato4 = Producto("Chuleta de cerdo", 5.50, 20, False)

    # --- VARIEDAD DE BEBIDAS ---
    bebida1 = Producto("Te Helado", 1.50, 50, True)
    bebida2 = Producto("Chocolate con crema", 1.25, 40, True)
    bebida3 = Producto("Limonada Imperial", 2.00, 30, True)
    bebida4 = Producto("Cerveza Artesanal", 3.50, 24, True)

    # --- VARIEDAD DE POSTRES ---
    postre1 = Producto("Helado de Paila", 3.00, 12, False)
    postre2 = Producto("Torta de Tres Leches", 4.50, 8, False)
    postre3 = Producto("Higos con Queso", 3.50, 10, False)
    postre4 = Producto("Torta de Chocolate", 3.50, 10, False)

    # --- CLIENTES ---
    cliente1 = Cliente("Kevin Lascano", 28, 45.0, True, "1600123456", "Puyo")
    cliente2 = Cliente("Ana Paz", 22, 15.75, False, "1700987654", "Quito")
    cliente3 = Cliente("Carlos Ruiz", 35, 120.0, True, "0900112233", "Guayaquil")
    cliente4 = Cliente("Elena Torres", 29, 60.50, False, "1800112233", "Cuenca")
    cliente5 = Cliente("Pedro Castro", 40, 10.0, True, "1900112233", "Ibarra")

    # Registro de productos en la lista del servicio
    mi_restaurante.registrar_producto(plato1)
    mi_restaurante.registrar_producto(plato2)
    mi_restaurante.registrar_producto(plato3)
    mi_restaurante.registrar_producto(plato4)
    
    mi_restaurante.registrar_producto(bebida1)
    mi_restaurante.registrar_producto(bebida2)
    mi_restaurante.registrar_producto(bebida3)
    mi_restaurante.registrar_producto(bebida4)
    
    mi_restaurante.registrar_producto(postre1)
    mi_restaurante.registrar_producto(postre2)
    mi_restaurante.registrar_producto(postre3)
    mi_restaurante.registrar_producto(postre4)
    
    # Registro de clientes en la lista del servicio
    mi_restaurante.registrar_cliente(cliente1)
    mi_restaurante.registrar_cliente(cliente2)
    mi_restaurante.registrar_cliente(cliente3)
    mi_restaurante.registrar_cliente(cliente4)
    mi_restaurante.registrar_cliente(cliente5)

    # Muestra la información de forma organizada en consola 
    mi_restaurante.mostrar_inventario_y_clientes()

if __name__ == "__main__":
    main()