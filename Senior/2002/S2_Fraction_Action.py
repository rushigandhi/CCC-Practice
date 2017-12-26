print("Numerator")
num = int(input())

print("Denominator")
den = int(input())

whole = num//den
quotient = num/den

if whole - quotient == 0:
    print(whole)
else:
    fraction = quotient - whole
    new_num = num - (den * whole)
    print(whole, str(new_num) +"/"+str(den))
