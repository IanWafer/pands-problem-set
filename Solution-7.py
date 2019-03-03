# Ian Wafer 03-03-2019
# Solution to problem 7
# Output approximate square root of an input positive floating point number

import math                                           # Import the math module for the square root function

x = float(input("Please enter a positive number: "))  # User must input a value to begin solution
y=math.sqrt(x)                                        # Make y value the square root of x

print("The square root of %f is approx. %.1f." % (x,y)) # Print text with the %f function being a floating number and %.1f being the floating number to 1 decimal point.