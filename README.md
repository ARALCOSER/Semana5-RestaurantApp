# 📌 Sistema de Gestión de Restaurant

## 🧠 Autor: Ramiro Alcoser A.

## 📖 Descripción

Este proyecto consiste en una aplicación básica desarrollada en Python utilizando Programación Orientada a Objetos (POO). El sistema permite registrar libros y usuarios dentro de una biblioteca, almacenando la información mediante objetos y organizando el código en diferentes módulos para facilitar su comprensión y mantenimiento.

## 📂 Estructura del Proyecto

```text
Semana5restauranteApp/
│
├── modelos/
│   ├── cliente.py
│   └── producto.py
│
├── servicios/
│   └── restaurante.py
│
└── main.py
```

## 🚀 Funcionalidades

- Crear objetos de tipo Producto.
- Crear objetos de tipo Cliente.
- Registrar productos en el restaurante.
- Registrar clientes en el restaurante.
- Mostrar la información almacenada.
- Organizar el programa mediante módulos y clases.

## 📌 Conceptos Aplicados

### 🎯 Identificadores Descriptivos

Se utilizan nombres claros y significativos para clases, métodos, atributos y variables, facilitando la lectura y comprensión del código.

**Ejemplos:**

- `Producto`
- `Cliente`
- `Restaurante`
- `nombre`
- `precio`
- `registrar_producto()`
- `mostrar_inventario_y_clientes()`

### 📜 Tipos de Datos

Durante el desarrollo del programa se utilizan diferentes tipos de datos:

| Tipo | Ejemplo |
|--------|----------|
| `str` | nombre, cedula_identidad, ciudad_origen, nombre_establecimiento |
| `int` | edad, stock |
| `float` | precio |
| `bool` | es_vip |

### 📜 Anotaciones de Tipos

Se emplean anotaciones de tipos para indicar el tipo de dato esperado en parámetros y valores de retorno.

```python
titulo: str
edad: int
precio: float
```

```python
def mostrar_inventario_y_clientes(self): -> str:
```

### 🛠️ Estructuras de Datos Compuestas

La clase `Restaurante` utiliza listas para almacenar múltiples objetos.

```python
self.lista_productos: list = []
self.lista_clientes: list = []
```

Estas estructuras permiten registrar varios productos y clientes dentro del sistema.

### 📉 Programación Orientada a Objetos

El proyecto aplica conceptos fundamentales de POO:

- Clases
- Objetos
- Atributos
- Métodos
- Modularidad

## 💻 Buenas Prácticas Aplicadas

- Uso de identificadores descriptivos.
- Organización del código en módulos.
- Separación de responsabilidades mediante clases.
- Uso de anotaciones de tipos.
- Comentarios claros para la funcionalidad de los codigos.
- Función principal `main()` como punto de entrada del programa.

## 🤝 Reflexion

El desarrollo de software modular en Python requiere más que lógica funcional; exige una estructura limpia y mantenible apoyada en tres componentes clave:
- Identificadores descriptivos (Legibilidad)
- Tipos de datos adecuados (Integridad)
- Listas como estructuras dinámicas (Escalabilidad)

La integración de estos tres elementos transforma programas planos e independientes en una arquitectura orientada a objetos profesional, robusta y optimizada para el mantenimiento a largo plazo.
