import numpy as np

import matplotlib.pyplot as plt


# Definir el sistema de ecuaciones diferenciales

def system(x, y):

    dxdt = x - y

    dydt = -6*x**2 + 1 - y

    return dxdt, dydt


# Crear una grilla uniforme
x_vals = np.linspace(-5, 5, 20)  # Más puntos para un gráfico más denso

y_vals = np.linspace(-5, 5, 20)

X, Y = np.meshgrid(x_vals, y_vals)


# Define the system of differential equations

def system(x, y):

    dxdt = x - y

    dydt = -0.6*x**2 + 1 - 1.1*y

    return dxdt, dydt


# Create a grid of points
x = np.linspace(-10, 10, 400)

y = np.linspace(-10, 10, 400)

X, Y = np.meshgrid(x, y)


# Compute the derivatives at each point

DX, DY = system(X, Y)


# Plot the phase diagram

plt.figure(figsize=(8, 6))

plt.streamplot(X, Y, DX, DY, color='black')


# Calculate and plot the nullclines

nullcline_x = X - Y

nullcline_y = -0.6*X**2 + 1 - 1.1*Y


plt.contour(X, Y, nullcline_x, levels=[0], colors='red', label='dx/dt = 0')

plt.contour(X, Y, nullcline_y, levels=[0], colors='blue', label='dy/dt = 0')


plt.xlabel('x')

plt.ylabel('y')

plt.title('Phase Diagram with Nullclines')

plt.grid()

plt.legend()

plt.show()


# Calcular el campo vectorial en cada punto de la grilla

U, V = system(X, Y)


# Normalizar los vectores para que todas las flechas tengan el mismo tamaño

magnitude = 3*np.sqrt(U**2 + V**2)

U /= magnitude

V /= magnitude


# Graficar el campo vectorial

plt.figure(figsize=(8, 8))

plt.quiver(X, Y, U, V, color="blue", angles="xy", scale_units="xy", scale=1)


# Configuración adicional del gráfico

plt.axhline(0, color="black", linewidth=0.8, linestyle="--")  # Eje x

plt.axvline(0, color="black", linewidth=0.8, linestyle="--")  # Eje y

plt.title("Campo Vectorial en la Grilla Uniforme")

plt.xlabel("x")

plt.ylabel("y")

plt.xlim(-5, 5)

plt.ylim(-5, 5)

plt.grid(True)

plt.show()
