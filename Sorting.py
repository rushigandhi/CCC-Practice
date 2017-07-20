total = int(input());
numList = list()

for x in range (0,    total):
    numList.append(input())

numList.sort();

for y in range (0, len(numList)):
    print(numList[y])
