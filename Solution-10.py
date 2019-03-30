# Ian Wafer 24-03-2019
# Solution to problem 10
# Write a program that displays a plot of the functions x, x^2 and 2^x in the range [0,4]
# Source https://docs.scipy.org/doc/numpy/reference/generated/numpy.power.html
# Source https://matplotlib.org/users/pyplot_tutorial.html
# Source https://jakevdp.github.io/PythonDataScienceHandbook/04.06-customizing-legends.html

import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange(0., 4., 0.05)
x2 = np.power(x1, 2)
x3 = np.power(2, x1)

fig, ax = plt.subplots()
ax.plot(x1, x1, 'r--', label='x')
ax.plot(x1, x2, 'bs', label='x^2')
ax.plot(x1, x3, 'g^', label='2^x')
ax.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Plot of the functions x, x^2 and 2^x in the range [0,4]')

plt.show()