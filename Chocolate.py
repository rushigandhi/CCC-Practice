total = int(input())
numList = list()

for x in range (0, total):
    dimen = input()
    dimen = dimen.split()
    breaks = (int(dimen[0])*int(dimen[1])) - 1
    numList.append(breaks)

for y in range (0, len(numList)):
    print(numList[y])
