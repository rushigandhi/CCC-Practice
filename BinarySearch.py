numList = [int(x) for x in input().split()]
target = int(input())

def binary_search(numList, target):
    start  = 1
    end = len(numList)
    while start <= end:
        mid = (end + start) // 2
        if numList[mid] > target:
            end = mid - 1
        elif numList[mid] < target:
            start = mid + 1
        elif numList[mid] == target:
            return mid
        else:
            return -1

print(binary_search(numList, target))





