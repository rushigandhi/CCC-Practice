cases = int(input())

for i in range(cases):

    total = int(input())
    candies = []

    for x in range(total):

        candies.append(int(input()))

    branch = []

    empty = False
    checker = False
    current = 1

    while not empty:

        # print(current)
        # print(candies)
        # print(branch)
        # print(" ")

        if not candies and not branch:
            empty = True
            checker = True
        elif not candies and branch and branch[-1] != current:
            empty = True
        elif candies and candies[-1] == current:
            candies.pop()
            current += 1
        elif branch and branch[-1] == current:
            branch.pop()
            current += 1
        else:
            branch.append(candies.pop())

    if checker:
        print("Y")
    else:
        print("N")