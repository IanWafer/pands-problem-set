# Ian Wafer 03-03-2019
# Solution to problem 8
# Display the current date and time in the format "Monday, January 10th 2019 at 1:15pm".

import time                                             # import the time module


if time.strftime("%d") == 1 or 21 or 31:
    q = "st"

if time.strftime("%d") == 2 or 22:
    q = "nd"

if time.strftime("%d") == 3 or 23:
    q == "rd"

if time.strftime("%d") == 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20 or 24 or 25 or 26 or 27 or 28 or 29 or 30:
    q == "th"

print(time.strftime("%A, %B %d %Y at %H:%M%p"))