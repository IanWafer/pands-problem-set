# Ian Wafer 24-03-2019
# Solution to problem 10
# Write a program that displays a plot of the functions x, x^2 and 2^x in the range [0,4]
# Info source https://docs.scipy.org/doc/numpy/reference/generated/numpy.power.html
# Info source https://matplotlib.org/users/pyplot_tutorial.html
# Info source https://jakevdp.github.io/PythonDataScienceHandbook/04.06-customizing-legends.html

import numpy as np                                                      # Import nuympy module
import matplotlib.pyplot as plt                                         # Import matplotlib.pyplot module

x1 = np.arange(0., 4., 0.05)                                            # Set up first range x
x2 = np.power(x1, 2)                                                    # Set up second range x^2
x3 = np.power(2, x1)                                                    # Set up third range 2^x

fig, ax = plt.subplots()
ax.plot(x1, x1, 'r--', label='x')                                       # Plot first range with red lines and legend x
ax.plot(x1, x2, 'bs', label='x^2')                                      # Plot second range with blue squares and legend x^2
ax.plot(x1, x3, 'g^', label='2^x')                                      # Plot third range with green triangles and legend 2^x
ax.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)        # Create lengend with defining box
plt.xlabel('X-Axis')                                                    # Axis Labels
plt.ylabel('Y-Axis')
plt.title('Plot of the functions x, x^2 and 2^x in the range [0,4]')    # Title label

plt.show()                                                              # Display plot