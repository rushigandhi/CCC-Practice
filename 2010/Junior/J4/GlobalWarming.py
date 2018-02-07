pattern = list()
'''
 3,  4,  6,   4,  5,  7, 5
(+1, +2, −2) (+1, +2, −2)
'''

def check(length):
    for i in range(len(pattern) - 1):
        diff = pattern[i+1] - pattern[i]
        primaryDiff = pattern[i%length + 1] - pattern[i%length]
        #print(i, diff, primaryDiff)
        if diff != primaryDiff:
            return False
    return True


def solve():
    for i in range(1, len(pattern)):
        if check(i):
            return i

while True:
    inputLine = input().split()
    if inputLine == ["0"]:
        break
    pattern = [ int(d) for d in inputLine[1:] ]
    answer = solve()
    print(answer)