import numpy as np
from scipy.optimize import minimize_scalar

def funcion_analitica(x):
    # Prototipo de función física continua analítica
    return -(x - 3.0)**2 + 10.0

def encontrar_maximo():
    # Buscamos el máximo acotando el intervalo de exploración
    res = minimize_scalar(lambda x: -funcion_analitica(x), bounds=(0, 6), method='bounded')
    max_x = res.x
    max_y = -res.fun
    
    print("=== PUNTO 3 ===")
    print(f"El máximo de la función analítica está en: x = {max_x:.4f}, y = {max_y:.4f}")

if __name__ == "__main__":
    encontrar_maximo()