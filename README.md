# 🏥 Dashboard de Consumo - Hospital San Juan de Dios

Dashboard interactivo para el seguimiento y análisis del consumo de Jabón Quirúrgico y Alcohol Glicerinado en el Hospital San Juan de Dios de Honda E.S.E.

## 📊 Características

- Visualización de consumo por servicio hospitalario
- Análisis de tendencias mensuales
- Comparación entre años
- Filtros interactivos por servicio, producto y período
- Gráficos interactivos con Plotly
- Exportación de datos filtrados

## 🚀 Instalación Local

```bash
pip install -r requirements.txt
streamlit run dashboard.py
```

## 📁 Estructura de Datos

Los archivos CSV deben tener el formato:
- `jabones_YYYY.csv` (ejemplo: `jabones_2026.csv`)

Columnas requeridas:
- MES
- SERVICIO
- PRODUCTO
- CANTIDAD
- AÑO

## 🛠️ Tecnologías

- **Streamlit** - Framework de aplicación web
- **Pandas** - Procesamiento de datos
- **Plotly** - Visualizaciones interactivas

## 📝 Licencia

Desarrollado para el Hospital San Juan de Dios de Honda E.S.E.
