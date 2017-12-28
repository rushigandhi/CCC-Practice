position = 1

while True:
    # print("Enter sum of dice:")
    roll = int(input())

    if roll == 0:
        print("You Quit!")
        break
    else:
        position += roll

        if position == 54:
            position = 19
        elif position == 90:
            position = 48
        elif position == 99:
            position = 77
        elif position == 9:
            position = 34
        elif position == 40:
            position = 64
        elif position == 67:
            position = 86
        elif position > 100:
            position -= roll
        elif position == 100:
            print("You are now on square " + str(position))
            print("You Win!")
            break
        print("You are now on square " + str(position))



