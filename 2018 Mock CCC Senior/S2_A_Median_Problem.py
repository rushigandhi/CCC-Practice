total = int(input())

medians_list = list()

for i in range(total):
    temp = [int(e) for e in input().split()]
    temp.sort()
    # print(temp)
    temp_median = temp[round((len(temp)-1)/2)]
    medians_list.append(temp_median)

medians_list.sort()
print(medians_list[round((len(medians_list)-1)/2)])

#
# print(sequences)
# print(round((len(sequences)-1)/2))
# sequences = list(sequences[round((len(sequences)-1)/2)])
# print(sequences)
#
# print(round((len(sequences)-1)/2))
#
# median = sequences[round((len(sequences)-1)/2)]
#
# print(median)

'''
5
1 2 3 4 5
5 6 7 8 9
10 1 11 12 12
1 2 3 4 5
3 4 12 4 5'''

'''
3
1 2 3
4 5 6
7 8 9

'''