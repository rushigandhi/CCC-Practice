# Get the coordinates of the windows
windows = [int(e) for e in input().split()]

# find the linear equation of the line connecting the windows
windows_slope = (windows[3]-windows[1])/(windows[2]-windows[0])
windows_constant = windows[3] - windows_slope*windows[0]

# Get the total number of buildings
total = int(input())

# for every building
for i in range(total):

    coordinates = [int(e) for e in input().split()]
    x_coord = list()
    y_coord = list()
    for x in range(1, len(coordinates)):
        print(coordinates[x])
        if x%2 == 1:
            x_coord.append(coordinates[x])
        else:
            y_coord.append(coordinates[x])

    total_edges = coordinates[0]

    print(x_coord, y_coord)
    for x in range(total_edges):
        if x == total_edges - 1:
            if x_coord[0]-x_coord[x] == 0:


            edge_slope = (y_coord[0]-y_coord[x])/()
        else:
            edge_slope = (y_coord[x+1]-y_coord[x])/(x_coord[x+1]-x_coord[x])
        edge_constant = y_coord[x] - edge_slope*x_coord[x]
        print(edge_slope, edge_constant)
