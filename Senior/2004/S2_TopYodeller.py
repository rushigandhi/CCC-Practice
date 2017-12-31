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

    order.reverse()
    print(results, order)

    # adding the lowest position of a contestant to a list
    for p in range(len(order)):
        lowest[order[p] - 1] = max(lowest[order[p] - 1], p + 1)
    print("lowest", lowest, "score", score)


# initializing the highest score variable
top_score = 0

# finding the highest score variable
for u in range(len(score)):
    top_score = max(top_score, score[u])

# printing the winning contestant(s), score(s), and worst rank(s)
for q in range(len(score)):
    if score[q] == top_score:
        print("Yodeller " + str(q + 1) + " is the TopYodeller: score " + str(score[q]) + ", worst rank " + str(lowest[q]))

print(score, lowest)
# Sample Input
'''
5 2
99 97 100 85 -4
95 97 100 62 1000
'''