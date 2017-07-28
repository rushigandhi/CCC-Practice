numList = [int(x) for x in input().split()]

def insertion_sort(numList):
    for i in range(len(numList)):
        print(numList)
        j = i
        while j > 0 and numList[i] < numList[j - 1]:
            j -= 1
        temp = numList[i]
        for x in range(i, j, -1):
            numList[x] = numList[x - 1]
        numList[j] = temp


insertion_sort(numList)
print(numList)
