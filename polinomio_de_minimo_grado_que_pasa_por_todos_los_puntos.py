import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

def resolver_extremos():
    # Vectores de ejemplo para el ejercicio
    x_datos = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    y_datos = np.array([2.1, 4.5, 5.2, 3.8, 1.2])

    # --- 1. Polinomio de Lagrange (Mínimo grado que pasa por todos los puntos) ---
    coef_lagrange = np.polyfit(x_datos, y_datos, len(x_datos) - 1)
    poly_lagrange = np.poly1d(coef_lagrange)
    
    # Encontrar el máximo del polinomio de Lagrange (maximizamos negando la función)
    res_lagrange = minimize_scalar(lambda t: -poly_lagrange(t), bounds=(x_datos[0], x_datos[-1]), method='bounded')
    max_x_lagrange = res_lagrange.x
    max_y_lagrange = -res_lagrange.fun

    # --- 2. Parábola de Vecinos (Ejercicio 1) ---
    idx_max = np.argmax(y_datos) # Índice del máximo (el 5.2 está en el índice 2)
    x_vecinos = x_datos[idx_max-1 : idx_max+2]
    y_vecinos = y_datos[idx_max-1 : idx_max+2]
    
    coef_parabola = np.polyfit(x_vecinos, y_vecinos, 2)
    poly_parabola = np.poly1d(coef_parabola)
    
    # Vértice analítico de la parábola: x = -b / (2a)
    a, b, c = coef_parabola
    max_x_parabola = -b / (2.0 * a)
    max_y_parabola = poly_parabola(max_x_parabola)

    # --- Reporte de Resultados ---
    print(" PUNTO 2 Y EJERCICIO 1 ")
    print(f"Máximo por Polinomio de Lagrange: x = {max_x_lagrange:.4f}, y = {max_y_lagrange:.4f}")
    print(f"Máximo por Parábola de Vecinos:   x = {max_x_parabola:.4f}, y = {max_y_parabola:.4f}")

    # --- Gráfica para el reporte ---
    x_ploteo = np.linspace(1, 5, 200)
    plt.figure(figsize=(8, 4))
    plt.scatter(x_datos, y_datos, color='red', zorder=5, label='Datos Originales')
    plt.plot(x_ploteo, poly_lagrange(x_ploteo), label='Lagrange (Grado 4)', color='blue')
    plt.plot(x_ploteo, poly_parabola(x_ploteo), '--', label='Parábola Vecinos (Grado 2)', color='green')
    plt.title('Búsqueda de Extremos: Lagrange vs. Parábola')
    plt.legend()
    plt.grid(True, linestyle=':')
    plt.show()

if __name__ == "__main__":
    resolver_extremos()