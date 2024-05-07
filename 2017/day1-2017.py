# Part 1

sum = 0

for line in open("day1-2017.txt", "r"):
    line = line.strip("\n")

first = line[0]

for digit in line[1:]:
    second = digit

    # checks if previous digit matches current digit
    if first == second:
        sum += int(second)
    
    first = digit

if first == line[0]:
    sum += int(first)

print('Part 1: ' + str(sum))

# Part 2
sum = 0

for line in open("day1-2017.txt", "r"):
    line = line.strip("\n")

steps = int(len(line) / 2)

first_half = line[0:steps]
second_half = line[steps:]

place = 0

# checking first half
while place < len(first_half):
    if first_half[place] == second_half[place]:
        sum += int(first_half[place])
    
    place += 1

place = 0

# checking second half
while place < len(second_half):
    if first_half[place] == second_half[place]:
        sum += int(second_half[place])
    
    place += 1

print('Part 2: ' + str(sum))
