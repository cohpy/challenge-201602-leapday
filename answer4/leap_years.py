from __future__ import print_function

current_date=2016
weekdays=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
# Feb. 29, 2016 is a Monday
day_index=1
print(current_date,weekdays[day_index])
# On Leap Year, add two days of the week for next year's day
print(366%7)
# Then add one day for each of the next three years
print(365%7)
# So, by the time the next Leap Year comes around, we will have added 5 days

for i in range(1, 10):
    current_date += 4
    day_index += 5
    day_index = day_index%7
    print(current_date,weekdays[day_index])

