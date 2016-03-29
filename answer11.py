# Next line added so it works the same in 2 or 3
from __future__ import print_function

import arrow
import toolz


def leap_mondays(year=2016):
    """Yield leap Mondays."""
    yield arrow.Arrow(year, 2, 29)
    while True:
        year += 4
        try:
            leap_day = arrow.Arrow(year, 2, 29)
        except ValueError:
            continue
        if leap_day.format('dddd') == 'Monday':
            yield leap_day
            
print(list(toolz.take(3, leap_mondays())))
