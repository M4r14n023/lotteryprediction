import csv
from datetime import datetime

def add_new_entry(filename):
    """
    Permite al usuario agregar nuevas entradas al archivo CSV.
    """
    print("\nAgregar nuevos datos de sorteos\n")
    
    while True:
        # Solicitar fecha
        try:
            fecha = input("Ingrese la fecha del sorteo (YYYY-MM-DD): ")
            datetime.strptime(fecha, "%Y-%m-%d")  # Validar formato de fecha
        except ValueError:
            print("Formato de fecha inválido. Intente nuevamente.")
            continue

        # Solicitar número sorteado
        numero = input("Ingrese el número sorteado (de 2 a 4 cifras): ")
        if not numero.isdigit() or not (2 <= len(numero) <= 4):
            print("Número inválido. Debe tener entre 2 y 4 dígitos. Intente nuevamente.")
            continue

        # Solicitar el tipo de sorteo
        try:
            sorteo = int(input("Ingrese el tipo de sorteo (1: Matutina, 2: Vespertina, 3: Nocturna): "))
            if sorteo not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            print("Tipo de sorteo inválido. Intente nuevamente.")
            continue

        # Confirmar entrada
        print(f"\nDatos ingresados:\nFecha: {fecha}\nNúmero: {numero}\nSorteo: {sorteo}")
        confirm = input("¿Desea guardar esta entrada? (s/n): ").lower()
        if confirm == 's':
            # Guardar datos en el archivo CSV
            with open(filename, mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([fecha, numero, sorteo])
            print("Entrada guardada con éxito.\n")

        # Preguntar si desea agregar otra entrada
        another = input("¿Desea agregar otra entrada? (s/n): ").lower()
        if another != 's':
            break

if __name__ == "__main__":
    # Ruta del archivo CSV
    filename = "data/sorteos.csv"
    add_new_entry(filename)
