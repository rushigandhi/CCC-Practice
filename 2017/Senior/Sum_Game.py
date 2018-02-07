total = int(input())
swifts = [int(x) for x in input().split()]
sema = [int(x) for x in input().split()]
K = 0
s1 = 0
s2 = 0
for i in range(total):
    s1 += swifts[i]
    s2 += sema[i]
    if s1 == s2:
        K = i + 1

print(K)
