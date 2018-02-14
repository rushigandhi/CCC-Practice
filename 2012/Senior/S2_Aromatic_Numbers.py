import re

aromatic = input()

aromatic = re.findall("..", aromatic)

roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

for i in range(len(aromatic)):

    roman_val = roman.get(aromatic[i][1])

    aromatic[i] = [int(aromatic[i][0]), roman_val]

for i in range(len(aromatic) - 1):
    if aromatic[i][1] < aromatic[i + 1][1]:
        aromatic[i] = ["-", aromatic[i][0], aromatic[i][1]]


output = 0

for i in range(len(aromatic)):

    if aromatic[i][0] == "-":

        output -= aromatic[i][1]*aromatic[i][2]
    else:
        output += aromatic[i][0]*aromatic[i][1]

print(output)
