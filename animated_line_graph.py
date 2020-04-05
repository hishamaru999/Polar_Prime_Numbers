# animating data with matplotlib
import numpy as np
import sympy
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('default')
from matplotlib.animation import FuncAnimation


# Create Prime Numbers
list_primes = list(sympy.primerange(2, 711))


# Set up the graph and animation
x_data = []
y_data = []

fig, ax = plt.subplots()
ax.set_xlim(0, 800)
ax.set_ylim(0, 12)
line, = ax.plot(0, 0)


def animation_frame(i):
    x_data.append(i * 10)
    y_data.append(i)

    line.set_xdata(x_data)
    line.set_ydata(y_data)
    return line,

animation = FuncAnimation(fig, func=animation_frame, frames=list_primes, interval=10)
plt.show