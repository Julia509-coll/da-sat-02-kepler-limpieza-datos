# 🌐 HTML Básico para Analistas de Datos

> **Nivel 2: Lectura de HTML**  
> Duración presencial: 1.5 horas  
> Trabajo autónomo: 2 horas  
> Objetivo: Leer y navegar estructura HTML desde Python

---

## ¿Por qué HTML en Python?

Como analista de datos, encontrarás datos en formato HTML en estas situaciones:

1. **Reportes automáticos:** pandas genera HTML con `df.to_html()`
2. **Tablas web:** Datos públicos en páginas web (Wikipedia, gov.es, etc.)
3. **APIs que devuelven HTML:** Algunos servicios antiguos devuelven HTML en vez de JSON
4. **Web scraping:** Extraer datos de páginas web (lo verás en profundidad en Satélite 5)

**No vas a crear páginas web.** Vas a **leer datos que están en formato HTML**.

---

## Repaso rápido: Estructura HTML

```html
<html>
    <head>
        <title>Datos</title>
    </head>
    <body>
        <h1>Reporte de Ventas</h1>
        <table>
            <tr>
                <th>Producto</th>
                <th>Precio</th>
            </tr>
            <tr>
                <td>Laptop</td>
                <td>1000</td>
            </tr>
        </table>
    </body>
</html>
```

### Tags esenciales para analistas:
- `<table>` - Tabla de datos
- `<tr>` - Fila (Table Row)
- `<td>` - Celda (Table Data)
- `<th>` - Cabecera (Table Header)
- `<div>` - Contenedor
- `<span>` - Texto inline
- `<a href="">` - Enlace

---

## Leer HTML con pandas (Método rápido)

pandas puede leer tablas HTML **automáticamente**:

```python
import pandas as pd

# Leer TODAS las tablas de una página
tablas = pd.read_html('https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_por_población')

# pd.read_html() devuelve una LISTA de DataFrames
print(f"Se encontraron {len(tablas)} tablas")

# Acceder a la primera tabla
df = tablas[0]
print(df.head())
```

### Leer desde archivo local:

```python
# Leer HTML desde archivo
df = pd.read_html('datos.html')[0]
```

### Opciones útiles:

```python
# Especificar encoding
df = pd.read_html('datos.html', encoding='utf-8')[0]

# Buscar tabla específica por atributo
df = pd.read_html('datos.html', attrs={'id': 'ventas'})[0]

# Buscar tabla por texto contenido
df = pd.read_html('datos.html', match='Producto')[0]
```

---

## Atributos HTML: class e id

Los elementos HTML pueden tener **atributos** que los identifican:

```html
<!-- ID: único en toda la página -->
<table id="ventas-2026">
    <tr>...</tr>
</table>

<!-- CLASS: puede repetirse -->
<div class="datos-financieros">
    <p class="dato">1000€</p>
    <p class="dato">2000€</p>
</div>
```

### ¿Por qué importan?

Cuando hagas web scraping, usarás estos atributos para encontrar elementos específicos:

```python
# Buscar tabla con id específico
df = pd.read_html('pagina.html', attrs={'id': 'ventas-2026'})[0]

# Buscar tabla con clase específica
df = pd.read_html('pagina.html', attrs={'class': 'tabla-datos'})[0]
```

---

## Generar HTML desde pandas

```python
import pandas as pd

# Crear DataFrame
df = pd.DataFrame({
    'Producto': ['Laptop', 'Mouse', 'Teclado'],
    'Precio': [1000, 20, 80],
    'Stock': [15, 50, 30]
})

# Convertir a HTML
html = df.to_html()

# Guardar en archivo
df.to_html('reporte.html')

# Con opciones
df.to_html('reporte.html', 
           index=False,              # Sin índice
           border=1,                 # Borde
           classes='tabla-datos')    # Clase CSS
```

### HTML generado:

```html
<table border="1" class="dataframe tabla-datos">
  <thead>
    <tr style="text-align: right;">
      <th>Producto</th>
      <th>Precio</th>
      <th>Stock</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Laptop</td>
      <td>1000</td>
      <td>15</td>
    </tr>
    ...
  </tbody>
</table>
```

---

## Estructura del DOM (Document Object Model)

HTML es un **árbol jerárquico**:

```
<body>
  ├── <div id="contenedor">
  │   ├── <h1>Título</h1>
  │   └── <table class="datos">
  │       ├── <tr>
  │       │   ├── <th>Col1</th>
  │       │   └── <th>Col2</th>
  │       └── <tr>
  │           ├── <td>Dato1</td>
  │           └── <td>Dato2</td>
```

Este concepto será fundamental cuando hagas web scraping en el Satélite 5.

---

## 🎯 Ejercicio práctico 1: Leer tabla HTML (30 min)

### Archivo: `ejercicio_leer_html.py`

```python
"""
EJERCICIO 1: Leer tabla HTML
=============================
Objetivo: Cargar datos desde archivo HTML y analizarlos
"""

import pandas as pd

# 1. Leer tabla HTML desde archivo
# (Usa el archivo ventas_enero.html proporcionado)
df = pd.read_html('ventas_enero.html')[0]

# 2. Explorar datos
print("Primeras filas:")
print(df.head())

print("\nInformación del DataFrame:")
print(df.info())

# 3. Análisis básico
print("\n--- ANÁLISIS ---")

# Total de ventas por categoría
print("\nVentas por categoría:")
print(df.groupby('Categoría')['Total'].sum())

# Producto más vendido (por unidades)
producto_top = df.loc[df['Unidades Vendidas'].idxmax()]
print(f"\nProducto más vendido: {producto_top['Producto']}")
print(f"Unidades: {producto_top['Unidades Vendidas']}")

# Total general
total_general = df['Total'].sum()
print(f"\nTotal general de ventas: {total_general}€")

# 4. Guardar resultado como CSV
df.to_csv('ventas_procesadas.csv', index=False)
print("\n✅ Datos guardados en ventas_procesadas.csv")
```

---

## 🎯 Ejercicio práctico 2: Generar reporte HTML (30 min)

### Archivo: `ejercicio_generar_reporte.py`

```python
"""
EJERCICIO 2: Generar reporte HTML
==================================
Objetivo: Crear un reporte HTML profesional con pandas
"""

import pandas as pd
from datetime import datetime

# 1. Crear datos de ejemplo
ventas = pd.DataFrame({
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'Ventas': [25000, 30000, 28000, 35000, 42000],
    'Gastos': [18000, 20000, 19000, 22000, 25000]
})

# 2. Calcular beneficio
ventas['Beneficio'] = ventas['Ventas'] - ventas['Gastos']
ventas['Margen %'] = (ventas['Beneficio'] / ventas['Ventas'] * 100).round(2)

# 3. Generar HTML con estilo
html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reporte de Ventas</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f5f5f5;
        }}
        h1 {{
            color: #2c3e50;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            background-color: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}
        th {{
            background-color: #3498db;
            color: white;
        }}
        tr:hover {{
            background-color: #f1f1f1;
        }}
        .resumen {{
            background-color: white;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
    </style>
</head>
<body>
    <h1>📊 Reporte de Ventas - {datetime.now().year}</h1>
    
    <div class="resumen">
        <h2>Resumen Ejecutivo</h2>
        <p><strong>Total Ventas:</strong> {ventas['Ventas'].sum():,}€</p>
        <p><strong>Total Gastos:</strong> {ventas['Gastos'].sum():,}€</p>
        <p><strong>Beneficio Total:</strong> {ventas['Beneficio'].sum():,}€</p>
        <p><strong>Margen Promedio:</strong> {ventas['Margen %'].mean():.2f}%</p>
    </div>
    
    <h2>Detalle Mensual</h2>
    {ventas.to_html(index=False, border=0)}
    
    <p style="color: #7f8c8d; margin-top: 40px;">
        Generado automáticamente el {datetime.now().strftime('%d/%m/%Y %H:%M')}
    </p>
</body>
</html>
"""

# 4. Guardar reporte
with open('reporte_ventas.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ Reporte generado: reporte_ventas.html")
print("   Ábrelo con tu navegador para verlo")
```

---

## 🎯 Ejercicio práctico 3: Extraer de Wikipedia (30 min)

### Archivo: `ejercicio_wikipedia.py`

```python
"""
EJERCICIO 3: Extraer datos de Wikipedia
========================================
Objetivo: Obtener datos reales de una página web
"""

import pandas as pd

# 1. URL de Wikipedia con tabla de países por población
url = 'https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_por_poblaci%C3%B3n'

# 2. Leer todas las tablas de la página
print("Descargando datos de Wikipedia...")
tablas = pd.read_html(url)
print(f"✅ Se encontraron {len(tablas)} tablas en la página")

# 3. Seleccionar la tabla principal (normalmente la primera)
df = tablas[0]

# 4. Explorar estructura
print("\nPrimeras filas:")
print(df.head())

print("\nColumnas disponibles:")
print(df.columns.tolist())

# 5. Limpieza básica (si es necesario)
# Las tablas de Wikipedia a veces tienen formato extraño
print("\nTipos de datos:")
print(df.dtypes)

# 6. Análisis simple
print("\n--- ANÁLISIS ---")
print(f"Total de países: {len(df)}")

# Los 10 países más poblados
print("\nTop 10 países por población:")
print(df.head(10)[['País', 'Población']])  # Ajusta nombres según columnas reales

# 7. Guardar datos
df.to_csv('paises_poblacion.csv', index=False, encoding='utf-8')
print("\n✅ Datos guardados en paises_poblacion.csv")

"""
DESAFÍO EXTRA:
1. Prueba con otra tabla de Wikipedia (ej: capitales, PIB, etc.)
2. Extrae datos, límpialos y crea un CSV
3. Genera un reporte HTML con los 10 primeros resultados
"""
```

---

## Conceptos clave para recordar

### 1. pandas.read_html() es tu mejor amigo
```python
# Retorna LISTA de DataFrames
tablas = pd.read_html(url)  # Puede ser URL o archivo

# Acceder a tabla específica
df = tablas[0]  # Primera tabla
```

### 2. Atributos id y class son identificadores
```python
# Buscar por id
df = pd.read_html(url, attrs={'id': 'mi-tabla'})[0]

# Buscar por clase
df = pd.read_html(url, attrs={'class': 'datos'})[0]
```

### 3. HTML es jerárquico (árbol)
```
<body>
  └── <div>
      └── <table>
          └── <tr>
              └── <td>
```

---

## 📚 Recursos para trabajo autónomo (2 horas)

### Videos:
1. **"Working with HTML in Python"** - Corey Schafer [30 min]
2. **"pandas read_html Tutorial"** - Data School [20 min]

### Lectura:
1. **pandas Documentation** - [pd.read_html()](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html)
2. **Real Python** - "HTML Parsing" (primeras secciones)

### Práctica:
1. Extrae datos de 3 páginas de Wikipedia diferentes
2. Genera un reporte HTML con tus datos personales (inventados)
3. Lee ese HTML de vuelta con pandas

---

## ✅ Checklist de competencias

Al terminar esta sesión, deberías poder:

- [ ] Usar `pd.read_html()` para leer tablas desde HTML
- [ ] Distinguir entre archivo local y URL
- [ ] Identificar atributos `id` y `class` en HTML
- [ ] Generar reportes HTML con `df.to_html()`
- [ ] Personalizar HTML generado con opciones
- [ ] Entender la estructura jerárquica del DOM
- [ ] Extraer datos de Wikipedia u otras webs con tablas

---

## 🔜 Próximos pasos

En **Satélite 5 (Curie - EDA)** aprenderás:
- **Web scraping profesional** con BeautifulSoup
- Navegar el DOM para encontrar elementos específicos
- Extraer datos de páginas sin tablas estructuradas
- Manejar paginación y múltiples páginas
- Limpiar y estructurar datos extraídos

---

## 💡 Tips profesionales

### Cuando uses `pd.read_html()`:
```python
# Siempre imprime cuántas tablas encontró
tablas = pd.read_html(url)
print(f"Tablas encontradas: {len(tablas)}")

# Inspecciona cada una
for i, tabla in enumerate(tablas):
    print(f"\nTabla {i}: {tabla.shape}")
    print(tabla.head(2))
```

### Si falla el encoding:
```python
# Prueba diferentes encodings
df = pd.read_html(url, encoding='utf-8')[0]
df = pd.read_html(url, encoding='latin-1')[0]
df = pd.read_html(url, encoding='iso-8859-1')[0]
```

---

**Autoría:** Anaïs Rodríguez Villanueva  
**Satélite 2 - Kepler: Programación con Python**  
**Bootcamp Data Analyst - 600h**

🎯 **Siguiente:** Web scraping completo en Satélite 5
