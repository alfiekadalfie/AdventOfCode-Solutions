# Part 1 
# include 170, 176, 179 as first three inputs for this part only
# exclude in Part 2

count = 0
prev = 170

for line in open("day1-2021.txt", "r"):
    line = int(line.strip("\n"))

    if line > prev:
        count += 1
    
    prev = line

print("Part 1 Answer: " + str(count))

# Part 2
count = 0
items = [170, 176, 179] # ignore first three inputs
prev = sum(items)

for line in open("day1-2021.txt", "r"):
    line = int(line.strip("\n"))

    items.pop(0)
    items.append(line)

    if sum(items) > prev:
        count += 1
    
    prev = sum(items)

print("Part 2 Answer: " + str(count))
