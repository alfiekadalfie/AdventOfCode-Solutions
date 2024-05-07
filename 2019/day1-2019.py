# Part 1
from math import floor

sum = 0

for line in open("day1-2019.txt", "r"):
    line = line.strip("\n")

    module = floor(int(line) / 3) - 2

    sum += module

print("Part 1: " + str(sum))

# Part 2
sum = 0

for line in open("day1-2019.txt", "r"):
    module = line.strip("\n")

    while floor(int(module) / 3) - 2 >= 0:

        module = floor(int(module) / 3) - 2

        sum += int(module)

print("Part 2: " + str(sum))
