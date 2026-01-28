"""
EJERCICIO 3: Extraer datos de Wikipedia
========================================
Objetivo: Obtener datos reales de una página web pública

Duración: 30 minutos
Nivel: Intermedio
"""

import pandas as pd

# =============================================================================
# PARTE 1: EXTRAER DATOS DE WIKIPEDIA
# =============================================================================

print("="*60)
print("EJERCICIO 3: Web scraping básico con pandas")
print("="*60)

# URL de Wikipedia con tabla de países por población
url = 'https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_por_poblaci%C3%B3n'

print(f"\n🌐 Conectando a Wikipedia...")
print(f"URL: {url}")

try:
    # Leer todas las tablas de la página
    tablas = pd.read_html(url, encoding='utf-8')
    print(f"✅ Conexión exitosa")
    print(f"📊 Se encontraron {len(tablas)} tablas en la página")
    
    # =============================================================================
    # PARTE 2: EXPLORAR TABLAS ENCONTRADAS
    # =============================================================================
    
    print("\n" + "="*60)
    print("EXPLORACIÓN DE TABLAS")
    print("="*60)
    
    # Mostrar información de cada tabla
    for i, tabla in enumerate(tablas):
        print(f"\nTabla {i}:")
        print(f"  Dimensiones: {tabla.shape[0]} filas x {tabla.shape[1]} columnas")
        print(f"  Columnas: {tabla.columns.tolist()[:5]}")  # Primeras 5 columnas
    
    # =============================================================================
    # PARTE 3: SELECCIONAR Y LIMPIAR TABLA PRINCIPAL
    # =============================================================================
    
    # Normalmente la tabla principal es la primera o segunda
    # Vamos a examinar las primeras tablas para encontrar la correcta
    
    print("\n" + "="*60)
    print("ANÁLISIS DE TABLA PRINCIPAL")
    print("="*60)
    
    # Seleccionar la tabla más grande (probablemente la correcta)
    df = max(tablas, key=lambda x: len(x))
    
    print(f"\n📋 Tabla seleccionada: {df.shape[0]} países")
    print(f"\n🔍 Primeras 5 filas:")
    print(df.head())
    
    print(f"\n📊 Columnas disponibles:")
    for col in df.columns:
        print(f"  - {col}")
    
    print(f"\n📈 Tipos de datos:")
    print(df.dtypes)
    
    # =============================================================================
    # PARTE 4: ANÁLISIS DE DATOS
    # =============================================================================
    
    print("\n" + "="*60)
    print("ANÁLISIS DE DATOS")
    print("="*60)
    
    print(f"\n🌍 Total de países en la tabla: {len(df)}")
    
    # Intentar mostrar los top 10 países
    # (Los nombres de columnas pueden variar, ajustar según sea necesario)
    print(f"\n🏆 Top 10 países (primeras filas):")
    print(df.head(10))
    
    # Estadísticas básicas si hay columnas numéricas
    print(f"\n📊 Estadísticas descriptivas:")
    print(df.describe())
    
    # =============================================================================
    # PARTE 5: GUARDAR DATOS
    # =============================================================================
    
    # Guardar datos completos
    df.to_csv('paises_poblacion.csv', index=False, encoding='utf-8')
    print(f"\n✅ Datos guardados en: paises_poblacion.csv")
    
    # Guardar solo top 20
    df.head(20).to_csv('top20_paises.csv', index=False, encoding='utf-8')
    print(f"✅ Top 20 guardado en: top20_paises.csv")
    
    # Generar reporte HTML
    df.head(20).to_html('reporte_paises.html', 
                        index=False, 
                        border=1,
                        classes='table table-striped')
    print(f"✅ Reporte HTML generado: reporte_paises.html")

except Exception as e:
    print(f"\n❌ Error al extraer datos: {e}")
    print("\nPosibles causas:")
    print("  - Sin conexión a internet")
    print("  - Wikipedia cambió la estructura de la página")
    print("  - Problema de encoding")

# =============================================================================
# PARTE 6: DESAFÍO EXTRA - OTRAS TABLAS DE WIKIPEDIA
# =============================================================================

print("\n" + "="*60)
print("🎯 DESAFÍO EXTRA: Explora otras tablas")
print("="*60)

# Sugerencias de URLs de Wikipedia con tablas interesantes:
urls_sugeridas = {
    'PIB por país': 'https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_por_PIB_(nominal)',
    'Capitales del mundo': 'https://es.wikipedia.org/wiki/Anexo:Capitales_de_pa%C3%ADses',
    'Medallas olímpicas': 'https://es.wikipedia.org/wiki/Anexo:Medallero_de_los_Juegos_Ol%C3%ADmpicos',
    'Idiomas más hablados': 'https://es.wikipedia.org/wiki/Anexo:Idiomas_por_n%C3%BAmero_de_hablantes',
}

print("\n📚 URLs sugeridas para practicar:")
for nombre, url in urls_sugeridas.items():
    print(f"\n  {nombre}:")
    print(f"  {url}")

print("\n" + "="*60)
print("📝 Tareas del desafío:")
print("="*60)
print("""
1. Elige una de las URLs sugeridas (o busca otra tabla en Wikipedia)
2. Extrae los datos con pd.read_html()
3. Limpia y explora los datos
4. Crea un CSV con los resultados
5. Genera un reporte HTML profesional
6. BONUS: Combina datos de 2 tablas diferentes (ej: población + PIB)

Pistas:
- Usa try/except para manejar errores
- Imprime len(tablas) para ver cuántas tablas encontró
- Explora df.columns para ver los nombres de columnas
- Usa df.head() para verificar que tienes la tabla correcta
""")

print("\n✅ Ejercicio completado!")
print("\n💡 TIP: En el Satélite 5 aprenderás web scraping avanzado")
print("   con BeautifulSoup para páginas más complejas.")
