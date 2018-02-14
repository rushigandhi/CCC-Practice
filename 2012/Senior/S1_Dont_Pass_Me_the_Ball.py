import math

scorer = int(input()) - 1


def comb(scorer):
    # return (math.factorial(n))/(math.factorial(r)*math.factorial(n-r))
    return (scorer * (scorer - 1) * (scorer - 2)) / 6


print(round(comb(scorer)))
