total = int(input())
smallList = list()
largeList = list()
for x in range(total):
    num = [int(x) for x in list(input())]
    lowIndex = 0
    highIndex = 0
    for i in range(len(num)):
        if num[i] < num[lowIndex] and num[i] > 0:
            lowIndex = i
        if num[i] > num[highIndex]:
            highIndex = i

    smallNum = list(num)
    largeNum = list(num)
    startNum = num[0]
    smallNum[0] = num[lowIndex]
    smallNum[lowIndex] = startNum
    smallList.append(smallNum)

    largeNum[0] = num[highIndex]
    largeNum[highIndex] = startNum
    largeList.append(largeNum)

for a in range(len(smallList)):
    print(''.join(str(e) for e in smallList[a]), ''.join(str(e) for e in largeList[a]))
