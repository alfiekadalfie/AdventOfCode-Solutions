sum = 0
numbers_in_line = []

# Part 1
for line in open("day3-2023.txt", "r"):
    print(line.strip("\n").split("."))

    line = line.strip("\n").split(".")

    for i in line:
        if(i.isnumeric()):
            numbers_in_line.append(i)

print(numbers_in_line)
