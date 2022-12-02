f = open("input.txt", "r")

values = f.readlines()

elves = []
currentElf = 1

topThree = 0

for i in values:
    if(i != "\n" and currentElf == len(elves)):
        elves[currentElf - 1] += int(i)
    elif(i == "\n"):
        currentElf += 1
    else:
        elves.append(int(i))



for i in range(3): 
    maxElf = max(elves)
    topThree += maxElf
    for x in range(len(elves)):
        if elves[x] == maxElf:
            del(elves[x])
            break

    

print(topThree)
        
    

f.close()
