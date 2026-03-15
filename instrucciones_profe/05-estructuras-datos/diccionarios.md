# 📚 Diccionarios en Python

## ¿Qué es un diccionario?

Un diccionario es una colección de **pares clave-valor**. Como un diccionario real donde buscas una palabra (clave) y encuentras su definición (valor).

```python
producto = {
    "nombre": "Laptop",
    "precio": 899.99,
    "stock": 15,
    "en_oferta": True
}
```

## Crear diccionarios

```python
# Diccionario vacío
vacio = {}

# Con datos
persona = {
    "nombre": "Ana",
    "edad": 28,
    "ciudad": "Madrid"
}

# Usando dict()
otro = dict(nombre="Carlos", edad=32)
```

## Acceder a valores

```python
producto = {
    "nombre": "Laptop",
    "precio": 899.99,
    "stock": 15
}

# Por clave
print(producto["nombre"])  # "Laptop"
print(producto["precio"])  # 899.99

# Con get() (más seguro, no da error si no existe)
print(producto.get("nombre"))  # "Laptop"
print(producto.get("descuento"))  # None
print(producto.get("descuento", 0))  # 0 (valor por defecto)
```

## Modificar diccionarios

```python
producto = {"nombre": "Laptop", "precio": 899.99}

# Cambiar valor
producto["precio"] = 799.99

# Añadir nueva clave
producto["stock"] = 20

# Actualizar varios valores
producto.update({"precio": 749.99, "en_oferta": True})

print(producto)
# {'nombre': 'Laptop', 'precio': 749.99, 'stock': 20, 'en_oferta': True}
```

## Eliminar elementos

```python
producto = {"nombre": "Laptop", "precio": 899.99, "stock": 15}

# Eliminar clave
del producto["stock"]

# Eliminar y devolver valor
precio = producto.pop("precio")
print(precio)  # 899.99

# Limpiar todo
producto.clear()
```

## Verificar existencia de claves

```python
producto = {"nombre": "Laptop", "precio": 899.99}

if "precio" in producto:
    print("El producto tiene precio")

if "descuento" not in producto:
    print("No hay descuento definido")
```

## Iterar sobre diccionarios

```python
producto = {"nombre": "Laptop", "precio": 899.99, "stock": 15}

# Solo claves
for clave in producto.keys():
    print(clave)

# Solo valores
for valor in producto.values():
    print(valor)

# Claves y valores
for clave, valor in producto.items():
    print(f"{clave}: {valor}")
```

Salida:
```
nombre: Laptop
precio: 899.99
stock: 15
```

## Diccionarios anidados

```python
biblioteca = {
    "libro_001": {
        "titulo": "1984",
        "autor": "George Orwell",
        "prestado": False
    },
    "libro_002": {
        "titulo": "El Quijote",
        "autor": "Cervantes",
        "prestado": True
    }
}

# Acceder
print(biblioteca["libro_001"]["titulo"])  # "1984"
print(biblioteca["libro_002"]["prestado"])  # True
```

## Listas de diccionarios

```python
prestamos = [
    {"usuario": "Ana", "libro": "1984", "dias": 15},
    {"usuario": "Carlos", "libro": "El Quijote", "dias": 22},
    {"usuario": "María", "libro": "Cien años", "dias": 18}
]

# Iterar
for prestamo in prestamos:
    print(f"{prestamo['usuario']} tiene '{prestamo['libro']}' por {prestamo['dias']} días")
```

## Métodos útiles

```python
producto = {"nombre": "Laptop", "precio": 899.99, "stock": 15}

# Obtener todas las claves
claves = list(producto.keys())
print(claves)  # ['nombre', 'precio', 'stock']

# Obtener todos los valores
valores = list(producto.values())
print(valores)  # ['Laptop', 899.99, 15]

# Obtener pares clave-valor
items = list(producto.items())
print(items)  # [('nombre', 'Laptop'), ('precio', 899.99), ('stock', 15)]
```

## Dictionary comprehensions

```python
# Crear diccionario a partir de listas
nombres = ["Ana", "Carlos", "María"]
edades = [28, 32, 25]

personas = {nombre: edad for nombre, edad in zip(nombres, edades)}
print(personas)  # {'Ana': 28, 'Carlos': 32, 'María': 25}

# Con condición
numeros = [1, 2, 3, 4, 5]
cuadrados_pares = {n: n**2 for n in numeros if n % 2 == 0}
print(cuadrados_pares)  # {2: 4, 4: 16}
```

## Práctica: análisis con diccionarios

Crea un archivo `diccionarios.py`:

```python
# Datos de biblioteca
prestamos = [
    {"id": 1, "categoria": "Ficción", "dias": 15},
    {"id": 2, "categoria": "Ensayo", "dias": 22},
    {"id": 3, "categoria": "Ficción", "dias": 18},
    {"id": 4, "categoria": "Cómic", "dias": 30},
    {"id": 5, "categoria": "Ensayo", "dias": 25},
    {"id": 6, "categoria": "Ficción", "dias": 12}
]

# Agrupar por categoría
estadisticas = {}

for prestamo in prestamos:
    categoria = prestamo["categoria"]
    dias = prestamo["dias"]
    
    if categoria not in estadisticas:
        estadisticas[categoria] = {
            "total": 0,
            "suma_dias": 0,
            "max_dias": dias,
            "min_dias": dias
        }
    
    estadisticas[categoria]["total"] += 1
    estadisticas[categoria]["suma_dias"] += dias
    estadisticas[categoria]["max_dias"] = max(estadisticas[categoria]["max_dias"], dias)
    estadisticas[categoria]["min_dias"] = min(estadisticas[categoria]["min_dias"], dias)

# Mostrar resultados
for categoria, datos in estadisticas.items():
    promedio = datos["suma_dias"] / datos["total"]
    print(f"\n{categoria}:")
    print(f"  Total préstamos: {datos['total']}")
    print(f"  Promedio días: {promedio:.1f}")
    print(f"  Máximo: {datos['max_dias']} días")
    print(f"  Mínimo: {datos['min_dias']} días")
```

## ¿Listas o diccionarios?

| Usa listas cuando | Usa diccionarios cuando |
|-------------------|-------------------------|
| El orden importa | Necesitas buscar por nombre/clave |
| Accedes por posición | Los datos tienen estructura (campos) |
| Datos homogéneos | Necesitas etiquetar cada valor |

En análisis de datos:
- **Listas:** Columnas de datos, series numéricas
- **Diccionarios:** Filas de datos (registros), configuraciones, metadatos

Pandas combina ambos: cada fila es como un diccionario, cada columna como una lista.

---

**Siguiente paso:** Practica con ejercicios integradores que combinan todo lo aprendido.
