# get the total number of phone numbers
total = int(input())

# character to number conversion dictionary
conversion = {"A": 2, "B": 2, "C": 2, "D": 3, "E": 3, "F": 3, "G": 4, "H": 4, "I": 4, "J": 5, "K": 5, "L": 5, "M": 6,
              "N": 6, "O": 6, "P": 7, "Q": 7, "R": 7, "S": 7, "T": 8, "U": 8, "V": 8, "W": 9, "X": 9, "Y": 9, "Z": 9}
# for every phone number
for i in range(total):

    # convert the phone number string to a list
    phone_number = list(input())

    # use a list comprehension to remove all the hyphens
    phone_number = [x for x in phone_number if x != "-"]

    # initialize the converted phone number variable
    converted_number = ""

    # for every character/number
    for a in range(10):

        # if it is a character, convert it to a number and concatenate to the converted phone number
        if phone_number[a] in conversion.keys():
            converted_number += str(conversion[phone_number[a]])

        # otherwise, concatenate it to the converted phone number
        else:
            converted_number += phone_number[a]

    # add all the necessary hyphens
    converted_number = converted_number[:3] + "-" + converted_number[3:6] + "-" + converted_number[6:]

    # print the converted number
    print(converted_number)
