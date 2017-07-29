collections = int(input())
ynList = list()
for x in range (0, collections):
	for y in range (0, 3):
		counter = 0
		first = input()
		second = input()
		third = input()
		if first in second or first in third:
			counter++
		elif second in first or second in third:
			counter++
		elif third in first or third in second:
			counter++
		if(counter > 0):
			ynList.append("Yes")
		elif(counter == 0):
			ynList.append("No")


for i in range (0, len(ynList)):
	print(ynList[i])



