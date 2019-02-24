# Ian Wafer 24-02-2019
# Solution to problem 5
# Determine whether input value is a prime number

x = int(input("Please enter a positive integer: "))  # User must input a value to begin solution

if x // range(1, x) == 0:
  print("This is a prime number")                  
 
else:print("This is not a prime number")