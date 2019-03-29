from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%Y")

month = now.strftime("%m")

day = now.strftime("%d")

dayAlt =””

#Yous elif to test it, change the values to whatever day it is just for the test
if day == 29:
   print "This worked!"
   dayAlt = “29th”
   print day
elif day == 22:
   print "This worked!"
   dayAlt = “22nd”
   print day
else:
  print “fail”
  dayAlt = “fail”


#Then if it worked your print statement should look something like this
print(dayAlt, month, year)	