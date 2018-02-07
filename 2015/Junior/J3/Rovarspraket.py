line = list(input())
#print(line)
vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(len(line)):
    newStr = line[i]
    if line[i] not in vowels:
        if line[i] == 'g':
            newStr += 'eh'
        elif line[i] == 'l':
            newStr == 'im'
        elif line[i] == 'r':
            newStr += 'os'
        elif line[i] == 'z':
            newStr += "uz"
        else:
            closest = abs(int(ord(line[i])) - int(ord(vowels[0])))
            closestVowel = 'a'
            for x in range(len(vowels)):
                if abs(ord(line[i])- ord(vowels[x])) < closest:
                    closest =  abs(ord(line[i])- ord(vowels[x]))
                    closestVowel = vowels[x]
                a = 1
            while True:
                if str(chr(ord(line[i]) + a)) in vowels:
                    a+=1
                    closestCon = str(chr(ord(line[i]) + a))
                else:
                    closestCon = str(chr(ord(line[i]) + a))
                    break

            newStr += str(closestVowel) + closestCon
    line[i] = newStr

#print(line)
line = ''.join(line)
print(line)
