# Ian Wafer 24-02-2019
# Solution to problem 4
# Output succesive values of input number. At each step calculate the next value by taking the current value and if even divide it by two but if odd multiply it by 3 and add one. Have the program end if the current value is one.

x = int(input("Please enter a positive integer: "))  # User must input a value to beign solution
print(x)

while x > 1:
  if x % 2 == 0:
    x = x // 2
  else: x = (x * 3) + 1
  print(x)