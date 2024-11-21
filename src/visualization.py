import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def plot_frequencies(frequency):
    """
    Grafica las frecuencias de los números sorteados.
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(x=frequency.index, y=frequency.values, color='blue')
    plt.title("Frecuencia de Números Sorteados")
    plt.xlabel("Número")
    plt.ylabel("Frecuencia Relativa")
    plt.show()

def plot_predictions(predictions):
    """
    Grafica los números predichos.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(predictions, bins=len(set(predictions)), kde=False, color='green')
    plt.title("Predicciones de Números de Lotería")
    plt.xlabel("Número")
    plt.ylabel("Frecuencia")
    plt.show()

def plot_simulation_results(data, cifras):
    """
    Genera un gráfico de barras mostrando la frecuencia de los números más frecuentes.
    """
    # Filtrar los números por la cantidad de cifras
    simulated_results = data['Numero'].value_counts().head(10)  # Tomamos solo los 10 números más frecuentes

    # Convertir a DataFrame si es necesario
    if isinstance(simulated_results, pd.Series):
        simulated_results = simulated_results.reset_index()
        simulated_results.columns = ['Número', 'Frecuencia']

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Número', y='Frecuencia', data=simulated_results, color='green')
    plt.title(f'Top 10 números más frecuentes con {cifras} cifras')
    plt.xlabel('Número')
    plt.ylabel('Frecuencia')
    plt.xticks(rotation=45)
    plt.show()



