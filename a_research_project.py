totalGuys = int(input())
lowList = list()
highList = list()

for x in range(0, totalGuys):
    picNum = int(input())

    picList = input();
    picList = picList.split()
    picList.sort();
    lowList.append(picList[0])
    highList.append(picList[len(picList)-1])

for i in range(0, len(lowList)):
    print(lowList[i] + " " + highList[i])
