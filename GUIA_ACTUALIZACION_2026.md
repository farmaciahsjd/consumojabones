# 📝 Guía para Actualizar Datos de 2026

## 🎯 Objetivo
Esta guía te ayudará a agregar datos mensuales de consumo para el año 2026 de manera fácil y organizada.

## 📂 Estructura de Archivos

El sistema ahora maneja múltiples años con archivos separados:
- `jabones_2025.csv` - Datos completos de 2025
- `jabones_2026.csv` - Datos de 2026 (se actualiza mensualmente)

## ✅ Cómo Agregar Datos Mensuales de 2026

### Opción 1: Editar el archivo CSV directamente

1. **Abre el archivo** `jabones_2026.csv` con Excel o un editor de texto
2. **Agrega una nueva línea** por cada servicio y producto para el mes correspondiente
3. **Formato de cada línea**: `SERVICIO;PRODUCTO;MES;CANTIDAD`

**Ejemplo para agregar datos de FEBRERO 2026:**
```csv
URGENCIAS;JABON QUIRURGICO;FEBRERO;25
URGENCIAS;ALCOHOL GLICERINADO;FEBRERO;20
MEDICOQUIRURGICO;JABON QUIRURGICO;FEBRERO;30
MEDICOQUIRURGICO;ALCOHOL GLICERINADO;FEBRERO;15
... (continuar con todos los servicios)
```

### Opción 2: Usar Excel

1. **Abre** `jabones_2026.csv` con Excel
2. **Agrega filas** con los siguientes datos:
   - **Columna A (SERVICIO)**: Nombre del servicio
   - **Columna B (PRODUCTO)**: JABON QUIRURGICO o ALCOHOL GLICERINADO
   - **Columna C (MES)**: Nombre del mes en MAYÚSCULAS
   - **Columna D (CANTIDAD)**: Número de unidades consumidas
3. **Guarda el archivo** como CSV (delimitado por punto y coma)

## 📋 Lista de Servicios

Asegúrate de incluir datos para todos estos servicios:
- URGENCIAS
- MEDICOQUIRURGICO
- GINECOLOGIA
- PEDIATRIA
- UCI
- CIRUGIA
- CONSULTA EXTERNA

## 📋 Lista de Productos

Para cada servicio, debes tener datos de:
- JABON QUIRURGICO
- ALCOHOL GLICERINADO

## 📅 Lista de Meses

Los meses deben escribirse en MAYÚSCULAS:
- ENERO, FEBRERO, MARZO, ABRIL, MAYO, JUNIO
- JULIO, AGOSTO, SEPTIEMBRE, OCTUBRE, NOVIEMBRE, DICIEMBRE

## 🔄 Proceso Mensual Recomendado

### Al final de cada mes:

1. **Recopila los datos** de consumo de todos los servicios
2. **Abre** el archivo `jabones_2026.csv`
3. **Agrega 14 líneas nuevas** (7 servicios × 2 productos) con los datos del mes
4. **Guarda el archivo**
5. **Reinicia el dashboard** (si está corriendo)
   - Presiona `Ctrl + C` en la terminal
   - Ejecuta nuevamente: `py -m streamlit run dashboard.py`

## ✨ Características del Dashboard con Múltiples Años

Una vez que tengas datos de 2025 y 2026, podrás:

### 📊 Modo "Año Único"
- Ver datos de un solo año a la vez
- Análisis detallado por año

### 📈 Modo "Comparación entre Años"
- Comparar consumo entre 2025 y 2026
- Visualizar tendencias año tras año
- Identificar cambios en patrones de consumo

## 🎨 Ejemplo Completo de Entrada de Datos

```csv
SERVICIO;PRODUCTO;MES;CANTIDAD
URGENCIAS;JABON QUIRURGICO;ENERO;23
URGENCIAS;ALCOHOL GLICERINADO;ENERO;18
MEDICOQUIRURGICO;JABON QUIRURGICO;ENERO;9
MEDICOQUIRURGICO;ALCOHOL GLICERINADO;ENERO;6
GINECOLOGIA;JABON QUIRURGICO;ENERO;4
GINECOLOGIA;ALCOHOL GLICERINADO;ENERO;4
PEDIATRIA;JABON QUIRURGICO;ENERO;11
PEDIATRIA;ALCOHOL GLICERINADO;ENERO;7
UCI;JABON QUIRURGICO;ENERO;17
UCI;ALCOHOL GLICERINADO;ENERO;17
CIRUGIA;JABON QUIRURGICO;ENERO;67
CIRUGIA;ALCOHOL GLICERINADO;ENERO;5
CONSULTA EXTERNA;JABON QUIRURGICO;ENERO;5
CONSULTA EXTERNA;ALCOHOL GLICERINADO;ENERO;12
```

## ⚠️ Puntos Importantes

1. **Separador**: Usa punto y coma (`;`) como separador
2. **Mayúsculas**: Los nombres de servicios, productos y meses deben estar en MAYÚSCULAS
3. **Sin espacios extra**: Evita espacios al inicio o final de cada campo
4. **Cantidad**: Debe ser un número entero (si no hubo consumo, usa `0`)
5. **Codificación**: Guarda el archivo con codificación `Latin-1` o `UTF-8`

## 🔍 Verificación de Datos

Después de agregar datos, verifica que:
- ✅ Todas las líneas tienen 4 campos separados por `;`
- ✅ Los nombres de servicios coinciden exactamente con los existentes
- ✅ Los meses están en MAYÚSCULAS
- ✅ Las cantidades son números válidos

## 🆘 Solución de Problemas

### El dashboard no muestra los nuevos datos
1. Reinicia el dashboard (`Ctrl + C` y vuelve a ejecutar)
2. Verifica que el archivo se guardó correctamente
3. Revisa que no haya errores de formato

### Error al cargar el archivo
1. Verifica que el separador sea punto y coma (`;`)
2. Asegúrate de que no haya líneas vacías al final
3. Comprueba que todos los campos estén completos

## 📞 Contacto

Para soporte adicional, contacta al área de sistemas del hospital.

---

**Hospital San Juan de Dios de Honda E.S.E**  
*Sistema de Gestión - Servicio Farmacéutico*
