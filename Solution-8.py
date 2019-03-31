# Ian Wafer 03-03-2019
# Solution to problem 8
# Display the current date and time in the format "Monday, January 10th 2019 at 1:15pm".
# Info source http://strftime.org/
# Info source https://stackoverflow.com/questions/3644417/python-format-datetime-with-st-nd-rd-th-english-ordinal-suffix-like?rq=1

import time                                             # import the time module


if time.strftime("%d") == "1" or "21" or "31":          # if string format shows these numbers create q string as st
    q = "st"

elif time.strftime("%d") == "2" or "22":                # elif string format shows these numbers create q string as nd
    q = "nd"

elif time.strftime("%d") == "3" or "23":                # elif string format shows these numbers create q string as rd
    q = "rd"
    
else:
    q = "th"                                            # If above conditions not met create q string as th

print(time.strftime(f"%A, %B %d{q} %Y at %I:%M%p" ))    # Using f" fucntion with strftime functions print out date with day suffix contained in q variable
