total = int(input())

friends = dict()

for i in range(total):
    assign = [int(e) for e in input().split()]
    friends.update({assign[0]:assign[1]})

while True:
    pair = input()
    if pair == "0 0":
        break
    else:
        pair = [int(e) for e in pair.split()]

        checker = False
        start = pair[0]
        destination = 0
        counter = 0

        while destination != pair[1]:

            if destination == start:
                print("No")
                checker = True
                break

            else:
                destination = friends[pair[0]]
                pair[0] = destination
                counter += 1
        if checker is False:
            print("Yes " + str(counter - 1))