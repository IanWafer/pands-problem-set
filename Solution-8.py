# Ian Wafer 03-03-2019
# Solution to problem 8
# Display the current date and time in the format "Monday, January 10th 2019 at 1:15pm".
# Info source http://strftime.org/
# Info source https://stackoverflow.com/questions/3644417/python-format-datetime-with-st-nd-rd-th-english-ordinal-suffix-like?rq=1

#import time                                             # import the time module


# if time.strftime("%d") == "1" or "21" or "31":                # if string format shows these numbers create q string as st
    #q = "st"

#  if time.strftime("%d") == "2" or "22":                      # if string format shows these numbers create q string as nd
    #q = "nd"

# if time.strftime("%d") == "3" or "23":                      # if string format shows these numbers create q string as rd
    #q = "rd"
    
# if time.strftime("%d") == "4" or "5" or "6" or "7" or "8" or "9" or "10" or "11" or "12" or "13" or "14" or "15" or "16" or "17" or "18" or "19" or "20" or "24" or "25" or "26" or "27" or "28" or "29" or "30":
    #q = "th"                                            # if string format shows these numbers create q string as th

#print(time.strftime(f"%A, %B %d{q} %Y at %H:%M%p" ))    # Using f" fucntion with strftime functions print out date with day suffix contained in q variable

import time

day = time.strftime("%d")

#Yous elif to test it, change the values to whatever day it is just for the test
if day == "30":
   print("This worked!")
   dayAlt = "30th"
   print(day)
elif day == 22:
   print("This worked!")
   dayAlt = "22nd"
   print(day)
else:
  print("fail")
  dayAlt = "fail"

#Then if it worked your print statement should look something like this
print(time.strftime(f"%A, %B {dayAlt} %Y at %H:%M%p" ))