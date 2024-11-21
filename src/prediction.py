import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_frequencies(data, cifras):
    """
    Calcula las frecuencias de los números sorteados con la longitud especificada.
    """
    # Filtrar los números por la cantidad de cifras seleccionada
    data_filtered = data[data['Numero'].str.len() == cifras]
    frequency = data_filtered['Numero'].value_counts(normalize=True)
    return frequency

def predict_next_number(frequency, n_predictions=1):
    """
    Predice los próximos números basados en las frecuencias observadas.
    """
    predicted_numbers = np.random.choice(
        frequency.index, 
        size=n_predictions, 
        replace=True, 
        p=frequency.values
    )
    return predicted_numbers

def plot_frequencies(frequency):
    """
    Muestra un gráfico de barras con los porcentajes de aparición de los 10 números más repetidos.
    """
    top_10 = frequency.head(10)  # Seleccionamos los 10 más frecuentes
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_10.index, y=top_10.values, color='green')
    plt.title('Top 10 números más frecuentes')
    plt.xlabel('Número')
    plt.ylabel('Frecuencia')
    plt.xticks(rotation=45)
    plt.show()




