# total number of strings
total = int(input())

# for each string
for i in range(total):

    # get the string and initialize the substring list
    line = input()
    substring_list = list()

    substring_list.append("")

    # try each substring case
    for x in range(len(line)):
        for a in range(len(line)):

            substring = line[x:a+1]

            # if the substring case is not a repeat add it to the list
            if substring not in substring_list:
                substring_list.append(substring)

    # print the number of substrings
    print(len(substring_list))