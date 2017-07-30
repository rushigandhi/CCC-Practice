line = input()
newLine = line
lenList = []
lenLine = len(line)


def check_drome(dromeline):
    reverse_line = str(dromeline[::-1])
    if(dromeline == reverse_line):
        lenList.append(len(dromeline))


for x in range(lenLine):
    check_drome(newLine)
    for y in range(0, lenLine):
        check_drome(newLine[:-y])
    newLine = str(newLine[1:])

lenList.sort()
print(lenList[len(lenList) - 1])

