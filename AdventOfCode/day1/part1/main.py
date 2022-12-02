f = open("input.txt", "r")

values = f.readlines()

elves = []
currentElf = 1

for i in values:
    if(i != "\n" and currentElf == len(elves)):
        elves[currentElf - 1] += int(i)
    elif(i == "\n"):
        currentElf += 1
    else:
        elves.append(int(i))

print(max(elves))
        
    

f.close()
