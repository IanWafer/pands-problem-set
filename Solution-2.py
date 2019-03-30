# Ian Wafer 23-02-2019
# Solution to problem 2
# Output whether today is a day beginning with T
# Info source http://strftime.org/

import time                                             # import the time module

if time.strftime("%A") in  ("Thursday" , "Tuesday"):    # %A represents the weekday section of the time module. The if function is used to determine if %A contains the list Thursday or Tuesday in it and if so to execute the next line in the command
  print("Yes - today begins with a T")                  # print function executed if the above condition is true
 
else:print("No - today does not begin with a T")        # if the above condition is not true it will execuue the print function here