# Ian Wafer 03-03-2019
# Solution to problem 6
# Output every second word of user string input

x = input("Please enter a sentence: ") # User must input a string to begin solution

y = x.split(" ")                       # Split string into a list with each word as a seperate item. Seperate wods identified by a " " (space) between them

print(" ".join(y[0::2]))               # From list y obtained above starting at the initial point (0) make a new list in increments of 2 till the end of the list. Join these values together seperated by a " " (space) and print output.  