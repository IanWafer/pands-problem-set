# Ian Wafer 24-02-2019
# Solution to problem 3
# Print all numbers between 1,000 and 10,000 that are divisible by 6 but not 12

a=1000                      # Define starting variable

while 1000 <= a <= 10000:   # Number must be between 1,000 and 10,000
  if a % 12 == 0:           # Check if function is divisible by 12 with no remainder
    a = a + 1               # If condition is true change a value to a + 1
  if a % 6 == 0:            # Check if function is divisible by 6 with no remainder
    print(a)                # If above function true print a
    a = a + 1               # After printing a value above the next iteration becomes a + 1
  else: a = a + 1           # If neither condition above met add one to a value and run script above again