infoLine = input()
infoLine = infoLine.split()
total = int(infoLine[0])
jump = int(infoLine[1])
bigJump = jump * 2
energy = int(infoLine[2])

for x in range (0, total):
    hold = int(input())
    if(hold > jump and hold <= bigJump):
        energy = energy - 1
    if(energy == 0):
        break

if(energy == 0):
    print("Unfair!")
else:
    print("Too easy!")






