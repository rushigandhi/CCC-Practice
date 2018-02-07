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
    first = first[-1]
    second = second[-1]
    third = third[-1]
    fourth = fourth[-1]

    # all to lowercase
    first = first.lower()
    second = second.lower()
    third = third.lower()
    fourth = fourth.lower()


    # find the last vowel of the first word
    if first.rfind('a') != -1:
        first = first[first.rfind('a'):]
    if first.rfind('e') != -1:
        first = first[first.rfind('e'):]
    if first.rfind('i') != -1:
        first = first[first.rfind('i'):]
    if first.rfind('o') != -1:
        first = first[first.rfind('o'):]
    if first.rfind('u') != -1:
        first = first[first.rfind('u'):]


    # find the last vowel of the second word
    if second.rfind('a') != -1:
        second = second[second.rfind('a'):]
    if second.rfind('e') != -1:
        second = second[second.rfind('e'):]
    if second.rfind('i') != -1:
        second = second[second.rfind('i'):]
    if second.rfind('o') != -1:
        second = second[second.rfind('o'):]
    if second.rfind('u') != -1:
        second = second[second.rfind('u'):]


    # find the last vowel of the third word
    if third.rfind('a') != -1:
        third = third[third.rfind('a'):]
    if third.rfind('e') != -1:
        third = third[third.rfind('e'):]
    if third.rfind('i') != -1:
        third = third[third.rfind('i'):]
    if third.rfind('o') != -1:
        third = third[third.rfind('o'):]
    if third.rfind('u') != -1:
        third = third[third.rfind('u'):]


    # find the last vowel of the fourth word
    if fourth.rfind('a') != -1:
        fourth = fourth[fourth.rfind('a'):]
    if fourth.rfind('e') != -1:
        fourth = fourth[fourth.rfind('e'):]
    if fourth.rfind('i') != -1:
        fourth = fourth[fourth.rfind('i'):]
    if fourth.rfind('o') != -1:
        fourth = fourth[fourth.rfind('o'):]
    if fourth.rfind('u') != -1:
        fourth = fourth[fourth.rfind('u'):]

    # print the type of poem
    if (first == second) and (second == third) and (third == fourth):
        print("perfect")
    elif (first == second) and (third == fourth):
        print("even")
    elif (first == third) and (second == fourth):
        print("cross")
    elif (first == fourth) and (second == third):
        print("shell")
    else:
        print("free")

