# Ian Wafer 03-03-2019
# Solution to problem 7
# Output approximate square root of an input positive floating point number

import math

x = float(input("Please enter a positive number: "))  # User must input a value to begin solution
y=math.sqrt(x)


print("The square root of %d is approx. %1f." % (x,y))