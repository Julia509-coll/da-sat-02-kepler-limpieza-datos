# 🔤 Variables y Tipos de Datos

## ¿Qué es una variable?

Una variable es un **espacio en la memoria** donde guardas información para usarla después.

Piensa en ella como una caja con una etiqueta. La etiqueta es el nombre de la variable, y dentro de la caja está el valor.

```python
edad = 25
nombre = "Ana"
precio = 19.99
```

Aquí creamos tres variables:
- `edad` guarda el número 25
- `nombre` guarda el texto "Ana"
- `precio` guarda el número 19.99

## ¿Por qué necesitamos variables?

Imagina que estás analizando datos de ventas. En lugar de escribir `19.99` cada vez que necesitas el precio, lo guardas en una variable:

```python
precio = 19.99
impuesto = precio * 0.21
total = precio + impuesto

print(total)  # 24.1879
```

Si el precio cambia, solo cambias una línea. El resto del código sigue funcionando.

## Tipos de datos básicos

Python distingue entre varios tipos de información:

### 1. Números enteros (`int`)

```python
edad = 30
filas = 1000
mes = 12
```

Sin decimales. Usados para contar cosas.

### 2. Números decimales (`float`)

```python
precio = 19.99
promedio = 45.6
tasa_conversion = 0.25
```

Con decimales. Usados para medidas, promedios, porcentajes.

### 3. Texto (`str` - strings)

```python
nombre = "María"
ciudad = "Madrid"
mensaje = "Análisis completado"
```

Entre comillas (simples o dobles). Representan texto.

### 4. Booleanos (`bool`)

```python
es_valido = True
tiene_descuento = False
```

Solo dos valores posibles: `True` o `False`. Usados para decisiones.

## ¿Cómo saber el tipo de una variable?

Usa `type()`:

```python
edad = 25
print(type(edad))  # <class 'int'>

precio = 19.99
print(type(precio))  # <class 'float'>

nombre = "Ana"
print(type(nombre))  # <class 'str'>
```

## Convertir entre tipos

A veces necesitas cambiar el tipo de un dato:

```python
# De texto a número
edad_texto = "25"
edad_numero = int(edad_texto)  # Ahora es 25 (número)

# De número a texto
precio = 19.99
precio_texto = str(precio)  # Ahora es "19.99" (texto)

# De entero a decimal
filas = 100
filas_decimal = float(filas)  # Ahora es 100.0
```

Esto es útil cuando lees datos de archivos (donde todo llega como texto) y necesitas hacer cálculos.

## Nombres de variables

Puedes usar casi cualquier nombre, pero:

✅ **Bien:**
```python
edad = 25
nombre_completo = "Ana García"
total_ventas = 1500
```

❌ **Mal:**
```python
1edad = 25  # No puede empezar con número
nombre-completo = "Ana"  # No uses guiones (usa _ en su lugar)
class = "Matemáticas"  # No uses palabras reservadas de Python
```

**Consejo:** Usa nombres descriptivos. `precio_producto` es mejor que `p`.

## Práctica: tus primeras variables

Crea un archivo `variables.py` y escribe:

```python
# Datos de un producto
nombre_producto = "Laptop"
precio = 899.99
cantidad_stock = 15
en_oferta = True

# Calcular valor total del stock
valor_total = precio * cantidad_stock

# Mostrar resultados
print("Producto:", nombre_producto)
print("Precio unitario:", precio)
print("Cantidad en stock:", cantidad_stock)
print("Valor total en stock:", valor_total)
print("¿En oferta?:", en_oferta)
```

Ejecuta el código. Deberías ver la información del producto.

Ahora cambia el precio y vuelve a ejecutar. Todo se recalcula automáticamente.

## ¿Por qué importa esto para datos?

Cuando trabajes con datasets, cada columna tiene un tipo de dato:
- Edades, cantidades → `int`
- Precios, promedios → `float`
- Nombres, categorías → `str`
- Indicadores (sí/no) → `bool`

Saber manejar tipos te permite hacer cálculos, filtros y transformaciones correctamente.

---

**Siguiente paso:** Aprende a hacer operaciones con estos datos (operadores básicos).
