total = int(input())
senList = list()

for x in range (0, total):
    senList.append(input())

for y in range (0, len(senList)):
    sentence = senList[y]
    sentence = sentence.split()
    for i in range (0, len(sentence)):
        last = len(sentence) - 1
        if(len(sentence[i]) == 4 and i != last):
            print("****" + " ", end="")
        elif(len(sentence[i]) == 4 and i == last):
            print("****")
        elif(i == last):
            print(sentence[i])
        else:
            print(sentence[i] + " ", end="")

