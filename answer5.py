#Author:  Joe Friedrich
#Purpose: When is the next COhPy Monthly meeting going to happen on LeapDay (February 29th)?

import calendar

for year in range(2017, 3000):                              #3000 was picked arbitrarily 
    if calendar.isleap(year) == True:
        if calendar.weekday(year, 2, 29) == calendar.MONDAY:
            print (year)
            break

