# Next line added so it works the same in 2 or 3
from __future__ import print_function
import arrow

US = arrow.locales.EnglishLocale()
then = arrow.get("2016-02-29").replace(years=4)

while then.weekday() != 0:
    then = then.replace(years=4)
    print(then.date(), US.day_name(then.weekday()+1))

