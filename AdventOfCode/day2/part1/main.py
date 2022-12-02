f = open("input.txt", "r")

values = f.readlines()
f.close()

points = 0

winLossChart = ['A X', 'B Y', 'C Z', 'A Y', 'B Z', 'C X']

for i in range(len(values)):
    values[i] = values[i].strip("\n")

for i in values:
    if i == winLossChart[0] or i == winLossChart[1] or i == winLossChart[2]:
        points += 3
    elif i == winLossChart[3] or i == winLossChart[4] or i == winLossChart[5]:
        points += 6

    x = i.split()
    if x[1] == 'X':
        points += 1
    elif x[1] == 'Y':
        points += 2
    else:
        points += 3

print(points)

