import datetime
import pprint

# from datetime import datetime

# datetime.date
# datetime.time
# datetime.datetime
# datetime.timedelta

# t = datetime.date.today()
# print(t.year)
# print(t.month)
bdate = datetime.date(1987, 2, 11)
print(bdate)
# print(bdate.weekday())
# print(bdate.isoweekday())


# t1 = datetime.time(14, 25)
# t2 = datetime.time()
# print(t1)
# print(t1.hour)

n = datetime.datetime.now()
print(n)
dt1 = datetime.datetime(year=2022, month=2, day=1)
print(dt1)

print(dt1.timestamp())
print(datetime.datetime.now().timestamp())

print(datetime.datetime.fromtimestamp(1643666400))
print(datetime.datetime.fromtimestamp(0))

my_bdate = datetime.datetime(1987, 2, 11)
temp = datetime.datetime.now() - my_bdate
print(type(temp))
print(temp)
td = datetime.timedelta()

# temp = datetime.datetime.now() + my_bdate

new_dt = datetime.datetime.now() + datetime.timedelta(days=2, hours=5, minutes=12)
print(new_dt)


print(my_bdate)
# 11/2/87
ret_val = my_bdate.strftime("%d/%m/%y")
print(ret_val)

# February 11, Year: 1987, Wed
ret_val = my_bdate.strftime("%B %d, Year: %Y, %a")
print(ret_val)

ret_val = datetime.datetime.strptime("18-01-23 7:45PM", "%d-%m-%y %I:%M%p")
print(ret_val)

# datetime.datetime.now() + datetime.timedelta(minutes=25)

print(datetime.timedelta(minutes=25) +
      datetime.timedelta(hours=5, seconds=3))


# print(datetime.datetime.strptime("21-01-22", "%d-%m-%Y"))

# """## isoformat"""
#
print(datetime.datetime.now().isoformat())
#
# """## Handling timezone in Python - pytz module"""
#
import pytz

# # not aware of timezone object
local = datetime.datetime.now()
print(local)
#
# # aware of timezone object
local_aware = datetime.datetime.now(pytz.UTC)
print(local_aware)

# print(local - local_aware)
#
pprint.pprint(pytz.all_timezones)
#
tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.datetime.now(tz_NY)
print(datetime_NY)

print("diff")
print(datetime_NY - local_aware)
#
# tz_London = pytz.timezone('Europe/London')
# datetime_London = datetime.datetime.now(tz_London)
# print(datetime_London)
#
# pytz.all_timezones
#
# datetime_NY.tzname()
#
print(datetime_NY.astimezone(pytz.timezone('Europe/London')))
#
# tz_Jerusalem = pytz.timezone('Israel')
#
# print(datetime_NY.astimezone(tz_Jerusalem))
#
# """Note: do not assume that differences in timezones are in round hours!

