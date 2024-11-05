import pandas as pd


def cargar_datos_ventas(ruta_archivo):
    """
    Esta función lee los datos de ventas desde un archivo CSV y los carga en un DataFrame de pandas.
    Utiliza la codificación 'latin1' para manejar caracteres especiales.

    Parámetros:
    ruta_archivo (str): La ruta al archivo CSV.

    Retorna:
    DataFrame: Los datos de ventas cargados en un DataFrame de pandas.
    """
    try:
        # Cargar los datos con la codificación especificada
        datos_ventas = pd.read_csv(ruta_archivo, encoding='latin1')
        print("Datos cargados exitosamente")
        return datos_ventas
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None


def procesar_datos(datos):
    """
    Esta función elimina las filas donde la columna 'STATE' esté vacía.

    Parámetros:
    datos (DataFrame): El DataFrame con los datos de ventas.

    Retorna:
    DataFrame: El DataFrame procesado sin filas con 'STATE' vacío.
    """
    # Eliminar filas donde la columna 'STATE' esté vacía
    datos_procesados = datos.dropna(subset=['STATE'])
    print("Filas con 'STATE' vacío eliminadas.")
    return datos_procesados


def guardar_en_xml(datos, ruta_salida):
    """
    Esta función guarda el DataFrame en un archivo XML.

    Parámetros:
    datos (DataFrame): El DataFrame que será guardado.
    ruta_salida (str): La ruta donde se guardará el archivo XML.
    """
    try:
        # Guardar el DataFrame en un archivo XML
        datos.to_xml(ruta_salida, index=False)
        print(f"Datos guardados exitosamente en {ruta_salida}")
    except Exception as e:
        print(f"Error al guardar los datos en XML: {e}")


# Ruta del archivo CSV de entrada
ruta_archivo = 'C:/Users/carlo/BD_Avzd/sales_data.csv'

# Cargar los datos
datos_ventas = cargar_datos_ventas(ruta_archivo)

# Procesar los datos eliminando filas con 'STATE' vacío
datos_ventas_procesados = procesar_datos(datos_ventas)

# Ruta donde se guardará el archivo XML (cambia la ruta según sea necesario)
ruta_salida = 'C:/Users/carlo/BD_Avzd/processed_data/sales_data.xml'

# Guardar los datos procesados en XML
guardar_en_xml(datos_ventas_procesados, ruta_salida)
