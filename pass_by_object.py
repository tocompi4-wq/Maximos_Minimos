import numpy as np

def encontrar_menor_referencia(arreglo): #pass-by-object-reference o pass-by-assigment
    menor = arreglo[0]
    for valor in arreglo:
        if valor < menor:
            menor = valor
    return menor

if __name__ == "__main__":
    # Arreglo de prueba con datos ficticios
    y_datos = np.array([2.1, 4.5, 5.2, 3.8, 1.2])
    
    resultado = encontrar_menor_referencia(y_datos)
    print("=== PUNTO 1 ===")
    print(f"El menor valor dentro del arreglo es: {resultado}")