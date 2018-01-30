# Get texts
decrypted = list(input())
encrypted = list(input())
new = list(input())

# initialize an empty dictionary in which the key will be the
# decrypted character and the value will be the encrypted character
conversion = dict()

# for each character in the message
for i in range(len(decrypted)):

    # if the character is not in the dictionary
    if decrypted[i] not in conversion.keys():

        # add that character and its corresponding decrypted character to the dictionary
        conversion.update({decrypted[i]:encrypted[i]})

# initialize the new decrypted string
output = ""

# for each character the new encrypted string
for i in range(len(new)):

    checker = False

    # for each key value pair in the dictionary
    for decryptedC, encryptedC in conversion.items():

        # if the value is equal to the character in the new encrypted string
        # add the corresponding key to the the output string
        if encryptedC == new[i]:
            output += decryptedC
            checker = True

    # if the value has no corresponding key, a period is added to the output string
    if checker is False:
        output += "."


print(output)