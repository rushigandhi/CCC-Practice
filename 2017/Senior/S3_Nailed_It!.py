boards = []

board = [int(e) for e in input().split()]
for x in board:
    boards.append(x)

sums = [0]*4000

for i in range(len(boards)):

    updated = list(boards)
    del updated[i]

    for x in range(len(updated)):

        sums[boards[i] + updated[x]] += 1

sums.sort()
print(sums)