import numpy as np

import matplotlib.pyplot as plt

from scipy.integrate import odeint



# Definir el sistema de ecuaciones diferenciales

def system(state, t):

  x, y = state

  dxdt = x - y

  dydt = -0.6*x**2 + 1 - 1.1*y

  return [dxdt, dydt]



# Crear condiciones iniciales distribuidas uniformemente en el plano

x_vals = np.linspace(-5, 5, 10) # Más puntos iniciales en el eje x

y_vals = np.linspace(-5, 5, 10) # Más puntos iniciales en el eje y

initial_conditions = [[x, y] for x in x_vals for y in y_vals] # Crear malla de condiciones iniciales



# Tiempo para resolver las trayectorias

t = np.linspace(0, 10, 1000) # Más pasos para trayectorias suaves

segment_count = 50 # Número de segmentos por trayectoria



# Graficar el diagrama de fases

plt.figure(figsize=(10, 10))



# Agregar trayectorias como segmentos de flechas

for ic in initial_conditions:

  trajectory = odeint(system, ic, t)

  

  # Dividir la trayectoria en segmentos equidistantes

  indices = np.linspace(0, len(trajectory) - 1, segment_count, dtype=int)

  for i in range(len(indices) - 1):

    x_start, y_start = trajectory[indices[i]]

    x_end, y_end = trajectory[indices[i + 1]]

    

    # Calcular el desplazamiento y normalizar la longitud de las flechas

    dx = x_end - x_start

    dy = y_end - y_start

    norm = np.sqrt(dx**2 + dy**2)

    scale = 0.3 # Escala uniforme para todas las flechas

    

    plt.arrow(

      x_start, y_start,

      dx / norm * scale, dy / norm * scale, # Normalización del tamaño

      head_width=0.15, head_length=0.15, fc='black', ec='black', alpha=0.7, length_includes_head=True

    )



# Configuración adicional del gráfico

plt.axhline(0, color="black", linewidth=0.8, linestyle="--") # Eje x

plt.axvline(0, color="black", linewidth=0.8, linestyle="--") # Eje y

plt.title("Diagrama de Fases con Flechas de Tamaño Uniforme")

plt.xlabel("x")

plt.ylabel("y")

plt.xlim(-5, 5)

plt.ylim(-5, 5)

plt.grid(True)

plt.show()