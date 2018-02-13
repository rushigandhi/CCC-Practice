num_gates = int(input())

gates = [0]*num_gates

num_planes = int(input())

planes = 0

for i in range(num_planes):

    plane = int(input()) - 1

    keep_going = True

    while keep_going:
        if plane == -1:
            break
        elif gates[plane] == 0:
            gates[plane] += 1
            keep_going = False
        else:
            plane -= 1

    if keep_going:
        break


counter = 0
for i in range(len(gates)):
    counter += gates[i]

print(counter)


