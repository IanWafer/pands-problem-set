# Ian Wafer 03-03-2019
# Solution to problem 7
# Output approximate square root of an input positive floating point number
# Info source https://stackoverflow.com/questions/6649597/python-decimal-places-putting-floats-into-a-string
# Info source https://stackoverflow.com/questions/2440692/formatting-floats-in-python-without-superfluous-zeros

import math                                           # Import the math module for the square root function

x = float(input("Please enter a positive number: "))  # User must input a value to begin solution

if x <= 0:                                            # Value needs to be positive for calculation 
   x = float(input("Negative numbers not accepted. Please enter a positive integer: ")) # Reminder for a positive value is required

assert x >= 0                                         # Check for true/false condition after x value input

print("The square root of %f is approx. %.1f." % (x,math.sqrt(x))) # Print text with the %f function being a floating number and %.1f being the floating number to 1 decimal point.