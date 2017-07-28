start = [int(x) for x in input().split()]
end = [int(i) for i in input().split()]
energy = int(input())

sumComponents = abs((end[0] - start[0])) + abs((end[1] - start[1]))

if sumComponents > energy:
    print("N")
elif sumComponents == energy:
    print("Y")
elif sumComponents < energy:
    if sumComponents%2 == energy%2:
        print("Y")
    else:
        print("N")
