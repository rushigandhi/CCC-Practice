aCount = 100
dCount = 100
rounds = int(input())

for i in range(rounds):
    score = list(input())
    antonia = int(score[0])
    david = int(score[len(score) - 1])
    if antonia > david:
        dCount -= antonia
    elif david > antonia:
        aCount -= david

print(aCount)
print(dCount)