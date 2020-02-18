#!/usr/local/bin/python3 
import sys
from datetime import date

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


if [len(sys.argv) > 1]:
    date_entry=sys.argv[1]
else:
    date_entry = input('Enter a date (i.e. YYYY/MM/DD): ')

year, month, day = map(int, date_entry.split('/'))
bdate = date(year, month, day)
print ("Your age is %d" % calculate_age(bdate))

