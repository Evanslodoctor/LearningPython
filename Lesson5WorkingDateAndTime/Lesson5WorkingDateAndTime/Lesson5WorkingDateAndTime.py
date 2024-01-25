#The import statement gives us access to  
#the functionality of the datetime class 
import datetime
#today is a function that returns today's date 
print(datetime.date.today())
currentDate = datetime.date.today() 
print (currentDate) 
print (currentDate.year) 
print (currentDate.month) 
print (currentDate.day)

print (currentDate.strftime('%d %B,%Y'))

#strftime allows you to specify the date format 
print (currentDate.strftime('Please attend our event %A, %B %d in the year %Y'))

import calendar
print(calendar.prcal(2020,12))
print(datetime.datetime.now())
currentTime = datetime.datetime.now() 
print (currentTime) 
print (currentTime.hour) 
print (currentTime.minute)
print (currentTime.second)
print(datetime.datetime.now().strftime("%I" + ":" "%M:%S %p"))