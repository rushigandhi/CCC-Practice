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

    print(x_coord, y_coord)
    total_edges = coordinates[0]

    # for x in range(1, total_edges):
    #
    #     if x == total_edges - 1:
    #         edge_slope = (coordinates[3]-coordinates[x+1])/(coordinates[x+2]-coordinates[x])
    #         edge_constant = coordinates[x+1] - edge_slope*coordinates[x]
    #     else:
    #         edge_slope = (coordinates[x+3]-coordinates[x+1])/(coordinates[x+2]-coordinates[x])
    #         edge_constant = coordinates[x+1] - edge_slope*coordinates[x]
