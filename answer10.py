# Next line added so it works the same in 2 or 3
from __future__ import print_function

import datetime
import itertools


def leapdates(begin_year):
    """Generate ``datetime.date``s for leap days in and after ``begin_year``.

    >>> dates = leapdates(2016)
    >>> next(dates)
    datetime.date(2016, 2, 29)
    >>> next(dates)
    datetime.date(2020, 2, 29)

    """
    # Leap years are always divisible by 4, but not all years divisible
    # by 4 are leap years
    begin_year = (int(begin_year) + 3) // 4 * 4
    for year in itertools.count(begin_year, 4):
        try:
            yield datetime.date(year, 2, 29)
        except ValueError:
            pass


cohpy_leapdates = (date for date in leapdates(2016) if date.weekday() == 0)

# Verify that this year is correctly identified
assert next(cohpy_leapdates) == datetime.date(2016, 2, 29)

# datetime.date(2044, 2, 29)
answer = next(cohpy_leapdates)
print(answer)
