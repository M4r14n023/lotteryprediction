from data_processing import load_data, preprocess_data
from prediction import predict_next_number, analyze_frequencies, plot_frequencies
from visualization import plot_simulation_results
from add_data import add_new_entry

def main():
    print("\nBienvenido al sistema de predicción de sorteos\n")
    print("Seleccione una opción:")
    print("1: Predecir números")
    print("2: Agregar nuevos datos")
    option = int(input("\nIngrese su elección: "))

    if option == 1:
        # Solicitar la cantidad de cifras para la predicción
        while True:
            try:
                cifras = int(input("¿Sobre cuántas cifras desea realizar la predicción? (2, 3, 4): "))
                if cifras not in [2, 3, 4]:
                    raise ValueError
                break
            except ValueError:
                print("Por favor, ingrese un valor válido (2, 3, 4).")

        # Cargar y procesar los datos
        filename = "data/sorteos.csv"
        data = load_data(filename)
        filtered_data = preprocess_data(data, cifras)

        # Analizar frecuencias
        frequency = analyze_frequencies(filtered_data, cifras)

        # Mostrar el número más probable
        prediction_count = int(input("¿Cuántos números le gustaría recibir en la predicción? (máximo 10): "))
        prediction_count = min(prediction_count, 10)  # Limitar a un máximo de 10 números
        predictions = predict_next_number(frequency, prediction_count)
        print(f"\nLos números más probables con {cifras} cifras son: {', '.join(predictions)}\n")

        # Mostrar el gráfico de frecuencias
        plot_frequencies(frequency)

        # Mostrar los resultados en gráficos
        plot_simulation_results(filtered_data, cifras)

    elif option == 2:
        add_new_entry("data/sorteos.csv")

    else:
        print("Opción inválida.")

if __name__ == "__main__":
    main()








