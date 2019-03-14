# Ian Wafer 14-03-2019
# Solution to problem 9
# Write a program to read a text file and output every second line.

with open("Simple.txt", "r") as f:  # Open the file and close once indented code is finished
    x = f.readlines()               # make value x equal to each line of the file
    print("".join(x[0::2]))         # Print every second line. This is done by joining to gether the list created in the function starting at 0 and increasing in increments of 2