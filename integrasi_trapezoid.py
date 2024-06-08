import numpy as np
import time

def f(x):
    return 4 / (1 + x**2)

def trapezoid_integral(f, a, b, N):
    x = np.linspace(a, b, N + 1)
    h = (b - a) / N
    integral = 0.5 * (f(a) + f(b))
    integral += np.sum(f(x[1:-1]))
    integral *= h
    return integral

# Nilai referensi pi
pi_ref = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]
results = []

for N in N_values:
    start_time = time.time()
    integral_value = trapezoid_integral(f, 0, 1, N)
    end_time = time.time()
    
    # Galat RMS
    rms_error = np.sqrt((integral_value - pi_ref) ** 2)
    
    # Waktu eksekusi
    execution_time = end_time - start_time
    
    results.append({
        'N': N,
        'Integral': integral_value,
        'RMS Error': rms_error,
        'Execution Time': execution_time
    })

# Print hasil
for result in results:
    print(f"N = {result['N']}, Integral = {result['Integral']}, RMS Error = {result['RMS Error']}, Execution Time = {result['Execution Time']} seconds")