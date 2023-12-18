# Part 1
floor = 0

for line in open("day1-2015.txt", "r"):
    for i in line:
        if i == "(":
            floor += 1
        else:
            floor -= 1

print("Part 1 Answer: " + str(floor))

# Part 2
position = 1
floor = 0

for line in open("day1-2015.txt", "r"):
    for i in line:
        if i == "(":
            floor += 1
        else:
            floor -= 1
        
        if(floor == -1):
            break
        else:
            position += 1

print("Part 1 Answer: " + str(position))
