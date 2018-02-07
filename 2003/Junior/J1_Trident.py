# Take user input regarding the tine length, spacing, and handle length
# print("Enter tine length:")
t_length = int(input())

# print("Enter tine spacing:")
t_spacing = int(input())

# print("Enter handle length:")
h_length = int(input())

# Initialize variables
space = ""
bar = ""
handle = ""

# Make the space
for i in range(t_spacing):
    space += " "

# Make the tine
tine = "*" + space + "*" + space + "*"

# Print the tine
for i in range(t_length):
    print(tine)

# Make the bar
for i in range(len(tine)):
    bar += "*"

# Print the bar
print(bar)

# Print the handle
for i in range(h_length):
    print(" " + space + "*")


