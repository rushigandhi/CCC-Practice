coinNum = int(input())
line = input()
line = line.split()
me = 0
friend = 0
for x in range (0, coinNum):
	if(line[0] > line[coinNum-1]):
		me = me + line[0]
		line.pop(0)
	else
		me = me + line[coinNum-1]
		line.pop(coinNum-1)

if(line[0] < line[coinNum-1]):
		friend = friend + line[0]
		line.pop(0)
	else
		friend = friend + line[coinNum-1]
		line.pop(coinNum-1)
print(str(me))
