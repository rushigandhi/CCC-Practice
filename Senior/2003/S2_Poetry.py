# total number of poems
total = int(input())

# for every poem
for i in range(total):

    # split the poem into words
    first = input().split()
    second = input().split()
    third = input().split()
    fourth = input().split()

    # find the last word
    first = first[-1].lower()
    second = second[-1].lower()
    third = third[-1].lower()
    fourth = fourth[-1].lower()

    # find the last vowel of the first word
    if first.rfind('a') != -1:
        first = first[first.rfind('a'):]
    elif first.rfind('e') != -1:
        first = first[first.rfind('e'):]
    elif first.rfind('i') != -1:
        first = first[first.rfind('i'):]
    elif first.rfind('o') != -1:
        first = first[first.rfind('o'):]
    elif first.rfind('u') != -1:
        first = first[first.rfind('u'):]

    # find the last vowel of the second word
    if second.rfind('a') != -1:
        second = second[second.rfind('a'):]
    elif second.rfind('e') != -1:
        second = second[second.rfind('e'):]
    elif second.rfind('i') != -1:
        second = second[second.rfind('i'):]
    elif second.rfind('o') != -1:
        second = second[second.rfind('o'):]
    elif second.rfind('u') != -1:
        second = second[second.rfind('u'):]

    # find the last vowel of the third word
    if third.rfind('a') != -1:
        third = third[third.rfind('a'):]
    elif third.rfind('e') != -1:
        third = third[third.rfind('e'):]
    elif third.rfind('i') != -1:
        third = third[third.rfind('i'):]
    elif third.rfind('o') != -1:
        third = third[third.rfind('o'):]
    elif third.rfind('u') != -1:
        third = third[third.rfind('u'):]

    # find the last vowel of the fourth word
    if fourth.rfind('a') != -1:
        fourth = fourth[fourth.rfind('a'):]
    elif fourth.rfind('e') != -1:
        fourth = fourth[fourth.rfind('e'):]
    elif fourth.rfind('i') != -1:
        fourth = fourth[fourth.rfind('i'):]
    elif fourth.rfind('o') != -1:
        fourth = fourth[fourth.rfind('o'):]
    elif fourth.rfind('u') != -1:
        fourth = fourth[fourth.rfind('u'):]

    # print the type of poem
    if (first == second) and (first == third) and (first == fourth):
        print("perfect")
    elif (first == second) and (third == fourth):
        print("even")
    elif (first == third) and (second == fourth):
        print("cross")
    elif (first == fourth) and (second == third):
        print("shell")
    else:
        print("free")