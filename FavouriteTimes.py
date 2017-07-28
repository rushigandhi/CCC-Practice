num = int(input())
hour = 12
min = 0
counter = 0;
# seq_in_a_day is number of arith seqs in 12 hrs starting from 12:00 noon
seq_in_a_day=31 #found by running loop below with input 719
counter+= (num//720) * seq_in_a_day
num = num%720

for x in range (num + 1):
    if hour == 12 and min == 34:
        counter+=1
        #print(hour,min)
    elif hour == 11 and min == 11:
        counter+=1
        #print(hour, min)
    elif hour < 10:
        if (2*((min//10)%10) == (hour + min%10)):
            counter+=1
            #print(hour, min)
    if (min//10)%10 + min%10  == 14:
        hour = (hour + 1)%12
        min = 0
        if hour == 0: hour = 12
    else:
        min+=1

print(counter)
#print('x',x)
#print('last time',hour, min)
