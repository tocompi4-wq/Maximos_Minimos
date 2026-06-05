import numpy as np

def f(x):
    return np.sin(1/x)

def df(x):
    return -np.cos(1/x)/(x**2)

def metodo_newton(x0, tol=1e-7, max_iter=100):
    x = x0

    for i in range(max_iter):

        fx = f(x)
        dfx = df(x)

        if abs(dfx) < 1e-12:
            print("Derivada demasiado pequeña.")
            break

        x_nuevo = x - fx/dfx

        if abs(x_nuevo - x) < tol:
            return x_nuevo, i + 1

        x = x_nuevo

    return x, max_iter


if __name__ == "__main__":

    # valor inicial a la derecha del origen
    x0 = 0.35

    raiz, iteraciones = metodo_newton(x0)

    print("PUNTO 6 (MÉTODO DE NEWTON)")
    print(f"Primer cero hallado: x = {raiz:.8f}")
    print(f"Iteraciones: {iteraciones}")

# en C++ esto se ve más profesional :v