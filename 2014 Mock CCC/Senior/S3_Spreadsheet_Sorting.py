dimen = [int(e) for e in input().split()]

grid = list()
for x in range(dimen[0]):
    grid.append([int(e) for e in input().split()])

numOfSorts = int(input())
for x in range(numOfSorts):
    colSort = int(input()) - 1
    for a in range(len(grid)):
        for i in range(len(grid) - 1):
            if grid[i][colSort] > grid[i + 1][colSort]:
                tempData = grid[i + 1]
                grid[i + 1] = grid[i]
                grid[i] = tempData

for y in range(len(grid)):
    line = ' '.join(str(e) for e in grid[y])
    print(line)
