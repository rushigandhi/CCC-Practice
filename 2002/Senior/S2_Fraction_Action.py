# print("Numerator")
num = int(input())

# print("Denominator")
den = int(input())

whole = num//den
quotient = num/den

if whole - quotient == 0:
    print(whole)
else:
    new_num = num - (den * whole)
    # print("new numerator", new_num)
    varying_num = new_num
    # print(varying_num)
    while varying_num > 1:
        if (den/varying_num - den//varying_num) == 0 and (new_num/varying_num - new_num//varying_num) == 0:
            new_num = new_num/varying_num
            den = den/varying_num
            varying_num = new_num
            # print("worked")
        else:
            varying_num = varying_num - 1
        # print(varying_num)

    if whole == 0:
        print(str(int(new_num)) + "/" + str(int(den)))
    else:
        print(whole, str(int(new_num)) + "/" + str(int(den)))
