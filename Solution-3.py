# Ian Wafer 23-02-2019
# Solution to problem 3
# Print all numbers between 1,000 and 10,000 that are divisible by 6 but not 12

a=1000

while 1000 <= a <= 10000:
  if a % 12 == 0:
    a = a + 1
  if a % 6 == 0: 
    print(a)  
    a = a + 1
  else: a = a + 1