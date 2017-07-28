numList = [int(x) for x in input().split()]


def bubble_sort(numList):
    for i in range (len(numList)):
        print(numList)
        for y in range (len(numList) - 1):
            if numList[y] > numList[y + 1]:
                temp = numList[y]
                numList[y] = numList[y + 1]
                numList[y + 1] = temp


bubble_sort(numList)

print(numList)
