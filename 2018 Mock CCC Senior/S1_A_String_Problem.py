line = list(input())
line_set = set(line)
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', ' l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']

freq = [0]*26

for i in range(len(line)):
    for x in range(len(alpha)):
        if line[i] == alpha[x]:
            freq[x] += 1

counter = 0

for i in range(len(freq)):
    if freq[i] > 0:
        counter += 1

if counter != 2:

    removal_counter_1 = 0
    removal_counter_2 = 0


    freq =[i for i in freq if i != 0]

    freq.sort()


    print(freq)

    for i in range(len(freq) - 2):
        removal_counter_1 += freq[i]

    for i in range(len(freq) - 1):
        removal_counter_2 += freq[i]

    if removal_counter_2 > removal_counter_1:
        print(removal_counter_1)
    else:
        print(removal_counter_2)
else:
    print(0)
