# print("Numerator")
num = int(input())

# print("Denominator")
den = int(input())

whole = num//den
quotient = num/den

if whole - quotient == 0:
    print(whole)
else:
    fraction = quotient - whole
    new_num = num - (den * whole)
    varying_num = new_num
    while varying_num > 1:
        if (den/varying_num - den//varying_num) == 0:
            new_num = new_num/varying_num
            den = den/varying_num
            varying_num = new_num
        else:
            varying_num = varying_num - 1
    print(whole, str(int(new_num)) + "/" + str(int(den)))
