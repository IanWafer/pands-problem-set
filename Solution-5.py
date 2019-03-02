# Ian Wafer 24-02-2019
# Solution to problem 5
# Determine whether input value is a prime number

x = int(input("Please enter a positive integer: "))  # User must input a value to begin solution

if x > 1:                                            # x must be a positive value greater than 1 to determine if it is prime.

  for i in range(2,x):
    if (x % i) == 0:
      print("This is not a prime number") 
      break
    

  else:print("This is a prime number")