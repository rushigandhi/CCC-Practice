
# gather all the competition information
competition = [int(x) for x in input().split()]
participants = competition[0]
rounds = competition[1]

# initialize empty score and lowest lists
score = [0 for x in range(participants)]
lowest = [0 for x in range(participants)]

# for every round
for i in range(rounds):

    # get the result data from the round
    results = [int(x) for x in input().split()]

    # make a list of the participants order
    order = list()
    for r in range(participants):
        order.append(r + 1)

    print(order)

    # add the participants score
    for a in range(len(results)):
        score[a] += results[a]

    # sort the scores and order
    for j in range(len(results)):
        for y in range(len(results) - 1):
            if results[y] > results[y + 1]:
                tempResults = results[y]
                tempOrder = order[y]
                results[y] = results[y + 1]
                order[y] = order[y + 1]
                results[y + 1] = tempResults
                order[y + 1] = tempOrder

    reversed(order)
    print(results)
    print(order)

    for p in range(len(order)):
        lowest[order[p] - 1] = max(lowest[order[p] - 1], order[p])
    print(lowest)


print(score, lowest)







'''
5 2
99 97 100 85 -4
95 97 100 62 1000

'''
