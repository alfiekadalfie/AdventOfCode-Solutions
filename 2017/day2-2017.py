# Part 1
sum = 0

entries = []

for line in open("day2-2017.txt", "r"):
    entries.append(line.strip("\n").split("\t"))

for entry in entries:
    entry = [int(x) for x in entry]

    maximum = max(entry)
    minimum = min(entry)

    sum += (int(maximum) - int(minimum))

print('Part 1: ' + str(sum))

# Part 2
sum = 0

entries = []

for line in open("day2-2017.txt", "r"):
    entries.append(line.strip("\n").split("\t"))

converted_entries = []

for entry in entries:
    entry = [int(x) for x in entry]

    converted_entries.append(entry)

for entry in converted_entries:

    entry = sorted(entry, reverse=True)
    
    for i in range(len(entry)-1):
        for j in range(i+1, len(entry)):

            if entry[i] % entry[j] == 0:
                sum += int(entry[i] / entry[j])

print('Part 2: ' + str(sum))