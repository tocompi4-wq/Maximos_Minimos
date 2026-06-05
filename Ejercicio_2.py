# Ejercicio 2
import numpy as np

def simular_hoja_calculo():
    # Generamos un barrido denso (simulando 1000 filas de celdas en Excel)
    x_celdas = np.linspace(0, np.pi, 1000)
    y_celdas = np.sin(x_celdas)
    
    # Buscamos el índice con la respuesta más alta
    idx_max = np.argmax(y_celdas)
    
    print(" EJERCICIO 2 ")
    print(f"Máximo de sin(x) encontrado en la celda x = {x_celdas[idx_max]:.4f} (aprox pi/2)")
    print(f"Valor máximo y = {y_celdas[idx_max]:.4f}")

if __name__ == "__main__":
    simular_hoja_calculo()