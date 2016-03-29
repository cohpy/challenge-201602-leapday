#!/usr/bin/env python2.7
import calendar

# It's gotta be some time this century, right?
for year in xrange(2020, 2100, 4):
    cal = calendar.monthcalendar(year, 2)

    # Last monday of the month is COhPy meeting
    if cal[-1][calendar.MONDAY] == 29:
        print year
        break
