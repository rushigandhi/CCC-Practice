time = input()
hour = int(time[:-3])
minute = int(time[3:])

# 24-Hour Clock
for i in range(120):
    # print(hour, minute)
    if 7 <= hour <= 9 or 15 <= hour <= 18:
        minute+=2

    else:
        minute+=1
    if minute == 60:
        hour += 1
        minute = 0
    if hour == 24:
        hour = 0

hourString = str(hour)
minuteString = str(minute)
if hour < 10:
    hourString = '0' + str(hour)
elif minute < 10:
    minuteString = '0' + str(minute)
if minute == 0:
    minuteString = '00'

print(hourString + ":" + minuteString)