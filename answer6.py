# Next line added so it works the same in 2 or 3
from __future__ import print_function

def next_leap_cohpy(year, days_from_monday):
    if days_from_monday == 0 and year != 2016:
        return year
    else:
        return next_leap_cohpy(year+4, (1461 + days_from_monday) % 7)

if __name__ == '__main__':
    print(next_leap_cohpy(2016, 0))
