aCount = 0
bCount = 0
total = int(input())
winnerLine = list(input())
for x in range(total):
    if winnerLine[x] == 'B':
        bCount += 1
    else:
        aCount += 1
if aCount > bCount:
    print("A")
elif bCount > aCount:
    print("B")
else:
    print("Tie")