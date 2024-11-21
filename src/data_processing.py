import pandas as pd

def load_data(file_path):
    """
    Carga los datos desde un archivo CSV.
    """
    data = pd.read_csv(file_path)
    
    # Verificar que las columnas necesarias existan
    required_columns = {'Fecha', 'Numero', 'Sorteo'}
    if not required_columns.issubset(data.columns):
        raise ValueError(f"El archivo CSV debe contener las columnas: {required_columns}")
    
    return data

def preprocess_data(data, cifras=None):
    """
    Realiza el preprocesamiento de los datos.
    """
    # Convertir la columna Fecha a tipo datetime
    data['Fecha'] = pd.to_datetime(data['Fecha'])
    
    # Asegurarse de que 'Numero' y 'Sorteo' son enteros
    data['Numero'] = data['Numero'].astype(str)  # Asegurar que los números sean strings
    data['Sorteo'] = data['Sorteo'].astype(int)
    
    # Filtrar números por longitud si se ha especificado el valor de 'cifras'
    if cifras is not None:
        if cifras < 4:
            # Seleccionar las últimas 'cifras' del número
            data['Numero'] = data['Numero'].str[-cifras:]
    
    return data

def filter_by_sorteo(data, sorteo_type):
    """
    Filtra los datos por tipo de sorteo.
    """
    return data[data['Sorteo'] == sorteo_type]



