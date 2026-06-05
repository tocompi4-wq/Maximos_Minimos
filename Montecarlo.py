import numpy as np
import matplotlib.pyplot as plt

def estimar_pi_montecarlo(N):
    x = np.random.uniform(-1, 1, N)
    y = np.random.uniform(-1, 1, N)
    dentro_circulo = np.sum(x**2 + y**2 <= 1)
    return 4.0 * dentro_circulo / N

def optimizar_r2_montecarlo(N_valores, pi_N):
    pi_inf_posibles = np.linspace(3.14, 3.15, 500)
    mejor_r2 = -np.inf
    mejor_pi = 0
    
    # El error de Montecarlo decae de forma algebraica de orden O(1/sqrt(N))
    inv_sqrt_N = 1.0 / np.sqrt(N_valores)
    
    for pi_inf in pi_inf_posibles:
        error = pi_inf - pi_N
        slope, intercept = np.polyfit(inv_sqrt_N, error, 1)
        valores_ajustados = slope * inv_sqrt_N + intercept
        
        ss_res = np.sum((error - valores_ajustados) ** 2)
        ss_tot = np.sum((error - np.mean(error)) ** 2)
        r2 = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0
        
        if r2 > mejor_r2:
            mejor_r2 = r2
            mejor_pi = pi_inf
            
    return mejor_pi, mejor_r2

if __name__ == "__main__":
    N_max = 5000
    paso = 200
    N_valores = np.arange(paso, N_max + paso, paso)
    
    # Experimento Numérico
    pi_mc = np.array([estimar_pi_montecarlo(n) for n in N_valores])
    
    # Optimización del R^2
    pi_inf_mc, r2_mc = optimizar_r2_montecarlo(N_valores, pi_mc)
    
    print(" PUNTO 4: MÉTODO DE MONTECARLO ")
    print(f"Valor de pi_inf (R^2 Máximo) = {pi_inf_mc:.5f} con R^2 = {r2_mc:.4f}")
  

    # Gráfica de convergencia
    plt.figure(figsize=(8, 4))
    plt.plot(N_valores, pi_mc, label='Aproximación Montecarlo', color='blue')
    plt.axhline(y=np.pi, color='red', linestyle='--', label=r'Valor Real $\pi$')
    plt.title(r'Convergencia Numérica: Método de Montecarlo')
    plt.xlabel('Número de muestras aleatorias (N)')
    plt.ylabel(r'Valor de $\pi$')
    plt.grid(True, linestyle=':')
    plt.legend()
    plt.show()