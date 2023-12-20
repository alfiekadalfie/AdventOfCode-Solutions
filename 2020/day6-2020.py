# Part 1
sum = 0

inputs = []     # 2D array consisting of each group
group = []

for line in open("day6-2020.txt", "r"):
    line = line.strip("\n")

    if line != "":
        group.append(line)
    else:
        inputs.append(group)
        group = []

# account for last group
inputs.append(group)
group = []

for i in inputs:
    count = 0
    letters = []

    for j in i:
        for k in j:
            if k not in letters:
                letters.append(k)
                count+=1
    
    sum += count

print("Part 1 Answer: " + str(sum))

# Part 2
sum = 0

inputs = []     # 2D array consisting of each group
group = []

for line in open("day6-2020.txt", "r"):
    line = line.strip("\n")

    if line != "":
        group.append(line)
    else:
        inputs.append(group)
        group = []

# account for last group
inputs.append(group)
group = []

sum = 0

for i in inputs:
    answers = set(i[0])
    for j in range(1, len(i)):
        answers &= set(i[j])
    sum += len(answers)

print("Part 2 Answer: " + str(sum))
