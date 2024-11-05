# Práctica de Carga y Procesamiento de Datos de Ventas

Este proyecto contiene un script en Python que lee un archivo CSV con datos de ventas, elimina las filas con valores nulos en la columna `STATE`, y guarda los datos procesados en un archivo XML.

## Archivos

- **main.py**: Script principal que realiza la carga, procesamiento y exportación de los datos.
- **sales_data.csv**: Archivo de datos de ejemplo.
- **sales_data.xml**: Archivo XML que contiene los datos de ventas procesados, sin registros con valores nulos en la columna `STATE`. Este archivo es el resultado final del procesamiento y está listo para su uso en otros sistemas o análisis.


## Instrucciones

1. Asegúrate de tener las bibliotecas necesarias instaladas (`pandas`, `lxml`).
2. Ejecuta `main.py` para cargar y procesar el archivo CSV.
3. Los datos procesados se guardarán en un archivo XML en la ubicación especificada.

## Requisitos

- Python 3.x
- Bibliotecas: `pandas`, `lxml`

## Notas

Este script está diseñado para ser ejecutado desde un entorno de desarrollo local.
