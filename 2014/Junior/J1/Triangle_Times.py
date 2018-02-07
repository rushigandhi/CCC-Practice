total = 0
angleSet = set()
for x in range(3):
    inputLine = int(input())
    total += inputLine
    angleSet.add(inputLine)
if total == 180:
    if len(angleSet) == 1:
        print("Equilateral")
    elif len(angleSet) == 2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")



