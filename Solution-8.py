# Ian Wafer 03-03-2019
# Solution to problem 8
# Display the current date and time in the format "Monday, January 10th 2019 at 1:15pm".
# Info source http://strftime.org/
# Info source https://stackoverflow.com/questions/3644417/python-format-datetime-with-st-nd-rd-th-english-ordinal-suffix-like?rq=1
# Info source https://stackoverflow.com/questions/12774279/how-to-check-if-a-variable-is-equal-to-one-string-or-another-string

import time                                             # import the time module

Day = time.strftime("%d")

if Day == "01" or Day == "21" or Day == "31":          # if string format shows these numbers create q string as st
    q = "st"

elif Day == "02" or Day == "22":                        # elif string format shows these numbers create q string as nd
    q = "nd"

elif Day == "03" or Day ==  "23":                       # elif string format shows these numbers create q string as rd
    q = "rd"
    
else:
    q = "th"                                            # If above conditions not met create q string as th

print(time.strftime(f"%A, %B %d{q} %Y at %I:%M%p" ))    # Using f" fucntion with strftime functions print out date with day suffix contained in q variable
