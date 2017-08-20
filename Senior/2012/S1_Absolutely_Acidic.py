total = int(input())
freq = [0] * 1000
for x in range(total):
    freq[int(input())] += 1
sorted_freq = list(freq)
sorted_freq.sort()

