# get the screen dimensions
max_dimen = [int(e) for e in input().split()]
max_c = max_dimen[0]
max_r = max_dimen[1]

# initialize the position variable
position = [0, 0]

# for every entry
while True:

    # get the amount the mouse must move by
    move = [int(i) for i in input().split()]

    # if it is [0, 0], end the program
    if move == [0, 0]:
        break

    else:

        # if the sum of the movement and position is above the maximum, make the position equal to the maximum
        if (position[0] + move[0]) > max_c:
            position[0] = max_c

        # if the sum of the movement and position is below zero, make the position equal to zero
        elif (position[0] + move[0]) < 0:
            position[0] = 0

        # otherwise, add the relative motion coordinates to the current position
        else:
            position[0] += move[0]

        # if the sum of the movement and position is above the maximum, make the position equal to the maximum
        if (position[1] + move[1]) > max_r:
            position[1] = max_r

        # if the sum of the movement and position is below zero, make the position equal to zero
        elif (position[1] + move[1]) < 0:
            position[1] = 0

        # otherwise, add the relative motion coordinates to the current position
        else:
            position[1] += move[1]

    # print the updated position
    print(str(position[0]) + " " + str(position[1]))
