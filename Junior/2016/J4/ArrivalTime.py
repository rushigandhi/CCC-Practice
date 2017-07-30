import datetime
from datetime import timedelta


time = input()
hour = int(time[:-3])
minute = int(time[3:])

# 24-Hour Clock
for i in range(120):
    print(hour, minute)
    if 7 <= hour <= 9 or 15 <= hour <= 18:
        minute+=2
    elif (hour == 10 and min == 0) or (hour == 19 and min == 0):
        minute+=2
    else:
        minute+=1
    if minute == 60:
        hour += 1
        minute = 0
    if hour == 25:
        hour = 1

'''
for i in range(120):
    if 7 <= hour:
        if hour <= 10 and min <= 0:
            minute += 2
    else:
        minute += 1
    if minute == 60:
        minute = 0
        hour += 1
    print(hour, minute)

'''
print(hour, minute)