# Ian Wafer 24-02-2019
# Solution to problem 4
# Output succesive values of input number. At each step calculate the next value by taking the current value and if even divide it by two but if odd multiply it by 3 and add one. Have the program end if the current value is one.

x = int(input("Please enter a positive integer: "))  # User must input a value to begin solution
print(x)                                             # Print value of x

if x <= 0:                                           # Value needs to be positive to create sum
   x = int(input("Negative numbers not accepted. Please enter a positive integer: ")) # Reminder for a positive value is required

while x > 1:                # Run the below while x is above 1. If x becomes lower or equal to 1 stop execution
  if x % 2 == 0:            # If x divided by 2 leaves no remainders then it is an even no. 
    x = x // 2              # If above line is true x becomes new value determined by formula
  else: x = (x * 3) + 1     # When above if function is not true execute this funtion
  print(x)                  # Print new value of x