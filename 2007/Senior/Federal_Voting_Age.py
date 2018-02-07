# total number of cases
total = int(input())

# date of the election
date = 2007 + 2/12 + 27/365

# for each case
for i in range(total):

    # store the birth date

    birth_date = [int(e) for e in input().split()]

    # convert to number
    birth_date = birth_date[0] + birth_date[1]/12 + birth_date[2]/365

    # if the person's age is less than 18, output no
    if date - birth_date < 18:
        print("No")

    # otherwise, output yes
    else:
        print("Yes")
