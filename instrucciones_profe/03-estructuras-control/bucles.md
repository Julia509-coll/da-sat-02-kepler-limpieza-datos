# 🔁 Bucles: for y while

## ¿Qué son los bucles?

Los bucles te permiten **repetir acciones** sin escribir el mismo código mil veces.

Imagina que necesitas analizar las ventas de 365 días. ¿Vas a escribir 365 líneas de código? No. Usas un bucle.

## El bucle `for`

El más común. Repite una acción para cada elemento de una secuencia:

```python
# Iterar sobre una lista
ventas = [100, 150, 200, 175, 225]

for venta in ventas:
    print(f"Venta: {venta}")
```

Salida:
```
Venta: 100
Venta: 150
Venta: 200
Venta: 175
Venta: 225
```

### Iterar sobre un rango

Si solo necesitas repetir N veces:

```python
# Imprimir números del 0 al 4
for i in range(5):
    print(i)
```

```python
# Imprimir números del 1 al 5
for i in range(1, 6):
    print(i)
```

```python
# Imprimir números del 0 al 10 de 2 en 2
for i in range(0, 11, 2):
    print(i)  # 0, 2, 4, 6, 8, 10
```

### Ejemplo con datos

```python
precios = [19.99, 25.50, 15.00, 30.00]
total = 0

for precio in precios:
    total = total + precio

print(f"Total: {total}")  # 90.49
```

## El bucle `while`

Repite **mientras** una condición sea verdadera:

```python
contador = 0

while contador < 5:
    print(f"Contador: {contador}")
    contador = contador + 1
```

Salida:
```
Contador: 0
Contador: 1
Contador: 2
Contador: 3
Contador: 4
```

**Cuidado:** Si la condición nunca se vuelve False, el bucle se ejecuta infinitamente.

### Ejemplo con datos

```python
saldo = 1000
gasto_mensual = 150
meses = 0

while saldo > 0:
    saldo = saldo - gasto_mensual
    meses = meses + 1
    print(f"Mes {meses}: Saldo restante = {saldo}")

print(f"El saldo se agotó en {meses} meses")
```

## `break` y `continue`

### `break` - detener el bucle

```python
ventas = [100, 200, 0, 300, 400]

for venta in ventas:
    if venta == 0:
        print("Dato inválido encontrado. Deteniendo análisis.")
        break
    print(f"Venta: {venta}")
```

Salida:
```
Venta: 100
Venta: 200
Dato inválido encontrado. Deteniendo análisis.
```

### `continue` - saltar a la siguiente iteración

```python
ventas = [100, -50, 200, -30, 300]

for venta in ventas:
    if venta < 0:
        continue  # Saltar ventas negativas
    print(f"Venta válida: {venta}")
```

Salida:
```
Venta válida: 100
Venta válida: 200
Venta válida: 300
```

## Bucles anidados

Un bucle dentro de otro:

```python
productos = ["Laptop", "Mouse", "Teclado"]
tiendas = ["Tienda A", "Tienda B"]

for producto in productos:
    for tienda in tiendas:
        print(f"{producto} en {tienda}")
```

Salida:
```
Laptop en Tienda A
Laptop en Tienda B
Mouse en Tienda A
Mouse en Tienda B
Teclado en Tienda A
Teclado en Tienda B
```

## Enumerar con índice

Si necesitas el índice además del valor:

```python
categorias = ["Ficción", "Ensayo", "Cómic"]

for i, categoria in enumerate(categorias):
    print(f"{i}: {categoria}")
```

Salida:
```
0: Ficción
1: Ensayo
2: Cómic
```

## Práctica: análisis de préstamos

Crea un archivo `bucles.py`:

```python
# Días de préstamo de varios libros
dias_prestamo = [15, 22, 18, 30, 12, 25]
limite = 21

prestamos_a_tiempo = 0
prestamos_retraso = 0
total_dias_retraso = 0

for dias in dias_prestamo:
    if dias <= limite:
        prestamos_a_tiempo += 1  # Equivale a: prestamos_a_tiempo = prestamos_a_tiempo + 1
    else:
        prestamos_retraso += 1
        dias_extra = dias - limite
        total_dias_retraso += dias_extra

# Mostrar resultados
print(f"Total de préstamos: {len(dias_prestamo)}")
print(f"Préstamos a tiempo: {prestamos_a_tiempo}")
print(f"Préstamos con retraso: {prestamos_retraso}")
print(f"Total días de retraso: {total_dias_retraso}")

# Calcular promedio de retraso
if prestamos_retraso > 0:
    promedio_retraso = total_dias_retraso / prestamos_retraso
    print(f"Promedio de días de retraso: {promedio_retraso:.2f}")
```

## ¿for o while?

- **Usa `for`** cuando sabes cuántas veces vas a iterar (lista, rango definido)
- **Usa `while`** cuando la condición de parada depende de algo que cambia durante la ejecución

En análisis de datos, `for` es mucho más común.

---

**Siguiente paso:** Aprende a organizar tu código con funciones.
