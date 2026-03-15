### Enunciado

#Tienes datos de ventas mensuales. Escribe un programa que:

#1. Guarde las ventas de cada mes en variables
#2. Calcule el total y el promedio
#3. Identifique el mes con mayores ventas
#4. Determine si se alcanzó la meta anual (50000)

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
promedio = round(promedio, 2)
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

meta = 50000

if total >= meta:
    print("Meta anual alcanzada")
else:
    print("Meta anual NO alcanzada")  

## Ejercicio 2: Clasificador de préstamos
def clasificar_prestamo(dias):

    if dias <= 21:
        estado = "A_tiempo"
        penalizacion = 0

    elif  dias <= 30:
        estado = "Retraso_leve"
        # calcular penalizacion
        extra = dias - 21
        penalizacion = extra * 0.50
    else:
        estado = "Retraso_grave"
          # calcular penalizacion
        extra = dias - 30
        penalizacion = extra * 1.00
    
    return {"estado" : estado, 
                "penalizacion" : penalizacion}    
        
print(clasificar_prestamo(15))
print(clasificar_prestamo(25))
print(clasificar_prestamo(35))  

#Luego procesa una lista de préstamos y muestra estadísticas.
prestamos_dias = [15, 22, 18, 35, 25, 12, 40, 19, 28, 33]
#Crear contadores
conteo_estados = {"A_tiempo": 0, "Retraso_leve": 0, "Retraso_grave": 0}
total_penalizacion = 0

for dias in prestamos_dias:
    resultado = clasificar_prestamo(dias)
    estado = resultado["estado"]
    penalizacion = resultado["penalizacion"]

    # Acumulamos la penalización económica
    total_penalizacion += penalizacion

    # Sumamos uno al contador de ese estado específico
    conteo_estados[estado] += 1

print(f"penalización total recaudada: {total_penalizacion}€")
print(f"Resumen por categorías: {conteo_estados}")

## Ejercicio 3: Análisis de categorías

#Objetivo:** Practicar listas, diccionarios y bucles
# Diccionario vacío para agrupar
prestamos = [
    {"titulo": "1984", "categoria": "Ficción", "dias": 15},
    {"titulo": "Sapiens", "categoria": "Ensayo", "dias": 22},
    {"titulo": "Watchmen", "categoria": "Cómic", "dias": 18},
    {"titulo": "El Quijote", "categoria": "Ficción", "dias": 30},
    {"titulo": "Breve historia", "categoria": "Ensayo", "dias": 25},
    {"titulo": "Batman", "categoria": "Cómic", "dias": 12}
]
agrupados = {}
 
for libro in prestamos:
    cat = libro["categoria"]
    dias = libro["dias"]
    # Si la categoría no existe en 'agrupados', la creamos con una lista vacía
    if cat not in agrupados:
        agrupados[cat] = []
        # Añadimos los días a esa categoría
    agrupados[cat].append(dias)

print(f"Datos agrupados: {agrupados}")

print("\n=== RESUMEN POR CATEGORÍA ===")

for cat, lista_dias in agrupados.items():
    # Calculamos el promedio: suma de días / cantidad de libros
    promedio = sum(lista_dias) / len(lista_dias)
    
    # Usamos f-string con 1 decimal para que quede limpio
    print(f"Categoría: {cat:10} | Promedio de días: {promedio:.1f}")

categoria_top = ""
max_prestamos = 0

for cat, lista in agrupados.items():
    if len(lista) > max_prestamos:
        max_prestamos = len(lista)
        categoria_top = cat

print(f"🏆 La categoría con más éxito es: {categoria_top} ({max_prestamos} libros)")
print("\n📖 Libros con préstamo extendido (> 20 días):")
for libro in prestamos:
    if libro["dias"] > 20:
        # Usamos f-strings para que el reporte sea elegante
        print(f" - {libro['titulo']} ({libro['categoria']}): {libro['dias']} días")
        
 ## Ejercicio 4: Procesador de datos 
#Crea un sistema que procese datos de ventas con las siguientes funciones:


def limpiar_datos(ventas):
    """Elimina valores negativos o None""" 
    ventas_limpias = []
    for v in ventas:
        if v is not None and v > 0:
            ventas_limpias.append(v)
    return ventas_limpias

def calcular_estadisticas(ventas):
    total_recaudado = sum(ventas)
    promedio_ventas = round(total_recaudado / len(ventas), 2)
    venta_maxima = max(ventas)
    venta_minima = min(ventas)
    return {
        "total": total_recaudado,
        "promedio": promedio_ventas,
        "max": venta_maxima,
        "min": venta_minima
    }

def clasificar_ventas(ventas, umbral_bajo, umbral_alto):
    conteo = {"bajas": 0, "medias": 0, "altas": 0}
    for v in ventas:
        if v < umbral_bajo:
            conteo["bajas"] += 1
        elif v >= umbral_alto:
            conteo["altas"] += 1
        else:
            conteo["medias"] += 1
    return conteo

# --- EJECUCIÓN DEL PROGRAMA ---

ventas_brutas = [1500, -200, 2500, None, 3000, 0, 4500, -100, 2800, 5000]

# 1. Limpiamos
datos_listos = limpiar_datos(ventas_brutas)

# 2. Calculamos estadísticas
estadisticas_finales = calcular_estadisticas(datos_listos)

# 3. Clasificamos (¡Aquí usamos datos_listos, NO limpiar_datos!)
distribucion = clasificar_ventas(datos_listos, 2000, 4000)

# 4. Definimos el total para los porcentajes
total_v = len(datos_listos)

# 5. IMPRIMIMOS EL REPORTE FINAL
print("\n=== REPORTE DE VENTAS ===")
print(f"Ventas procesadas: {total_v}")
print(f"Total: {estadisticas_finales['total']}€")
print(f"Promedio: {estadisticas_finales['promedio']}€")
print("-" * 25)

# Calculamos porcentajes al vuelo para que el print sea limpio
print(f"Ventas bajas (< 2000): {distribucion['bajas']} ({(distribucion['bajas']/total_v)*100:.1f}%)")
print(f"Ventas medias: {distribucion['medias']} ({(distribucion['medias']/total_v)*100:.1f}%)")
print(f"Ventas altas (>= 4000): {distribucion['altas']} ({(distribucion['altas']/total_v)*100:.1f}%)")

import random

def generar_datos(n=100):
    """Misión 1: Crear 100 préstamos inventados"""
    categorias = ["Ficción", "Ensayo", "Cómic", "Poesía"]
    lista_prestamos = []
    for _ in range(n):
        prestamo = {
            "categoria": random.choice(categorias),
            "dias": random.randint(5, 45) # Días que el usuario tuvo el libro
        }
        lista_prestamos.append(prestamo)
    return lista_prestamos

def analizar_por_categoria(prestamos):
    """Misión 2: Agrupar por género literario"""
    conteo = {}
    for p in prestamos:
        cat = p["categoria"]
        if cat not in conteo:
            conteo[cat] = {"cantidad": 0, "suma_dias": 0}
        conteo[cat]["cantidad"] += 1
        conteo[cat]["suma_dias"] += p["dias"]
    return conteo

def analizar_por_estado(prestamos):
    """Misión 3: Clasificar según el tiempo (igual que las ventas)"""
    estados = {"A tiempo": 0, "Retraso leve": 0, "Retraso grave": 0}
    for p in prestamos:
        if p["dias"] <= 21:
            estados["A tiempo"] += 1
        elif 22 <= p["dias"] <= 30:
            estados["Retraso leve"] += 1
        else:
            estados["Retraso grave"] += 1
    return estados

def calcular_penalizaciones(prestamos):
    """Misión 4: Calcular la multa (2€ por cada día después del 21)"""
    total_multas = 0
    con_retraso = 0
    for p in prestamos:
        if p["dias"] > 21:
            dias_extra = p["dias"] - 21
            total_multas += dias_extra * 2 # 2 euros por día de multa
            con_retraso += 1
    
    promedio_multa = total_multas / con_retraso if con_retraso > 0 else 0
    return total_multas, promedio_multa

def main():
    """Misión 5: El Director de Orquesta que imprime el reporte"""
    n_total = 100
    datos = generar_datos(n_total)
    
    # Ejecutamos los análisis
    por_cat = analizar_por_categoria(datos)
    por_estado = analizar_por_estado(datos)
    multa_total, multa_promedio = calcular_penalizaciones(datos)

    print("="*40)
    print("      REPORTE DE LA BIBLIOTECA")
    print("="*40)

    # 1. Mostrar por Categoría
    print("\n--- ANÁLISIS POR CATEGORÍA ---")
    for cat, info in por_cat.items():
        porcentaje = (info['cantidad'] / n_total) * 100
        promedio = info['suma_dias'] / info['cantidad']
        print(f"{cat:8}: {info['cantidad']} préstamos ({porcentaje:2.0f}%) | Media: {promedio:.1f} días")

    # 2. Mostrar por Estado
    print("\n--- ESTADO DE LOS PRÉSTAMOS ---")
    for estado, cant in por_estado.items():
        print(f"{estado:15}: {cant} libros")

    # 3. Mostrar Penalizaciones
    print("\n--- PENALIZACIONES ---")
    print(f"Total recaudado: {multa_total}€")
    print(f"Multa promedio:  {multa_promedio:.2f}€")
    print("="*40)

if __name__ == "__main__":
    main()
 


    
