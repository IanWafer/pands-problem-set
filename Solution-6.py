# Ian Wafer 03-03-2019
# Solution to problem 6
# Output every second word of user string input

x = input("Please enter a sentence: ")

y = x.split(" ")

print(y[1::2])