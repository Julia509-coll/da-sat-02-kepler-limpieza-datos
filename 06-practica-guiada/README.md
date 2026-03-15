# 🎯 Práctica Guiada: Ejercicios Progresivos

Aquí encontrarás ejercicios que integran todo lo aprendido en Kepler. Van de más simple a más complejo.

No hay "soluciones correctas únicas". Lo importante es que tu código funcione y que entiendas por qué funciona.

---

## Ejercicio 1: Análisis básico de ventas

**Objetivo:** Practicar variables, operadores y condicionales

### Enunciado

Tienes datos de ventas mensuales. Escribe un programa que:

1. Guarde las ventas de cada mes en variables
2. Calcule el total y el promedio
3. Identifique el mes con mayores ventas
4. Determine si se alcanzó la meta anual (50000)

```python
# Datos
enero = 4500
febrero = 5200
marzo = 4800
# ... completa los demás meses
abril = 5100
 mayo = 5300
junio = 4700
julio = 4900
agosto = 5200
septiembre = 5000
octubre = 5100
noviembre = 4800
diciembre = 5500

# Tu código aquí
# Calcular total
total = (enero + febrero + marzo + abril + mayo + junio +
         julio + agosto + septiembre + octubre + noviembre + diciembre)

 print ("total:" , total)        

# Promedio
promedio = total / 12
print("promedio:" , promedio)


# Encontrar mes con mayor venta
mayor = enero
mes = "enero"

if febrero > mayor:
    mayor = febrero
    mes = "febrero"

if marzo > mayor:
    mayor = marzo
    mes = "marzo"

if abril > mayor:
    mayor = abril
    mes = "abril"

if mayo > mayor:
    mayor = mayo
    mes = "mayo"

if junio > mayor:
    mayor = junio
    mes = "junio"


if julio > mayor:
    mayor = julio
    mes = "julio"

if agosto > mayor:
    mayor = agosto
    mes = "agosto"

if septiembre > mayor:
    mayor = septiembre
    mes = "septiembre"

if octubre > mayor:
    mayor = octubre
    mes = "octubre"

if noviembre > mayor:
    mayor = noviembre
    mes = "noviembre"

if diciembre > mayor:
    mayor = diciembre
    mes = "diciembre"

print("El mes con mayor venta fue:", mes)
print("Ventas:", mayor)                                   
```

### Pistas

- Usa variables para cada mes
- `total = enero + febrero + ...`
- `promedio = total / 12`
- Usa `if` para comparar meses y encontrar el máximo
- Compara `total >= 50000` para la meta

---

## Ejercicio 2: Clasificador de préstamos

**Objetivo:** Practicar funciones, condicionales y listas

### Enunciado

Crea una función que clasifique préstamos según días transcurridos:
- 0-21 días: "A tiempo"
- 22-30 días: "Retraso leve" (penalización: 0.50€/día extra)
- Más de 30 días: "Retraso grave" (penalización: 1.00€/día extra)

Luego procesa una lista de préstamos y muestra estadísticas.

```python
def clasificar_prestamo(dias):
    # Tu código aquí
    pass

# Datos de prueba
prestamos_dias = [15, 22, 18, 35, 25, 12, 40, 19, 28, 33]

# Procesar y mostrar estadísticas
```

### Pistas

- La función debe devolver un diccionario con `estado` y `penalizacion`
- Usa un bucle `for` para procesar la lista
- Cuenta cuántos están en cada categoría
- Calcula la penalización total

---

## Ejercicio 3: Análisis de categorías

**Objetivo:** Practicar listas, diccionarios y bucles

### Enunciado

Tienes una lista de libros prestados con su categoría y días de préstamo:

```python
prestamos = [
    {"titulo": "1984", "categoria": "Ficción", "dias": 15},
    {"titulo": "Sapiens", "categoria": "Ensayo", "dias": 22},
    {"titulo": "Watchmen", "categoria": "Cómic", "dias": 18},
    {"titulo": "El Quijote", "categoria": "Ficción", "dias": 30},
    {"titulo": "Breve historia", "categoria": "Ensayo", "dias": 25},
    {"titulo": "Batman", "categoria": "Cómic", "dias": 12}
]
```

Escribe un programa que:

1. Agrupe los préstamos por categoría
2. Calcule el promedio de días por categoría
3. Identifique la categoría más prestada
4. Muestre libros con más de 20 días

### Pistas

- Crea un diccionario para agrupar por categoría
- Usa un bucle para iterar sobre los préstamos
- Para cada categoría, guarda una lista de días
- Calcula promedios usando `sum()` y `len()`

---

## Ejercicio 4: Procesador de datos

**Objetivo:** Integrar todo (funciones, estructuras, validación)

### Enunciado

Crea un sistema que procese datos de ventas con las siguientes funciones:

```python
def limpiar_datos(ventas):
    """Elimina valores negativos o None"""
    pass

def calcular_estadisticas(ventas):
    """Devuelve dict con total, promedio, max, min"""
    pass

def clasificar_ventas(ventas, umbral_bajo, umbral_alto):
    """Devuelve dict con ventas bajas, medias, altas"""
    pass

def generar_reporte(ventas):
    """Usa las funciones anteriores y muestra reporte completo"""
    pass
```

Datos de prueba (con valores inválidos):
```python
ventas_brutas = [1500, -200, 2500, None, 3000, 0, 4500, -100, 2800, 5000]
```

### Requerimientos

1. `limpiar_datos`: Filtrar valores válidos (> 0 y no None)
2. `calcular_estadisticas`: Total, promedio, máximo, mínimo
3. `clasificar_ventas`: 
   - Baja: < umbral_bajo
   - Media: entre umbrales
   - Alta: >= umbral_alto
4. `generar_reporte`: Llamar todas las funciones y mostrar resultados formateados

### Salida esperada (aproximada)

```
=== REPORTE DE VENTAS ===

Datos procesados: 7 ventas válidas (3 inválidas eliminadas)

Estadísticas:
  Total: 21800
  Promedio: 3114.29
  Máximo: 5000
  Mínimo: 1500

Clasificación:
  Ventas bajas (< 2000): 1 (14.3%)
  Ventas medias: 4 (57.1%)
  Ventas altas (>= 4000): 2 (28.6%)
```

---

## Ejercicio 5: Mini proyecto integrador

**Objetivo:** Crear un análisis completo desde cero

### Enunciado

Crea un programa que simule el análisis de una biblioteca durante un mes.

**Datos a generar aleatoriamente** (o puedes usar datos fijos):
- 100 préstamos
- Categorías: Ficción, Ensayo, Cómic, Poesía
- Días de préstamo: entre 5 y 45 días

**Análisis a realizar:**

1. **Por categoría:**
   - Cuántos préstamos
   - Promedio de días
   - Porcentaje del total

2. **Por estado:**
   - A tiempo (≤ 21 días)
   - Retraso leve (22-30 días)
   - Retraso grave (> 30 días)

3. **Penalizaciones:**
   - Total recaudado en penalizaciones
   - Promedio por préstamo con retraso

4. **Top 5:**
   - Préstamos más largos

### Estructura sugerida

```python
import random

def generar_datos(n=100):
    """Genera n préstamos aleatorios"""
    pass

def analizar_por_categoria(prestamos):
    """Análisis por categoría"""
    pass

def analizar_por_estado(prestamos):
    """Análisis por estado"""
    pass

def calcular_penalizaciones(prestamos):
    """Calcula penalizaciones"""
    pass

def main():
    """Función principal que coordina todo"""
    datos = generar_datos(100)
    
    print("=== ANÁLISIS DE BIBLIOTECA ===\n")
    
    # Llamar funciones de análisis y mostrar resultados
    pass

if __name__ == "__main__":
    main()
```

---

## Consejos para todos los ejercicios

1. **Empieza simple:** Resuelve una parte del problema, pruébala, luego sigue
2. **Usa print():** Para ver qué valores tienen tus variables
3. **Prueba con datos pequeños:** Antes de usar 100 registros, prueba con 3
4. **Lee los errores:** Python te dice qué está mal, léelo con atención
5. **Compara con tus compañeras:** Ver otras soluciones te ayuda a aprender
6. **Documenta tu código:** Escribe comentarios explicando tu lógica

## ¿Dónde compartir tus soluciones?

Puedes compartir tus soluciones en:
- Tu bitácora (carpeta `07-bitacora/`)
- Chat del grupo para discutir enfoques
- Sesiones de código con tus compañeras

Recuerda: no hay una única forma correcta de resolver estos problemas. Lo importante es que funcione y que lo entiendas.

---

¡Adelante! Estos ejercicios son tu oportunidad de consolidar todo lo aprendido. 💪
