import re

question = int(input())
citiNum = int(input())
dmoj = input()
dmoj = re.split('\s+', dmoj)
peg = input()
peg = re.split('\s+', peg)

dmoj = list(map(int, dmoj))
peg = list(map(int, peg))
dmoj.sort()
peg.sort()

maxi = 0
mini = 0

for x in range(citiNum):
    smaller = 0
    if int(dmoj[x]) > int(peg[x]):
        smaller = int(dmoj[x])
    else:
        smaller = int(peg[x])
    mini += smaller

    bigger = 0
    if int(dmoj[citiNum - 1 - x]) > int(peg[x]):
        bigger = int(dmoj[citiNum - 1 - x])
    else:
        bigger = int(peg[x])
    maxi += bigger

'''listMerge = dmoj + peg
listMerge.sort()

for x in range(citiNum):
    maxi += int(listMerge[citiNum - 1 - x])
    print(maxi)'''


if question == 1:
    print(mini)
else:
    print(maxi)

#print(dmoj, peg, maxi, mini)


