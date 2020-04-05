# fibonacci numbers and polar plots

import numpy as np
import sympy
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('default')

# Fibonacci Numbers
a = 0
b = 1
fibList = [a, b]
while b < 1420:
    a, b = b, a + b
    fibList.append(b)
    print(fibList)


# Fibonacci Numbers in Polar Plot
# r is the number of tree rings
# f
n = 710
f = 3
r = 12



# DATA
theta = np.linspace(0, fibList, n)
curve3 = r*np.cos(f*theta)
curve4 = r*np.sin(f*theta)

# Get an axes handle/object
ax1 = plt.subplot(111, polar=True)


#Plot the figure
#ax1.plot(theta, curve3, color='xkcd:salmon')
ax1.plot(theta, curve4, color='xkcd:azure')
#plt.legend()
plt.title('Rose Plots')
# -1 so 0 and 360 labels don't overlap
ax1.set_xticks(np.linspace(0, 2.0*np.pi, 17)[:-1])