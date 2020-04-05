# Creating polar plots with python and matplotlib

import numpy as np
import sympy
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('default')


# Prime Numbers
list_primes = list(sympy.primerange(2, 711))
more_primes = list(sympy.primerange(2, 1421))
#print("All prime values in the range: ", list_primes)


# Not using prime numbers
# Parameters - n(points), f(), r(radius/scaling factor)
n = 2001
f = 6
r = 5.0

# DATA
theta = np.linspace(0,2.0 * np.pi, n)
curve = r*np.cos(f*theta)

# Get an axes handle/object
ax1 = plt.subplot(111, polar=True)


#Plot the figure
ax1.plot(theta, curve)


# Print primes to 710
n = 1420
f = 6
r = 5.0

# DATA
theta = np.linspace(0, list_primes, n)
curve = r*np.cos(f*theta)


# Get an axes handle/object
ax1 = plt.subplot(111, polar=True)


#Plot the figure
ax1.plot(theta, curve)



# Print using 1420/1420
n = 1420
f = 6
r = 5.0

# DATA
theta = np.linspace(0, more_primes, n)
curve = r*np.cos(f*theta)

# Get an axes handle/object
ax1 = plt.subplot(111, polar=True)



# Prime numbers 710/710
n = 710
f = 6
r = 5.0

# DATA
theta = np.linspace(0, list_primes, n)
curve = r*np.cos(f*theta)

# Get an axes handle/object
ax1 = plt.subplot(111, polar=True)


#Plot the figure
ax1.plot(theta, curve)


# Print with 1420/710
n = 710
f = 6
r = 5.0

# DATA
theta = np.linspace(0, more_primes, n)
curve = r*np.cos(f*theta)

# Get an axes handle/object
ax1 = plt.subplot(111, polar=True)


#Plot the figure
ax1.plot(theta, curve)