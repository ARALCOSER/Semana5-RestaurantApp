# Defino la clase Cliente para representar un cliente en el sistema de gestión de pedidos

class Cliente:

    def __init__(
        self,
        nombre: str,
        edad: int,
        saldo_disponible: float,
        es_vip: bool,
        cedula_identidad: str,
        ciudad_origen: str
    ):
        self.nombre = nombre
        self.edad = edad
        self.saldo_disponible = saldo_disponible
        self.es_vip = es_vip
        self.cedula_identidad = cedula_identidad
        self.ciudad_origen = ciudad_origen

    def mostrar_informacion(self) -> str:
        estatus = "VIP" if self.es_vip else "Regular"
        return (
            f"{self.nombre} | "
            f"{estatus}"
        )

    def __str__(self) -> str:
        estatus = "VIP" if self.es_vip else "Regular"
        return (
            f"Cliente: {self.nombre} "
            f"({self.edad} años) | CI: {self.cedula_identidad} | Ciudad: {self.ciudad_origen} | Estatus: {estatus}"
        )
    

