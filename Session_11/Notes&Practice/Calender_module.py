#Calender
'''
import the calendar module.
'''

#month()
'''
The built-in function month() inside the module takes in the year and the month and displays the calendar for that month of the year.
'''

import calendar

yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print('\n')
print(calendar.month(yy, mm))
