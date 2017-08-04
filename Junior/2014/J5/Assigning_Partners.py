import re

total = int(input())
firstLine = re.split('\s+', input())
secondLine = re.split('\s+', input())
partners = dict()
output = 'good'

for i in range(total):

    firstName = firstLine[i]
    secondName = secondLine[i]
    if firstName == secondName:
        output = "bad"
        break
    if firstName not in partners and secondName not in partners:
        partners[firstName] = secondName

    elif firstName in partners.keys():
        if partners[firstName] != secondName:
            output = "bad"
            break
    elif secondName in partners.keys():
        if partners[secondName] != firstName:
            output = "bad"
            break

print(output)
