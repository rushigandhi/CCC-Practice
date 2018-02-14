total = int(input())

freq = [0]*1000

values = []

for i in range(total):

    reading = int(input())

    values.append(reading)

    freq[reading - 1] += 1

max_freq = max(freq)

max_occur = []

for i in range(len(freq)):
    if freq[i] == max_freq:
        max_occur.append(i + 1)


if len(max_occur) != 1:
    print(abs(max_occur[0]-max_occur[-1]))
else:
    second_max_freq = 0

    for i in range(len(freq)):

        if freq[i] != max_freq:
            second_max_freq = max(second_max_freq, freq[i])

    second_max_occur = []

    for i in range(len(freq)):
        if freq[i] == second_max_freq:
            second_max_occur.append(i + 1)

    differences = []

    for i in range(len(second_max_occur)):
        differences.append(abs(max_occur[0]-second_max_occur[i]))
    differences.sort()
    print(differences[-1])