# Get mother and father's alleles
mother = list(input())
father = list(input())

# total number of babies
total = int(input())

# for each baby
for i in range(total):

    # get the information about the baby
    fly = list(input())
    checker = 0

    # for each character
    for x in range(len(fly)):

        # if it is a recessive allele
        if fly[x].islower():

            # make sure it is in both the mother and father
            if fly[x] in mother and fly[x] in father:
                checker += 1

        # else make sure it is in one of the parents
        else:
            if fly[x] in mother or fly[x] in father:
                checker += 1

    # output whether it is their baby or not
    if checker == 5:
        print("Possible baby.")
    else:
        print("Not their baby!")