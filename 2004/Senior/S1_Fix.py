# total number of collections
total = int(input())

# for every collection of words
for i in range(total):

    # convert the words to list
    first = list(input())
    second = list(input())
    third = list(input())

    # if prefixes are present, print "No"
    if (first == second[:len(first)]) or (first == third[:len(first)]):
        print("No")
    elif (second == first[:len(second)]) or (second == third[:len(second)]):
        print("No")
    elif (third == first[:len(third)]) or (third == second[:len(third)]):
        print("No")

    # if suffixes are present, print "No"
    elif (first == second[len(second)-len(first):]) or (first == third[len(third)-len(first):]):
        print("No")
    elif (second == first[len(first)-len(second):]) or (second == third[len(third)-len(second):]):
        print("No")
    elif (third == first[len(first)-len(third):]) or (third == second[len(second)-len(third):]):
        print("No")

    # if prefixes and suffixes are not present, print "Yes"
    else:
        print("Yes")
