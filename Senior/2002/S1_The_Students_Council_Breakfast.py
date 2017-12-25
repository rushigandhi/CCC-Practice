print("Cost of PINK tickets:")
p_cost = int(input())

print("Cost of GREEN tickets:")
g_cost = int(input())

print("Cost of RED tickets:")
r_cost = int(input())

print("Cost of ORANGE tickets:")
o_cost = int(input())

print("How much must be raised with ticket sales?")
total = int(input())

total = [total,total,total,total]

pink = [0,0,0,0]
green = [0,0,0,0]
red = [0,0,0,0]
orange = [0,0,0,0]

while total[0] > 0:
    while total[0] >= o_cost:
            total[0] = total[0] - o_cost
            orange[0] += 1
    while total[0] >= r_cost:
            total[0] = total[0] - r_cost
            red[0] += 1
    while total[0] >= g_cost:
            total[0] = total[0] - g_cost
            green[0] += 1
    while total[0] >= p_cost:
            total[0] = total[0] - p_cost
            pink[0] += 1

while total[1] > 0:
    while total[1] >= r_cost:
        total[1] = total[1] - r_cost
        red[1] += 1
    while total[1] >= g_cost:
        total[1] = total[1] - g_cost
        green[1] += 1
    while total[1] >= p_cost:
        total[1] = total[1] - p_cost
        pink[1] += 1

while total[2] > 0:
    while total[2] >= g_cost:
        total[2] = total[2] - g_cost
        green[2] += 1
    while total[2] >= p_cost:
        total[2] = total[2] - p_cost
        pink[2] += 1

while total[3] > 0:
    while total[3] >= p_cost:
        total[3] = total[3] - p_cost
        pink[3] += 1

combinations = list()
for i in range(4):
    combinations.append([pink[4-1-i], green[4-1-i], red[4-1-i], orange[4-1-i]])

print(combinations)