from math import ceil

total = int(input())
measure = [int(x) for x in input().split()]
measure.sort()
lowList = measure[0:ceil(total / 2)]
highList = measure[total - ceil(total // 2):]
lowList.reverse()

if total == 1:
    print(str(measure[0]))
else:
    for i in range(len(highList)):
        print(lowList[i], highList[i], end=' ')
        if (len(highList) != len(lowList)) and (i == len(highList) - 1):
            print(lowList[i + 1])
