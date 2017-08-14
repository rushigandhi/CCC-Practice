total = int(input())
for i in range(total):
    listNum = int(input())
    numList = [int(e) for e in input().split()]
    #print(numList)
    counter = 0
    for x in range(listNum):
        for x in range(listNum - 1):
            if numList[x + 1] < numList[x]:
                tempData = numList[x + 1]
                numList[x + 1] = numList[x]
                numList[x] = tempData
                counter += 1
    print("Optimal train swapping takes", counter, "swap(s).")
    #print(numList)


'''
3
3
1 3 2
4
4 3 2 1
2
2 1

'''