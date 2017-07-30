import re

lenList = list()
while True:
    inputLine = input()
    inputLine = re.split('\s+', inputLine)
    if len(inputLine) == 1 and inputLine[0] == '0':
        break
    patternList = list()
    for x in range (1, len(inputLine)):
        if x != len(inputLine) -1:
            diff = int(inputLine[x + 1]) - int(inputLine[x])
            if diff in patternList:
                break
            else:
                patternList.append(diff)
    lenList.append(len(patternList))

for x in range(len(lenList)):
    print(lenList[x])
