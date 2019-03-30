# Ian Wafer 14-03-2019
# Solution to problem 9
# Write a program to read a text file and output every second line. The filename should take the filename from an argument on the command line

import sys                                           # Import sys module

if len(sys.argv) == 1:                               # If a single argument is presented re prompt the user to input a file name with the script
    print("Please provide a file name to read.")

else:
    with open(sys.argv[1], "r") as f:                 # Open the file and close once indented code is finished
        if len(sys.argv) == 2:
            x = f.readlines()                         # make value x equal to each line of the file
            print("".join(x[0::2]))                   # Print every second line. This is done by joining to gether the list created in the function starting at 0 
                                                      # and increasing in increments of 2
        else: 
            print("You should supply a single filename.") # If too many arguments re prompt user to enter a single filename