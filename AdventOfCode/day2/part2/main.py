f = open("input.txt", "r")

values = f.readlines()
f.close()

points = 0

whatToPick = ['A Y', 'B X', 'C Z', 'A Z', 'B Y', 'C X']

for i in range(len(values)):
    values[i] = values[i].strip("\n")

for i in values:
    if i == whatToPick[0] or i == whatToPick[1] or i == whatToPick[2]:
        points += 1
    elif i == whatToPick[3] or i == whatToPick[4] or i == whatToPick[5]:
        points += 2
    else:
        points += 3

    x = i.split()
    if x[1] == 'Z':
        points += 6
    elif x[1] == 'Y':
        points += 3

print(points)

