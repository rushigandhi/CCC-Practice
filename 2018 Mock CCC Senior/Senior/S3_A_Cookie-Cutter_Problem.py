total = int(input())

points = list()

for i in range(total):
    points.append([int(e) for e in input().split()])

# print(points)

diameter_list = list()


for i in range(len(points)):

    for x in range(1, len(points)):
        diameter = ((points[x][0]-points[i][0])**2 + (points[x][1]-points[i][1])**2)**0.5
        diameter_list.append(diameter)

diameter_list.sort()
print(diameter_list)





print(diameter_list[-1]/2)