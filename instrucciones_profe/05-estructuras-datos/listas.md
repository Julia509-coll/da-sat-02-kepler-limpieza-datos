# 📋 Listas en Python

## ¿Qué es una lista?

Una lista es una **colección ordenada** de elementos. Puedes guardar múltiples valores en una sola variable.

```python
ventas = [100, 150, 200, 175, 225]
nombres = ["Ana", "Carlos", "María"]
mixta = [100, "texto", True, 25.5]  # Pueden ser de tipos diferentes
```

## Crear listas

```python
# Lista vacía
lista_vacia = []

# Lista con valores
numeros = [1, 2, 3, 4, 5]

# Lista usando range
numeros = list(range(1, 6))  # [1, 2, 3, 4, 5]
```

## Acceder a elementos

Los índices empiezan en 0:

```python
categorias = ["Ficción", "Ensayo", "Cómic", "Poesía"]

print(categorias[0])  # Ficción (primer elemento)
print(categorias[2])  # Cómic (tercer elemento)
print(categorias[-1])  # Poesía (último elemento)
print(categorias[-2])  # Cómic (penúltimo)
```

## Slicing (rebanadas)

Obtener subconjuntos de la lista:

```python
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numeros[2:5])  # [2, 3, 4] (desde índice 2 hasta 4)
print(numeros[:3])  # [0, 1, 2] (desde el inicio hasta índice 2)
print(numeros[5:])  # [5, 6, 7, 8, 9] (desde índice 5 hasta el final)
print(numeros[::2])  # [0, 2, 4, 6, 8] (de 2 en 2)
```

## Modificar listas

```python
ventas = [100, 150, 200]

# Cambiar un valor
ventas[1] = 180
print(ventas)  # [100, 180, 200]

# Añadir al final
ventas.append(250)
print(ventas)  # [100, 180, 200, 250]

# Añadir en posición específica
ventas.insert(1, 120)
print(ventas)  # [100, 120, 180, 200, 250]

# Extender con otra lista
ventas.extend([300, 350])
print(ventas)  # [100, 120, 180, 200, 250, 300, 350]
```

## Eliminar elementos

```python
nombres = ["Ana", "Carlos", "María", "Luis"]

# Eliminar por valor
nombres.remove("Carlos")
print(nombres)  # ["Ana", "María", "Luis"]

# Eliminar por índice
del nombres[1]
print(nombres)  # ["Ana", "Luis"]

# Eliminar y devolver el último
ultimo = nombres.pop()
print(ultimo)  # "Luis"
print(nombres)  # ["Ana"]
```

## Operaciones comunes

```python
numeros = [10, 20, 30, 40, 50]

# Longitud
print(len(numeros))  # 5

# Suma total
print(sum(numeros))  # 150

# Máximo y mínimo
print(max(numeros))  # 50
print(min(numeros))  # 10

# Ordenar
desordenado = [30, 10, 50, 20, 40]
desordenado.sort()
print(desordenado)  # [10, 20, 30, 40, 50]

# Invertir
numeros.reverse()
print(numeros)  # [50, 40, 30, 20, 10]
```

## Verificar pertenencia

```python
ventas = [100, 200, 300]

if 200 in ventas:
    print("200 está en la lista")

if 400 not in ventas:
    print("400 no está en la lista")
```

## Iterar sobre listas

```python
categorias = ["Ficción", "Ensayo", "Cómic"]

# Forma básica
for categoria in categorias:
    print(categoria)

# Con índice
for i, categoria in enumerate(categorias):
    print(f"{i}: {categoria}")
```

## List comprehensions

Forma compacta de crear listas:

```python
# Crear lista de cuadrados
numeros = [1, 2, 3, 4, 5]
cuadrados = [n ** 2 for n in numeros]
print(cuadrados)  # [1, 4, 9, 16, 25]

# Con condición
pares = [n for n in numeros if n % 2 == 0]
print(pares)  # [2, 4]

# Transformar datos
nombres = ["ana", "carlos", "maría"]
mayusculas = [nombre.upper() for nombre in nombres]
print(mayusculas)  # ["ANA", "CARLOS", "MARÍA"]
```

## Listas anidadas (matrices)

```python
# Tabla de ventas por día y producto
ventas_semanales = [
    [100, 150, 200],  # Lunes
    [120, 180, 210],  # Martes
    [110, 160, 190]   # Miércoles
]

# Acceder
print(ventas_semanales[0])  # [100, 150, 200] (lunes)
print(ventas_semanales[1][2])  # 210 (martes, producto 3)
```

## Práctica: análisis de datos con listas

Crea un archivo `listas.py`:

```python
# Datos de préstamos (días)
prestamos = [15, 22, 18, 30, 12, 25, 19, 28, 14, 35]
limite = 21

# Separar en dos listas
a_tiempo = []
con_retraso = []

for dias in prestamos:
    if dias <= limite:
        a_tiempo.append(dias)
    else:
        con_retraso.append(dias)

# Análisis
print(f"Total de préstamos: {len(prestamos)}")
print(f"A tiempo: {len(a_tiempo)} ({len(a_tiempo)/len(prestamos)*100:.1f}%)")
print(f"Con retraso: {len(con_retraso)} ({len(con_retraso)/len(prestamos)*100:.1f}%)")

if len(con_retraso) > 0:
    promedio_retraso = sum(con_retraso) / len(con_retraso)
    print(f"Promedio de días con retraso: {promedio_retraso:.1f}")
    print(f"Máximo retraso: {max(con_retraso)} días")
```

## ¿Por qué importan las listas?

En análisis de datos, las listas representan:
- Columnas de datos
- Series temporales
- Resultados de filtros
- Agrupaciones

Dominar listas es fundamental para trabajar luego con Pandas (donde todo son "listas mejoradas").

---

**Siguiente:** Aprende sobre diccionarios (pares clave-valor).
