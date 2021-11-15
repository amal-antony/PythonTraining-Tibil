# What is DateTime Module?
"""
A module which aloows us to work with dates and time

import datetime

"""
#Current Date - .date().today()

import datetime as dt
current_date=dt.date.today()
print(f"\nTodays date is {current_date}")


#date class-work with dates
'''
.date()-can be used to create a date based on format yy-mm-dd
Takes 3 parameteres 
1.Year
2.Month
3.Date
'''

date1=dt.date(2021,11,15)
print(f'\nCustom created date is {date1}')

#Get individual info
'''
We can get induvdual info from date eg year , month and day .
date has attributes like
1..year-To get year
2.month-To get month
3.day-To get day
'''

print(f'Year from  date is {date1.year}')
print(f'Month from date is {date1.month}')
print(f'Day from date is {date1.day}')


#time class-work with time
'''
.time()-can be used to create a time based on format yy-mm-dd
Takes 3 parameteres 
1.hrs- b/w 0 and 24 range
2.minutes- from 0-60
3.seconds 0-60
4.microsecond-o to 1 million

Each of these induvidual values can be accessed by attribute
'''

time1=dt.time(10,45,30,4567)
print(f'\nCustom created time is {time1}')
print(f'Hour: {time1.hour}')
print(f'Minute: {time1.minute}')
print(f'Seconds {time1.second}')
print(f'MicroSeconds {time1.microsecond}')





#datetimeclass-work with combination of both date and time
'''
.datetime()-can be used to create a date based on format yy-mm-dd
Takes 6 parameteres 
1.Year
2.Month
3.Date
4.hrs- b/w 0 and 24 range
5.minutes- from 0-60
6.seconds 0-60
'''

date_time=dt.datetime(2021,11,28,23,55,34)
print(f'\nCustom created datetime is {date_time}')

'''
Can get date or time value induvudually from this object
Use
.date()
.time()
'''

print(f'Time from datetime object is {date_time.time()}')
print(f'Date from datetime object is {date_time.date()}')

#Current date and time
'''
datetime.now()-Get current date and time
'''

current_date_time=dt.datetime.now()
print(f'\nCurrent date and time is {current_date_time}')


#TimeDelta-to get difference b/w 2 datetime

date_diff=current_date-date1
print(f"The diffrenece b/w 2 dates are {date_diff} and its of type")
print(type(date_diff))


#strftime()
'''
returns string representing date and time for datetime object
%A-weekday
%B-Month full name
%d - Day of the month
%Y-Year
'''

string_date=current_date.strftime("%A,  %B %d,%Y")
print(f"\nDemo of strftime {string_date}")

'''
Directive               Meaning                             Example
		
%a
				Abbreviated weekday name.                                               Sun, Mon, ...
		
%A                  Full weekday name.                                              Sunday, Monday, ...
		
%w                  Weekday as a decimal number.                                         0, 1, ..., 6
		
%d                  Day of the month as a zero-padded decimal.                      01, 02, ..., 31
		
%-d                     Day of the month as a decimal number                            1, 2, ..., 30
		
%b                    Abbreviated month name.                                             Jan, Feb, ..., Dec
		
%B                          Full month name.                                        January, February, ...
		
%m                      Month as a zero-padded decimal number.                                  01, 02, ..., 12
		
%-m                             Month as a decimal number.                                      1, 2, ..., 12
		
%y
				Year without century as a zero-padded decimal number.
				00, 01, ..., 99
		
%-y
				Year without century as a decimal number.
				0, 1, ..., 99
		
%Y
				Year with century as a decimal number.
				2013, 2019 etc.
		
%H
				Hour (24-hour clock) as a zero-padded decimal number.
				00, 01, ..., 23
		
%-H
				Hour (24-hour clock) as a decimal number.
				0, 1, ..., 23
		
%I
				Hour (12-hour clock) as a zero-padded decimal number.
				01, 02, ..., 12
		
%-I
				Hour (12-hour clock) as a decimal number.
				1, 2, ... 12
		
%p
				Locale’s AM or PM.
				AM, PM
		
%M
				Minute as a zero-padded decimal number.
				00, 01, ..., 59
		
%-M
				Minute as a decimal number.
				0, 1, ..., 59
		
%S
				Second as a zero-padded decimal number.
				00, 01, ..., 59
		
%-S
				Second as a decimal number.
				0, 1, ..., 59
		
%f
				Microsecond as a decimal number, zero-padded on the left.
				000000 - 999999
		
%z
				UTC offset in the form +HHMM or -HHMM.
				 
		
%Z
				Time zone name.
				 
		
%j
				Day of the year as a zero-padded decimal number.
				001, 002, ..., 366
		
%-j
				Day of the year as a decimal number.
				1, 2, ..., 366
		
%U
				Week number of the year (Sunday as the first day of the week). All days in a new year preceding the first Sunday are considered to be in week 0.
				00, 01, ..., 53
		
%W
				Week number of the year (Monday as the first day of the week). All days in a new year preceding the first Monday are considered to be in week 0.
				00, 01, ..., 53
		
%c
				Locale’s appropriate date and time representation.
				Mon Sep 30 07:06:05 2013
		
%x
				Locale’s appropriate date representation.
				09/30/13
		
%X
				Locale’s appropriate time representation.
				07:06:05
		
%%
				A literal '%' character.
				%

'''


#strptime - converts strings to datetime object

date_time_new="21 June,2021"
date_object=dt.datetime.strptime(date_time_new,"%d %B,%Y")
print(f"\nDemo of strptime ")
print(f"\nThe date object from ur input {date_time_new} is {date_object}")