# Ian Wafer 24-02-2019
# Solution to problem 5
# Determine whether input value is a prime number

x = int(input("Please enter a positive integer: "))  # User must input a value to begin solution

if x > 1:                                            # x must be a positive value greater than 1 to determine if it is prime.

  for i in range(2,x):                               # Check for within range of 2 to x
    if (x % i) == 0:                                 # Check if x divided by i value leaves a remainder
      print("This is not a prime number")            # If there is no remainder in formula on line above then x is not a prime. Print string
      break                                          # Once x is first determined to not be prime end algorithm. This removes the need to run through all possible calculations as we know it's not a prime numnber witha single confirmation.
    

  else:print("This is a prime number")                # When If function not met then x must be prime. Print string. 