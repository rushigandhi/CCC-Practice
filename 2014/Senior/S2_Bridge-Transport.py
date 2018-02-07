max_weight = int(input())
car_num = int(input())
weight_list = list()

for i in range (car_num):
    weight_list.append(int(input()))

temp_list = list()

for a in range(car_num):
    total = 0
    temp_list.append(weight_list[a])
    if a%4 == 0 and a != 0:
        temp_list.pop(0)
    '''print(temp_list)'''
    for x in range(len(temp_list)):
        total = temp_list[x] + total
    '''print(total)'''
    if total > max_weight:
        break
    '''print(temp_list)'''

print(a)
'''

100
6
50
30
10
10
40
50




'''