import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# Page configuration
st.set_page_config(
    page_title="Consumo Jabón Quirúrgico - Alcohol Glicerinado",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for premium hospital design
st.markdown("""
    <style>
    /* Hide Streamlit branding and toolbar */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Remove white spaces */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
    }
    
    /* Main background */
    .main {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
    }
    
    .stApp {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
    }
    
    /* Header styling with new color */
    .hospital-header {
        background: linear-gradient(135deg, #27C8F5 0%, #1fb5e0 100%);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(39, 200, 245, 0.3);
        margin-bottom: 2rem;
        display: flex;
        align-items: center;
        gap: 2rem;
    }
    
    .header-content {
        flex: 1;
    }
    
    .hospital-title {
        color: #ffffff !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        text-align: center;
        text-transform: uppercase;
    }
    
    .hospital-subtitle {
        color: #ffffff;
        font-size: 1.1rem;
        margin-top: 0.5rem;
        font-weight: 700;
        text-align: center;
    }
    
    /* Sidebar styling with new color and better contrast */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #27C8F5 0%, #1a9bc7 100%);
        padding-top: 0 !important;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background: linear-gradient(180deg, #27C8F5 0%, #1a9bc7 100%);
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: white;
    }
    
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] h4 {
        color: white !important;
    }
    
    [data-testid="stSidebar"] p {
        color: white !important;
    }
    
    [data-testid="stSidebar"] label {
        color: #1e3a8a !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
    }
    
    /* Filter section styling with dark background */
    .filter-container {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        padding: 1rem 1.5rem 0.5rem 1.5rem;
        border-radius: 16px;
        margin-bottom: 1.2rem;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3), 0 2px 6px rgba(39, 200, 245, 0.2);
        border: 2px solid rgba(39, 200, 245, 0.4);
        transition: all 0.3s ease;
    }
    
    .filter-container:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4), 0 3px 8px rgba(39, 200, 245, 0.35);
        border-color: rgba(39, 200, 245, 0.6);
    }
    
    .filter-title {
        color: #ffffff;
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .filter-description {
        color: #cbd5e1;
        font-size: 0.82rem;
        margin-bottom: 0.5rem;
        font-style: normal;
        line-height: 1.4;
    }
    
    /* Metric cards with new color */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        color: #27C8F5;
        font-weight: 700;
    }
    
    [data-testid="stMetricLabel"] {
        color: #475569;
        font-weight: 600;
        font-size: 1rem;
    }
    
    div[data-testid="metric-container"] {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        border-top: 4px solid #27C8F5;
        transition: all 0.3s ease;
    }
    
    div[data-testid="metric-container"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 24px rgba(39, 200, 245, 0.25);
    }
    
    /* Chart containers */
    .chart-container {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        margin-bottom: 1.5rem;
    }
    
    /* Section headers with new color */
    .section-header {
        color: #27C8F5;
        font-size: 1.5rem;
        font-weight: 700;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #27C8F5;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Dataframe styling */
    [data-testid="stDataFrame"] {
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }
    
    /* Download button with new color */
    .stDownloadButton button {
        background: linear-gradient(135deg, #27C8F5 0%, #1fb5e0 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 8px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(39, 200, 245, 0.3);
    }
    
    .stDownloadButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(39, 200, 245, 0.4);
    }
    
    /* Selectbox styling - better visibility */
    .stSelectbox > div > div {
        background-color: white;
        border-radius: 10px;
        border: 2px solid #e2e8f0;
        color: #1e293b;
        transition: all 0.2s ease;
    }
    
    .stSelectbox > div > div:hover {
        border-color: #27C8F5;
        box-shadow: 0 0 0 3px rgba(39, 200, 245, 0.1);
    }
    
    .stSelectbox > div > div:focus-within {
        border-color: #27C8F5;
        box-shadow: 0 0 0 3px rgba(39, 200, 245, 0.15);
    }
    
    .stSelectbox label {
        color: #1e3a8a !important;
    }
    
    /* Multiselect styling */
    .stMultiSelect > div > div {
        background-color: white;
        border-radius: 10px;
        border: 2px solid #e2e8f0;
        transition: all 0.2s ease;
    }
    
    .stMultiSelect > div > div:hover {
        border-color: #27C8F5;
        box-shadow: 0 0 0 3px rgba(39, 200, 245, 0.1);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #64748b;
        padding: 2rem;
        margin-top: 3rem;
        border-top: 2px solid #e2e8f0;
    }
    
    /* Logo container */
    .logo-container {
        width: 120px;
        height: 120px;
        background: white;
        border-radius: 50%;
        padding: 10px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }
    
    .logo-container img {
        width: 100%;
        height: 100%;
        object-fit: contain;
    }
    
    /* Active filters box - better contrast */
    .active-filters-box {
        background: rgba(255, 255, 255, 0.25);
        padding: 1rem;
        border-radius: 8px;
        margin-top: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    .active-filters-box h4 {
        color: white !important;
        margin-top: 0;
        font-size: 1.1rem;
    }
    
    .active-filters-box p {
        color: white !important;
        margin: 0.3rem 0;
        font-size: 0.9rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    """Carga datos de múltiples años desde archivos CSV separados"""
    import os
    import glob
    
    month_order = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 
                   'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']
    
    # Buscar todos los archivos jabones_YYYY.csv
    csv_files = glob.glob('jabones_*.csv')
    
    if not csv_files:
        # Si no hay archivos con año, buscar el archivo original
        if os.path.exists('jabones.csv'):
            df = pd.read_csv('jabones.csv', sep=';', encoding='latin-1')
            df['AÑO'] = 2025  # Asumir que es 2025
            df['MES'] = pd.Categorical(df['MES'], categories=month_order, ordered=True)
            return df
        else:
            st.error("No se encontraron archivos de datos")
            return pd.DataFrame()
    
    # Cargar y combinar todos los archivos
    dfs = []
    for file in csv_files:
        # Extraer el año del nombre del archivo (jabones_2025.csv -> 2025)
        year = int(file.split('_')[1].split('.')[0])
        df_year = pd.read_csv(file, sep=';', encoding='latin-1')
        df_year['AÑO'] = year
        dfs.append(df_year)
    
    # Combinar todos los DataFrames
    df = pd.concat(dfs, ignore_index=True)
    df['MES'] = pd.Categorical(df['MES'], categories=month_order, ordered=True)
    
    return df

df = load_data()

# Header
st.markdown("""
    <div class="hospital-header">
        <div class="header-content">
            <h1 class="hospital-title">🏥 Seguimiento de Consumo Jabón Quirúrgico - Alcohol Glicerinado</h1>
            <p class="hospital-subtitle">HOSPITAL SAN JUAN DE DIOS DE HONDA E.S.E</p>
        </div>
    </div>
    """, unsafe_allow_html=True)


# Sidebar filters with improved design
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 1.5rem 0; border-bottom: 2px solid rgba(255,255,255,0.2); margin-bottom: 2rem;">
            <h2 style="color: white; margin: 0; font-size: 1.8rem;">🔍 Panel de Filtros</h2>
            <p style="color: #e0f2fe; margin-top: 0.5rem; font-size: 0.9rem;">Personaliza tu vista de datos</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Modo de visualización
    st.markdown('<div class="filter-title">📊 Modo de Visualización</div>', unsafe_allow_html=True)
    st.markdown('<div class="filter-description">Selecciona cómo visualizar los datos</div>', unsafe_allow_html=True)
    modo_visualizacion = st.selectbox("Modo de Visualización", ["Año Único", "Comparación entre Años"], key="modo", label_visibility="collapsed")
    
    # Filtro de año(s)
    años_disponibles = sorted(df['AÑO'].unique().tolist(), reverse=True)
    
    if modo_visualizacion == "Año Único":
        st.markdown('<div class="filter-title">📅 Año</div>', unsafe_allow_html=True)
        st.markdown('<div class="filter-description">Selecciona el año a analizar</div>', unsafe_allow_html=True)
        año_seleccionado = st.selectbox("Año", años_disponibles, key="año", label_visibility="collapsed")
        años_comparar = [año_seleccionado]
    else:
        st.markdown('<div class="filter-title">📅 Años a Comparar</div>', unsafe_allow_html=True)
        st.markdown('<div class="filter-description">Selecciona los años para comparar</div>', unsafe_allow_html=True)
        años_comparar = st.multiselect("Años a Comparar", años_disponibles, default=años_disponibles[:2] if len(años_disponibles) >= 2 else años_disponibles, key="años_comp", label_visibility="collapsed")
    
    st.markdown('<div class="filter-title">🏥 Servicio</div>', unsafe_allow_html=True)
    st.markdown('<div class="filter-description">Selecciona el departamento a analizar</div>', unsafe_allow_html=True)
    servicios = ['Todos'] + sorted(df['SERVICIO'].unique().tolist())
    servicio_seleccionado = st.selectbox("Servicio", servicios, key="servicio", label_visibility="collapsed")
    
    st.markdown('<div class="filter-title">🧴 Producto</div>', unsafe_allow_html=True)
    st.markdown('<div class="filter-description">Filtra por tipo de insumo</div>', unsafe_allow_html=True)
    productos = ['Todos'] + sorted(df['PRODUCTO'].unique().tolist())
    producto_seleccionado = st.selectbox("Producto", productos, key="producto", label_visibility="collapsed")
    
    st.markdown('<div class="filter-title">📅 Período Mensual</div>', unsafe_allow_html=True)
    st.markdown('<div class="filter-description">Selecciona el mes a consultar</div>', unsafe_allow_html=True)
    meses = ['Todos'] + df['MES'].cat.categories.tolist()
    mes_seleccionado = st.selectbox("Mes", meses, key="mes", label_visibility="collapsed")
    
    
    # Active filters summary
    st.markdown("---")
    st.markdown("""
        <div class="active-filters-box">
            <h4>📋 Filtros Activos</h4>
    """, unsafe_allow_html=True)
    
    active_filters = []
    if modo_visualizacion == "Año Único":
        active_filters.append(f"• Año: {año_seleccionado}")
    else:
        active_filters.append(f"• Comparando: {', '.join(map(str, años_comparar))}")
    if servicio_seleccionado != 'Todos':
        active_filters.append(f"• Servicio: {servicio_seleccionado}")
    if producto_seleccionado != 'Todos':
        active_filters.append(f"• Producto: {producto_seleccionado}")
    if mes_seleccionado != 'Todos':
        active_filters.append(f"• Mes: {mes_seleccionado}")
    
    if active_filters:
        for filter_text in active_filters:
            st.markdown(f'<p>{filter_text}</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p style="font-style: italic;">Sin filtros aplicados</p>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Apply filters
df_filtered = df.copy()

# Filtrar por años
if años_comparar:
    df_filtered = df_filtered[df_filtered['AÑO'].isin(años_comparar)]

if servicio_seleccionado != 'Todos':
    df_filtered = df_filtered[df_filtered['SERVICIO'] == servicio_seleccionado]
if producto_seleccionado != 'Todos':
    df_filtered = df_filtered[df_filtered['PRODUCTO'] == producto_seleccionado]
if mes_seleccionado != 'Todos':
    df_filtered = df_filtered[df_filtered['MES'] == mes_seleccionado]

# Key Metrics
st.markdown('<div class="section-header">📊 Indicadores Clave de Consumo</div>', unsafe_allow_html=True)

# Métricas por producto
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🧴 Jabón Quirúrgico")
    df_jabon = df_filtered[df_filtered['PRODUCTO'] == 'JABON QUIRURGICO']
    total_jabon = df_jabon['CANTIDAD'].sum()
    promedio_jabon = df_jabon.groupby('MES', observed=False)['CANTIDAD'].sum().mean() if len(df_jabon) > 0 else 0
    
    subcol1, subcol2 = st.columns(2)
    with subcol1:
        st.metric(
            label="📦 Consumo Total",
            value=f"{total_jabon:,}",
            delta="unidades"
        )
    with subcol2:
        st.metric(
            label="📈 Promedio Mensual",
            value=f"{promedio_jabon:.1f}",
            delta="unidades/mes"
        )

with col2:
    st.markdown("#### 🧴 Alcohol Glicerinado")
    df_alcohol = df_filtered[df_filtered['PRODUCTO'] == 'ALCOHOL GLICERINADO']
    total_alcohol = df_alcohol['CANTIDAD'].sum()
    promedio_alcohol = df_alcohol.groupby('MES', observed=False)['CANTIDAD'].sum().mean() if len(df_alcohol) > 0 else 0
    
    subcol1, subcol2 = st.columns(2)
    with subcol1:
        st.metric(
            label="📦 Consumo Total",
            value=f"{total_alcohol:,}",
            delta="unidades"
        )
    with subcol2:
        st.metric(
            label="📈 Promedio Mensual",
            value=f"{promedio_alcohol:.1f}",
            delta="unidades/mes"
        )

# Métricas generales
st.markdown("---")
col3, col4 = st.columns(2)

with col3:
    num_servicios = df_filtered['SERVICIO'].nunique()
    st.metric(
        label="🏥 Servicios Activos",
        value=num_servicios,
        delta="departamentos"
    )

with col4:
    mes_mayor = df_filtered.groupby('MES', observed=False)['CANTIDAD'].sum().idxmax() if len(df_filtered) > 0 else "N/A"
    st.metric(
        label="🔝 Mes Pico",
        value=mes_mayor,
        delta="mayor consumo"
    )

st.markdown("---")

# Charts section
st.markdown('<div class="section-header">📈 Análisis de Tendencias y Distribución</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 📊 Evolución Mensual por Producto")
    
    if modo_visualizacion == "Comparación entre Años" and len(años_comparar) > 1:
        # Crear una columna combinada para año y producto
        df_mensual = df_filtered.groupby(['MES', 'PRODUCTO', 'AÑO'], observed=False)['CANTIDAD'].sum().reset_index()
        df_mensual['PRODUCTO_AÑO'] = df_mensual['PRODUCTO'] + ' (' + df_mensual['AÑO'].astype(str) + ')'
        
        # Colores alternados para diferentes años
        colores = ['#27C8F5', '#FF6B35', '#10B981', '#F59E0B', '#8B5CF6', '#EC4899']
        
        fig1 = px.line(
            df_mensual, 
            x='MES', 
            y='CANTIDAD', 
            color='PRODUCTO_AÑO',
            markers=True,
            color_discrete_sequence=colores
        )
    else:
        # Visualización normal para un solo año
        df_mensual = df_filtered.groupby(['MES', 'PRODUCTO'], observed=False)['CANTIDAD'].sum().reset_index()
        fig1 = px.line(
            df_mensual, 
            x='MES', 
            y='CANTIDAD', 
            color='PRODUCTO',
            markers=True,
            color_discrete_sequence=['#27C8F5', '#FF6B35']
        )
    
    fig1.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=12, color='#334155'),
        hovermode='x unified',
        xaxis_title="Mes",
        yaxis_title="Cantidad (unidades)",
        legend=dict(
            title="Producto" if modo_visualizacion == "Año Único" else "Producto (Año)",
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='#0891b2',
            borderwidth=1
        ),
        height=400
    )
    fig1.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(148,163,184,0.2)')
    fig1.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(148,163,184,0.2)')
    fig1.update_traces(line=dict(width=3), marker=dict(size=8))
    st.plotly_chart(fig1, width='stretch')

with col2:
    st.markdown("#### 🏥 Consumo Total por Servicio")
    df_servicio = df_filtered.groupby('SERVICIO', observed=False)['CANTIDAD'].sum().reset_index()
    df_servicio = df_servicio.sort_values('CANTIDAD', ascending=True)
    fig2 = px.bar(
        df_servicio,
        x='CANTIDAD',
        y='SERVICIO',
        orientation='h',
        color='CANTIDAD',
        color_continuous_scale=['#e0f2fe', '#27C8F5', '#1a9bc7']
    )
    fig2.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=12, color='#334155'),
        showlegend=False,
        xaxis_title="Cantidad Total (unidades)",
        yaxis_title="Servicio Hospitalario",
        height=400
    )
    fig2.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(148,163,184,0.2)')
    fig2.update_traces(marker=dict(line=dict(width=0)))
    st.plotly_chart(fig2, width='stretch')

# Pie chart and comparison
st.markdown('<div class="section-header">🎯 Distribución y Comparación Detallada</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("#### 📊 Distribución por Producto")
    df_producto = df_filtered.groupby('PRODUCTO', observed=False)['CANTIDAD'].sum().reset_index()
    fig3 = go.Figure(data=[go.Pie(
        labels=df_producto['PRODUCTO'],
        values=df_producto['CANTIDAD'],
        hole=.5,
        marker=dict(colors=['#27C8F5', '#FF6B35'], line=dict(color='white', width=2)),
        textinfo='label+percent',
        textfont_size=13,
        textfont_color='white',
        textposition='inside'
    )])
    fig3.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=12, color='#334155'),
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.1
        ),
        height=400
    )
    st.plotly_chart(fig3, width='stretch')

with col2:
    st.markdown("#### 📊 Comparación por Servicio y Producto")
    df_comparison = df_filtered.groupby(['SERVICIO', 'PRODUCTO'], observed=False)['CANTIDAD'].sum().reset_index()
    fig4 = px.bar(
        df_comparison,
        x='SERVICIO',
        y='CANTIDAD',
        color='PRODUCTO',
        barmode='group',
        color_discrete_sequence=['#27C8F5', '#FF6B35']
    )
    fig4.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=12, color='#334155'),
        xaxis_title="Servicio Hospitalario",
        yaxis_title="Cantidad Total (unidades)",
        legend=dict(
            title="Producto",
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='#0891b2',
            borderwidth=1
        ),
        height=400
    )
    fig4.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(148,163,184,0.2)', tickangle=-45)
    fig4.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(148,163,184,0.2)')
    st.plotly_chart(fig4, width='stretch')

# Data table
st.markdown('<div class="section-header">📋 Tabla de Datos Detallada</div>', unsafe_allow_html=True)
st.dataframe(
    df_filtered.sort_values(['SERVICIO', 'PRODUCTO', 'MES']),
    width='stretch',
    hide_index=True,
    height=400
)

# Download section
st.markdown('<div class="section-header">💾 Exportar Datos</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    csv = df_filtered.to_csv(index=False, sep=';', encoding='latin-1')
    st.download_button(
        label="📥 Descargar CSV Filtrado",
        data=csv,
        file_name=f"consumo_filtrado_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv"
    )

with col2:
    total_records = len(df_filtered)
    st.info(f"📊 Total de registros: **{total_records}**")

# Footer
st.markdown("""
    <div class="footer">
        <p style="margin: 0; font-size: 0.9rem; color: #64748b;">
            <strong>Hospital San Juan de Dios de Honda</strong> - Empresa Social del Estado
        </p>
        <p style="margin: 0.5rem 0 0 0; font-size: 0.85rem; color: #94a3b8;">
            Sistema de Gestión - Servicio Farmacéutico | Desarrollado con Streamlit
        </p>
    </div>
""", unsafe_allow_html=True)
