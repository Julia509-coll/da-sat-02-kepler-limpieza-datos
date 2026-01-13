# 🔀 Condicionales: if, elif, else

## ¿Qué son los condicionales?

Son estructuras que permiten que tu código **tome decisiones** basándose en condiciones.

Como en la vida real:
- **Si** llueve → llevo paraguas
- **Si no** → no lo llevo

En Python:

```python
esta_lloviendo = True

if esta_lloviendo:
    print("Lleva paraguas")
else:
    print("No necesitas paraguas")
```

## Sintaxis básica

```python
if condicion:
    # Código que se ejecuta si la condición es True
    print("La condición se cumplió")
```

**Importante:** La indentación (espacios al inicio) es obligatoria. Indica qué código pertenece al `if`.

## if - else

```python
edad = 17

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

## if - elif - else

Cuando tienes más de dos opciones:

```python
nota = 7.5

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
```

Python evalúa las condiciones **en orden**. Cuando encuentra una True, ejecuta ese bloque y se detiene.

## Condiciones múltiples

Puedes combinar condiciones con `and`, `or`:

```python
temperatura = 25
esta_soleado = True

if temperatura > 20 and esta_soleado:
    print("Buen día para salir")
elif temperatura > 20:
    print("Hace calor pero está nublado")
else:
    print("Mejor quedarse en casa")
```

## Ejemplo con datos: análisis de ventas

```python
ventas_mes = 15000
meta = 12000
mes_anterior = 14000

# Evaluar rendimiento
if ventas_mes >= meta:
    print("✅ Meta alcanzada")
    
    if ventas_mes > mes_anterior:
        print("📈 Y mejoramos respecto al mes pasado")
    else:
        print("📊 Pero no superamos al mes pasado")
else:
    deficit = meta - ventas_mes
    print(f"❌ No alcanzamos la meta. Faltaron {deficit}")
```

## Condicionales anidados

Puedes poner un `if` dentro de otro:

```python
tiene_stock = True
precio = 25
presupuesto = 30

if tiene_stock:
    if precio <= presupuesto:
        print("Compra el producto")
    else:
        print("No tienes suficiente presupuesto")
else:
    print("Producto agotado")
```

Pero cuidado: demasiados niveles de anidación hacen el código difícil de leer.

## Expresiones condicionales (ternario)

Forma compacta para casos simples:

```python
edad = 20
categoria = "Adulto" if edad >= 18 else "Menor"
print(categoria)  # "Adulto"
```

Es equivalente a:

```python
if edad >= 18:
    categoria = "Adulto"
else:
    categoria = "Menor"
```

## Práctica: clasificador de datos

Crea un archivo `condicionales.py`:

```python
# Datos de un préstamo en biblioteca
dias_prestamo = 25
limite_normal = 21
limite_extendido = 30

# Clasificar estado del préstamo
if dias_prestamo <= limite_normal:
    estado = "A tiempo"
    penalizacion = 0
elif dias_prestamo <= limite_extendido:
    dias_retraso = dias_prestamo - limite_normal
    estado = "Retraso leve"
    penalizacion = dias_retraso * 0.50
else:
    dias_retraso = dias_prestamo - limite_normal
    estado = "Retraso grave"
    penalizacion = dias_retraso * 1.00

print(f"Estado: {estado}")
print(f"Días de préstamo: {dias_prestamo}")
print(f"Penalización: {penalizacion}€")
```

Modifica `dias_prestamo` con diferentes valores (10, 25, 35) y ve cómo cambia la salida.

## ¿Por qué importa esto para datos?

Cuando analices datos, constantemente necesitarás:
- Clasificar registros (bajo/medio/alto)
- Filtrar datos según condiciones
- Aplicar reglas de negocio
- Validar información

Los condicionales son la base de toda esa lógica.

---

**Siguiente paso:** Aprende a repetir acciones con bucles (`for` y `while`).
