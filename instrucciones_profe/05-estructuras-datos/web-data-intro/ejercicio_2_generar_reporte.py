"""
EJERCICIO 2: Generar reporte HTML
==================================
Objetivo: Crear un reporte HTML profesional con pandas

Duración: 30 minutos
Nivel: Intermedio
"""

import pandas as pd
from datetime import datetime

# =============================================================================
# PARTE 1: CREAR DATOS DE EJEMPLO
# =============================================================================

print("="*60)
print("EJERCICIO 2: Generar reporte HTML")
print("="*60)

# Crear datos de ventas mensuales
ventas = pd.DataFrame({
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
    'Ventas': [25000, 30000, 28000, 35000, 42000, 38000],
    'Gastos': [18000, 20000, 19000, 22000, 25000, 23000]
})

# Calcular métricas adicionales
ventas['Beneficio'] = ventas['Ventas'] - ventas['Gastos']
ventas['Margen %'] = (ventas['Beneficio'] / ventas['Ventas'] * 100).round(2)

print("\n📊 Datos generados:")
print(ventas)

# =============================================================================
# PARTE 2: CALCULAR RESUMEN EJECUTIVO
# =============================================================================

total_ventas = ventas['Ventas'].sum()
total_gastos = ventas['Gastos'].sum()
total_beneficio = ventas['Beneficio'].sum()
margen_promedio = ventas['Margen %'].mean()
mejor_mes = ventas.loc[ventas['Beneficio'].idxmax(), 'Mes']
mejor_beneficio = ventas['Beneficio'].max()

print(f"\n📈 Resumen:")
print(f"   Total Ventas: {total_ventas:,}€")
print(f"   Total Gastos: {total_gastos:,}€")
print(f"   Beneficio: {total_beneficio:,}€")
print(f"   Margen promedio: {margen_promedio:.2f}%")
print(f"   Mejor mes: {mejor_mes} ({mejor_beneficio:,}€)")

# =============================================================================
# PARTE 3: GENERAR HTML PROFESIONAL
# =============================================================================

html_completo = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reporte de Ventas {datetime.now().year}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 40px;
            min-height: 100vh;
        }}
        
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background-color: white;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 36px;
            margin-bottom: 10px;
        }}
        
        .header p {{
            font-size: 18px;
            opacity: 0.9;
        }}
        
        .content {{
            padding: 40px;
        }}
        
        .resumen {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }}
        
        .card {{
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 25px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }}
        
        .card:hover {{
            transform: translateY(-5px);
        }}
        
        .card h3 {{
            color: #667eea;
            font-size: 14px;
            margin-bottom: 10px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        .card .value {{
            font-size: 32px;
            font-weight: bold;
            color: #2c3e50;
        }}
        
        .card .subvalue {{
            font-size: 14px;
            color: #7f8c8d;
            margin-top: 5px;
        }}
        
        h2 {{
            color: #2c3e50;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        
        thead {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }}
        
        th {{
            padding: 15px;
            text-align: left;
            font-weight: 600;
            text-transform: uppercase;
            font-size: 12px;
            letter-spacing: 1px;
        }}
        
        td {{
            padding: 15px;
            border-bottom: 1px solid #ecf0f1;
        }}
        
        tbody tr:hover {{
            background-color: #f8f9fa;
        }}
        
        tbody tr:last-child td {{
            border-bottom: none;
        }}
        
        .positivo {{
            color: #27ae60;
            font-weight: bold;
        }}
        
        .negativo {{
            color: #e74c3c;
            font-weight: bold;
        }}
        
        .footer {{
            background-color: #f8f9fa;
            padding: 20px 40px;
            text-align: center;
            color: #7f8c8d;
            font-size: 14px;
        }}
        
        .footer .timestamp {{
            margin-top: 10px;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Reporte de Ventas</h1>
            <p>Análisis Financiero Semestral {datetime.now().year}</p>
        </div>
        
        <div class="content">
            <h2>📈 Resumen Ejecutivo</h2>
            <div class="resumen">
                <div class="card">
                    <h3>Ventas Totales</h3>
                    <div class="value">{total_ventas:,}€</div>
                    <div class="subvalue">6 meses</div>
                </div>
                <div class="card">
                    <h3>Gastos Totales</h3>
                    <div class="value">{total_gastos:,}€</div>
                    <div class="subvalue">{(total_gastos/total_ventas*100):.1f}% de ventas</div>
                </div>
                <div class="card">
                    <h3>Beneficio Neto</h3>
                    <div class="value positivo">{total_beneficio:,}€</div>
                    <div class="subvalue">{margen_promedio:.2f}% margen</div>
                </div>
                <div class="card">
                    <h3>Mejor Mes</h3>
                    <div class="value">{mejor_mes}</div>
                    <div class="subvalue">{mejor_beneficio:,}€ beneficio</div>
                </div>
            </div>
            
            <h2>📋 Detalle Mensual</h2>
"""

# Añadir tabla manualmente para tener control total
html_completo += """
            <table>
                <thead>
                    <tr>
                        <th>Mes</th>
                        <th>Ventas</th>
                        <th>Gastos</th>
                        <th>Beneficio</th>
                        <th>Margen %</th>
                    </tr>
                </thead>
                <tbody>
"""

# Añadir filas de datos
for _, row in ventas.iterrows():
    clase_margen = "positivo" if row['Margen %'] > 25 else ""
    html_completo += f"""
                    <tr>
                        <td><strong>{row['Mes']}</strong></td>
                        <td>{row['Ventas']:,}€</td>
                        <td>{row['Gastos']:,}€</td>
                        <td class="positivo">{row['Beneficio']:,}€</td>
                        <td class="{clase_margen}">{row['Margen %']}%</td>
                    </tr>
"""

html_completo += f"""
                </tbody>
            </table>
        </div>
        
        <div class="footer">
            <p><strong>Nota:</strong> Este reporte fue generado automáticamente con Python y pandas</p>
            <p class="timestamp">Generado el {datetime.now().strftime('%d/%m/%Y a las %H:%M:%S')}</p>
        </div>
    </div>
</body>
</html>
"""

# =============================================================================
# PARTE 4: GUARDAR HTML
# =============================================================================

with open('reporte_ventas_profesional.html', 'w', encoding='utf-8') as f:
    f.write(html_completo)

print("\n✅ Reporte HTML generado: reporte_ventas_profesional.html")
print("   👉 Ábrelo con tu navegador para verlo")

# También generar versión simple con pandas
ventas.to_html('reporte_ventas_simple.html', 
               index=False, 
               border=1,
               classes='dataframe',
               float_format='%.2f')

print("✅ Reporte simple generado: reporte_ventas_simple.html")

# =============================================================================
# DESAFÍO EXTRA (Opcional)
# =============================================================================

print("\n" + "="*60)
print("🎯 DESAFÍO EXTRA:")
print("="*60)
print("1. Añade un gráfico al reporte (pista: usa plotly o matplotlib)")
print("2. Añade una sección de 'Tendencias' calculando crecimientos mes a mes")
print("3. Añade alertas visuales si el margen baja de 20%")
print("\n✅ Ejercicio completado!")
