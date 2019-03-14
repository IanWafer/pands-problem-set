# Ian Wafer 14-03-2019
# Solution to problem 9
# Write a program to read a text file and output every second line.

with open("Simple.txt", "r") as f:
    x = f.readlines()
    print("".join(x[0::2]))