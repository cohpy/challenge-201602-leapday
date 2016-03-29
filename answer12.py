# Next line added so it works the same in 2 or 3
from __future__ import print_function

import datetime
from itertools import count


def isleap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def cohpy_leap_day(leap_year=2016):
    if not isleap(leap_year):
        raise ValueError('year is not a valid leap year')
    days = 0
    for year in count(leap_year + 4, 4):
        days += 4 * 365 + isleap(year)
        if days % 7 == 0:
            return year


leap_day_year = cohpy_leap_day(2016)
next_cohpy_leap_day = datetime.date(leap_day_year, 2, 29)
print("The next leap cohPy is", next_cohpy_leap_day.strftime("%A, %B %d, %Y"))

### other code to list all cohpy's for the next 2000 years

def all_matching_leap_day_years(start=2016, end=4016):
    year = start
    while year <= end:
        year = cohpy_leap_day(year)
        yield year


for year in all_matching_leap_day_years():
    print(year)
