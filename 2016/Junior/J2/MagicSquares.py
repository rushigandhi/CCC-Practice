import re

output = "magic"
sumList = []
grid = [[0 for j in range (4)] for i in range (4)]
for y in range(4):
        tempList = input()
        tempList= re.split('\s+', tempList)
        grid[y] = tempList

for y in range(4):
    sumX = 0
    sumY = 0
    for x in range(4):
        sumX += int(grid[y][x])
        sumY += int(grid[x][y])

    sumList.append(sumX)
    sumList.append(sumY)

for i in range(len(sumList)):
    if i == len(sumList) - 1:
        break
    if sumList[i] != sumList[i + 1] :
        output = "not magic"
        break

print(output)