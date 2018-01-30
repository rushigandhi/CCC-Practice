#Get mother and father's alleles
mother = list(input())
father = list(input())

total = int(input())

for i in range(total):
    fly = list(input())
    checker = 0
    for x in range(len(fly)):
        if fly[x].islower():
            if fly[x] in mother and fly[x] in father:
                checker += 1
        else:
            if fly[x] in mother or fly[x] in father:
                checker += 1
    if checker == 5:
        print("Possible baby.")
    else:
        print("Not their baby!")



'''
AABbCcddEe
AaBBccddee
5
ABCdE
aBcdE
ABcdE
ABCde
ABcDe
'''