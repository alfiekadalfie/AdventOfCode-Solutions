# Part 1
horizontal_position = 0
depth = 0

for line in open("day2-2021.txt", "r"):
    line = line.strip("\n").split(" ")

    if line[0] == "forward":
        horizontal_position += int(line[1])
    elif line[0] == "down":
        depth += int(line[1])
    elif line[0] == "up":
        depth -= int(line[1])
    
print("Part 1 Answer: " + str(horizontal_position * depth))

# Part 2
horizontal_position = 0
depth = 0
aim = 0

for line in open("day2-2021.txt", "r"):
    line = line.strip("\n").split(" ")

    if line[0] == "forward":
        horizontal_position += int(line[1])
        depth += (aim * int(line[1]))
    elif line[0] == "down":
        aim += int(line[1])
    elif line[0] == "up":
        aim -= int(line[1])
    
print("Part 2 Answer: " + str(horizontal_position * depth))
