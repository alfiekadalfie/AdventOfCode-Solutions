# Part 1
count = 1   # starting point
x = 0
y = 0
houses = [[0, 0]]

for line in open("day3-2015.txt", "r"):
    line = line.strip("\n")

    for i in line:
        if i == ">":
            x += 1
        elif i == "<":
            x -= 1
        elif i == "^":
            y += 1
        elif i == "v":
            y -= 1
        
        if [x, y] not in houses:
            count += 1
            houses.append([x, y])
    
print("Part 1 Answer: " + str(count))

# Part 2
count = 1   # starting point
# Santa
x1 = 0
y1 = 0
# robo-Santa
x2 = 0
y2 = 0
houses = [[0, 0]]

pace = 1

for line in open("day3-2015.txt", "r"):
    line = line.strip("\n")

    for i in line:
        # Santa
        if pace % 2 == 1:
            if i == ">":
                x1 += 1
            elif i == "<":
                x1 -= 1
            elif i == "^":
                y1 += 1
            elif i == "v":
                y1 -= 1
            
            if [x1, y1] not in houses:
                count += 1
                houses.append([x1, y1])
        # robo-Santa
        else:
            if i == ">":
                x2 += 1
            elif i == "<":
                x2 -= 1
            elif i == "^":
                y2 += 1
            elif i == "v":
                y2 -= 1
            
            if [x2, y2] not in houses:
                count += 1
                houses.append([x2, y2])
        
        pace += 1

print("Part 2 Answer: " + str(count))
