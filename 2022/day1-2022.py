# Part 1
max = 0
all = []        # list of lists of all numbers for each elf
numbers = []    # each elf

for line in open("day1-2022.txt", "r"):
    if line != "\n":
        numbers.append(int(line.strip("\n")))
    else:
        all.append(numbers)
        numbers = []

for i in all:
    if sum(i) > max:
        max = sum(i)
    
print("Part 1 Answer: " + str(max))

# Part 2
elf_total = []
total = 0
all = []        # list of lists of all numbers for each elf
numbers = []    # each elf

for line in open("day1-2022.txt", "r"):
    if line != "\n":
        numbers.append(int(line.strip("\n")))
    else:
        all.append(numbers)
        numbers = []

for i in all:
    elf_total.append(sum(i))

elf_total = sorted(elf_total)

total += (elf_total[len(elf_total)-3] + elf_total[len(elf_total)-2] + elf_total[len(elf_total)-1])

print("Part 2 Answer: " + str(total))
