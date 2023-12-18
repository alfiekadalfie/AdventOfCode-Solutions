# Part 1
surface_areas = []

for line in open("day2-2015.txt", "r"):
    line = line.strip("\n").split("x")

    minimum = min(int(line[0])*int(line[1]), (int(line[0])*int(line[2])), int(line[2])*int(line[1]))

    surface_areas.append(2*int(line[0])*int(line[1]) + 2*int(line[0])*int(line[2]) + 2*int(line[1])*int(line[2]) + minimum)

print("Part 1 Answer " + str(sum(surface_areas)))

# Part 2
volume = 1
perimeter = 0
sum = 0

for line in open("day2-2015.txt", "r"):
    line = line.strip("\n").split("x")

    # volume
    for i in line:
        volume *= int(i)

    # perimeter
    sides = []
    for i in line:
        sides.append(int(i))
    
    if sides[0] <= sides[1] <= sides[2]:
        perimeter += 2*sides[0] + 2*sides[1]
    elif sides[1] <= sides[0] <= sides[2]:
        perimeter += 2*sides[1] + 2*sides[0]
    elif sides[0] <= sides[2] <= sides[1]:
        perimeter += 2*sides[0] + 2*sides[2]
    elif sides[2] <= sides[0] <= sides[1]:
        perimeter += 2*sides[2] + 2*sides[0]
    elif sides[1] <= sides[2] <= sides[0]:
        perimeter += 2*sides[1] + 2*sides[2]
    elif sides[2] <= sides[1] <= sides[1]:
        perimeter += 2*sides[2] + 2*sides[1]
    
    sum += volume + perimeter
    
    volume = 1
    perimeter = 0

print("Part 2 Answer " + str(sum))
