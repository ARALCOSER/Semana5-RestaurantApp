# Defino la clase Producto para representar un producto en el sistema de gestión de pedidos

class Producto:

    # Definición de atributos con tipos de datos básicos en parámetros
    def __init__(
        self,
        nombre: str,
        precio: float,
        stock: int,
        es_bebida: bool
    ):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

        self.es_bebida = es_bebida

    def mostrar_informacion(self) -> str:
        tipo = "Bebida" if self.es_bebida else "Plato"
        return (
            f"Producto: {self.nombre} | "
            f"Tipo: {tipo} | "
            f"Stock: {self.stock}"
        )

    # Método especial para representar el objeto como texto
    def __str__(self) -> str:
        tipo = "Bebida" if self.es_bebida else "Plato"
        return (
            f"{self.nombre} | "
            f"({tipo}) | "
            f"${self.precio:.2f}"
        )
    

