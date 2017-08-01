import math

pointsList = list()
while True:
    radius = int(input())
    if radius == 0:
        break
    points = 0
    for x in range(-radius, radius):
        pointsY = 2 * math.floor(math.sqrt(radius**2 - x**2))
        points += pointsY
    pointsX = 2*radius + 1
    points += pointsX
    pointsList.append(points)

for i in range(len(pointsList)):
    print(pointsList[i])

