import sys

total = int(input())
freq = [0] * 1000
for x in range(total):
    freq[int(input())] += 1

freq_index = list()
freq_count = list()


for i in range(len(freq)):
    if freq[i] != 0:
        freq_index.append(i)
        freq_count.append(freq[i])

print(freq_index, freq_count)

for x in range(len(freq_index)):
    for i in range(len(freq_index) - 1):
        if freq_count[i+1] < freq_count[i]:
            temp = freq_count[i+1]
            tempI = freq_index[i+1]
            freq_count[i+1] = freq_count[i]
            freq_index[i+1] = freq_index[i]
            freq_count[i] = temp
            freq_index[i] = tempI

print(freq_index, freq_count)
highest = freq_count[-1]
smallest = -sys.maxsize

freq_index_reversed = list(reversed(freq_index))
freq_count_reversed = list(reversed(freq_count))

checker = False
print(freq_index_reversed,freq_count_reversed)
for i in range(len(freq_count_reversed)):
    if freq_count_reversed[i] != highest:
        smallest = freq_index_reversed[-i]
        checker = True

if checker == False:
    

print(smallest)


