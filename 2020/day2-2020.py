# Part 1
passwords = 0   #how many valid?

for line in open("day2-2020.txt", "r"):
    line = line.strip("\n").split(": ")

    min = line[0].split(" ")[0].split("-")[0]
    max = line[0].split(" ")[0].split("-")[1]
    char = line[0].split(" ")[1]

    count = 0

    for i in line[1]:
        if i == char:
            count+=1

    if int(min) <= count <= int(max):
        passwords += 1

print("Part 1 Answer: " + str(passwords))

# Part 2
passwords = 0   #how many valid?

for line in open("day2-2020.txt", "r"):
    line = line.strip("\n").split(": ")

    first_position = int(line[0].split(" ")[0].split("-")[0]) - 1
    second_position = int(line[0].split(" ")[0].split("-")[1]) - 1
    char = line[0].split(" ")[1]

    if line[1][first_position] == char and line[1][second_position] != char:
        passwords += 1
    elif line[1][second_position] == char and line[1][first_position] != char:
        passwords += 1

print("Part 2 Answer: " + str(passwords))
