# 🎯 Parámetros y Return

## Parámetros: la entrada de la función

Los parámetros son los valores que le pasas a una función para que trabaje con ellos.

```python
def calcular_iva(precio, tasa_iva):
    iva = precio * (tasa_iva / 100)
    return iva

# precio=100 y tasa_iva=21 son los argumentos
iva_calculado = calcular_iva(100, 21)
print(iva_calculado)  # 21.0
```

**Parámetro** = variable en la definición de la función  
**Argumento** = valor que pasas cuando llamas la función

## Parámetros posicionales vs por nombre

**Posicionales** (el orden importa):
```python
def dividir(numerador, denominador):
    return numerador / denominador

print(dividir(10, 2))  # 5.0
print(dividir(2, 10))  # 0.2
```

**Por nombre** (el orden no importa):
```python
print(dividir(numerador=10, denominador=2))  # 5.0
print(dividir(denominador=2, numerador=10))  # 5.0
```

## Parámetros con valores por defecto

Si no pasas un argumento, usa el valor por defecto:

```python
def calcular_descuento(precio, porcentaje=10):
    descuento = precio * (porcentaje / 100)
    return precio - descuento

print(calcular_descuento(100))  # 90.0 (usa 10%)
print(calcular_descuento(100, 15))  # 85.0 (usa 15%)
print(calcular_descuento(100, porcentaje=20))  # 80.0 (usa 20%)
```

**Regla:** Los parámetros con valores por defecto deben ir al final.

```python
# ✅ Correcto
def funcion(a, b, c=0):
    pass

# ❌ Incorrecto
def funcion(a, b=0, c):
    pass
```

## El `return`: la salida de la función

`return` devuelve un valor y **termina la ejecución** de la función.

```python
def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    return False

print(es_mayor_de_edad(20))  # True
print(es_mayor_de_edad(15))  # False
```

### Devolver múltiples valores

```python
def estadisticas_basicas(numeros):
    total = sum(numeros)
    promedio = total / len(numeros)
    maximo = max(numeros)
    return total, promedio, maximo  # Devuelve una tupla

# Desempaquetar los valores
t, p, m = estadisticas_basicas([10, 20, 30, 40])
print(f"Total: {t}, Promedio: {p}, Máximo: {m}")
```

### `return` sin valor

Si no especificas nada, devuelve `None`:

```python
def saludar(nombre):
    print(f"Hola, {nombre}")
    # No hay return

resultado = saludar("Ana")  # Imprime "Hola, Ana"
print(resultado)  # None
```

## Ejemplo completo: clasificador de datos

```python
def clasificar_venta(monto, meta_baja=1000, meta_alta=5000):
    """
    Clasifica una venta según su monto.
    
    Args:
        monto (float): Monto de la venta
        meta_baja (float): Umbral para ventas bajas
        meta_alta (float): Umbral para ventas altas
    
    Returns:
        str: Clasificación de la venta
    """
    if monto < meta_baja:
        return "Venta baja"
    elif monto < meta_alta:
        return "Venta media"
    else:
        return "Venta alta"

# Usar la función
ventas = [500, 2500, 7000, 800, 4500]

for venta in ventas:
    categoria = clasificar_venta(venta)
    print(f"Venta de {venta}: {categoria}")
```

Salida:
```
Venta de 500: Venta baja
Venta de 2500: Venta media
Venta de 7000: Venta alta
Venta de 800: Venta baja
Venta de 4500: Venta media
```

## Funciones con listas como parámetros

Puedes pasar listas (o cualquier estructura de datos):

```python
def filtrar_mayores_que(lista, umbral):
    """
    Filtra valores mayores que un umbral.
    
    Args:
        lista (list): Lista de números
        umbral (float): Valor mínimo
    
    Returns:
        list: Lista filtrada
    """
    resultado = []
    for valor in lista:
        if valor > umbral:
            resultado.append(valor)
    return resultado

ventas = [100, 250, 50, 300, 80, 400]
ventas_altas = filtrar_mayores_que(ventas, 200)
print(ventas_altas)  # [250, 300, 400]
```

## Práctica

Crea un archivo `parametros_return.py`:

```python
def analizar_prestamo(dias, categoria, limite_normal=21):
    """
    Analiza un préstamo y calcula penalización.
    
    Args:
        dias (int): Días del préstamo
        categoria (str): Tipo de material ("libro", "revista", "dvd")
        limite_normal (int): Límite de días para préstamos normales
    
    Returns:
        dict: Información del análisis
    """
    # Ajustar límite según categoría
    if categoria == "revista":
        limite = limite_normal - 7
    elif categoria == "dvd":
        limite = limite_normal - 14
    else:
        limite = limite_normal
    
    # Calcular retraso
    if dias <= limite:
        retraso = 0
        estado = "A tiempo"
        penalizacion = 0
    else:
        retraso = dias - limite
        estado = "Retrasado"
        penalizacion = retraso * 0.50
    
    return {
        'estado': estado,
        'dias': dias,
        'limite': limite,
        'retraso': retraso,
        'penalizacion': penalizacion
    }

# Probar la función
resultado = analizar_prestamo(25, "libro")
print(f"Estado: {resultado['estado']}")
print(f"Días de retraso: {resultado['retraso']}")
print(f"Penalización: {resultado['penalizacion']}€")

# Probar con revista
resultado2 = analizar_prestamo(20, "revista")
print(f"\nRevista - Estado: {resultado2['estado']}")
print(f"Días de retraso: {resultado2['retraso']}")
```

## Buenas prácticas

1. **Nombres descriptivos:** `calcular_promedio()` es mejor que `calc()`
2. **Una función, una tarea:** Si hace muchas cosas, divídela en funciones más pequeñas
3. **Documenta con docstrings:** Explica qué hace, qué recibe, qué devuelve
4. **Valida entradas:** Comprueba que los parámetros tienen sentido
5. **Usa valores por defecto con cuidado:** Solo para casos donde el valor por defecto tiene sentido lógico

---

**Siguiente paso:** Aprende a manejar listas y diccionarios (estructuras de datos esenciales).
