import numpy as np

import matplotlib.pyplot as plt

from ipywidgets import interact, FloatSlider


# Define the system of differential equations with parameters

def system(x, y, a, b, c, d):

    dxdt = a * x**3 - b * x - y

    dydt = c * x**2 + 1 - d * y

    return dxdt, dydt


# Function to plot the phase diagram with nullclines

def plot_phase_diagram(a, b, c, d):

    # Create a grid of points

    x = np.linspace(-10, 10, 400)

    y = np.linspace(-10, 10, 400)

    X, Y = np.meshgrid(x, y)

    # Compute the derivatives at each point

    DX, DY = system(X, Y, a, b, c, d)

    # Plot the phase diagram

    plt.figure(figsize=(8, 6))

    plt.streamplot(X, Y, DX, DY, color='black')

    # Calculate and plot the nullclines

    nullcline_x = a * X**3 - b * X - Y

    nullcline_y = c * X**2 + 1 - d * Y

    plt.contour(X, Y, nullcline_x, levels=[0], colors='red', label='dx/dt = 0')

    plt.contour(X, Y, nullcline_y, levels=[
                0], colors='blue', label='dy/dt = 0')

    plt.xlabel('x')

    plt.ylabel('y')

    plt.title('Phase Diagram with Nullclines')

    plt.grid()

    plt.legend()

    plt.show()


# Create sliders for the coefficients
a_slider = FloatSlider(min=-1, max=1, step=0.01, value=1, description='a')

b_slider = FloatSlider(min=-1, max=1, step=0.01, value=1, description='b')

c_slider = FloatSlider(min=-1, max=1, step=0.01, value=-0.6, description='c')

d_slider = FloatSlider(min=-1, max=1, step=0.01, value=1, description='d')


# Use interact to update the plot with slider values

interact(plot_phase_diagram, a=a_slider, b=b_slider, c=c_slider, d=d_slider)
