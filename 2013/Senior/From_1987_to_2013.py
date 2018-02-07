year = int(input()) + 1
while True:
    yearLine = str(year)
    yearList = list(yearLine)
    yearSet = set(yearLine)
    if len(yearSet) == len(yearLine):
        print(str(yearLine))
        break
    else:
        year += 1

