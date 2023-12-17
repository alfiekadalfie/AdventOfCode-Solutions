# Part 1
total = 0

for line in open("day4-2022.txt", "r"):
    line = line.strip("\n").split(",")

    # [first-second, third-fourth]
    first = int(line[0].split("-")[0])
    second = int(line[0].split("-")[1])
    third = int(line[1].split("-")[0])
    fourth = int(line[1].split("-")[1])

    if (first <= third <= fourth <= second) or (third <= first <= second <= fourth):
        total += 1

print("Part 1 Answer: " + str(total))

# Part 2
total = 0

for line in open("day4-2022.txt", "r"):
    line = line.strip("\n").split(",")

    # [first-second, third-fourth]
    first = int(line[0].split("-")[0])
    second = int(line[0].split("-")[1])
    third = int(line[1].split("-")[0])
    fourth = int(line[1].split("-")[1])

    # overlaps?
    if first <= fourth and second >= third:
        total += 1

print("Part 2 Answer: " + str(total))
