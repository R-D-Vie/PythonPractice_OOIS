import datetime
from datetime import date
import calendar

now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))


curr_date = date.today()
print("Day today: ")
print(calendar.day_name[curr_date.weekday()])

#Resources:
#https://www.w3resource.com/python-exercises/python-basic-exercise-3.php
#https://www.delftstack.com/howto/python/python-datetime-day-of-week/
