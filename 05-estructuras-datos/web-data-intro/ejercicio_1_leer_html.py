"""
EJERCICIO 1: Leer tabla HTML
=============================
Objetivo: Cargar datos desde archivo HTML y analizarlos

Duración: 30 minutos
Nivel: Básico
"""

import pandas as pd

# =============================================================================
# PARTE 1: CARGAR DATOS DESDE HTML
# =============================================================================

print("="*60)
print("EJERCICIO 1: Leer tabla HTML")
print("="*60)

# 1. Leer tabla HTML desde archivo
# (Usa el archivo ventas_enero.html proporcionado)
df = pd.read_html('ventas_enero.html')[0]

# 2. Explorar datos básicos
print("\n📊 Primeras 5 filas:")
print(df.head())

print("\n📋 Información del DataFrame:")
print(df.info())

print("\n📈 Estadísticas descriptivas:")
print(df.describe())

# =============================================================================
# PARTE 2: ANÁLISIS DE DATOS
# =============================================================================

print("\n" + "="*60)
print("ANÁLISIS DE VENTAS")
print("="*60)

# Total de ventas por categoría
print("\n💰 Ventas por categoría:")
ventas_categoria = df.groupby('Categoría')['Total'].sum().sort_values(ascending=False)
print(ventas_categoria)

# Producto más vendido (por unidades)
idx_max_unidades = df['Unidades Vendidas'].idxmax()
producto_top = df.loc[idx_max_unidades]
print(f"\n🏆 Producto más vendido:")
print(f"   Nombre: {producto_top['Producto']}")
print(f"   Unidades: {producto_top['Unidades Vendidas']}")
print(f"   Categoría: {producto_top['Categoría']}")

# Producto con mayor ingreso total
idx_max_total = df['Total'].idxmax()
producto_top_ingreso = df.loc[idx_max_total]
print(f"\n💵 Producto con mayor ingreso:")
print(f"   Nombre: {producto_top_ingreso['Producto']}")
print(f"   Total: {producto_top_ingreso['Total']}€")

# Total general
total_general = df['Total'].sum()
total_unidades = df['Unidades Vendidas'].sum()
precio_promedio = df['Precio'].mean()

print(f"\n📊 RESUMEN GENERAL:")
print(f"   Total ventas: {total_general:,.0f}€")
print(f"   Unidades vendidas: {total_unidades}")
print(f"   Precio promedio: {precio_promedio:.2f}€")
print(f"   Productos diferentes: {len(df)}")

# =============================================================================
# PARTE 3: GUARDAR RESULTADOS
# =============================================================================

# Guardar DataFrame original como CSV
df.to_csv('ventas_procesadas.csv', index=False)
print("\n✅ Datos guardados en ventas_procesadas.csv")

# Guardar resumen de categorías
ventas_categoria.to_csv('resumen_categorias.csv', header=['Total'])
print("✅ Resumen por categorías guardado en resumen_categorias.csv")

# =============================================================================
# DESAFÍO EXTRA (Opcional)
# =============================================================================

print("\n" + "="*60)
print("🎯 DESAFÍO EXTRA:")
print("="*60)
print("1. Calcula el ticket promedio (Total / Unidades Vendidas)")
print("2. Encuentra qué categoría tiene el precio promedio más alto")
print("3. Crea un nuevo DataFrame solo con productos que vendieron >30 unidades")
print("\nPista: Usa operaciones con pandas y filtros con df[condición]")

# Descomentar las siguientes líneas cuando quieras resolver el desafío:

# # 1. Ticket promedio
# df['Ticket Promedio'] = df['Total'] / df['Unidades Vendidas']
# print("\n💳 Ticket promedio por producto:")
# print(df[['Producto', 'Ticket Promedio']].sort_values('Ticket Promedio', ascending=False))

# # 2. Precio promedio por categoría
# print("\n💰 Precio promedio por categoría:")
# precio_categoria = df.groupby('Categoría')['Precio'].mean().sort_values(ascending=False)
# print(precio_categoria)

# # 3. Productos con más de 30 unidades vendidas
# df_top_ventas = df[df['Unidades Vendidas'] > 30]
# print(f"\n🔥 Productos con >30 unidades vendidas ({len(df_top_ventas)} productos):")
# print(df_top_ventas[['Producto', 'Unidades Vendidas']])

print("\n✅ Ejercicio completado!")
