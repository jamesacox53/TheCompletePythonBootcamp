from datetime import time

my_time = time(2, 20)

print(my_time)
print(my_time.hour)
print(my_time.minute)
print(type(my_time))

from datetime import date

today = date.today()
print(today)
print(today.ctime())

from datetime import datetime

my_datetime = datetime(2021, 10, 3, 14, 20, 1)
print(my_datetime)

my_datetime2 = my_datetime.replace(year=2024)
print(my_datetime2)

print(datetime.today())

date1 = date(2021, 11, 3)
date2 = date(2020, 11, 3)
date_delta = date1 - date2

print(date_delta)

datetime1 = datetime(2021, 11, 3, 22, 0)
datetime2 = datetime(2020, 11, 3, 12, 0)
datetime_delta = datetime1 - datetime2

print(datetime_delta)